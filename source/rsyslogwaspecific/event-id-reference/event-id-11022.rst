:orphan:

.. _rsyslog-event-id-11022:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11022: Action processing: action type is missing from configuration.
   :event-id: 11022
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Action processing
   :event-reference: true

rsyslog Windows Agent Event ID 11022: Action processing: action type is missing from configuration
==================================================================================================

Answer
------

Action processing: action type is missing from configuration. The product recorded this while processing action processing; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11022``
- **Severity:** Error
- **Component:** Action processing
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Action processing: action type is missing from configuration. Additional detail: {event_detail}

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

- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11022 does not recur and that action processing processing continues.

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

- :ref:`Event ID 11014 <rsyslog-event-id-11014>`
- :ref:`Event ID 11019 <rsyslog-event-id-11019>`
- :ref:`Event ID 11021 <rsyslog-event-id-11021>`
