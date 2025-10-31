"""Minimal Sphinx configuration for building the shared content library."""
import importlib

project = "Shared Content Library"
author = "Adiscon GmbH"
copyright = "2025, Adiscon GmbH"

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
]

master_doc = "index"
source_suffix = ".rst"
language = "en"
todo_include_todos = True

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "actions/*",
]

# The shared library frequently references documents that live in the
# product-specific trees. Those references resolve during full builds but are
# unavailable when we render the shared subset in isolation, so the associated
# warnings can be suppressed safely here.
suppress_warnings = [
    "toc.not_readable",
    "ref.doc",
]

if importlib.util.find_spec("furo") is not None:
    html_theme = "furo"
    html_theme_options = {
        "sidebar_hide_name": False,
        "light_css_variables": {
            "color-brand-primary": "#336699",
            "color-brand-content": "#336699",
        },
        "dark_css_variables": {
            "color-brand-primary": "#5599dd",
            "color-brand-content": "#5599dd",
        },
    }
else:
    html_theme = "alabaster"
    html_theme_options = {}

html_static_path = []
