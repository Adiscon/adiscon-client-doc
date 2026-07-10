:orphan:

.. _event-id-procedure-license-verify-license-state:

.. meta::
   :description: Confirm product, version, validity, edition, and required feature without exposing license data.
   :procedure-id: license.verify-license-state
   :procedure-reference: true

Verify product license and feature entitlement state
====================================================

When to use this procedure
--------------------------

Use for trial, license validation, edition, and feature-denied events.

Applies to
----------

Prerequisites
-------------

.. only:: eventreporter

   This procedure applies to EventReporter.

.. only:: winsyslog or winsyslog_j

   This procedure applies to WinSyslog.

.. only:: mwagent

   This procedure applies to MonitorWare Agent.

.. only:: rsyslog

   This procedure applies to rsyslog Windows Agent.

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Never publish license files, signed payloads, keys, customer identifiers, or activation material.
- Do not edit a signed license file.

Configuration paths
-------------------

.. only:: eventreporter

   **EventReporter:** Configuration Client > General > License.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > General > License.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > General > License.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > General > License.

Procedure
---------

#. Record product version, displayed license status, edition, and feature named in the event without copying the license payload.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Item -LiteralPath '<PRODUCT_EXECUTABLE>' | Select-Object -ExpandProperty VersionInfo | Format-List ProductName,ProductVersion,FileVersion

   **Expected result:** The signed license targets the running product/version and includes the configured feature.

   **If it fails:** Install the authorized license or disable unsupported configuration; never edit signed data.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 118
   - WinSyslog Event ID 125
   - WinSyslog Event ID 900
   - WinSyslog Event ID 901
   - WinSyslog Event ID 11005
   - WinSyslog Event ID 11043
   - WinSyslog Event ID 11044

.. only:: eventreporter

   - EventReporter Event ID 118
   - EventReporter Event ID 901
   - EventReporter Event ID 11005
   - EventReporter Event ID 11043
   - EventReporter Event ID 11044

.. only:: mwagent

   - MonitorWare Agent Event ID 118
   - MonitorWare Agent Event ID 11005
   - MonitorWare Agent Event ID 11043
   - MonitorWare Agent Event ID 11044

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 118
   - rsyslog Windows Agent Event ID 11005
   - rsyslog Windows Agent Event ID 11043
   - rsyslog Windows Agent Event ID 11044
