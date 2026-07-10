#!/usr/bin/env python3
"""Generate product Event ID and troubleshooting procedure references."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
SNAPSHOT = SOURCE / "_data" / "himalaya-event-catalog.json"
PROCEDURE_CATALOG = SOURCE / "_data" / "event-id-procedures.json"
PROCEDURE_ROOT = SOURCE / "shared" / "troubleshooting" / "event-id"

PRODUCTS = {
    "winsyslog": {
        "name": "WinSyslog",
        "source_dir": "winsyslogspecific",
        "conf": ROOT / "winsyslog" / "conf.py",
        "tag": "winsyslog or winsyslog_j",
    },
    "eventreporter": {
        "name": "EventReporter",
        "source_dir": "eventreporterspecific",
        "conf": ROOT / "eventreporter" / "conf.py",
        "tag": "eventreporter",
    },
    "mwagent": {
        "name": "MonitorWare Agent",
        "source_dir": "mwagentspecific",
        "conf": ROOT / "mwagent" / "conf.py",
        "tag": "mwagent",
    },
    "rsyslog-client": {
        "name": "rsyslog Windows Agent",
        "source_dir": "rsyslogwaspecific",
        "conf": ROOT / "rsyslog" / "conf.py",
        "tag": "rsyslog",
    },
}

PROCEDURE_ARRAY_FIELDS = (
    "prerequisites",
    "safety",
    "repair_steps",
    "rollback_steps",
    "evidence_to_collect",
    "optional_tools",
    "related_procedures",
)


def conf_value(path: Path, name: str) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(rf"^{name}\s*=\s*(?:u)?['\"]([^'\"]+)['\"]", text, re.M)
    if not match:
        raise ValueError(f"{path}: cannot find {name}")
    return match.group(1)


def conf_baseurl(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^html_baseurl\s*=.*?\bor\s*['\"]([^'\"]+)['\"]", text, re.M)
    if not match:
        raise ValueError(f"{path}: cannot find html_baseurl fallback")
    return match.group(1)


def version_tuple(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in re.findall(r"\d+", value))


def applies_to_version(event: dict, product: str, product_version: str) -> bool:
    introduced = event.get("introduced_in", {}).get(product)
    return introduced is None or version_tuple(introduced) <= version_tuple(product_version)


def rst_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("`", "\\`")


def title_block(title: str, marker: str = "=") -> str:
    return f"{title}\n{marker * len(title)}\n"


def write_utf8_lf(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content)


def publication_ready(catalog: dict, procedures: dict) -> bool:
    return catalog.get("catalog_status") == "ready" and procedures.get("catalog_status") == "ready"


def validate_procedure_catalog(catalog: dict, procedures: dict) -> list[str]:
    errors: list[str] = []
    if procedures.get("schema_version") != 1:
        errors.append("procedure catalog schema_version must be 1")
    if procedures.get("catalog_status") not in {"draft", "ready"}:
        errors.append("procedure catalog catalog_status must be draft or ready")
    definitions = procedures.get("procedures")
    mappings = procedures.get("event_mappings")
    if not isinstance(definitions, dict):
        return errors + ["procedures must be an object"]
    if not isinstance(mappings, dict):
        return errors + ["event_mappings must be an object"]

    events = {event["id"]: event for event in catalog.get("events", [])}
    for missing in sorted(set(events) - set(mappings)):
        errors.append(f"{missing}: missing procedure mapping")
    for stale in sorted(set(mappings) - set(events)):
        errors.append(f"{stale}: stale procedure mapping")

    ready = procedures.get("catalog_status") == "ready"
    documents: dict[str, str] = {}
    for procedure_id, procedure in definitions.items():
        if not re.fullmatch(r"[a-z][a-z0-9.-]+", procedure_id):
            errors.append(f"{procedure_id}: invalid public procedure id")
        if not isinstance(procedure, dict):
            errors.append(f"{procedure_id}: procedure must be an object")
            continue
        for field in ("title", "summary", "document", "when_to_use", "verification", "review_status"):
            if not isinstance(procedure.get(field), str) or not procedure[field].strip():
                errors.append(f"{procedure_id}: {field} must be a non-empty string")
        document = procedure.get("document", "")
        if not document.startswith("shared/troubleshooting/event-id/"):
            errors.append(f"{procedure_id}: document must be in shared/troubleshooting/event-id")
        if document in documents:
            errors.append(f"{procedure_id}: document also used by {documents[document]}")
        documents[document] = procedure_id
        products = procedure.get("products")
        if not isinstance(products, list) or not products or any(item not in PRODUCTS for item in products):
            errors.append(f"{procedure_id}: products must contain known public products")
        for field in PROCEDURE_ARRAY_FIELDS:
            value = procedure.get(field)
            allow_empty = field in {"repair_steps", "rollback_steps", "optional_tools", "related_procedures"}
            if not isinstance(value, list) or (not value and not allow_empty) or not all(
                isinstance(item, str) and item.strip() for item in value
            ):
                errors.append(f"{procedure_id}: {field} must be a string array")
        steps = procedure.get("steps")
        if not isinstance(steps, list) or not steps:
            errors.append(f"{procedure_id}: steps must be a non-empty array")
        else:
            for index, step in enumerate(steps, 1):
                if not isinstance(step, dict) or not isinstance(step.get("instruction"), str) or not step["instruction"].strip():
                    errors.append(f"{procedure_id}: step {index} requires instruction")
                    continue
                for field in ("commands",):
                    value = step.get(field, [])
                    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
                        errors.append(f"{procedure_id}: step {index} {field} must be a string array")
                for field in ("expected", "failure"):
                    if not isinstance(step.get(field), str) or not step[field].strip():
                        errors.append(f"{procedure_id}: step {index} requires {field}")
        product_paths = procedure.get("product_paths", {})
        if not isinstance(product_paths, dict) or any(key not in PRODUCTS for key in product_paths):
            errors.append(f"{procedure_id}: product_paths contains an unknown product")
        elif any(key not in procedure.get("products", []) for key in product_paths):
            errors.append(f"{procedure_id}: product_paths must be a subset of products")
        for related in procedure.get("related_procedures", []):
            if related not in definitions:
                errors.append(f"{procedure_id}: unknown related procedure {related}")
        if procedure.get("review_status") not in {"draft", "reviewed"}:
            errors.append(f"{procedure_id}: invalid review_status")
        if ready and procedure.get("review_status") != "reviewed":
            errors.append(f"{procedure_id}: ready procedure catalog contains an unreviewed procedure")

    for event_id, mapping in mappings.items():
        if not isinstance(mapping, dict):
            errors.append(f"{event_id}: mapping must be an object")
            continue
        disposition = mapping.get("disposition")
        if disposition not in {"self_service", "monitor_only", "escalation_only"}:
            errors.append(f"{event_id}: invalid disposition")
        procedure_ids = mapping.get("procedure_ids")
        if not isinstance(procedure_ids, list) or not procedure_ids or len(procedure_ids) != len(set(procedure_ids)):
            errors.append(f"{event_id}: procedure_ids must be a non-empty ordered unique array")
            continue
        for procedure_id in procedure_ids:
            if procedure_id not in definitions:
                errors.append(f"{event_id}: unknown procedure {procedure_id}")
        if not any(item.startswith("evidence.") or item == "runtime.collect-escalation-evidence" for item in procedure_ids):
            errors.append(f"{event_id}: mapping requires an evidence procedure")
        if disposition == "self_service" and not any(
            not item.startswith("evidence.") and not item.startswith("runtime.") for item in procedure_ids
        ):
            errors.append(f"{event_id}: self-service mapping requires a diagnostic procedure")
        if disposition == "escalation_only" and "runtime.collect-escalation-evidence" not in procedure_ids:
            errors.append(f"{event_id}: escalation-only mapping requires runtime.collect-escalation-evidence")
        event = events.get(event_id)
        if event:
            for product in event["products"]:
                if not any(product in definitions.get(item, {}).get("products", []) for item in procedure_ids):
                    errors.append(f"{event_id}: no mapped procedure applies to {product}")
        if mapping.get("review_status") not in {"draft", "reviewed"}:
            errors.append(f"{event_id}: invalid mapping review_status")
        if ready and mapping.get("review_status") != "reviewed":
            errors.append(f"{event_id}: ready procedure catalog contains an unreviewed mapping")
    return errors


def event_page(product: dict, event: dict, mapping: dict) -> str:
    product_name = product["name"]
    event_id = event["event_id"]
    title = f"{product_name} Event ID {event_id}: {event['title']}"
    description = f"Meaning and troubleshooting for {product_name} Event ID {event_id}: {event['title']}."
    introduced = event["introduced_in"].get(product["key"])
    version_text = introduced or "Current supported versions; original introduction not recorded"
    provider = event["event_sources"][product["key"]]
    procedures = [
        product["procedure_by_id"][procedure_id]
        for procedure_id in mapping["procedure_ids"]
        if procedure_id in product["procedure_by_id"]
    ]

    lines = [
        ":orphan:",
        "",
        f".. _{product['key'].replace('-client', '')}-event-id-{event_id}:",
        "",
        ".. meta::",
        f"   :description: {rst_text(description)}",
        f"   :event-id: {event_id}",
        f"   :event-product: {product_name}",
        f"   :event-severity: {event['severity'].capitalize()}",
        f"   :event-component: {rst_text(event['component'])}",
        "   :event-reference: true",
        "",
        title_block(title).rstrip(),
        "",
        "Answer",
        "------",
        "",
        rst_text(event["meaning"]),
        "",
        "Event details",
        "-------------",
        "",
        f"- **Event ID:** ``{event_id}``",
        f"- **Severity:** {event['severity'].capitalize()}",
        f"- **Component:** {rst_text(event['component'])}",
        f"- **Windows Event Log source:** ``{provider}``",
        f"- **Available since:** {version_text}",
        f"- **Message pattern:** {rst_text(event['message_pattern'])}",
        "",
        "Possible causes",
        "---------------",
        "",
    ]
    lines.extend(f"- {rst_text(item)}" for item in event["likely_causes"])
    lines.extend(["", "Immediate checks", "----------------", ""])
    lines.extend(f"#. {rst_text(item)}" for item in event["troubleshooting_steps"])
    lines.extend(["", "Detailed procedures", "-------------------", ""])
    for procedure in procedures:
        docname = procedure["document"].rsplit("/", 1)[-1]
        lines.append(
            f"- :doc:`{rst_text(procedure['title'])} <../../shared/troubleshooting/event-id/{docname}>` — "
            f"{rst_text(procedure['summary'])}"
        )
    lines.extend(
        [
            "",
            "Verify the result",
            "-----------------",
            "",
            rst_text(event["success_verification"]),
            "",
            "Evidence to collect",
            "-------------------",
            "",
        ]
    )
    lines.extend(f"- {rst_text(item)}" for item in event["evidence_to_collect"])
    lines.extend(["", "Escalation", "----------", ""])
    if mapping["disposition"] == "escalation_only":
        lines.append(
            "No safe general self-service repair is available for this event. Follow the escalation "
            "evidence procedure above and contact Adiscon Support."
        )
    elif mapping["disposition"] == "monitor_only":
        lines.append(
            "This event normally records state rather than a failure. Escalate only when the state was "
            "unexpected or the associated operation does not recover."
        )
    else:
        lines.append(
            "If the event continues after the detailed procedures, collect the listed evidence and "
            "contact Adiscon Support."
        )

    related = event.get("related_ids", [])
    if related:
        lines.extend(["", "Related Event IDs", "-----------------", ""])
        for related_key in related:
            related_event = product["event_by_id"].get(related_key)
            if related_event:
                lines.append(f"- :doc:`Event ID {related_event['event_id']} <event-id-{related_event['event_id']}>`")
    lines.append("")
    return "\n".join(lines)


def procedure_page(procedure_id: str, procedure: dict, catalog: dict, mappings: dict) -> str:
    title = procedure["title"]
    lines = [
        ":orphan:",
        "",
        f".. _event-id-procedure-{procedure_id.replace('.', '-') }:",
        "",
        ".. meta::",
        f"   :description: {rst_text(procedure['summary'])}",
        f"   :procedure-id: {procedure_id}",
        "   :procedure-reference: true",
        "",
        title_block(title).rstrip(),
        "",
        "When to use this procedure",
        "--------------------------",
        "",
        rst_text(procedure["when_to_use"]),
        "",
        "Applies to",
        "----------",
        "",
        "Prerequisites",
        "-------------",
        "",
    ]
    for product in procedure["products"]:
        lines.extend(
            [
                f".. only:: {PRODUCTS[product]['tag']}",
                "",
                f"   This procedure applies to {PRODUCTS[product]['name']}.",
                "",
            ]
        )
    lines.extend(f"- {rst_text(item)}" for item in procedure["prerequisites"])
    lines.extend(["", "Safety", "------", ""])
    lines.extend(f"- {rst_text(item)}" for item in procedure["safety"])
    if procedure.get("product_paths"):
        lines.extend(["", "Configuration paths", "-------------------", ""])
        for product, path_text in procedure["product_paths"].items():
            lines.extend(
                [
                    f".. only:: {PRODUCTS[product]['tag']}",
                    "",
                    f"   **{PRODUCTS[product]['name']}:** {rst_text(path_text)}",
                    "",
                ]
            )
    lines.extend(["Procedure", "---------", ""])
    for step in procedure["steps"]:
        lines.append(f"#. {rst_text(step['instruction'])}")
        if step.get("commands"):
            lines.extend(["", "   .. code-block:: powershell", ""])
            lines.extend(f"      {command}" for command in step["commands"])
        lines.extend(
            [
                "",
                f"   **Expected result:** {rst_text(step['expected'])}",
                "",
                f"   **If it fails:** {rst_text(step['failure'])}",
                "",
            ]
        )
    if procedure["repair_steps"]:
        lines.extend(["Repair", "------", ""])
        lines.extend(f"#. {rst_text(item)}" for item in procedure["repair_steps"])
        lines.append("")
    if procedure["rollback_steps"]:
        lines.extend(["Rollback", "--------", ""])
        lines.extend(f"#. {rst_text(item)}" for item in procedure["rollback_steps"])
        lines.append("")
    lines.extend(["Verify the result", "-----------------", "", rst_text(procedure["verification"]), ""])
    lines.extend(["Evidence to collect", "-------------------", ""])
    lines.extend(f"- {rst_text(item)}" for item in procedure["evidence_to_collect"])
    if procedure["optional_tools"]:
        lines.extend(["", "Optional tools", "--------------", ""])
        lines.extend(f"- {rst_text(item)}" for item in procedure["optional_tools"])

    related_events: dict[str, list[int]] = {key: [] for key in PRODUCTS}
    for event in catalog["events"]:
        mapping = mappings[event["id"]]
        if procedure_id not in mapping["procedure_ids"]:
            continue
        for product in event["products"]:
            if product in procedure["products"]:
                related_events[product].append(event["event_id"])
    if any(related_events.values()):
        lines.extend(["", "Related Event IDs", "-----------------", ""])
        for product, event_ids in related_events.items():
            if not event_ids:
                continue
            lines.extend([f".. only:: {PRODUCTS[product]['tag']}", ""])
            displayed_event_ids = sorted(set(event_ids))[:40]
            for event_id in displayed_event_ids:
                lines.append(f"   - {PRODUCTS[product]['name']} Event ID {event_id}")
            if len(set(event_ids)) > len(displayed_event_ids):
                lines.append(
                    f"   - This procedure is used by {len(set(event_ids)) - len(displayed_event_ids)} "
                    "additional Event IDs; use the product Event ID index to locate them."
                )
            lines.append("")
    if procedure["related_procedures"]:
        lines.extend(["", "Related procedures", "------------------", ""])
        for related in procedure["related_procedures"]:
            related_def = catalog["procedure_definitions"][related]
            related_doc = related_def["document"].rsplit("/", 1)[-1]
            lines.append(f"- :doc:`{rst_text(related_def['title'])} <{related_doc}>`")
        lines.append("")
    return "\n".join(lines)


def index_page(product: dict, events: list[dict]) -> str:
    name = product["name"]
    title = f"{name} product Event ID reference"
    lines = [
        f".. _{product['key'].replace('-client', '')}-event-id-reference:",
        "",
        ".. meta::",
        f"   :description: Complete reference for {name} product-generated Windows Application Event Log IDs, meanings, and troubleshooting.",
        "",
        title_block(title).rstrip(),
        "",
        f"Use this appendix to look up Windows Application Event Log entries generated by {name}.",
        "Each Event ID links to its meaning, immediate checks, exact procedures, and escalation evidence.",
        "",
        "Scope",
        "-----",
        "",
        "This reference covers product service diagnostics emitted by current supported builds.",
        "It does not cover Event IDs collected from other Windows applications or IDs chosen",
        "by an administrator in the Write to Windows Event Log action.",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
        "   procedures",
        "",
        "Event ID index",
        "--------------",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 12 42 16 30",
        "",
        "   * - Event ID",
        "     - Meaning",
        "     - Severity",
        "     - Component",
    ]
    for event in events:
        lines.extend(
            [
                f"   * - :doc:`{event['event_id']} <event-id-{event['event_id']}>`",
                f"     - {rst_text(event['title'])}",
                f"     - {event['severity'].capitalize()}",
                f"     - {rst_text(event['component'])}",
            ]
        )
    lines.append("")
    return "\n".join(lines)


def procedure_index_page(product: dict, procedures: list[tuple[str, dict]]) -> str:
    title = f"{product['name']} Event ID troubleshooting procedures"
    lines = [
        f".. _{product['key'].replace('-client', '')}-event-id-procedures:",
        "",
        ".. meta::",
        f"   :description: Exact diagnostic procedures referenced by {product['name']} Event ID pages.",
        "",
        title_block(title).rstrip(),
        "",
        "Use these procedures from the applicable Event ID page. Each procedure includes commands,",
        "expected results, failure branches, recovery verification, and evidence collection.",
        "",
    ]
    for procedure_id, procedure in procedures:
        docname = procedure["document"].rsplit("/", 1)[-1]
        lines.append(
            f"- :doc:`{rst_text(procedure['title'])} <../../shared/troubleshooting/event-id/{docname}>` — "
            f"{rst_text(procedure['summary'])}"
        )
    lines.append("")
    return "\n".join(lines)


def public_procedure(procedure_id: str, procedure: dict, product: dict) -> dict:
    base = product["baseurl"].rstrip("/") + "/"
    return {
        "id": procedure_id,
        "title": procedure["title"],
        "summary": procedure["summary"],
        "url": base + procedure["document"] + ".html",
        "when_to_use": procedure["when_to_use"],
        "prerequisites": procedure["prerequisites"],
        "safety": procedure["safety"],
        "steps": procedure["steps"],
        "repair_steps": procedure["repair_steps"],
        "rollback_steps": procedure["rollback_steps"],
        "verification": procedure["verification"],
        "evidence_to_collect": procedure["evidence_to_collect"],
        "optional_tools": procedure["optional_tools"],
        "related_procedures": procedure["related_procedures"],
    }


def public_event(event: dict, product: dict, mapping: dict) -> dict:
    base = product["baseurl"].rstrip("/") + "/"
    procedure_links = []
    for procedure_id in mapping["procedure_ids"]:
        procedure = product["procedure_by_id"].get(procedure_id)
        if not procedure:
            continue
        procedure_links.append(
            {
                "id": procedure_id,
                "title": procedure["title"],
                "url": base + procedure["document"] + ".html",
            }
        )
    related_event_ids = []
    for related_id in event.get("related_ids", []):
        related = product["event_by_id"].get(related_id)
        if related:
            related_event_ids.append(related["event_id"])
    return {
        "event_id": event["event_id"],
        "severity": event["severity"],
        "event_source": event["event_sources"][product["key"]],
        "title": event["title"],
        "component": event["component"],
        "message_pattern": event["message_pattern"],
        "meaning": event["meaning"],
        "likely_causes": event["likely_causes"],
        "immediate_checks": event["troubleshooting_steps"],
        "success_verification": event["success_verification"],
        "evidence_to_collect": event["evidence_to_collect"],
        "disposition": mapping["disposition"],
        "introduced_in": event["introduced_in"].get(product["key"]),
        "related_event_ids": sorted(set(related_event_ids)),
        "procedures": procedure_links,
    }


def product_json(catalog: dict, procedure_catalog: dict, product: dict, events: list[dict]) -> str:
    procedures = [
        public_procedure(procedure_id, procedure, product)
        for procedure_id, procedure in product["procedures"]
    ]
    payload = {
        "schema_version": 2,
        "catalog_status": "ready" if publication_ready(catalog, procedure_catalog) else "draft",
        "source_commit": catalog["source_commit"],
        "product": product["key"],
        "product_name": product["name"],
        "product_version": product["version"],
        "procedure_index_url": (
            product["baseurl"].rstrip("/")
            + f"/{product['source_dir']}/event-id-reference/procedures.html"
        ),
        "procedures": procedures,
        "events": [public_event(event, product, product["mappings"][event["id"]]) for event in events],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def llms_text(product: dict) -> str:
    base = product["baseurl"].rstrip("/") + "/"
    index_url = base + product["source_dir"] + "/event-id-reference/index.html"
    procedure_url = base + product["source_dir"] + "/event-id-reference/procedures.html"
    return "\n".join(
        [
            f"# {product['name']} documentation",
            "",
            f"> Canonical documentation for {product['name']} {product['version']}.",
            "",
            "## Event ID reference",
            "",
            f"- Human-readable Event ID index: {index_url}",
            f"- Exact troubleshooting procedures: {procedure_url}",
            f"- Machine-readable Event ID and procedure catalog: {base}event-ids.json",
            f"- Documentation sitemap: {base}sitemap.xml",
            "",
            "HTML pages are authoritative. The JSON catalog and this file are discovery aids.",
            "The reference covers product-generated Windows Application Event Log diagnostics and",
            "excludes externally collected events and administrator-selected action Event IDs.",
            "",
        ]
    )


def navigation_include(catalog: dict, procedure_catalog: dict) -> str:
    lines = [".. Generated by scripts/generate_event_id_reference.py.", ""]
    if publication_ready(catalog, procedure_catalog):
        lines.extend([".. toctree::", "   :maxdepth: 1", "", "   event-id-reference/index", ""])
    return "\n".join(lines)


def expected_files(catalog: dict, procedure_catalog: dict, root: Path) -> dict[Path, str]:
    files: dict[Path, str] = {}
    definitions = procedure_catalog["procedures"]
    mappings = procedure_catalog["event_mappings"]
    procedure_context = dict(catalog)
    procedure_context["procedure_definitions"] = definitions
    for procedure_id, procedure in definitions.items():
        path = root / (procedure["document"] + ".rst")
        files[path] = procedure_page(procedure_id, procedure, procedure_context, mappings)

    for key, definition in PRODUCTS.items():
        product = dict(definition)
        product["key"] = key
        product["version"] = conf_value(product["conf"], "version")
        product["baseurl"] = conf_baseurl(product["conf"])
        events = [
            event
            for event in catalog["events"]
            if key in event["products"] and applies_to_version(event, key, product["version"])
        ]
        events.sort(key=lambda event: (event["event_id"], event["id"]))
        product["event_by_id"] = {event["id"]: event for event in events}
        product["mappings"] = mappings
        product["procedures"] = sorted(
            (
                (procedure_id, procedure)
                for procedure_id, procedure in definitions.items()
                if key in procedure["products"]
                and any(procedure_id in mappings[event["id"]]["procedure_ids"] for event in events)
            ),
            key=lambda item: (item[1]["title"].lower(), item[0]),
        )
        product["procedure_by_id"] = dict(product["procedures"])
        page_dir = root / product["source_dir"] / "event-id-reference"
        files[page_dir / "index.rst"] = index_page(product, events)
        files[page_dir / "procedures.rst"] = procedure_index_page(product, product["procedures"])
        for event in events:
            files[page_dir / f"event-id-{event['event_id']}.rst"] = event_page(
                product, event, mappings[event["id"]]
            )
        artifact_dir = root / "_generated" / "event-ids" / key
        files[artifact_dir / "event-ids.json"] = product_json(catalog, procedure_catalog, product, events)
        files[artifact_dir / "llms.txt"] = llms_text(product)
        files[artifact_dir / "navigation.inc"] = navigation_include(catalog, procedure_catalog)
    return files


def generate(catalog: dict, procedure_catalog: dict, check: bool) -> int:
    if catalog.get("catalog_status") not in {"draft", "ready"}:
        print("ERROR: catalog_status must be draft or ready")
        return 1
    errors = validate_procedure_catalog(catalog, procedure_catalog)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    files = expected_files(catalog, procedure_catalog, SOURCE)
    generated_roots = [
        SOURCE / product["source_dir"] / "event-id-reference" for product in PRODUCTS.values()
    ] + [SOURCE / "_generated" / "event-ids", PROCEDURE_ROOT]

    if check:
        stale = []
        for path, content in files.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        expected_paths = set(files)
        for generated_root in generated_roots:
            if generated_root.is_dir():
                for path in generated_root.rglob("*"):
                    if path.is_file() and path not in expected_paths:
                        stale.append(path.relative_to(ROOT).as_posix())
        if stale:
            print("ERROR: generated Event ID files are stale:")
            for error in sorted(set(stale)):
                print(f"  {error}")
            return 1
        print(f"verified {len(files)} generated Event ID and procedure files")
        return 0

    for generated_root in generated_roots:
        if generated_root.is_dir():
            shutil.rmtree(generated_root)
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        write_utf8_lf(path, content)
    print(f"generated {len(files)} Event ID and procedure files")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=SNAPSHOT)
    parser.add_argument("--procedures", type=Path, default=PROCEDURE_CATALOG)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    procedure_catalog = json.loads(args.procedures.read_text(encoding="utf-8"))
    return generate(catalog, procedure_catalog, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
