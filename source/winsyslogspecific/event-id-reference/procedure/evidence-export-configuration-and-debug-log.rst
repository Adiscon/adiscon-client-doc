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

This procedure applies to WinSyslog.

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

#. Export settings as a text registry file, then enable the minimum debug level that reproduces the problem.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Item -LiteralPath '<CONFIG_EXPORT>' | Format-List FullName,Length,LastWriteTime
      Get-Item -LiteralPath '<DEBUG_LOG>' | Format-List FullName,Length,LastWriteTime

   **Expected result:** Both files exist, are readable, and cover the recorded reproduction interval.

   **If it fails:** Verify the service account can write the debug directory and restart only if the setting requires it.

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

- :ref:`WinSyslog Event ID 100 <winsyslog-event-id-100>`
- :ref:`WinSyslog Event ID 101 <winsyslog-event-id-101>`
- :ref:`WinSyslog Event ID 102 <winsyslog-event-id-102>`
- :ref:`WinSyslog Event ID 103 <winsyslog-event-id-103>`
- :ref:`WinSyslog Event ID 104 <winsyslog-event-id-104>`
- :ref:`WinSyslog Event ID 105 <winsyslog-event-id-105>`
- :ref:`WinSyslog Event ID 106 <winsyslog-event-id-106>`
- :ref:`WinSyslog Event ID 108 <winsyslog-event-id-108>`
- :ref:`WinSyslog Event ID 118 <winsyslog-event-id-118>`
- :ref:`WinSyslog Event ID 125 <winsyslog-event-id-125>`
- :ref:`WinSyslog Event ID 900 <winsyslog-event-id-900>`
- :ref:`WinSyslog Event ID 901 <winsyslog-event-id-901>`
- :ref:`WinSyslog Event ID 11000 <winsyslog-event-id-11000>`
- :ref:`WinSyslog Event ID 11001 <winsyslog-event-id-11001>`
- :ref:`WinSyslog Event ID 11002 <winsyslog-event-id-11002>`
- :ref:`WinSyslog Event ID 11003 <winsyslog-event-id-11003>`
- :ref:`WinSyslog Event ID 11004 <winsyslog-event-id-11004>`
- :ref:`WinSyslog Event ID 11005 <winsyslog-event-id-11005>`
- :ref:`WinSyslog Event ID 11006 <winsyslog-event-id-11006>`
- :ref:`WinSyslog Event ID 11007 <winsyslog-event-id-11007>`
- :ref:`WinSyslog Event ID 11009 <winsyslog-event-id-11009>`
- :ref:`WinSyslog Event ID 11010 <winsyslog-event-id-11010>`
- :ref:`WinSyslog Event ID 11011 <winsyslog-event-id-11011>`
- :ref:`WinSyslog Event ID 11012 <winsyslog-event-id-11012>`
- :ref:`WinSyslog Event ID 11013 <winsyslog-event-id-11013>`
- :ref:`WinSyslog Event ID 11014 <winsyslog-event-id-11014>`
- :ref:`WinSyslog Event ID 11015 <winsyslog-event-id-11015>`
- :ref:`WinSyslog Event ID 11016 <winsyslog-event-id-11016>`
- :ref:`WinSyslog Event ID 11017 <winsyslog-event-id-11017>`
- :ref:`WinSyslog Event ID 11018 <winsyslog-event-id-11018>`
- :ref:`WinSyslog Event ID 11019 <winsyslog-event-id-11019>`
- :ref:`WinSyslog Event ID 11020 <winsyslog-event-id-11020>`
- :ref:`WinSyslog Event ID 11022 <winsyslog-event-id-11022>`
- :ref:`WinSyslog Event ID 11023 <winsyslog-event-id-11023>`
- :ref:`WinSyslog Event ID 11024 <winsyslog-event-id-11024>`
- :ref:`WinSyslog Event ID 11025 <winsyslog-event-id-11025>`
- :ref:`WinSyslog Event ID 11026 <winsyslog-event-id-11026>`
- :ref:`WinSyslog Event ID 11027 <winsyslog-event-id-11027>`
- :ref:`WinSyslog Event ID 11028 <winsyslog-event-id-11028>`
- :ref:`WinSyslog Event ID 11029 <winsyslog-event-id-11029>`
- This procedure is used by 173 additional Event IDs; use the product Event ID index to locate them.
