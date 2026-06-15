"""
pipeline.py
===========
Three-stage pipeline: URL → scraped JSON → verified curl → MCP server.

  Stage 1  llm_page_extractor   → output/scraped_api_json/extracted_*.json
  Stage 2  api_call_prober       → output/successful_curl_commands/<slug>/verified.json
  Stage 3  mcp_auto_coder        → output/mcp_servers/<fragment>_server.py

Usage:
  export CMC_API_KEY="your-key"
  python pipeline.py "https://pro.coinmarketcap.com/api/documentation/pro-api-reference/cryptocurrency#coinmarketcap-id-map"
"""

from __future__ import annotations

import argparse
import os
import sys

from api_call_prober import APICallProber
from llm_page_extractor import LLMPageExtractor
from mcp_auto_coder import CMC_API_KEY, MCPAutoCoder
from python_runtime import ensure_requirements_file, python_executable
from paths import (
    MCP_SERVERS_DIR,
    SCRAPED_API_JSON_DIR,
    ensure_dirs,
    migrate_legacy_files,
    successful_curl_output_dir,
)


def paths_from_url(url: str) -> tuple[str, str, str, str, str]:
    """Return (file_slug, fragment, extracted_path, verified_path, mcp_output_name)."""
    file_slug = url.strip("/").split("/")[-1]
    fragment = url.split("#")[-1] if "#" in url else file_slug
    extracted_path = SCRAPED_API_JSON_DIR / f"extracted_{file_slug}.json"
    verified_path = successful_curl_output_dir(file_slug) / "verified.json"
    mcp_output = f"{fragment}_server.py"
    return file_slug, fragment, str(extracted_path), str(verified_path), mcp_output


def run_pipeline(
    url: str,
    api_key: str | None = None,
    model_name: str = "gemma4:e2b-mlx",
    max_retries: int = 5,
) -> str | None:
    api_key = api_key or CMC_API_KEY
    file_slug, fragment, extracted_path, verified_path, mcp_output = paths_from_url(url)

    ensure_dirs()
    migrate_legacy_files()

    print(f"\nPipeline Python: {python_executable()}")
    if not ensure_requirements_file():
        print("Warning: could not install all dependencies from requirements.txt.")

    env_backup: dict[str, str | None] = {}
    if api_key:
        for var in ("CMC_API_KEY", "API_KEY"):
            env_backup[var] = os.environ.get(var)
            os.environ[var] = api_key

    try:
        print("\n" + "=" * 60)
        print("  STAGE 1 — Scrape API documentation (llm_page_extractor)")
        print("=" * 60)

        extractor = LLMPageExtractor(model_name=model_name, max_retries=max_retries)
        extracted = extractor.run(target_url=url)
        if not extracted:
            print("\nStage 1 failed — extraction returned nothing.")
            return None
        if not os.path.isfile(extracted_path):
            print(f"\nStage 1 failed — expected file not found: {extracted_path}")
            return None
        print(f"\nStage 1 complete → {extracted_path}")

        print("\n" + "=" * 60)
        print("  STAGE 2 — Verify curl command (api_call_prober)")
        print("=" * 60)

        prober = APICallProber(
            input_json_file=extracted_path,
            model_name=model_name,
            max_retries=max_retries,
        )
        verified_result = prober.run()
        if not verified_result:
            print("\nStage 2 failed — could not verify API call.")
            return None
        if not os.path.isfile(verified_path):
            print(f"\nStage 2 failed — expected file not found: {verified_path}")
            return None
        print(f"\nStage 2 complete → {verified_path}")

        print("\n" + "=" * 60)
        print("  STAGE 3 — Generate MCP server (mcp_auto_coder)")
        print("=" * 60)

        coder = MCPAutoCoder(
            input_json_file=verified_path,
            model_name=model_name,
            max_retries=max_retries,
            output_name=mcp_output,
            api_key=api_key,
        )
        if not coder.run():
            print("\nStage 3 failed — MCP server generation failed.")
            return None

        final_path = MCP_SERVERS_DIR / mcp_output
        if final_path.is_file():
            print(f"\nPipeline complete!")
            print(f"  scraped JSON     → {extracted_path}")
            print(f"  verified curl    → {verified_path}")
            print(f"  MCP server       → {final_path}")
            return str(final_path)

        print(f"\nStage 3 finished but server not found at {final_path}")
        return None

    finally:
        for var, original in env_backup.items():
            if original is None:
                os.environ.pop(var, None)
            else:
                os.environ[var] = original


def main():
    parser = argparse.ArgumentParser(
        description="URL → scraped JSON → verified curl → MCP server."
    )
    parser.add_argument("url", help="API documentation URL (may include #fragment)")
    parser.add_argument(
        "--api-key",
        default=os.environ.get("API_KEY") or CMC_API_KEY,
        help="API key for live calls (defaults to built-in CMC key)",
    )
    parser.add_argument(
        "--model",
        default="gemma4:e2b-mlx",
        help="Ollama model for all stages",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=5,
        help="Max LLM retries per stage",
    )
    args = parser.parse_args()

    result = run_pipeline(
        url=args.url,
        api_key=args.api_key,
        model_name=args.model,
        max_retries=args.retries,
    )
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
