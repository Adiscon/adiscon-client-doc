:orphan:

.. _eventreporter-event-id-11037:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11037: Action processing: runtime operation failed.
   :event-id: 11037
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Action processing
   :event-reference: true

EventReporter Event ID 11037: Action processing: runtime operation failed
=========================================================================

Answer
------

Action processing: runtime operation failed. The product recorded this while processing action processing; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11037``
- **Severity:** Error
- **Component:** Action processing
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Action processing: runtime operation failed. Additional detail: {event_detail}

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
- :doc:`Validate configuration and reload it safely <../../shared/troubleshooting/event-id/config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11037 does not recur and that action processing processing continues.

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

- :doc:`Event ID 11014 <event-id-11014>`
- :doc:`Event ID 11019 <event-id-11019>`
- :doc:`Event ID 11021 <event-id-11021>`
