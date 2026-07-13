#!/usr/bin/env python3
"""Write a review-oriented summary for an automated Event ID docs PR."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load(path: Path) -> dict:
    if not path.is_file():
        return {"events": [], "source_commit": "none"}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    old = load(args.old)
    new = load(args.new)
    old_events = {event["id"]: event for event in old.get("events", [])}
    new_events = {event["id"]: event for event in new.get("events", [])}
    added = sorted(set(new_events) - set(old_events))
    removed = sorted(set(old_events) - set(new_events))
    changed = sorted(
        key for key in set(old_events) & set(new_events) if old_events[key] != new_events[key]
    )
    counts = Counter(
        product for event in new_events.values() for product in event.get("products", [])
    )
    lines = [
        "## Event ID documentation synchronization",
        "",
        f"- Himalaya source commit: `{new.get('source_commit')}`",
        f"- Catalog entries: {len(new_events)}",
        f"- Added: {len(added)}",
        f"- Removed: {len(removed)}",
        f"- Changed or applicability-updated: {len(changed)}",
        "",
        "### Product counts",
        "",
    ]
    for product, count in sorted(counts.items()):
        lines.append(f"- `{product}`: {count}")
    for heading, values in (("Added IDs", added), ("Removed IDs", removed), ("Changed IDs", changed)):
        if values:
            lines.extend(["", f"### {heading}", ""])
            lines.extend(f"- `{value}`" for value in values[:100])
            if len(values) > 100:
                lines.append(f"- ...and {len(values) - 100} more")
    lines.extend(
        [
            "",
            "This PR is generated. Edit the Himalaya diagnostic catalog, not generated RST or JSON files.",
            "Engineering review is required before publication.",
            "",
        ]
    )
    args.output.write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
