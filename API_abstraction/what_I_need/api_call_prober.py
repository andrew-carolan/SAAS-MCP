"""
api_call_prober.py
==================
Takes extracted JSON from llm_page_extractor and autonomously discovers
how to call the API via an LLM generate → execute → evaluate loop.

Usage:
  export CMC_API_KEY="your-key"
  python api_call_prober.py output/scraped_api_json/extracted_cryptocurrency#coinmarketcap-id-map.json
"""

from anyio import Path

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

import ollama

from python_runtime import ensure_requirements_file, python_executable
from paths import (
    SCRAPED_API_JSON_DIR,
    WORKSPACE_API_PROBE,
    WORKSPACE_ENDPOINT_JSON,
    ensure_dirs,
    migrate_legacy_files,
    successful_curl_output_dir,
)

MAX_RETRIES = 5
MODEL_NAME = "gemma4:e2b-mlx"
RESPONSE_PREVIEW_MAX_CHARS = 2048
# --------------------------------
# --------------------------------
# did you get a successful call?
# --------------------------------
# --------------------------------
def extract_result_json(stdout: str) -> tuple[dict | None, str | None]:
    text = stdout.strip()
    if not text:
        return None, "stdout is empty"
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        pass
    for marker in ('{"success"', '{"success":'):
        idx = text.find(marker)
        if idx >= 0:
            try:
                obj, _ = json.JSONDecoder().raw_decode(text[idx:])
                return obj, None
            except json.JSONDecodeError as e:
                return None, f"JSON decode error: {e}"
    return None, "No JSON object found in stdout"


def redact_secrets(obj: dict, api_key: str) -> dict:
    text = json.dumps(obj)
    text = text.replace(api_key, "***")
    return json.loads(text)


def slug_from_input_path(path: str) -> str:
    name = path.rsplit("/", 1)[-1]
    if name.startswith("extracted_"):
        name = name[len("extracted_") :]
    return name.replace(".json", "")


def build_prompt_block(endpoint: dict, probe_result: dict) -> str:
    req = probe_result.get("request", {})
    auth = probe_result.get("auth", {})
    
    call = {
        "method": req.get("method", "GET").upper(),
        "url": req.get("url", ""),
        "headers": {auth.get("header"): "***"} if auth.get("header") else {},
        "params": req.get("params") or {},
        "json": req.get("body"),
    }
    
    # drop empty fields
    call = {k: v for k, v in call.items() if v}
    
    return f"import requests\n\nresponse = requests.request(**{call})"


class APICallProber:
    def __init__(
        self,
        input_json_file: str,
        model_name: str = MODEL_NAME,
        max_retries: int = MAX_RETRIES,
    ):
        self.input_json_file = input_json_file
        self.model_name = model_name
        self.max_retries = max_retries
        self.slug = slug_from_input_path(input_json_file)

    def _load_endpoints(self) -> list[dict]:
        with open(self.input_json_file, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return [data]

    def _call_llm(self, prompt: str) -> str | None:
        print(f"\n[API-Prober] Sending prompt to {self.model_name}...")
        try:
            response = ollama.generate(model=self.model_name, prompt=prompt)
            return response["response"]
        except Exception as e:
            print(f"[API-Prober] Error calling LLM: {e}")
            return None

    def _extract_python_code(self, text: str) -> str:
        m = re.search(r"```python\n(.*?)\n```", text, re.DOTALL)
        if m:
            return m.group(1)
        m = re.search(r"```\n(.*?)\n```", text, re.DOTALL)
        if m:
            return m.group(1)
        return text

    def _build_initial_prompt(self, endpoint: dict) -> str:
        curl_cmd = endpoint.get("curl", "").strip()
        if not curl_cmd:
            raise ValueError(f"Endpoint '{endpoint.get('name')}' has no curl field")

        params_json = json.dumps(endpoint.get("params", {}), indent=2)
        errors_json = json.dumps(endpoint.get("error_messaging", {}), indent=2)

        return f"""You are an expert at calling REST APIs with Python.

Here is the curl command extracted from the API documentation:

```
{curl_cmd}
```

Endpoint name: {endpoint.get("name", "unknown")}

Optional query params (from docs — use minimal values for a test call, e.g. limit=3):
{params_json}

Error codes hint: {errors_json}

Your job: write a short Python script that executes this API call using `requests`.
- Read API keys/tokens from `os.environ` only (try CMC_API_KEY, API_KEY, etc. as appropriate).
- Figure out auth headers from the curl and error codes (401/403 = wrong auth).
- Figure out query params from the curl and params block above.
- On success: print ONE JSON object to stdout and exit 0.
- On failure: print errors to stderr and exit 1.
- Do NOT print debug text to stdout — only the final JSON.

Stdout JSON on success:
{{
  "success": true,
  "status_code": 200,
  "request": {{"method": "...", "url": "...", "headers": {{"...": "***"}}, "params": {{}}, "body": null}},
  "response_preview": {{ ... }},
  "auth": {{"type": "header", "header": "...", "env_var": "..."}}
}}

Redact secrets in headers as "***". Output ONLY python in a ```python ``` block.
"""

    def _build_retry_prompt(self, code: str, error: str, curl_cmd: str) -> str:
        return f"""Your script failed to run this curl command:

```
{curl_cmd}
```

Previous code:
```python
{code}
```

Error:
{error}

Fix it. Secrets from os.environ only. Print result JSON to stdout on success.
Output ONLY python in a ```python ``` block.
"""

    def _execute_probe(self, endpoint_path: str) -> subprocess.CompletedProcess:
        cmd = [python_executable(), str(WORKSPACE_API_PROBE), endpoint_path]
        print(f"[API-Prober] Executing {WORKSPACE_API_PROBE} ...")
        return subprocess.run(cmd, capture_output=True, text=True)

    def _evaluate_probe_output(
        self, result: subprocess.CompletedProcess
    ) -> tuple[bool, str, dict | None]:
        """Programmatic evaluation of probe stdout. Returns (ok, message, parsed)."""
        if result.returncode != 0:
            err = result.stderr.strip() or result.stdout.strip() or "Unknown error"
            hint = ""
            if "401" in err or "403" in err or "Unauthorized" in err:
                hint = " — wrong auth header or missing env var (export the API key first)"
            elif "400" in err or "422" in err:
                hint = " — missing or invalid params; adjust test params"
            return False, f"Probe exited {result.returncode}: {err[:800]}{hint}", None

        stdout = result.stdout.strip()
        if not stdout:
            return False, "Probe exited 0 but stdout is empty", None

        data, parse_err = extract_result_json(stdout)
        if data is None:
            return False, f"Probe stdout is not valid JSON: {parse_err}\nstdout: {stdout[:500]}", None

        if not data.get("success"):
            return False, f"Probe JSON has success=false or missing: {stdout[:500]}", None

        status = data.get("status_code")
        if not isinstance(status, int) or not (200 <= status < 300):
            return False, f"Probe status_code not 2xx: {status}", data

        req = data.get("request")
        if not isinstance(req, dict) or not req.get("method") or not req.get("url"):
            return False, "Probe JSON missing request.method or request.url", data

        preview = data.get("response_preview")
        if isinstance(preview, str) and preview.strip():
            try:
                preview = json.loads(preview)
                data["response_preview"] = preview
            except json.JSONDecodeError:
                pass  # non-empty string is acceptable
        if preview is None or preview == "" or preview == {} or preview == []:
            return False, "Probe response_preview is empty", data

        return True, f"Probe OK — {req.get('method')} {req.get('url')} → {status}", data

    def _api_returned_successful_call(self, parsed: dict | None) -> bool:
        """Explicit gate: did the live API call succeed? If yes, caller should break the loop."""
        if not parsed:
            print("[API-Prober] Did the API return a successful call? NO — no result to evaluate.")
            return False

        status = parsed.get("status_code")
        success_flag = parsed.get("success") is True
        preview = parsed.get("response_preview")
        has_preview = preview not in (None, "", {}, [])

        if isinstance(status, int) and 200 <= status < 300 and success_flag and has_preview:
            print(
                f"[API-Prober] Did the API return a successful call? YES "
                f"(HTTP {status}, response has data) — saving code and breaking loop."
            )
            return True

        print(
            f"[API-Prober] Did the API return a successful call? NO "
            f"(success={success_flag}, status={status}, has_preview={has_preview})"
        )
        return False

    def _save_success_to_folder(
        self,
        merged_endpoint: dict,
        prompt_block: str,
        code: str,
    ) -> Path:
        """Save winning probe script + verified JSON into output/successful_curl_commands/<slug>/."""
        out_dir = successful_curl_output_dir(self.slug)
        out_dir.mkdir(parents=True, exist_ok=True)

        probe_path = out_dir / "probe.py"
        verified_path = out_dir / "verified.json"

        with open(probe_path, "w", encoding="utf-8") as f:
            f.write(code.strip())

        payload = {
            "endpoints": [merged_endpoint],
            "prompt_block": prompt_block,
            "api_call_successful": True,
        }
        with open(verified_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

        print(f"[API-Prober] Saved probe code  → {probe_path}")
        print(f"[API-Prober] Saved verified JSON → {verified_path}")
        return out_dir

    def _merge_verified_endpoint(self, endpoint: dict, probe_result: dict) -> dict:
        api_key = os.environ.get("API_KEY", "")
        probe_result = redact_secrets(probe_result, api_key)
        req = probe_result.get("request", {})
        merged = dict(endpoint)
        merged["verified_call"] = {
            "method": req.get("method"),
            "url": req.get("url"),
            "headers": req.get("headers"),
            "query_params": req.get("params"),
            "body": req.get("body"),
            "auth": probe_result.get("auth"),
            "status_code": probe_result.get("status_code"),
            "response_preview": probe_result.get("response_preview"),
        }
        return merged

    def _probe_endpoint(self, endpoint: dict, index: int) -> dict | None:
        name = endpoint.get("name", f"endpoint_{index}")
        print(f"\n{'=' * 50}")
        print(f"  Probing: {name}")
        print(f"{'=' * 50}")

        curl_cmd = endpoint.get("curl", "").strip()
        if not curl_cmd:
            print(f"[API-Prober] No curl field on '{name}' — skipping.")
            return None

        print(f"[API-Prober] curl: {curl_cmd}")

        with open(WORKSPACE_ENDPOINT_JSON, "w", encoding="utf-8") as f:
            json.dump(endpoint, f, indent=2)

        current_prompt = self._build_initial_prompt(endpoint)
        code = ""

        for attempt in range(1, self.max_retries + 1):
            print(f"\n--- Attempt {attempt} / {self.max_retries} ---")

            llm_response = self._call_llm(current_prompt)
            if not llm_response:
                print("[API-Prober] LLM returned nothing.")
                break

            code = self._extract_python_code(llm_response)
            with open(WORKSPACE_API_PROBE, "w", encoding="utf-8") as f:
                f.write(code.strip())

            result = self._execute_probe(str(WORKSPACE_ENDPOINT_JSON))
            if result.stdout:
                print(f"[API-Prober] stdout (first 400 chars): {result.stdout.strip()[:400]}")
            if result.stderr:
                print(f"[API-Prober] stderr (first 400 chars): {result.stderr.strip()[:400]}")

            ok, message, parsed = self._evaluate_probe_output(result)
            print(f"[API-Prober] {message}")

            if ok and parsed and self._api_returned_successful_call(parsed):
                merged = self._merge_verified_endpoint(endpoint, parsed)
                probe_result = {
                    "request": {
                        "method": merged["verified_call"]["method"],
                        "url": merged["verified_call"]["url"],
                        "params": merged["verified_call"].get("query_params"),
                        "body": merged["verified_call"].get("body"),
                    },
                    "auth": merged["verified_call"].get("auth"),
                    "status_code": merged["verified_call"]["status_code"],
                    "response_preview": merged["verified_call"].get("response_preview"),
                }
                prompt_block = build_prompt_block(endpoint, probe_result)
                self._save_success_to_folder(merged, prompt_block, code)
                return merged  # break retry loop

            error_for_llm = message
            if result.stderr:
                error_for_llm += f"\n\nstderr:\n{result.stderr.strip()[:1000]}"
            if result.stdout and not ok:
                error_for_llm += f"\n\nstdout:\n{result.stdout.strip()[:1000]}"
            current_prompt = self._build_retry_prompt(code, error_for_llm, curl_cmd)

        print(f"[API-Prober] Failed to verify '{name}' after {self.max_retries} attempts.")
        return None

    def run(self) -> str | None:
        ensure_dirs()
        migrate_legacy_files()

        print(f"[API-Prober] Using Python: {python_executable()}")
        if not ensure_requirements_file():
            print("[API-Prober] Warning: could not install all runtime dependencies.")

        endpoints = self._load_endpoints()
        if not endpoints:
            print("[API-Prober] No endpoints in input JSON.")
            return None

        print(f"[API-Prober] Loaded {len(endpoints)} endpoint(s) from {self.input_json_file}")
        print("[API-Prober] Secrets must be in environment variables (never hardcoded).")

        verified: list[dict] = []
        prompt_blocks: list[str] = []

        for i, ep in enumerate(endpoints):
            merged = self._probe_endpoint(ep, i)
            if merged is None:
                print(f"\n[API-Prober] Aborting — could not verify endpoint {i + 1}.")
                return None
            verified.append(merged)
            probe_result = {
                "request": {
                    "method": merged["verified_call"]["method"],
                    "url": merged["verified_call"]["url"],
                    "params": merged["verified_call"].get("query_params"),
                    "body": merged["verified_call"].get("body"),
                },
                "auth": merged["verified_call"].get("auth"),
                "status_code": merged["verified_call"]["status_code"],
                "response_preview": merged["verified_call"].get("response_preview"),
            }
            prompt_blocks.append(build_prompt_block(ep, probe_result))

        prompt_block = "\n\n".join(prompt_blocks)
        out_dir = successful_curl_output_dir(self.slug)

        # Final combined output (all endpoints) — also written if multi-endpoint file
        verified_json_path = out_dir / "verified.json"
        probe_py_path = out_dir / "probe.py"
        output_payload = {
            "endpoints": verified,
            "prompt_block": prompt_block,
            "api_call_successful": True,
        }

        out_dir.mkdir(parents=True, exist_ok=True)
        with open(verified_json_path, "w", encoding="utf-8") as f:
            json.dump(output_payload, f, indent=2)

        if WORKSPACE_API_PROBE.is_file() and not probe_py_path.is_file():
            shutil.copy(WORKSPACE_API_PROBE, probe_py_path)

        print(f"\n[API-Prober] Success!")
        print(f"   Output folder  → {out_dir}")
        print(f"   Verified JSON  → {verified_json_path}")
        if probe_py_path.is_file():
            print(f"   Probe script   → {probe_py_path}")
        print(f"\n--- prompt_block (for MCPAutoCoder) ---\n{prompt_block}\n---")

        return str(verified_json_path)


def main():
    parser = argparse.ArgumentParser(
        description="Verify extracted API JSON by autonomously probing live HTTP calls."
    )
    parser.add_argument(
        "input_json",
        nargs="?",
        default=str(
            SCRAPED_API_JSON_DIR / "extracted_cryptocurrency#coinmarketcap-id-map.json"
        ),
        help="Path to extracted JSON from llm_page_extractor",
    )
    parser.add_argument(
        "--model",
        default=MODEL_NAME,
        help=f"Ollama model (default: {MODEL_NAME})",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=MAX_RETRIES,
        help=f"Max LLM retries per endpoint (default: {MAX_RETRIES})",
    )
    args = parser.parse_args()

    if not args.input_json or not os.path.exists(args.input_json):
        print(f"Error: File not found: {args.input_json}")
        print("Usage: python api_call_prober.py <path_to_extracted.json>")
        sys.exit(1)

    prober = APICallProber(
        input_json_file=args.input_json,
        model_name=args.model,
        max_retries=args.retries,
    )
    result = prober.run()
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
