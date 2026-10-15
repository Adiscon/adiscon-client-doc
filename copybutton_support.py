"""Register accessible local styling around the maintained copybutton extension."""

from pathlib import Path


def _register_accessibility_stylesheet(app) -> None:
    """Make the local copybutton stylesheet available to HTML output."""
    static_path = str(Path(__file__).resolve().parent / "_static")
    static_paths = list(app.config.html_static_path or [])
    if static_path not in static_paths:
        static_paths.append(static_path)
        app.config.html_static_path = static_paths

    app.add_css_file("copybutton-accessibility.css", priority=600)


def setup(app):
    """Load upstream copy buttons and register the keyboard visibility styles."""
    app.setup_extension("sphinx_copybutton")
    app.connect("builder-inited", _register_accessibility_stylesheet)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
