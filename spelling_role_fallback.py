"""Fallback Sphinx extension for ``:spelling:ignore:`` / ``:spelling:word:``.

Used when ``sphinxcontrib.spelling`` is unavailable (missing package or Enchant).
Keeps HTML/HTMLHelp builds working under ``-W`` when sources use those roles.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.domains import Domain


def _passthrough_role(
    typ: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Dict[str, Any] | None = None,
    content: List[str] | None = None,
) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
    """Render the role content as plain text (no spellcheck metadata)."""
    return [nodes.inline(rawtext, text)], []


class SpellingRoleFallbackDomain(Domain):
    """Minimal stand-in for sphinxcontrib.spelling's domain roles."""

    name = "spelling"
    label = "Spelling (fallback)"
    roles = {
        "ignore": _passthrough_role,
        "word": _passthrough_role,
    }

    def get_objects(self):
        return []

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        return None

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        return []

    def merge_domaindata(self, docnames, otherdata):
        return


def setup(app: Sphinx) -> Dict[str, Any]:
    # If the real spelling extension already registered the domain, do nothing.
    if "spelling" in app.registry.domains:
        return {
            "version": "1.0",
            "parallel_read_safe": True,
            "parallel_write_safe": True,
        }

    app.add_domain(SpellingRoleFallbackDomain)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
