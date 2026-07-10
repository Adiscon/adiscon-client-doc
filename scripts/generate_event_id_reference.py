#!/usr/bin/env python3
"""Generate product Event ID reference pages from the Himalaya public export."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
SNAPSHOT = SOURCE / "_data" / "himalaya-event-catalog.json"

PRODUCTS = {
    "winsyslog": {
        "name": "WinSyslog",
        "source_dir": "winsyslogspecific",
        "conf": ROOT / "winsyslog" / "conf.py",
    },
    "eventreporter": {
        "name": "EventReporter",
        "source_dir": "eventreporterspecific",
        "conf": ROOT / "eventreporter" / "conf.py",
    },
    "mwagent": {
        "name": "MonitorWare Agent",
        "source_dir": "mwagentspecific",
        "conf": ROOT / "mwagent" / "conf.py",
    },
    "rsyslog-client": {
        "name": "rsyslog Windows Agent",
        "source_dir": "rsyslogwaspecific",
        "conf": ROOT / "rsyslog" / "conf.py",
    },
}


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


def event_page(product: dict, event: dict) -> str:
    product_name = product["name"]
    event_id = event["event_id"]
    title = f"{product_name} Event ID {event_id}: {event['title']}"
    description = (
        f"Meaning and troubleshooting for {product_name} Event ID {event_id}: "
        f"{event['title']}."
    )
    introduced = event["introduced_in"].get(product["key"])
    version_text = introduced or "Current supported versions; original introduction not recorded"
    provider = event["event_sources"][product["key"]]

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
    lines.extend(["", "Troubleshooting", "---------------", ""])
    lines.extend(f"#. {rst_text(item)}" for item in event["troubleshooting_steps"])
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
    if event["resolution_type"] == "escalate":
        lines.append(
            "No safe general self-service repair is available for this event. "
            "Collect the evidence above and contact Adiscon Support."
        )
    elif event["resolution_type"] == "monitor":
        lines.append(
            "This event normally records state rather than a failure. Escalate only when "
            "the state was unexpected or the associated operation does not recover."
        )
    else:
        lines.append(
            "If the event continues after the troubleshooting steps, collect the evidence "
            "above and contact Adiscon Support."
        )

    related = event.get("related_ids", [])
    if related:
        lines.extend(["", "Related Event IDs", "-----------------", ""])
        event_by_id = product["event_by_id"]
        for related_key in related:
            related_event = event_by_id.get(related_key)
            if related_event:
                lines.append(
                    f"- :doc:`Event ID {related_event['event_id']} <event-id-{related_event['event_id']}>`"
                )
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
        "Each Event ID links to its meaning, likely causes, troubleshooting steps, and escalation evidence.",
        "",
        "Scope",
        "-----",
        "",
        "This reference covers product service diagnostics emitted by current supported builds.",
        "It does not cover Event IDs collected from other Windows applications or IDs chosen",
        "by an administrator in the Write to Windows Event Log action.",
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


def product_json(catalog: dict, product: dict, events: list[dict]) -> str:
    payload = {
        "schema_version": catalog["schema_version"],
        "source_commit": catalog["source_commit"],
        "product": product["key"],
        "product_name": product["name"],
        "product_version": product["version"],
        "events": events,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def llms_text(product: dict) -> str:
    base = product["baseurl"].rstrip("/") + "/"
    index_url = base + product["source_dir"] + "/event-id-reference/index.html"
    return "\n".join(
        [
            f"# {product['name']} documentation",
            "",
            f"> Canonical documentation for {product['name']} {product['version']}.",
            "",
            "## Event ID reference",
            "",
            f"- Human-readable index: {index_url}",
            f"- Machine-readable Event ID catalog: {base}event-ids.json",
            f"- Documentation sitemap: {base}sitemap.xml",
            "",
            "The Event ID reference covers product-generated Windows Application Event Log",
            "diagnostics. It excludes events collected from other providers and user-selected",
            "IDs emitted by the Write to Windows Event Log action.",
            "",
        ]
    )


def navigation_include(catalog: dict) -> str:
    """Return navigation only after engineering marks the catalog ready."""
    lines = [".. Generated by scripts/generate_event_id_reference.py.", ""]
    if catalog["catalog_status"] == "ready":
        lines.extend(
            [
                ".. toctree::",
                "   :maxdepth: 1",
                "",
                "   event-id-reference/index",
                "",
            ]
        )
    return "\n".join(lines)


def expected_files(catalog: dict, root: Path) -> dict[Path, str]:
    files: dict[Path, str] = {}
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
        page_dir = root / product["source_dir"] / "event-id-reference"
        files[page_dir / "index.rst"] = index_page(product, events)
        for event in events:
            files[page_dir / f"event-id-{event['event_id']}.rst"] = event_page(product, event)
        artifact_dir = root / "_generated" / "event-ids" / key
        files[artifact_dir / "event-ids.json"] = product_json(catalog, product, events)
        files[artifact_dir / "llms.txt"] = llms_text(product)
        files[artifact_dir / "navigation.inc"] = navigation_include(catalog)
    return files


def generate(catalog: dict, check: bool) -> int:
    if catalog.get("catalog_status") not in {"draft", "ready"}:
        print("ERROR: catalog_status must be draft or ready")
        return 1
    files = expected_files(catalog, SOURCE)
    generated_roots = [
        SOURCE / product["source_dir"] / "event-id-reference" for product in PRODUCTS.values()
    ] + [SOURCE / "_generated" / "event-ids"]

    if check:
        errors = []
        for path, content in files.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                errors.append(path.relative_to(ROOT).as_posix())
        expected_paths = set(files)
        for generated_root in generated_roots:
            if generated_root.is_dir():
                for path in generated_root.rglob("*"):
                    if path.is_file() and path not in expected_paths:
                        errors.append(path.relative_to(ROOT).as_posix())
        if errors:
            print("ERROR: generated Event ID files are stale:")
            for error in sorted(set(errors)):
                print(f"  {error}")
            return 1
        print(f"verified {len(files)} generated Event ID files")
        return 0

    for generated_root in generated_roots:
        if generated_root.is_dir():
            shutil.rmtree(generated_root)
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        write_utf8_lf(path, content)
    print(f"generated {len(files)} Event ID files")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=SNAPSHOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    return generate(catalog, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
