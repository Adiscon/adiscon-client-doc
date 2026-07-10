:orphan:

.. _mwagent-event-id-11174:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11174: Queue manager: queue capacity condition.
   :event-id: 11174
   :event-product: MonitorWare Agent
   :event-severity: Information
   :event-component: Queue manager
   :event-reference: true

MonitorWare Agent Event ID 11174: Queue manager: queue capacity condition
=========================================================================

Answer
------

Queue manager: queue capacity condition. The product recorded this while processing queue manager; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11174``
- **Severity:** Information
- **Component:** Queue manager
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Queue manager: queue capacity condition. Additional detail: {event_detail}

Possible causes
---------------

- A downstream action is failing or retrying, so queued work cannot drain.
- The queue directory, permissions, free space, or queue artifact state prevents normal processing.

Immediate checks
----------------

#. Identify the first downstream action error and record queue depth and oldest-item time.
#. Check queue-directory access and free space without changing live queue files.
#. Correct the downstream cause, send one test event, and verify that the backlog decreases.

Detailed procedures
-------------------

- :doc:`Diagnose an action backlog or disk queue <../../shared/troubleshooting/event-id/queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11174 does not recur and that queue manager processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :doc:`Event ID 11170 <event-id-11170>`
- :doc:`Event ID 11171 <event-id-11171>`
- :doc:`Event ID 11172 <event-id-11172>`
