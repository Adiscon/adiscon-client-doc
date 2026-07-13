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

This procedure applies to MonitorWare Agent.

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

- :ref:`MonitorWare Agent Event ID 11008 <mwagent-event-id-11008>`
- :ref:`MonitorWare Agent Event ID 11021 <mwagent-event-id-11021>`
- :ref:`MonitorWare Agent Event ID 11027 <mwagent-event-id-11027>`
- :ref:`MonitorWare Agent Event ID 11028 <mwagent-event-id-11028>`
- :ref:`MonitorWare Agent Event ID 11041 <mwagent-event-id-11041>`
- :ref:`MonitorWare Agent Event ID 11068 <mwagent-event-id-11068>`
- :ref:`MonitorWare Agent Event ID 11073 <mwagent-event-id-11073>`
- :ref:`MonitorWare Agent Event ID 11116 <mwagent-event-id-11116>`
- :ref:`MonitorWare Agent Event ID 11118 <mwagent-event-id-11118>`
- :ref:`MonitorWare Agent Event ID 11122 <mwagent-event-id-11122>`
- :ref:`MonitorWare Agent Event ID 11146 <mwagent-event-id-11146>`
- :ref:`MonitorWare Agent Event ID 11152 <mwagent-event-id-11152>`
- :ref:`MonitorWare Agent Event ID 11159 <mwagent-event-id-11159>`
- :ref:`MonitorWare Agent Event ID 11163 <mwagent-event-id-11163>`
- :ref:`MonitorWare Agent Event ID 11169 <mwagent-event-id-11169>`
- :ref:`MonitorWare Agent Event ID 11170 <mwagent-event-id-11170>`
- :ref:`MonitorWare Agent Event ID 11175 <mwagent-event-id-11175>`
- :ref:`MonitorWare Agent Event ID 11177 <mwagent-event-id-11177>`
- :ref:`MonitorWare Agent Event ID 11188 <mwagent-event-id-11188>`
- :ref:`MonitorWare Agent Event ID 11190 <mwagent-event-id-11190>`
- :ref:`MonitorWare Agent Event ID 11195 <mwagent-event-id-11195>`
- :ref:`MonitorWare Agent Event ID 11196 <mwagent-event-id-11196>`
- :ref:`MonitorWare Agent Event ID 11197 <mwagent-event-id-11197>`
- :ref:`MonitorWare Agent Event ID 11212 <mwagent-event-id-11212>`
- :ref:`MonitorWare Agent Event ID 11213 <mwagent-event-id-11213>`
- :ref:`MonitorWare Agent Event ID 11214 <mwagent-event-id-11214>`
- :ref:`MonitorWare Agent Event ID 11215 <mwagent-event-id-11215>`


Related procedures
------------------

- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>`
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
