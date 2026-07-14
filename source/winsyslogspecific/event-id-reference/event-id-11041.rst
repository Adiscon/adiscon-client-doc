:orphan:

.. _winsyslog-event-id-11041:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11041: Start Program action received an unexpected wait result.
   :event-id: 11041
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Start Program action
   :event-reference: true

WinSyslog Event ID 11041: Start Program action received an unexpected wait result
=================================================================================

Answer
------

A synchronous Start Program action received an unexpected Windows wait result while monitoring the child process or shutdown event. The product closes the process handles and continues rule processing.

Event details
-------------

- **Event ID:** ``11041``
- **Severity:** Error
- **Component:** Start Program action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Spawn Sync WaitForMultipleObjects returned {wait_result}; processing continues.`

Possible causes
---------------

- Windows returned a wait failure or abandoned synchronization state.
- The child process or shutdown event handle became invalid.
- System resource pressure or a product defect disrupted process waiting.

Immediate checks
----------------

#. Record the wait result, program path, timeout, and whether shutdown was in progress.
#. Run the configured program under the product service account and check Windows Error Reporting and neighboring system events.
#. Collect a bounded debug log and escalate if the unexpected result is reproducible.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the program completes under a controlled test and Event ID 11041 does not recur.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.
