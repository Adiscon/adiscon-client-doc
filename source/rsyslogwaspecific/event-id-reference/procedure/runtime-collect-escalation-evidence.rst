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

This procedure applies to rsyslog Windows Agent.

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

- :ref:`rsyslog Windows Agent Event ID 11008 <rsyslog-event-id-11008>`
- :ref:`rsyslog Windows Agent Event ID 11021 <rsyslog-event-id-11021>`
- :ref:`rsyslog Windows Agent Event ID 11027 <rsyslog-event-id-11027>`
- :ref:`rsyslog Windows Agent Event ID 11028 <rsyslog-event-id-11028>`
- :ref:`rsyslog Windows Agent Event ID 11041 <rsyslog-event-id-11041>`
- :ref:`rsyslog Windows Agent Event ID 11068 <rsyslog-event-id-11068>`
- :ref:`rsyslog Windows Agent Event ID 11073 <rsyslog-event-id-11073>`
- :ref:`rsyslog Windows Agent Event ID 11116 <rsyslog-event-id-11116>`
- :ref:`rsyslog Windows Agent Event ID 11118 <rsyslog-event-id-11118>`
- :ref:`rsyslog Windows Agent Event ID 11122 <rsyslog-event-id-11122>`
- :ref:`rsyslog Windows Agent Event ID 11146 <rsyslog-event-id-11146>`
- :ref:`rsyslog Windows Agent Event ID 11152 <rsyslog-event-id-11152>`
- :ref:`rsyslog Windows Agent Event ID 11159 <rsyslog-event-id-11159>`
- :ref:`rsyslog Windows Agent Event ID 11163 <rsyslog-event-id-11163>`
- :ref:`rsyslog Windows Agent Event ID 11169 <rsyslog-event-id-11169>`
- :ref:`rsyslog Windows Agent Event ID 11170 <rsyslog-event-id-11170>`
- :ref:`rsyslog Windows Agent Event ID 11175 <rsyslog-event-id-11175>`
- :ref:`rsyslog Windows Agent Event ID 11177 <rsyslog-event-id-11177>`
- :ref:`rsyslog Windows Agent Event ID 11188 <rsyslog-event-id-11188>`
- :ref:`rsyslog Windows Agent Event ID 11190 <rsyslog-event-id-11190>`
- :ref:`rsyslog Windows Agent Event ID 11195 <rsyslog-event-id-11195>`
- :ref:`rsyslog Windows Agent Event ID 11196 <rsyslog-event-id-11196>`
- :ref:`rsyslog Windows Agent Event ID 11197 <rsyslog-event-id-11197>`
- :ref:`rsyslog Windows Agent Event ID 11212 <rsyslog-event-id-11212>`
- :ref:`rsyslog Windows Agent Event ID 11213 <rsyslog-event-id-11213>`
- :ref:`rsyslog Windows Agent Event ID 11214 <rsyslog-event-id-11214>`
- :ref:`rsyslog Windows Agent Event ID 11215 <rsyslog-event-id-11215>`


Related procedures
------------------

- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>`
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
