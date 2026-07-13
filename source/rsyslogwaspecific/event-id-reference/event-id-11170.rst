:orphan:

.. _rsyslog-event-id-11170:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11170: Queue worker received an unexpected wake-up.
   :event-id: 11170
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Main message queue
   :event-reference: true

rsyslog Windows Agent Event ID 11170: Queue worker received an unexpected wake-up
=================================================================================

Answer
------

A main-queue worker returned from its wait without a recognized work or shutdown signal. The worker loop continues, but queue processing may be unreliable if the condition repeats.

Event details
-------------

- **Event ID:** ``11170``
- **Severity:** Error
- **Component:** Main message queue
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Queue worker awoke without a signaled work or shutdown condition.`

Possible causes
---------------

- A Windows wait object returned an unexpected state.
- A queue synchronization handle became invalid.
- System resource pressure or a product defect disrupted worker coordination.

Immediate checks
----------------

#. Check whether queue depth is increasing and whether other workers continue processing.
#. Collect neighboring events, queue metrics, Windows Error Reporting data, and a bounded debug log.
#. Restart only after preserving evidence if processing has stopped, then escalate a recurrence.

Detailed procedures
-------------------

- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that queue workers process a controlled event and queue depth returns to normal without Event ID 11170.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11171 <rsyslog-event-id-11171>`
- :ref:`Event ID 11172 <rsyslog-event-id-11172>`
- :ref:`Event ID 11173 <rsyslog-event-id-11173>`
