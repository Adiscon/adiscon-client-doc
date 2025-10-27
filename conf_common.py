"""Shared helpers for Sphinx configuration files."""

from __future__ import annotations

import importlib
from pathlib import Path
from typing import List


def _shared_directory(current_file: str) -> Path:
    """Return the repository-wide shared configuration directory."""
    conf_path = Path(current_file).resolve()
    return conf_path.parents[1] / "source" / "shared"


def load_linkcheck_ignore(current_file: str) -> List[str]:
    """Load ignored URL patterns for Sphinx linkcheck from a text file."""
    ignore_file = _shared_directory(current_file) / "linkcheck-ignore.txt"
    if not ignore_file.exists():
        return []

    patterns: List[str] = []
    for raw_line in ignore_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        patterns.append(line)
    return patterns


def get_spelling_word_list(current_file: str) -> str:
    """Return the absolute path to the spelling word list file."""
    word_list = _shared_directory(current_file) / "spelling-wordlist.txt"
    return str(word_list)


def enable_spelling_extension(extensions: List[str]) -> List[str]:
    """Ensure the spelling builder is available when dependencies are installed."""
    if "sphinxcontrib.spelling" in extensions:
        return extensions

    try:
        has_extension = importlib.util.find_spec("sphinxcontrib.spelling") is not None
    except Exception:  # pragma: no cover - defensive guard for importlib issues
        has_extension = False

    if has_extension:
        extensions.append("sphinxcontrib.spelling")

    return extensions
