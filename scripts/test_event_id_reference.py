#!/usr/bin/env python3
"""Regression tests for Event ID procedure mappings and public output."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_event_id_reference import (  # noqa: E402
    PROCEDURE_CATALOG,
    SNAPSHOT,
    PRODUCTS,
    SOURCE,
    expected_files,
    public_event,
    validate_procedure_catalog,
)


class EventIdProcedureTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        self.procedures = json.loads(PROCEDURE_CATALOG.read_text(encoding="utf-8"))

    def test_current_registry_is_complete(self):
        self.assertEqual([], validate_procedure_catalog(self.catalog, self.procedures))

    def test_missing_mapping_fails(self):
        procedures = copy.deepcopy(self.procedures)
        del procedures["event_mappings"][self.catalog["events"][0]["id"]]
        self.assertTrue(any("missing procedure mapping" in item for item in validate_procedure_catalog(self.catalog, procedures)))

    def test_ready_registry_rejects_draft_content(self):
        procedures = copy.deepcopy(self.procedures)
        procedures["catalog_status"] = "ready"
        next(iter(procedures["procedures"].values()))["review_status"] = "draft"
        next(iter(procedures["event_mappings"].values()))["review_status"] = "draft"
        errors = validate_procedure_catalog(self.catalog, procedures)
        self.assertTrue(any("unreviewed procedure" in item for item in errors))
        self.assertTrue(any("unreviewed mapping" in item for item in errors))

    def test_wrong_product_mapping_fails(self):
        procedures = copy.deepcopy(self.procedures)
        event = self.catalog["events"][0]
        mapping = procedures["event_mappings"][event["id"]]
        for procedure_id in mapping["procedure_ids"]:
            procedures["procedures"][procedure_id]["products"] = []
        errors = validate_procedure_catalog(self.catalog, procedures)
        self.assertTrue(any("no mapped procedure applies" in item for item in errors))

    def test_public_event_omits_internal_join_fields(self):
        event = self.catalog["events"][0]
        mapping = self.procedures["event_mappings"][event["id"]]
        key = event["products"][0]
        product = {
            **PRODUCTS[key],
            "key": key,
            "baseurl": "https://example.invalid/manual/",
            "procedure_by_id": self.procedures["procedures"],
            "event_by_id": {item["id"]: item for item in self.catalog["events"] if key in item["products"]},
        }
        exported = public_event(event, product, mapping)
        self.assertFalse({"id", "kind", "products", "event_sources", "related_ids"} & set(exported))
        self.assertTrue(exported["procedures"])

    def test_product_procedure_uses_sphinx_event_links(self):
        files = expected_files(self.catalog, self.procedures, SOURCE)
        path = (
            SOURCE
            / "winsyslogspecific"
            / "event-id-reference"
            / "procedure"
            / "snmp-verify-trap-path.rst"
        )
        page = files[path]
        self.assertIn(
            ":ref:`WinSyslog Event ID 11016 <winsyslog-event-id-11016>`",
            page,
        )
        self.assertNotIn("- WinSyslog Event ID 11016", page)
        self.assertNotIn(
            SOURCE / "shared" / "troubleshooting" / "event-id" / "snmp-verify-trap-path.rst",
            files,
        )


if __name__ == "__main__":
    unittest.main()
