"""
Shared Python runtime helpers for the auto-coder pipeline.

Ensures subprocesses use the same interpreter as the parent process and that
required packages are installed before generated scripts are executed.
"""

from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

# Pip package names for imports used by generated MCP servers and this pipeline.
MCP_SERVER_PACKAGES = ("mcp", "requests")

# import name -> pip distribution (when they differ)
PIP_NAME_FOR_IMPORT = {
    "PIL": "pillow",
    "cv2": "opencv-python",
    "sklearn": "scikit-learn",
    "yaml": "pyyaml",
}

_DIR = Path(__file__).resolve().parent
REQUIREMENTS_FILE = _DIR / "requirements.txt"


def python_executable() -> str:
    """Interpreter running this pipeline — use for all subprocesses."""
    return sys.executable


def _pip_install(*packages: str) -> bool:
    if not packages:
        return True
    unique = sorted(set(packages))
    print(f"[Runtime] Installing packages with {python_executable()}: {', '.join(unique)}")
    result = subprocess.run(
        [python_executable(), "-m", "pip", "install", *unique],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[Runtime] pip install failed:\n{result.stderr or result.stdout}")
        return False
    return True


def _importable(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def ensure_packages(*packages: str) -> bool:
    """Install any listed packages that are not importable in the current interpreter."""
    missing = [p for p in packages if not _importable(p)]
    if not missing:
        return True
    return _pip_install(*missing)


def ensure_requirements_file(path: Path | None = None) -> bool:
    """pip install -r requirements.txt if the file exists."""
    req = path or REQUIREMENTS_FILE
    if not req.is_file():
        return ensure_packages(*MCP_SERVER_PACKAGES)

    print(f"[Runtime] Ensuring dependencies from {req}")
    result = subprocess.run(
        [python_executable(), "-m", "pip", "install", "-r", str(req)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[Runtime] pip install -r failed:\n{result.stderr or result.stdout}")
        return False
    return True


def pip_name_for_import(module_name: str) -> str:
    root = module_name.split(".")[0]
    return PIP_NAME_FOR_IMPORT.get(root, root)


def missing_module_from_error(error: str) -> str | None:
    """Extract root module name from ModuleNotFoundError text, if present."""
    m = re.search(r"No module named ['\"]([^'\"]+)['\"]", error)
    if not m:
        return None
    return m.group(1).split(".")[0]


def try_install_missing_from_error(error: str) -> bool:
    """If error is a missing import, pip install it and return True."""
    module = missing_module_from_error(error)
    if not module:
        return False
    if _importable(module):
        return True
    return _pip_install(pip_name_for_import(module))


def subprocess_env(extra: dict | None = None) -> dict:
    """Environment for child processes: inherit parent env and prefer same Python."""
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    if extra:
        env.update(extra)
    return env
