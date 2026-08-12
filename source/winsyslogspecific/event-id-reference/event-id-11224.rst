:orphan:

.. _winsyslog-event-id-11224:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11224: Configuration reload shutdown incomplete.
   :event-id: 11224
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Service shutdown
   :event-reference: true

WinSyslog Event ID 11224: Configuration reload shutdown incomplete
==================================================================

Answer
------

The old runtime could not stop safely, so replacement configuration was not initialized.

Event details
-------------

- **Event ID:** ``11224``
- **Severity:** Error
- **Component:** Service shutdown
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`Configuration reload was stopped because the old runtime did not shut down completely; restart the process. Additional detail: {event_detail}`

Possible causes
---------------

- A source, action callback, queue worker, or persistence operation did not complete within the configured allowance.

Immediate checks
----------------

#. Restart the service process.
#. Review the event detail for the blocking phase before attempting another reload.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Perform one configuration reload and confirm that Event ID 11224 does not recur and the new configuration starts.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and adjacent reload events.
- The product version, configuration export, and debug log covering the reload.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11223 <winsyslog-event-id-11223>`
