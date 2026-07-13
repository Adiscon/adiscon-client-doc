:orphan:

.. _event-id-procedure-runtime-collect-escalation-evidence:

.. meta::
   :description: Capture a bounded reproducible support package without unsafe generic repair.
   :procedure-id: runtime.collect-escalation-evidence
   :procedure-reference: true

Collect evidence for an escalation-only runtime event
=====================================================

When to use this procedure
--------------------------

Use when the Event ID page states that no safe self-service repair exists.

Applies to
----------

This procedure applies to WinSyslog.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Do not delete queues, clear Event Logs, reset collection positions, disable TLS validation, or broaden permissions.
- Preserve timestamps and pre-change state.

Configuration path
------------------

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Preserve the first event, neighboring events, exact reproduction sequence, and pre-change state.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-ComputerInfo | Select-Object WindowsProductName,WindowsVersion,OsBuildNumber,OsArchitecture
      Get-CimInstance Win32_Service -Filter "Name='<SERVICE_NAME>'" | Format-List Name,State,StartName,ExitCode

   **Expected result:** The support package identifies environment, service context, configuration, and the bounded failure interval.

   **If it fails:** Do not repeatedly restart, clear logs, reset positions, broaden permissions, or alter queue files to obtain different evidence.

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

- :ref:`WinSyslog Event ID 11008 <winsyslog-event-id-11008>`
- :ref:`WinSyslog Event ID 11021 <winsyslog-event-id-11021>`
- :ref:`WinSyslog Event ID 11068 <winsyslog-event-id-11068>`
- :ref:`WinSyslog Event ID 11175 <winsyslog-event-id-11175>`
- :ref:`WinSyslog Event ID 11177 <winsyslog-event-id-11177>`
- :ref:`WinSyslog Event ID 11188 <winsyslog-event-id-11188>`
- :ref:`WinSyslog Event ID 11190 <winsyslog-event-id-11190>`
- :ref:`WinSyslog Event ID 11195 <winsyslog-event-id-11195>`
- :ref:`WinSyslog Event ID 11196 <winsyslog-event-id-11196>`
- :ref:`WinSyslog Event ID 11197 <winsyslog-event-id-11197>`
- :ref:`WinSyslog Event ID 11212 <winsyslog-event-id-11212>`
- :ref:`WinSyslog Event ID 11213 <winsyslog-event-id-11213>`
- :ref:`WinSyslog Event ID 11214 <winsyslog-event-id-11214>`


Related procedures
------------------

- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>`
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
