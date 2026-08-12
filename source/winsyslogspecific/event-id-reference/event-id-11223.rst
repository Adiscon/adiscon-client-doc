:orphan:

.. _winsyslog-event-id-11223:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11223: Protected service shutdown deadline expired.
   :event-id: 11223
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Service shutdown
   :event-reference: true

WinSyslog Event ID 11223: Protected service shutdown deadline expired
=====================================================================

Answer
------

Cooperative shutdown did not reach a safe terminal boundary before the configured process-wide deadline.

Event details
-------------

- **Event ID:** ``11223``
- **Severity:** Error
- **Component:** Service shutdown
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`The protected service shutdown deadline expired; the process will exit without destroying live worker owners. Additional detail: {event_detail}`

Possible causes
---------------

- A source, action callback, queue worker, or log rotation operation exceeded its cancellation or persistence allowance.

Immediate checks
----------------

#. Review the event detail for the blocking phase and queue counts.
#. Correct the blocked component or configure a larger shutdown protection timeout.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Stop the service again and confirm that Event ID 11223 does not recur and the process exits within the configured bound.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and adjacent shutdown events.
- The product version, shutdown configuration, debug log, and queue or ring-buffer configuration.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11224 <winsyslog-event-id-11224>`
- :ref:`Event ID 11227 <winsyslog-event-id-11227>`
