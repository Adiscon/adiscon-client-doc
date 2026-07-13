#!/usr/bin/env python3
"""Validate public product Event ID JSON does not expose internal join data."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "source" / "_generated" / "event-ids"
FORBIDDEN_EVENT_FIELDS = {"id", "kind", "products", "event_sources", "related_ids", "review_status"}
FORBIDDEN_TEXT = (
    re.compile(r"\b(?:DIAG|EVMSG)_[A-Z0-9_]+\b"),
    re.compile(r"[A-Za-z0-9_./-]+\.(?:cpp|cxx|h)(?:\b|:\d+)", re.IGNORECASE),
    re.compile(r"\bC(?:action|info(?:source|unit)|que|misc|service)[A-Za-z0-9_]*\b"),
)


def main() -> int:
    errors: list[str] = []
    for path in sorted(ARTIFACTS.glob("*/event-ids.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("schema_version") != 2:
            errors.append(f"{path}: schema_version must be 2")
        procedures = data.get("procedures", [])
        procedure_ids = {item.get("id") for item in procedures}
        if len(procedure_ids) != len(procedures) or None in procedure_ids:
            errors.append(f"{path}: procedure IDs must be unique and non-empty")
        for event in data.get("events", []):
            exposed = FORBIDDEN_EVENT_FIELDS & set(event)
            if exposed:
                errors.append(f"{path}: Event ID {event.get('event_id')} exposes {sorted(exposed)}")
            if not event.get("procedures"):
                errors.append(f"{path}: Event ID {event.get('event_id')} has no procedures")
            for procedure in event.get("procedures", []):
                if procedure.get("id") not in procedure_ids:
                    errors.append(
                        f"{path}: Event ID {event.get('event_id')} references missing procedure {procedure.get('id')}"
                    )
                if not str(procedure.get("url", "")).startswith("https://"):
                    errors.append(f"{path}: procedure URL must be canonical HTTPS")
            public_text = json.dumps(event, ensure_ascii=False)
            if any(pattern.search(public_text) for pattern in FORBIDDEN_TEXT):
                errors.append(f"{path}: Event ID {event.get('event_id')} exposes implementation text")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("validated public Event ID and procedure JSON artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
