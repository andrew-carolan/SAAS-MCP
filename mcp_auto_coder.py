import os
import json
import re
import shutil
import asyncio
import ollama
import sys
import requests
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from python_runtime import (
    ensure_requirements_file,
    missing_module_from_error,
    python_executable,
    subprocess_env,
    try_install_missing_from_error,
)
from paths import (
    MCP_SERVERS_DIR,
    SCRAPED_API_JSON_DIR,
    WORKSPACE_MCP_SERVER,
    ensure_dirs,
    migrate_legacy_files,
)

MAX_RETRIES = 3
MODEL_NAME = 'gemma4:e2b-mlx'
CMC_API_KEY = "e4acb088e9c34dfa894c22d5218c615e"


def parse_curl(curl: str) -> tuple[str, str]:
    """Return (method, url) from a curl command string."""
    method = "GET"
    m = re.search(r"--request\s+(\w+)", curl, re.I)
    if m:
        method = m.group(1).upper()
    m = re.search(r"'(https?://[^']+)'|\"(https?://[^\"]+)\"", curl)
    if m:
        return method, m.group(1) or m.group(2)
    raise ValueError(f"Could not parse curl: {curl}")


def test_api_endpoint(endpoint: dict, api_key: str) -> tuple[bool, str]:
    """Verify the endpoint curl works via requests before MCP generation."""
    curl = endpoint.get("curl", "")
    name = endpoint.get("name", "unknown")
    try:
        method, url = parse_curl(curl)
    except ValueError as e:
        return False, f"API pre-test failed for '{name}': {e}"

    headers = {"X-CMC-PRO-API-KEY": api_key, "Accept": "application/json"}
    params = {"limit": 3}

    try:
        if method == "GET":
            resp = requests.get(url, headers=headers, params=params, timeout=30)
        else:
            resp = requests.request(method, url, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and isinstance(data.get("data"), list):
            count = len(data["data"])
            return True, f"API pre-test OK: {name} — {method} {url} returned {count} item(s)"
        if data:
            return True, f"API pre-test OK: {name} — {method} {url} returned JSON"
        return False, f"API pre-test failed for '{name}': empty response"
    except Exception as e:
        return False, f"API pre-test failed for '{name}': {e}"


def validate_generated_code(code: str) -> tuple[bool, str]:
    """Fast checks before spinning up the MCP subprocess."""
    if "@mcp.tool" not in code:
        return False, "Generated code is missing @mcp.tool() decorators on tool functions."
    if "FastMCP" not in code:
        return False, "Generated code is missing FastMCP server setup."
    if "mcp.run()" not in code:
        return False, "Generated code is missing mcp.run() entry point."
    return True, "OK"


class MCPAutoCoder:
    def __init__(
        self,
        input_json_file,
        model_name=MODEL_NAME,
        max_retries=MAX_RETRIES,
        output_name: str | None = None,
        api_key: str | None = None,
    ):
        self.input_json_file = input_json_file
        self.model_name = model_name
        self.max_retries = max_retries
        self.output_name = output_name
        self.api_key = api_key or CMC_API_KEY

    def get_api_definition(self):
        with open(self.input_json_file, 'r') as f:
            return f.read()

    def _load_input(self) -> tuple[list[dict], str, bool]:
        """Returns (endpoints, verified_block, skip_pretest)."""
        raw = json.loads(self.get_api_definition())
        if isinstance(raw, dict) and "endpoints" in raw:
            block = raw.get("prompt_block", "")
            return raw["endpoints"], block, True
        endpoints = raw if isinstance(raw, list) else [raw]
        return endpoints, "", False

    def call_llm(self, prompt):
        print(f"\n[MCP-Auto-Coder] Sending prompt to {self.model_name}...")
        try:
            response = ollama.generate(
                model=self.model_name, 
                prompt=prompt
            )
            return response['response']
        except Exception as e:
            print(f"[MCP-Auto-Coder] Error calling LLM: {e}")
            return None

    def extract_python_code(self, text):
        pattern = r"```python\n(.*?)\n```"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return match.group(1)
        pattern_fallback = r"```\n(.*?)\n```"
        match_fallback = re.search(pattern_fallback, text, re.DOTALL)
        if match_fallback:
            return match_fallback.group(1)
        return text

    def _final_path(self):
        if self.output_name:
            return MCP_SERVERS_DIR / self.output_name
        return MCP_SERVERS_DIR / os.path.basename(self.input_json_file).replace(".json", "_server.py")

    def _save_final_server(self) -> str:
        final_path = self._final_path()
        shutil.copy(WORKSPACE_MCP_SERVER, final_path)
        print(f"[MCP-Auto-Coder] Final server saved to {final_path}")
        return str(final_path)

    async def verify_server(self, test_arguments: dict | None = None):
        """
        Verifies the generated MCP server by running it as a subprocess,
        calling a tool with test args, and checking the response has data.
        """
        server_path = str(WORKSPACE_MCP_SERVER.resolve())
        print(f"[MCP-Auto-Coder] Verifying {server_path}...")

        server_params = StdioServerParameters(
            command=python_executable(),
            args=[server_path],
            env=subprocess_env({"CMC_API_KEY": self.api_key}),
        )
        test_args = test_arguments if test_arguments is not None else {"limit": 3}

        try:
            async with asyncio.timeout(60):
                async with stdio_client(server_params) as (read, write):
                    async with ClientSession(read, write) as session:
                        await session.initialize()

                        tools_result = await session.list_tools()
                        tools = tools_result.tools

                        if not tools:
                            return False, "No tools were registered by the MCP server."

                        print(f"[MCP-Auto-Coder] Found {len(tools)} tools: {[t.name for t in tools]}")

                        first_tool = tools[0]
                        try:
                            result = await session.call_tool(first_tool.name, arguments=test_args)
                        except Exception as e:
                            if "Internal error" in str(e) or "Traceback" in str(e):
                                return False, f"Tool {first_tool.name} crashed: {e}"
                            raise

                        if result.isError:
                            err_text = "".join(
                                getattr(c, "text", str(c)) for c in result.content
                            )
                            return False, f"Tool {first_tool.name} returned error: {err_text[:500]}"

                        text = "".join(getattr(c, "text", str(c)) for c in result.content)
                        if not text.strip():
                            return False, f"Tool {first_tool.name} returned empty response"
                        if '"data"' not in text and '"error"' in text.lower():
                            return False, f"Tool {first_tool.name} returned error payload: {text[:500]}"

                        return True, f"Server verified — tool returned {len(text)} chars of data"

        except asyncio.TimeoutError:
            return False, "Server verification timed out after 60 seconds."
        except Exception as e:
            return False, f"Server failed to start or connect: {e}"


    def run(self):
        ensure_dirs()
        migrate_legacy_files()

        print(f"[MCP-Auto-Coder] Using Python: {python_executable()}")
        if not ensure_requirements_file():
            print("[MCP-Auto-Coder] Warning: could not install all runtime dependencies.")
            
        endpoints, verified_block, skip_pretest = self._load_input()
        api_def = json.dumps(endpoints, indent=2)

        if skip_pretest:
            print("\n[MCP-Auto-Coder] Using verified call context from prober (skipping pre-test).")
        else:
            print("\n[MCP-Auto-Coder] Pre-testing API endpoints...")
            verified_notes = []
            for ep in endpoints:
                ok, msg = test_api_endpoint(ep, self.api_key)
                print(f"[MCP-Auto-Coder] {msg}")
                if not ok:
                    print("[MCP-Auto-Coder] Aborting — fix the curl/API definition before generating MCP code.")
                    return False
                verified_notes.append(msg)
            verified_block = "\n".join(f"- {n}" for n in verified_notes)

        initial_prompt = f"""You are an expert Python developer specializing in the Model Context Protocol (MCP).
Your goal is to create a fully functional MCP server using the `mcp` Python SDK.

The server should implement tools based on the following API definitions:
```json
{api_def}
```

Verified API calls (your code must match this working pattern):
{verified_block}
- Read `CMC_API_KEY` from `os.environ` and send header `X-CMC-PRO-API-KEY` (not Bearer auth).
- Use `response.raise_for_status()` — not `raise_for_status_code()`.
- Use `Optional[str]` / `Optional[int]` for optional parameters, not bare `str = None`.

Requirements:
1. Use the `FastMCP` class. The correct import is: `from mcp.server.fastmcp import FastMCP`.
2. Create a global server instance: `mcp = FastMCP("API Server")`.
3. Define each tool as a standalone function decorated with `@mcp.tool()`. DO NOT wrap them in a class. Every tool function MUST have the `@mcp.tool()` decorator directly above it.
4. Use the `requests` library to make the API calls.
5. The `curl` command in the JSON provides the exact endpoint, method, and headers. Use it to implement the tool logic.
6. Handle authentication by expecting an API key in an environment variable (e.g., `CMC_API_KEY`). For CoinMarketCap, use header `X-CMC-PRO-API-KEY`, not Bearer auth.
7. Ensure all tool arguments are properly typed using Python type hints.
8. The script must end with `if __name__ == "__main__": mcp.run()`.

Runtime note: the verifier runs your script with the same Python as this pipeline (`{python_executable()}`). Dependencies (`mcp`, `requests`) are installed automatically; do not add install steps or alternate interpreters in the generated code.

Write the COMPLETE, fully working Python script. Only output the python code inside a ```python ``` markdown block.
"""

        
        current_prompt = initial_prompt
        
        for attempt in range(1, self.max_retries + 1):
            print(f"\n================ Attempt {attempt} / {self.max_retries} ================")
            
            llm_response = self.call_llm(current_prompt)
            if not llm_response:
                print("[MCP-Auto-Coder] Failed to get response from LLM.")
                break
                
            code = self.extract_python_code(llm_response)
            
            with open(WORKSPACE_MCP_SERVER, 'w') as f:
                f.write(code.strip())

            ok, static_msg = validate_generated_code(code)
            if not ok:
                print(f"[MCP-Auto-Coder] Static check failed: {static_msg}")
                success, message = False, static_msg
            else:
                success, message = asyncio.run(self.verify_server())
                print(f"[MCP-Auto-Coder] Result: {message}")

            if ok and success:
                print(f"[MCP-Auto-Coder] Success! MCP Server is working.")
                self._save_final_server()
                return True

            # Missing packages are an environment issue — fix before asking the LLM again.
            if ok and missing_module_from_error(message) and try_install_missing_from_error(message):
                print("[MCP-Auto-Coder] Installed missing package; re-verifying without consuming a retry...")
                success, message = asyncio.run(self.verify_server())
                print(f"[MCP-Auto-Coder] Result after install: {message}")
                if success:
                    print(f"[MCP-Auto-Coder] Success! MCP Server is working.")
                    self._save_final_server()
                    return True

            if attempt == self.max_retries:
                print(f"\n[MCP-Auto-Coder] Max retries reached. Failed to generate a working MCP server.")
                return False

            print(f"\n[MCP-Auto-Coder] Requesting fix from LLM...")
            current_prompt = f"""You previously wrote an MCP server, but it failed verification.
Here is the code you wrote:
```python
{code}
```

Here is the error:
{message}

Please fix the code and return the entire corrected Python script. Remember to ONLY output the python code inside a ```python ``` markdown block.
"""
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
    else:
        # Default test file if none provided
        test_file = str(
            SCRAPED_API_JSON_DIR / "extracted_cryptocurrency#coinmarketcap-id-map.json"
        )
    
    if os.path.exists(test_file):
        print(f"[MCP-Auto-Coder] Target file: {test_file}")
        coder = MCPAutoCoder(
            test_file,
            output_name="coinmarketcap-id-map_server.py",
        )
        coder.run()
    else:
        print(f"Error: File {test_file} not found.")
        print("Usage: python3 mcp_auto_coder.py <path_to_json_file>")
