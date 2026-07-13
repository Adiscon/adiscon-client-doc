"""Shared helpers for Sphinx configuration files."""

from __future__ import annotations

import json
import html
import importlib
import os
import re
import shutil
import sys
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


def get_sphinx_builder_name() -> str:
    """Return the requested Sphinx builder from env or command-line args."""
    builder = os.environ.get("SPHINX_BUILDER")
    if builder:
        return builder

    for index, arg in enumerate(sys.argv):
        if arg in {"-b", "--builder"} and index + 1 < len(sys.argv):
            return sys.argv[index + 1]
        if arg.startswith("--builder="):
            return arg.split("=", 1)[1]

    return ""


def configure_builder_extensions(extensions: List[str]) -> List[str]:
    """Remove extensions that are only useful for specific Sphinx builders."""
    builder = get_sphinx_builder_name()
    if builder and builder not in {"html", "dirhtml", "singlehtml"}:
        extensions = [extension for extension in extensions if extension != "sphinx_sitemap"]

    return extensions


def configure_pdf_defaults(config: Dict) -> None:
    """Apply PDF defaults shared by all product manuals."""
    pdf_style_dir = str(Path(__file__).resolve().parent / "pdfstyles")
    existing_style_path = config.get("pdf_style_path", [])
    if isinstance(existing_style_path, str):
        existing_style_path = [existing_style_path]

    config["pdf_break_level"] = -1
    config["pdf_breakside"] = "any"
    config["pdf_cover_template"] = "pdf-cover.tmpl"
    config["pdf_fit_mode"] = "shrink"
    config["pdf_style_path"] = [
        pdf_style_dir,
        *[path for path in existing_style_path if path != pdf_style_dir],
    ]
    config["pdf_stylesheets"] = ["sphinx", "a4", "adiscon-readable"]
    config["pdf_toc_depth"] = 3
    config["pdf_use_coverpage"] = True


def relax_pdf_odd_page_breaks(app) -> None:
    """Avoid blank filler pages caused by rst2pdf's hardcoded odd-page breaks."""
    if getattr(app.builder, "name", "") != "pdf":
        return

    try:
        from docutils import nodes
        from sphinx import addnodes
        import rst2pdf.flowables as flowables
        import rst2pdf.genelements as genelements
        import rst2pdf.pdfbuilder as pdfbuilder
        import rst2pdf.utils as utils
    except Exception:
        return

    if getattr(utils.parseRaw, "_adiscon_relaxed", False):
        return

    original_parse_raw = utils.parseRaw

    def parse_raw_without_odd_breaks(data, node):
        return original_parse_raw(data.replace("OddPageBreak", "PageBreak"), node)

    parse_raw_without_odd_breaks._adiscon_relaxed = True
    utils.parseRaw = parse_raw_without_odd_breaks
    genelements.parseRaw = parse_raw_without_odd_breaks

    if getattr(pdfbuilder.PDFContents.build_contents, "_adiscon_source_pages", False):
        return

    def build_source_page_contents(self, node, source_depth=0):
        entries = []
        max_source_depth = self.toc_depth

        def source_page_sections(parent, parent_depth):
            for child in parent.children:
                if isinstance(child, addnodes.start_of_file):
                    child_depth = parent_depth + 1
                    if child_depth <= max_source_depth:
                        for section in child.children:
                            if isinstance(section, nodes.section):
                                yield section, child_depth
                elif isinstance(child, nodes.section):
                    if parent_depth == 0 and any(
                        isinstance(descendant, addnodes.start_of_file)
                        for descendant in child.traverse(addnodes.start_of_file)
                    ):
                        yield child, parent_depth
                    else:
                        yield from source_page_sections(child, parent_depth)
                elif isinstance(child, nodes.compound):
                    yield from source_page_sections(child, parent_depth)

        for section, section_depth in source_page_sections(node, source_depth):
            section["pdf_toc_source_page"] = True
            section["pdf_source_depth"] = section_depth
            title = section[0]
            auto = title.get("auto")
            entrytext = self.copy_and_filter(title)
            reference = nodes.reference("", "", refid=section["ids"][0], *entrytext)
            ref_id = self.document.set_id(reference)
            entry = nodes.paragraph("", "", reference)
            item = nodes.list_item("", entry)

            if (
                self.backlinks in ("entry", "top")
                and title.next_node(nodes.reference) is None
            ):
                if self.backlinks == "entry":
                    title["refid"] = ref_id
                elif self.backlinks == "top":
                    title["refid"] = self.toc_id

            if section_depth < max_source_depth:
                item += self.build_contents(section, section_depth)

            entries.append(item)

        if not entries:
            return []

        contents = nodes.bullet_list("", *entries)
        if auto:
            contents["classes"].append("auto-toc")
        return contents

    build_source_page_contents._adiscon_source_pages = True
    pdfbuilder.PDFContents.build_contents = build_source_page_contents

    if not getattr(genelements.HandleTitle.gather_elements, "_adiscon_source_breaks", False):
        original_gather_title_elements = genelements.HandleTitle.gather_elements

        def gather_title_elements_with_source_breaks(self, client, node, style):
            elements = original_gather_title_elements(self, client, node, style)
            section = getattr(node, "parent", None)
            if (
                isinstance(section, nodes.section)
                and section.get("pdf_toc_source_page", False)
                and section.get("pdf_source_depth", 0) >= 3
            ):
                elements.insert(0, flowables.MyPageBreak(breakTo="any"))
                node.elements = elements
            return elements

        gather_title_elements_with_source_breaks._adiscon_source_breaks = True
        genelements.HandleTitle.gather_elements = gather_title_elements_with_source_breaks

    if getattr(flowables.MyTableOfContents.notify, "_adiscon_source_pages", False):
        return

    original_notify = flowables.MyTableOfContents.notify

    def notify_source_page_entries(self, kind, stuff):
        if self.parent is None:
            node = stuff[4]
            section = getattr(node, "parent", None)
            if section is None or not section.get("pdf_toc_source_page", False):
                return
        return original_notify(self, kind, stuff)

    notify_source_page_entries._adiscon_source_pages = True
    flowables.MyTableOfContents.notify = notify_source_page_entries


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
    doctree_meta = {}
    if doctree is not None:
        for meta_node in doctree.traverse(nodes.meta):
            name = meta_node.get("name")
            content = meta_node.get("content")
            if name and content:
                doctree_meta[name] = content
    metatags = context.get("metatags", "")
    for match in re.finditer(
        r'<meta\s+content="([^"]*)"\s+name="([^"]*)"\s*/?>', metatags
    ):
        doctree_meta.setdefault(match.group(2), html.unescape(match.group(1)))

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
    if not description:
        description = doctree_meta.get("description")

    if description:
        json_ld["description"] = description

    def meta_value(name):
        if name in doctree_meta:
            return doctree_meta[name]
        if not isinstance(meta, dict):
            return None
        value = meta.get(name)
        if isinstance(value, list):
            return value[0] if value else None
        return value

    event_id = meta_value("event-id")
    event_product = meta_value("event-product")
    event_component = meta_value("event-component")
    event_severity = meta_value("event-severity")
    if event_id and event_product:
        json_ld["identifier"] = {
            "@type": "PropertyValue",
            "propertyID": "Windows Event ID",
            "value": str(event_id),
        }
        json_ld["about"] = [
            {"@type": "SoftwareApplication", "name": str(event_product)},
            {"@type": "DefinedTerm", "name": str(event_component or "Product diagnostics")},
            {"@type": "DefinedTerm", "name": str(event_severity or "Event severity")},
        ]
        parent_page = pagename.rsplit("/", 1)[0] + "/index.html"
        json_ld["isPartOf"] = {
            "@type": "CollectionPage",
            "name": f"{event_product} product Event ID reference",
            "url": urljoin(baseurl, parent_page),
        }

    procedure_id = meta_value("procedure-id")
    if procedure_id:
        procedure_catalog = _load_event_id_procedure_catalog()
        procedure = procedure_catalog.get("procedures", {}).get(str(procedure_id))
        if procedure:
            json_ld["@type"] = "HowTo"
            json_ld["name"] = procedure["title"]
            json_ld["step"] = [
                {
                    "@type": "HowToStep",
                    "position": position,
                    "name": step["instruction"],
                    "text": " ".join(
                        [step["instruction"], *step.get("commands", []), step["expected"], step["failure"]]
                    ),
                }
                for position, step in enumerate(procedure["steps"], 1)
            ]
            json_ld["about"] = [
                {"@type": "SoftwareApplication", "name": app.config.project}
            ]
            product_dirs = {
                "WinSyslog": "winsyslogspecific",
                "EventReporter": "eventreporterspecific",
                "MonitorWare Agent": "mwagentspecific",
                "rsyslog Windows Agent": "rsyslogwaspecific",
            }
            source_dir = product_dirs.get(app.config.project)
            if source_dir:
                json_ld["isPartOf"] = {
                    "@type": "CollectionPage",
                    "name": f"{app.config.project} Event ID troubleshooting procedures",
                    "url": urljoin(baseurl, f"{source_dir}/event-id-reference/procedures.html"),
                }

    json_ld_string = json.dumps(json_ld, indent=2)
    script_tag = f'\n<script type="application/ld+json">\n{json_ld_string}\n</script>\n'
    context["metatags"] = metatags + script_tag


def enable_json_ld(app) -> None:
    """Enable JSON-LD unless disabled via DISABLE_JSON_LD env variable."""
    disable_json_ld = os.environ.get("DISABLE_JSON_LD", "").lower() in {"1", "true", "yes"}
    if disable_json_ld:
        return

    app.connect("html-page-context", _inject_json_ld)


def _load_event_id_catalog() -> dict:
    """Load the imported catalog used to gate public Event ID publication."""
    catalog_path = Path(__file__).resolve().parent / "source" / "_data" / "himalaya-event-catalog.json"
    if not catalog_path.is_file():
        return {}
    return json.loads(catalog_path.read_text(encoding="utf-8"))


def _load_event_id_procedure_catalog() -> dict:
    """Load the docs-owned troubleshooting procedure registry."""
    path = Path(__file__).resolve().parent / "source" / "_data" / "event-id-procedures.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _event_id_publication_ready() -> bool:
    """Return true only when event facts and detailed procedures are reviewed."""
    return (
        _load_event_id_catalog().get("catalog_status") == "ready"
        and _load_event_id_procedure_catalog().get("catalog_status") == "ready"
    )


def _copy_event_id_artifacts(app, exception) -> None:
    """Copy the generated JSON catalog and AI discovery index to HTML roots."""
    if exception is not None or app.builder.name != "html":
        return

    if not _event_id_publication_ready():
        for filename in ("event-ids.json", "llms.txt"):
            (Path(app.outdir) / filename).unlink(missing_ok=True)
        return

    product_keys = {
        "WinSyslog": "winsyslog",
        "EventReporter": "eventreporter",
        "MonitorWare Agent": "mwagent",
        "rsyslog Windows Agent": "rsyslog-client",
    }
    product_key = product_keys.get(app.config.project)
    if not product_key:
        return
    artifact_dir = Path(__file__).resolve().parent / "source" / "_generated" / "event-ids" / product_key
    for filename in ("event-ids.json", "llms.txt"):
        source = artifact_dir / filename
        if not source.is_file():
            raise FileNotFoundError(f"missing generated Event ID artifact: {source}")
        shutil.copyfile(source, Path(app.outdir) / filename)


def _exclude_other_event_id_references(app, config) -> None:
    """Keep generated product references isolated in each manual build."""
    product_dirs = {
        "WinSyslog": "winsyslogspecific",
        "EventReporter": "eventreporterspecific",
        "MonitorWare Agent": "mwagentspecific",
        "rsyslog Windows Agent": "rsyslogwaspecific",
    }
    current_dir = product_dirs.get(config.project)
    if not current_dir:
        return
    ready = _event_id_publication_ready()
    if ready:
        app.tags.add("event_id_catalog_ready")
    for source_dir in product_dirs.values():
        if ready and source_dir == current_dir:
            continue
        pattern = f"{source_dir}/event-id-reference/**"
        if pattern not in config.exclude_patterns:
            config.exclude_patterns.append(pattern)
    procedure_pattern = "shared/troubleshooting/event-id/**"
    if not ready:
        if procedure_pattern not in config.exclude_patterns:
            config.exclude_patterns.append(procedure_pattern)
        return

    product_keys = {
        "WinSyslog": "winsyslog",
        "EventReporter": "eventreporter",
        "MonitorWare Agent": "mwagent",
        "rsyslog Windows Agent": "rsyslog-client",
    }
    product_key = product_keys.get(config.project)
    for procedure in _load_event_id_procedure_catalog().get("procedures", {}).values():
        if product_key not in procedure.get("products", []):
            pattern = procedure["document"] + ".rst"
            if pattern not in config.exclude_patterns:
                config.exclude_patterns.append(pattern)


def enable_event_id_artifacts(app) -> None:
    """Publish root-level Event ID JSON and llms.txt files for product manuals."""
    app.connect("config-inited", _exclude_other_event_id_references)
    app.connect("build-finished", _copy_event_id_artifacts)


def _apply_htmlhelp_utf8(app) -> None:
    """Override the HTMLHelp builder encoding to UTF-8.

    sphinxcontrib-htmlhelp maps ``language = 'en'`` to ``cp1252`` (Windows
    Western-European codepage).  On Japanese Windows systems the CHM viewer
    (IE/Trident engine) ignores the ``<meta charset>`` declaration and falls
    back to the system ANSI code page (cp932/Shift-JIS).  Any cp1252 byte in
    the range 0x81-0x9F is then consumed as a Shift-JIS double-byte lead byte,
    swallowing the next ASCII character and garbling the text.

    Forcing UTF-8 resolves this: the HTMLHelp builder already HTML-escapes all
    non-ASCII body text to ``&#NNNN;`` entities, so the file content is
    effectively 7-bit ASCII.  Declaring UTF-8 causes the CHM viewer on *any*
    Windows locale to decode that ASCII-safe content correctly.
    """
    if getattr(app.builder, 'encoding', None) not in (None, 'utf-8'):
        app.builder.encoding = 'utf-8'


def fix_htmlhelp_encoding(app) -> None:
    """Connect the UTF-8 encoding fix to the builder-inited event.

    Call this from ``setup(app)`` in each product ``conf.py``::

        def setup(app):
            fix_htmlhelp_encoding(app)
    """
    app.connect('builder-inited', _apply_htmlhelp_utf8)
