:orphan:

.. _event-id-procedure-evidence-export-configuration-and-debug-log:

.. meta::
   :description: Create a text configuration export and time-bounded debug capture, then disable debugging.
   :procedure-id: evidence.export-configuration-and-debug-log
   :procedure-reference: true

Export configuration and collect a bounded debug log
====================================================

When to use this procedure
--------------------------

Use this when configuration or runtime sequencing must be reviewed.

Applies to
----------

This procedure applies to EventReporter.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Disable debug logging immediately after the bounded capture.
- Remove credentials, private keys, license material, and unrelated customer data before sharing.

Configuration path
------------------

Configuration Client > Computer > Export Settings to Registry File; then General > Debug.

Procedure
---------

#. Before changing settings, use Computer > Export Settings to Registry File and save a pre-change text export in a protected working directory.

   **Expected result:** A readable pre-change export exists and its modification time precedes the troubleshooting change.

   **If it fails:** Do not continue with a state-changing repair until a readable pre-change export exists.

#. Record the start time, enable only the debug output required to reproduce once, then record the end time and disable debugging immediately.

   .. code-block:: powershell

      $captureStart=Get-Date; $captureStart.ToString('o')
      Get-Item -LiteralPath '<CONFIG_EXPORT>' | Format-List FullName,Length,LastWriteTime
      Get-Item -LiteralPath '<DEBUG_LOG>' | Format-List FullName,Length,LastWriteTime
      $captureEnd=Get-Date; $captureEnd.ToString('o')

   **Expected result:** The export and debug log are readable, the log covers the recorded interval, and debug output is disabled after the reproduction.

   **If it fails:** Verify the configured debug path and service-account write access. Do not leave debugging enabled while investigating a missing log.

#. Preserve only the bounded interval around one uniquely identifiable test, then create redacted copies for review.

   **Expected result:** The test and its outcome can be correlated across the redacted export, Event Log, and bounded debug interval.

   **If it fails:** Repeat only after correcting the capture window; do not collect an unbounded debug log.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The capture start and end timestamps, complete Event Log entry, and neighboring product events.
- The pre-change configuration export and bounded debug log from the same interval.
- Redacted review copies with credentials, license data, private keys, addresses, hostnames, paths, database identifiers, certificate identities, and environment-specific service, ruleset, and action names removed.

Related Event IDs
-----------------

- :ref:`EventReporter Event ID 100 <eventreporter-event-id-100>`
- :ref:`EventReporter Event ID 101 <eventreporter-event-id-101>`
- :ref:`EventReporter Event ID 102 <eventreporter-event-id-102>`
- :ref:`EventReporter Event ID 103 <eventreporter-event-id-103>`
- :ref:`EventReporter Event ID 104 <eventreporter-event-id-104>`
- :ref:`EventReporter Event ID 105 <eventreporter-event-id-105>`
- :ref:`EventReporter Event ID 106 <eventreporter-event-id-106>`
- :ref:`EventReporter Event ID 108 <eventreporter-event-id-108>`
- :ref:`EventReporter Event ID 118 <eventreporter-event-id-118>`
- :ref:`EventReporter Event ID 901 <eventreporter-event-id-901>`
- :ref:`EventReporter Event ID 11000 <eventreporter-event-id-11000>`
- :ref:`EventReporter Event ID 11001 <eventreporter-event-id-11001>`
- :ref:`EventReporter Event ID 11002 <eventreporter-event-id-11002>`
- :ref:`EventReporter Event ID 11003 <eventreporter-event-id-11003>`
- :ref:`EventReporter Event ID 11004 <eventreporter-event-id-11004>`
- :ref:`EventReporter Event ID 11005 <eventreporter-event-id-11005>`
- :ref:`EventReporter Event ID 11006 <eventreporter-event-id-11006>`
- :ref:`EventReporter Event ID 11007 <eventreporter-event-id-11007>`
- :ref:`EventReporter Event ID 11009 <eventreporter-event-id-11009>`
- :ref:`EventReporter Event ID 11010 <eventreporter-event-id-11010>`
- :ref:`EventReporter Event ID 11011 <eventreporter-event-id-11011>`
- :ref:`EventReporter Event ID 11012 <eventreporter-event-id-11012>`
- :ref:`EventReporter Event ID 11013 <eventreporter-event-id-11013>`
- :ref:`EventReporter Event ID 11014 <eventreporter-event-id-11014>`
- :ref:`EventReporter Event ID 11015 <eventreporter-event-id-11015>`
- :ref:`EventReporter Event ID 11016 <eventreporter-event-id-11016>`
- :ref:`EventReporter Event ID 11017 <eventreporter-event-id-11017>`
- :ref:`EventReporter Event ID 11018 <eventreporter-event-id-11018>`
- :ref:`EventReporter Event ID 11019 <eventreporter-event-id-11019>`
- :ref:`EventReporter Event ID 11020 <eventreporter-event-id-11020>`
- :ref:`EventReporter Event ID 11022 <eventreporter-event-id-11022>`
- :ref:`EventReporter Event ID 11023 <eventreporter-event-id-11023>`
- :ref:`EventReporter Event ID 11024 <eventreporter-event-id-11024>`
- :ref:`EventReporter Event ID 11025 <eventreporter-event-id-11025>`
- :ref:`EventReporter Event ID 11026 <eventreporter-event-id-11026>`
- :ref:`EventReporter Event ID 11027 <eventreporter-event-id-11027>`
- :ref:`EventReporter Event ID 11028 <eventreporter-event-id-11028>`
- :ref:`EventReporter Event ID 11029 <eventreporter-event-id-11029>`
- :ref:`EventReporter Event ID 11030 <eventreporter-event-id-11030>`
- :ref:`EventReporter Event ID 11031 <eventreporter-event-id-11031>`
- This procedure is used by 177 additional Event IDs; use the product Event ID index to locate them.
