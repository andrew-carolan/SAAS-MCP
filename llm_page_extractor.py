"""
llm_page_extractor.py
=====================
Works with ANY website.

Takes a SINGLE URL and autonomously extracts API documentation:
  • curl command (constructed from server + method + path)
  • parameters
  • description
  • example response
  • error messaging

Strategy:
  1. Deterministic pre-processing: extract operations from scraped JSON or
     window.DATA (no LLM needed for this step).
  2. If operations found, ask the LLM to format/assemble the final output
     (curl construction, param mapping, response extraction).
  3. If NO operations found, fall back to asking the LLM to write a
     BeautifulSoup parser against the raw HTML.
  4. Strict programmatic + LLM evaluation loop.

Usage:
  python llm_page_extractor.py --url https://pro.coinmarketcap.com/api/documentation/pro-api-reference/cryptocurrency#coinmarketcap-id-map
  python llm_page_extractor.py --url https://example.com/api/docs --model gemma4:e4b
"""

import os
import re
import json
import shutil
import subprocess
import argparse

import ollama
from playwright.sync_api import sync_playwright

from python_runtime import ensure_requirements_file, python_executable
from paths import (
    SCRAPED_API_JSON_DIR,
    SCRAPED_JSON_DIR,
    WORKSPACE_OPERATIONS_JSON,
    WORKSPACE_PAGE_EXTRACTOR,
    WORKSPACE_PAGE_HTML,
    ensure_dirs,
    migrate_legacy_files,
    scraped_json_candidates,
)

HTML_TRUNCATE = 40_000   # chars sent to LLM — keep context manageable


# ---------------------------------------------------------------------------
# Class
# ---------------------------------------------------------------------------

class LLMPageExtractor:
    def __init__(
        self,
        model_name: str = "gemma4:e2b-mlx",
        max_retries: int = 5,
        scraped_json_dir: str | None = None,
        success_dir: str | None = None,
    ):
        self.model_name = model_name
        self.max_retries = max_retries
        self.scraped_json_dir = scraped_json_dir or str(SCRAPED_JSON_DIR)
        self.success_dir = success_dir or str(SCRAPED_API_JSON_DIR)

    # ------------------------------------------------------------------
    # Playwright helpers
    # ------------------------------------------------------------------

    def _fetch_page_data(self, url: str) -> tuple[str, str]:
        """
        Navigate to url with Playwright.
        Returns (html_content, window_data_json_string).
        html_content is the full rendered HTML.
        window_data_json_string is window.DATA serialised as JSON (or '{}').
        """
        print(f"🌍 Fetching page data from: {url}")
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch()
            except Exception as e:
                if "Executable doesn't exist" in str(e):
                    print("📦 Playwright browser missing — installing Chromium...")
                    subprocess.run(
                        [python_executable(), "-m", "playwright", "install", "chromium"],
                        check=True,
                    )
                    browser = p.chromium.launch()
                else:
                    raise
            page = browser.new_page()
            page.goto(url, wait_until="networkidle")
            html = page.content()
            try:
                win_data = page.evaluate("JSON.stringify(window.DATA || {})")
            except Exception:
                win_data = "{}"
            browser.close()
        return html, win_data

    # ------------------------------------------------------------------
    # File helpers
    # ------------------------------------------------------------------

    def _slug_from_url(self, url: str) -> str:
        """Return the last path segment of the URL (used as slug / file stem)."""
        return url.strip("/").split("/")[-1]

    def _find_existing_json(self, slug: str) -> str | None:
        """Return path to scraped JSON if it exists (new or legacy layout)."""
        for candidate in scraped_json_candidates(slug):
            if candidate.is_file():
                print(f"📂 Found existing scraped JSON: {candidate}")
                return str(candidate)
        print(f"⚠️  No existing JSON found for slug '{slug}' under data/scraped_jsons/")
        return None

    # ------------------------------------------------------------------
    # Deterministic pre-processing (Phase 2)
    # ------------------------------------------------------------------

    def _extract_operations(self, data: object) -> list[dict]:
        """
        Recursively walk a parsed JSON object (from scraped JSON or window.DATA)
        looking for the 'operations' array inside a GraphQL query result.

        Returns a list of operation dicts, each having keys like:
        slug, summary, method, path, description, parameters, responses, servers
        """
        results = []

        def search(obj):
            if isinstance(obj, dict):
                # Check if this dict has an 'operations' key with a list value
                if "operations" in obj and isinstance(obj["operations"], list):
                    ops = obj["operations"]
                    # Validate: operations should have dicts with 'slug' and 'path'
                    valid_ops = [
                        op for op in ops
                        if isinstance(op, dict) and ("slug" in op or "path" in op)
                    ]
                    if valid_ops:
                        # Also grab the parent server URL if available
                        parent_servers = obj.get("servers", [])
                        for op in valid_ops:
                            if not op.get("servers") and parent_servers:
                                op["_parent_servers"] = parent_servers
                        results.extend(valid_ops)
                        return  # Don't recurse further into this branch
                # Otherwise recurse into values
                for v in obj.values():
                    search(v)
            elif isinstance(obj, list):
                for item in obj:
                    search(item)

        search(data)
        return results

    def _preprocess_operations(self, json_path: str | None, windata_json: str, target_slug: str | None) -> list[dict]:
        """
        Phase 2: Deterministically extract clean operation summaries.
        Tries scraped JSON first, then window.DATA.
        Returns a list of clean dicts ready for the LLM.
        """
        raw_ops = []

        # Strategy A: scraped JSON file
        if json_path and os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                raw_ops = self._extract_operations(data)
                if raw_ops:
                    print(f"✅ Found {len(raw_ops)} operations from scraped JSON")
            except Exception as e:
                print(f"⚠️  Error reading scraped JSON: {e}")

        # Strategy B: window.DATA
        if not raw_ops:
            try:
                data = json.loads(windata_json)
                raw_ops = self._extract_operations(data)
                if raw_ops:
                    print(f"✅ Found {len(raw_ops)} operations from window.DATA")
            except Exception as e:
                print(f"⚠️  Error parsing window.DATA: {e}")

        if not raw_ops:
            print("⚠️  No operations found in either source.")
            return []

        # Build clean summaries
        clean_ops = []
        for op in raw_ops:
            servers = op.get("servers", op.get("_parent_servers", []))
            server_url = servers[0]["url"] if servers and isinstance(servers[0], dict) else ""

            # Extract parameters
            params = {}
            for p in op.get("parameters", []):
                if isinstance(p, dict):
                    name = p.get("name", "unknown")
                    params[name] = {
                        "description": p.get("description", ""),
                        "required": p.get("required", False),
                        "in": p.get("in", ""),
                        "type": p.get("schema", {}).get("type", "") if isinstance(p.get("schema"), dict) else "",
                    }

            # Extract responses
            responses = {}
            example_response = {}
            error_responses = {}
            for r in op.get("responses", []):
                if isinstance(r, dict):
                    status = str(r.get("statusCode", "?"))
                    desc = r.get("description", "")
                    content = r.get("content", [])
                    schema_snippet = {}
                    examples = {}
                    if content and isinstance(content, list) and len(content) > 0:
                        c = content[0]
                        if isinstance(c, dict):
                            raw_schema = c.get("schema", {})
                            if isinstance(raw_schema, dict):
                                # Keep a trimmed version of the schema
                                schema_snippet = {
                                    "type": raw_schema.get("type", ""),
                                    "description": raw_schema.get("description", ""),
                                }
                                # Extract example if available
                                props = raw_schema.get("properties", {})
                                if isinstance(props, dict):
                                    for pk, pv in props.items():
                                        if isinstance(pv, dict) and "example" in pv:
                                            examples[pk] = pv["example"]
                            # Also check for explicit examples in content
                            for ex in c.get("examples", []):
                                if isinstance(ex, dict) and "value" in ex:
                                    examples[ex.get("name", "example")] = ex["value"]

                    responses[status] = {"description": desc, "schema": schema_snippet}
                    if status == "200":
                        example_response = examples if examples else schema_snippet
                    else:
                        error_responses[status] = desc

            # Build curl command
            method = op.get("method", "get").upper()
            path = op.get("path", "")
            header_params = [p for p in op.get("parameters", [])
                           if isinstance(p, dict) and p.get("in") == "header"]
            header_flags = ""
            for hp in header_params:
                name = hp.get("name", "")
                default = ""
                if isinstance(hp.get("schema"), dict):
                    default = hp["schema"].get("default", "")
                header_flags += f" -H '{name}: {default}'"

            curl_cmd = f"curl --request {method} '{server_url}{path}'{header_flags}" if server_url and path else ""

            clean_ops.append({
                "name": op.get("summary", op.get("slug", "Unknown")),
                "slug": op.get("slug", ""),
                "curl": curl_cmd,
                "params": params,
                "description": op.get("description", ""),
                "example_response": example_response,
                "error_messaging": error_responses,
            })

        if target_slug:
            filtered_ops = [op for op in clean_ops if op["slug"] == target_slug]
            if not filtered_ops:
                print(f"⚠️  No operation found exactly matching slug '{target_slug}'. Trying fuzzy match...")
                filtered_ops = [op for op in clean_ops if target_slug in op["slug"]]
            if filtered_ops:
                clean_ops = filtered_ops
                print(f"✅ Filtered down to {len(clean_ops)} matching operation(s) for '{target_slug}'")
            else:
                print(f"⚠️  Could not filter operations by '{target_slug}'. Returning all {len(clean_ops)} operations.")

        return clean_ops

    # ------------------------------------------------------------------
    # LLM helpers
    # ------------------------------------------------------------------

    def _call_llm(self, prompt: str) -> str | None:
        print(f"\n[LLM] Sending prompt to {self.model_name}...")
        try:
            response = ollama.generate(model=self.model_name, prompt=prompt)
            return response["response"]
        except Exception as e:
            print(f"[LLM] Error: {e}")
            return None

    def _extract_python_code(self, text: str) -> str:
        """Strip ```python ... ``` fences, or return raw text as fallback."""
        m = re.search(r"```python\n(.*?)\n```", text, re.DOTALL)
        if m:
            return m.group(1)
        m = re.search(r"```\n(.*?)\n```", text, re.DOTALL)
        if m:
            return m.group(1)
        return text

    def _execute_script(self, script_path: str, *extra_args):
        """Run the generated script, passing data file paths as CLI args."""
        cmd = [python_executable(), script_path] + [str(a) for a in extra_args]
        print(f"[Runner] Executing {script_path} ...")
        return subprocess.run(cmd, capture_output=True, text=True)

    # ------------------------------------------------------------------
    # Evaluator (Phase 5: strict programmatic + LLM)
    # ------------------------------------------------------------------

    def _evaluate_output(self, stdout: str) -> bool:
        """
        Two-stage evaluation:
        1. Programmatic checks (fast, deterministic)
        2. LLM semantic check (only if programmatic passes)
        """
        # --- Stage 1: Programmatic ---
        print("[Evaluator] Stage 1: Programmatic checks...")

        # Must be valid JSON
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError:
            print("[Evaluator] ❌ Output is not valid JSON.")
            return False

        # Must be a list
        if not isinstance(data, list):
            print("[Evaluator] ❌ Output is not a JSON array.")
            return False

        # Must have at least one item
        if len(data) == 0:
            print("[Evaluator] ❌ Output array is empty.")
            return False

        # Check required keys in each object
        required_keys = {"name", "curl", "params", "description", "example_response", "error_messaging"}
        for i, obj in enumerate(data):
            if not isinstance(obj, dict):
                print(f"[Evaluator] ❌ Item {i} is not a dict.")
                return False
            missing = required_keys - set(obj.keys())
            if missing:
                print(f"[Evaluator] ❌ Item {i} missing keys: {missing}")
                return False

        # Reject if ALL curl fields are garbage
        garbage_phrases = ["not found", "explicitly", "unavailable", "no curl", "n/a"]
        real_curls = 0
        for obj in data:
            curl = str(obj.get("curl", "")).lower()
            if curl.startswith("curl ") and not any(g in curl for g in garbage_phrases):
                real_curls += 1
        if real_curls == 0:
            print(f"[Evaluator] ❌ No real curl commands found (all are empty or garbage).")
            return False

        # Reject if ALL params are empty
        has_params = any(bool(obj.get("params")) for obj in data)
        if not has_params:
            print("[Evaluator] ❌ All endpoints have empty params.")
            return False

        # Reject entries with empty names
        empty_names = sum(1 for obj in data if not obj.get("name", "").strip())
        if empty_names > len(data) // 2:
            print(f"[Evaluator] ❌ Too many empty names ({empty_names}/{len(data)}).")
            return False

        print(f"[Evaluator] ✅ Programmatic checks passed ({len(data)} endpoints, {real_curls} real curls).")

        # --- Stage 2: LLM semantic check ---
        print("[Evaluator] Stage 2: LLM semantic check...")
        sample = json.dumps(data[:3], indent=2)[:2000]
        prompt = f"""You are a strict evaluator. A script extracted API documentation and produced a JSON array.

Here is a sample of the first 3 items:
---
{sample}
---

Total items: {len(data)}

Does this look like real, accurate API documentation (not hallucinated or placeholder data)?
- Do the curl commands look like real API calls?
- Do the params have meaningful names and descriptions?
- Do the descriptions describe actual API operations?

Reply with exactly one word: YES or NO.
"""
        resp = self._call_llm(prompt)
        if resp is None:
            return False
        answer = resp.strip().upper()
        print(f"[Evaluator] LLM response: {answer}")
        return "YES" in answer

    # ------------------------------------------------------------------
    # Prompt builders
    # ------------------------------------------------------------------

    def _build_operations_prompt(self, clean_ops_json: str) -> str:
        """
        Phase 3: When we have pre-extracted operations, the LLM just needs
        to format/validate them into the final output schema.
        """
        return f"""You are an expert Python developer.

I have pre-extracted API operation data from a documentation page. The data is stored as a JSON array in a file passed as sys.argv[1].

Write a Python script that:
1. Reads the JSON file at sys.argv[1]
2. For each operation object, ensures all 6 required output fields are present and clean:
   - "name": use the existing "name" field
   - "curl": use the existing "curl" field. If empty, try to construct it from other fields.
   - "params": use the existing "params" field. Clean it into a simple dict of {{param_name: description_string}}.
   - "description": use the existing "description" field. Strip any markdown formatting.
   - "example_response": use the existing "example_response" field. If it's a dict, keep it. If empty, set to {{}}.
   - "error_messaging": use the existing "error_messaging" field. If it's a dict, keep it. If empty, set to {{}}.
3. Remove the "slug" field from each object (internal use only).
4. Print the cleaned JSON array to stdout. ONLY the JSON array, no other text.

Here is a sample of the pre-extracted data for reference:
```json
{clean_ops_json[:5000]}
```

Rules:
- The output MUST be ONLY a valid JSON array to stdout. No extra text, no print statements, no debug output.
- Use json.dumps with indent=2 for readability.
- Do NOT crash — catch all exceptions.

Write the COMPLETE Python script inside a ```python``` block.
"""

    def _build_html_fallback_prompt(self, html_snippet: str, target_slug: str | None) -> str:
        """
        Phase 4: When no operations were found in the structured data,
        fall back to asking the LLM to parse the raw HTML.
        """
        target_instruction = ""
        if target_slug:
            target_instruction = f"\nCRITICAL: The user specifically requested the endpoint associated with the name/slug '{target_slug}'. Extract ONLY that endpoint. Do not extract all endpoints on the page.\n"

        return f"""You are an expert Python developer.
{target_instruction}
No structured API data was found for this page, so you need to parse the raw HTML.

Write a Python script that:
1. Reads an HTML file at sys.argv[1]
2. Uses BeautifulSoup (with html.parser) to find ALL API endpoints documented on the page
3. For each endpoint, extract:
   - "name": the endpoint name (from headings, h2/h3 tags)
   - "curl": any curl command found in <code> or <pre> blocks near this endpoint
   - "params": parameter names and descriptions from tables or lists
   - "description": descriptive text about the endpoint
   - "example_response": any JSON example response found in code blocks
   - "error_messaging": any error codes/messages found
4. Print a JSON array of these objects to stdout. ONLY the JSON array.

Here is the first {HTML_TRUNCATE} chars of the page HTML:
```html
{html_snippet}
```

Rules:
- Output MUST be ONLY a valid JSON array to stdout. No extra text.
- If you can't find a field, set it to "" or {{}}.
- Do NOT crash — catch all exceptions.
- Use beautifulsoup4 (import bs4). Do NOT use lxml, use html.parser.

Write the COMPLETE Python script inside a ```python``` block.
"""

    def _build_retry_prompt(self, prev_code: str, error_or_output: str, is_semantic: bool) -> str:
        if is_semantic:
            return f"""You previously wrote a Python script to extract API info, but the output failed validation.

Here is the code you wrote:
```python
{prev_code}
```

Here is the output or error:
{error_or_output[:3000]}

The output must be a JSON array of objects, each with:
- "name": a string
- "curl": a real curl command string (starting with "curl ") or ""
- "params": a dictionary with param names as keys
- "description": a descriptive string
- "example_response": a dict or string
- "error_messaging": a dict or string

Fix the script. Only print the JSON array to stdout — NO other text.
Return ONLY the corrected Python code inside a ```python``` block.
"""
        else:
            return f"""You previously wrote a Python script, but it crashed with an error.

Here is the code you wrote:
```python
{prev_code}
```

Here is the error:
{error_or_output}

Please fix the code. Return ONLY the corrected Python code inside a ```python``` block.
"""

    # ------------------------------------------------------------------
    # Main orchestration loop
    # ------------------------------------------------------------------

    def run(self, target_url: str):
        ensure_dirs()
        migrate_legacy_files()
        os.makedirs(self.success_dir, exist_ok=True)
        ensure_requirements_file()

        slug = self._slug_from_url(target_url)
        target_slug = target_url.split("#")[1] if "#" in target_url else None
        print(f"\n🎯 Target URL: {target_url}")
        print(f"   Target Slug (Fragment): {target_slug}")
        print(f"   File Slug: {slug}\n")

        # ---- Step 1: gather data sources ----
        json_path = self._find_existing_json(slug) or ""
        html_content, windata_json = self._fetch_page_data(target_url)

        # Write html to temp file (needed for HTML fallback)
        with open(WORKSPACE_PAGE_HTML, "w", encoding="utf-8") as f:
            f.write(html_content)

        # ---- Step 2: deterministic pre-processing ----
        print("\n" + "=" * 50)
        print("  Phase 2: Deterministic Pre-Processing")
        print("=" * 50)
        clean_ops = self._preprocess_operations(json_path or None, windata_json, target_slug)

        if clean_ops:
            print(f"\n📋 Pre-extracted {len(clean_ops)} operations:")
            for op in clean_ops:
                print(f"   • {op['name']} — {op['curl'][:60]}...")

            # Write clean ops to workspace for the LLM script
            with open(WORKSPACE_OPERATIONS_JSON, "w", encoding="utf-8") as f:
                json.dump(clean_ops, f, indent=2)

            # Build the simple formatting prompt
            clean_ops_json = json.dumps(clean_ops[:3], indent=2)
            current_prompt = self._build_operations_prompt(clean_ops_json)
            script_args = [str(WORKSPACE_OPERATIONS_JSON)]
            mode = "OPERATIONS"
        else:
            print("\n⚠️  No structured operations found. Falling back to HTML scraping.")
            html_snippet = html_content[:HTML_TRUNCATE]
            current_prompt = self._build_html_fallback_prompt(html_snippet, target_slug)
            script_args = [str(WORKSPACE_PAGE_HTML)]
            mode = "HTML_FALLBACK"

        # ---- Step 3: LLM loop ----
        print(f"\n{'=' * 50}")
        print(f"  Phase 3: LLM Generate → Execute → Evaluate Loop (mode: {mode})")
        print(f"{'=' * 50}")

        code = ""
        success = False

        for attempt in range(1, self.max_retries + 1):
            print(f"\n{'─' * 40}")
            print(f"  Attempt {attempt} / {self.max_retries}")
            print(f"{'─' * 40}")

            # 1. Get code from LLM
            llm_response = self._call_llm(current_prompt)
            if not llm_response:
                print("[Loop] LLM returned nothing. Aborting.")
                break

            code = self._extract_python_code(llm_response)

            # 2. Write temp script
            with open(WORKSPACE_PAGE_EXTRACTOR, "w", encoding="utf-8") as f:
                f.write(code.strip())

            # 3. Execute
            result = self._execute_script(str(WORKSPACE_PAGE_EXTRACTOR), *script_args)

            print(f"[Runner] Return code: {result.returncode}")
            if result.stdout:
                print(f"[Runner] stdout (first 800 chars):\n{result.stdout.strip()[:800]}")

            # 4a. Runtime / compile error → send stderr back
            if result.returncode != 0:
                error_msg = result.stderr.strip()
                print(f"[Runner] stderr:\n{error_msg}")
                current_prompt = self._build_retry_prompt(code, error_msg, is_semantic=False)
                continue

            # 4b. Script ran — evaluate output
            stdout = result.stdout.strip()
            if self._evaluate_output(stdout):
                print(f"\n✅ Success! Evaluator approved the output.")

                # Save winning script
                final_script = os.path.join(self.success_dir, f"page_extractor_{slug}.py")
                shutil.copy(WORKSPACE_PAGE_EXTRACTOR, final_script)
                print(f"   Winning script → {final_script}")

                # Save extracted JSON
                try:
                    extracted = json.loads(stdout)
                except json.JSONDecodeError:
                    extracted = {"raw_output": stdout}

                result_json_path = os.path.join(self.success_dir, f"extracted_{slug}.json")
                with open(result_json_path, "w", encoding="utf-8") as f:
                    json.dump(extracted, f, indent=2)
                print(f"   Extracted data  → {result_json_path}")

                print("\n📋 Final extracted data (first 1000 chars):")
                print(json.dumps(extracted, indent=2)[:1000] + "\n...")
                success = True
                return extracted

            else:
                print("[Loop] Evaluation failed — looping with feedback.")
                current_prompt = self._build_retry_prompt(code, stdout, is_semantic=True)

        if not success:
            print(f"\n❌ Max retries ({self.max_retries}) reached without success for {target_url}.")

        return None

    def __call__(self, target_url: str):
        return self.run(target_url)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "LLM-powered page extractor — works with ANY website. "
            "Pass an exact URL and it autonomously extracts curl, params, "
            "description, example responses, and error messaging."
        )
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Exact target URL to extract API details from",
    )
    parser.add_argument(
        "--model",
        default="gemma4:e2b-mlx",
        help="Ollama model name (default: gemma4:e2b-mlx)",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=5,
        help="Max LLM retry attempts (default: 5)",
    )
    args = parser.parse_args()

    extractor = LLMPageExtractor(
        model_name=args.model,
        max_retries=args.retries,
    )
    extractor.run(target_url=args.url)
