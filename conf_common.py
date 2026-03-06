"""Shared helpers for Sphinx configuration files."""

from __future__ import annotations

import json
import importlib
import os
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin

from docutils import nodes


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


def get_shared_templates_path() -> str:
    """Return path to shared templates (e.g. for CHM localStorage compatibility)."""
    return str(Path(__file__).resolve().parent / "_templates")


def enable_spelling_extension(extensions: List[str]) -> List[str]:
    """Add spelling extension only when the package and Enchant C library are available."""
    if "sphinxcontrib.spelling" in extensions:
        return extensions

    try:
        import sphinxcontrib.spelling  # noqa: F401
        extensions.append("sphinxcontrib.spelling")
    except Exception:  # pragma: no cover - e.g. Enchant C library not installed
        pass

    return extensions


def _extract_faq_entries(doctree: Optional[nodes.document]) -> List[Dict]:
    """Build FAQPage entries from section titles and paragraph content."""
    faq_entries: List[Dict] = []
    if doctree is None:
        return faq_entries

    for section in doctree.traverse(nodes.section):
        title_node = section.next_node(nodes.title)
        if title_node is None:
            continue

        question = title_node.astext().strip()
        if not question:
            continue

        answers: List[str] = []
        for child in section.children:
            if isinstance(child, nodes.title):
                continue

            text = child.astext().strip()
            if text:
                answers.append(text)

        if not answers:
            continue

        faq_entries.append(
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "\n\n".join(answers),
                },
            }
        )

    return faq_entries


def _inject_json_ld(app, pagename, templatename, context, doctree):
    """Inject schema.org JSON-LD into HTML page metatags."""
    if app.builder.format != "html":
        return

    baseurl = app.config.html_baseurl
    if not baseurl:
        return

    canonical_url = urljoin(baseurl, f"{pagename}.html")
    meta = context.get("meta")

    author_name = None
    if isinstance(meta, dict):
        author_name = meta.get("author") or meta.get("authors")
        if isinstance(author_name, list):
            author_name = author_name[0] if author_name else None

    if not author_name:
        author_name = context.get("author") or app.config.author

    faq_entries = _extract_faq_entries(doctree) if pagename.startswith("faq/") else []

    json_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage" if faq_entries else "TechArticle",
        "headline": context.get("title", pagename),
        "author": author_name,
        "url": canonical_url,
        "inLanguage": context.get("language", app.config.language) or "en",
    }

    if faq_entries:
        json_ld["mainEntity"] = faq_entries

    description = None
    if isinstance(meta, dict):
        description = meta.get("description")
        if isinstance(description, list) and description:
            description = description[0]

    if description:
        json_ld["description"] = description

    metatags = context.get("metatags", "")
    json_ld_string = json.dumps(json_ld, indent=2)
    script_tag = f'\n<script type="application/ld+json">\n{json_ld_string}\n</script>\n'
    context["metatags"] = metatags + script_tag


def enable_json_ld(app) -> None:
    """Enable JSON-LD unless disabled via DISABLE_JSON_LD env variable."""
    disable_json_ld = os.environ.get("DISABLE_JSON_LD", "").lower() in {"1", "true", "yes"}
    if disable_json_ld:
        return

    app.connect("html-page-context", _inject_json_ld)
