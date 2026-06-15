"""
Project directory layout for the API → MCP pipeline.

  workspace/                    ephemeral scratch (safe to delete between runs)
  output/
    scraped_api_json/           JSON scraped from API documentation pages
    successful_curl_commands/   proven working curl → requests probe scripts
    mcp_servers/                generated MCP server files
  data/                         cached inputs (scraped JSON, etc.)
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ── Workspace (temp / scratch) ───────────────────────────────────────────────
WORKSPACE_DIR = ROOT / "workspace"
WORKSPACE_PAGE_HTML = WORKSPACE_DIR / "page.html"
WORKSPACE_OPERATIONS_JSON = WORKSPACE_DIR / "operations.json"
WORKSPACE_WINDOW_DATA_JSON = WORKSPACE_DIR / "window_data.json"
WORKSPACE_PAGE_EXTRACTOR = WORKSPACE_DIR / "page_extractor.py"
WORKSPACE_MCP_SERVER = WORKSPACE_DIR / "mcp_server.py"
WORKSPACE_API_PROBE = WORKSPACE_DIR / "api_probe.py"
WORKSPACE_ENDPOINT_JSON = WORKSPACE_DIR / "endpoint.json"

# ── Output (kept after success) ──────────────────────────────────────────────
OUTPUT_DIR = ROOT / "output"
SCRAPED_API_JSON_DIR = OUTPUT_DIR / "scraped_api_json"
SUCCESSFUL_CURL_COMMANDS_DIR = OUTPUT_DIR / "successful_curl_commands"
MCP_SERVERS_DIR = OUTPUT_DIR / "mcp_servers"

# Renamed folders (read fallback + one-time migrate source)
LEGACY_OUTPUT_EXTRACTIONS_DIR = OUTPUT_DIR / "extractions"
LEGACY_OUTPUT_VERIFIED_CALLS_DIR = OUTPUT_DIR / "verified_calls"


def successful_curl_output_dir(slug: str) -> Path:
    """Per-endpoint folder under successful_curl_commands/."""
    return SUCCESSFUL_CURL_COMMANDS_DIR / slug


# ── Data (inputs / cache) ────────────────────────────────────────────────────
DATA_DIR = ROOT / "data"
SCRAPED_JSON_DIR = DATA_DIR / "scraped_jsons"

# ── Legacy paths (read fallback only) ────────────────────────────────────────
LEGACY_SCRAPED_JSON_DIR = ROOT / "scraped_jsons"
LEGACY_EXTRACTIONS_DIR = ROOT / "llm_successful_scripts"
LEGACY_MCP_SERVERS_DIR = ROOT / "mcp_successful_servers"


def ensure_dirs() -> None:
    """Create workspace, output, and data directories."""
    for d in (
        WORKSPACE_DIR,
        SCRAPED_API_JSON_DIR,
        SUCCESSFUL_CURL_COMMANDS_DIR,
        MCP_SERVERS_DIR,
        SCRAPED_JSON_DIR,
    ):
        d.mkdir(parents=True, exist_ok=True)


def scraped_json_candidates(slug: str) -> list[Path]:
    """Paths to check for a pre-scraped JSON file (new layout first)."""
    name = f"{slug}.json"
    return [
        SCRAPED_JSON_DIR / name,
        LEGACY_SCRAPED_JSON_DIR / name,
    ]


def _merge_dir_contents(src: Path, dst: Path) -> None:
    """Move files/subdirs from src into dst without overwriting existing."""
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            _merge_dir_contents(item, target)
        elif not target.exists():
            shutil.move(str(item), str(target))


def _remove_empty_dirs(path: Path) -> None:
    if not path.is_dir():
        return
    for child in list(path.iterdir()):
        if child.is_dir():
            _remove_empty_dirs(child)
    try:
        path.rmdir()
    except OSError:
        pass


def _migrate_output_folder(old: Path, new: Path) -> None:
    if not old.is_dir() or old == new:
        return
    _merge_dir_contents(old, new)
    _remove_empty_dirs(old)


def migrate_legacy_files() -> None:
    """One-time move of old root-level temp/output files into subfolders."""
    ensure_dirs()
    moves: list[tuple[Path, Path]] = [
        (ROOT / "temp_page.html", WORKSPACE_PAGE_HTML),
        (ROOT / "temp_operations.json", WORKSPACE_OPERATIONS_JSON),
        (ROOT / "temp_window_data.json", WORKSPACE_WINDOW_DATA_JSON),
        (ROOT / "temp_page_extractor.py", WORKSPACE_PAGE_EXTRACTOR),
        (ROOT / "temp_mcp_server.py", WORKSPACE_MCP_SERVER),
    ]
    for src, dst in moves:
        if not src.is_file():
            continue
        if dst.exists():
            src.unlink()
        else:
            shutil.move(str(src), str(dst))

    _migrate_output_folder(LEGACY_OUTPUT_EXTRACTIONS_DIR, SCRAPED_API_JSON_DIR)
    _migrate_output_folder(LEGACY_OUTPUT_VERIFIED_CALLS_DIR, SUCCESSFUL_CURL_COMMANDS_DIR)

    if LEGACY_EXTRACTIONS_DIR.is_dir():
        for f in LEGACY_EXTRACTIONS_DIR.iterdir():
            if f.is_file():
                target = SCRAPED_API_JSON_DIR / f.name
                if not target.exists():
                    shutil.move(str(f), str(target))

    if LEGACY_MCP_SERVERS_DIR.is_dir():
        for f in LEGACY_MCP_SERVERS_DIR.iterdir():
            if f.is_file():
                target = MCP_SERVERS_DIR / f.name
                if not target.exists():
                    shutil.move(str(f), str(target))

    if LEGACY_SCRAPED_JSON_DIR.is_dir():
        for f in LEGACY_SCRAPED_JSON_DIR.iterdir():
            if f.is_file():
                target = SCRAPED_JSON_DIR / f.name
                if not target.exists():
                    shutil.move(str(f), str(target))
