:orphan:

.. _rsyslog-event-id-11084:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11084: Heartbeat service: heartbeat operation raised an exception.
   :event-id: 11084
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Heartbeat service
   :event-reference: true

rsyslog Windows Agent Event ID 11084: Heartbeat service: heartbeat operation raised an exception
================================================================================================

Answer
------

Heartbeat service: heartbeat operation raised an exception. The product recorded this while processing heartbeat service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11084``
- **Severity:** Error
- **Component:** Heartbeat service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Heartbeat service: heartbeat operation raised an exception. Additional detail: {event_detail}`

Possible causes
---------------

- The product service, dependency, service account, or required Windows resource is unavailable or incorrectly configured.
- Windows returned the appended startup, shutdown, permission, timeout, or resource error.

Immediate checks
----------------

#. Record the affected service or component, service account, state, dependencies, and complete runtime detail.
#. Check recent Service Control Manager and neighboring product events for the first failure.
#. Correct the specific dependency, account, permission, or resource condition and perform one controlled retry.

Detailed procedures
-------------------

- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11084 does not recur and that heartbeat service processing continues.

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

- :ref:`Event ID 11085 <rsyslog-event-id-11085>`
