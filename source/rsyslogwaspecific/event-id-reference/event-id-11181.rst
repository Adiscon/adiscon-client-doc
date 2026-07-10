:orphan:

.. _rsyslog-event-id-11181:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11181: Queue manager: disk queue cache operation failed.
   :event-id: 11181
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Queue manager
   :event-reference: true

rsyslog Windows Agent Event ID 11181: Queue manager: disk queue cache operation failed
======================================================================================

Answer
------

Queue manager: disk queue cache operation failed. The product recorded this while processing queue manager; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11181``
- **Severity:** Error
- **Component:** Queue manager
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Queue manager: disk queue cache operation failed. Additional detail: {event_detail}

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

Repeat or monitor the affected operation and confirm that Event ID 11181 does not recur and that queue manager processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11170 <event-id-11170>`
- :doc:`Event ID 11171 <event-id-11171>`
- :doc:`Event ID 11172 <event-id-11172>`
