:orphan:

.. _rsyslog-event-id-11111:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11111: Windows Service Monitor: Windows Service Monitor raised an exception.
   :event-id: 11111
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Windows Service Monitor
   :event-reference: true

rsyslog Windows Agent Event ID 11111: Windows Service Monitor: Windows Service Monitor raised an exception
==========================================================================================================

Answer
------

Windows Service Monitor: Windows Service Monitor raised an exception. The product recorded this while processing windows service monitor; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11111``
- **Severity:** Error
- **Component:** Windows Service Monitor
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Windows Service Monitor: Windows Service Monitor raised an exception. Additional detail: {event_detail}

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

- :doc:`Verify service state, dependencies, and service account <../../shared/troubleshooting/event-id/service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11111 does not recur and that windows service monitor processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
