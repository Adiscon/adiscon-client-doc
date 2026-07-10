:orphan:

.. _rsyslog-event-id-11095:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11095: NNTP Probe service: probe operation raised an exception.
   :event-id: 11095
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: NNTP Probe service
   :event-reference: true

rsyslog Windows Agent Event ID 11095: NNTP Probe service: probe operation raised an exception
=============================================================================================

Answer
------

NNTP Probe service: probe operation raised an exception. The product recorded this while processing nntp probe service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11095``
- **Severity:** Error
- **Component:** NNTP Probe service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** NNTP Probe service: probe operation raised an exception. Additional detail: {event_detail}

Possible causes
---------------

- Name resolution, routing, listener state, TLS, authentication, or protocol expectations do not match the remote service.
- The remote service rejected the request, exceeded the configured timeout, or returned an unexpected response.

Immediate checks
----------------

#. Record the endpoint, port, TLS and authentication mode, timeout, and complete protocol response.
#. Resolve the host and test the configured port from the product system.
#. Run the smallest safe protocol test and compare its response with the configured success condition.

Detailed procedures
-------------------

- :doc:`Verify a monitored remote service <../../shared/troubleshooting/event-id/probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11095 does not recur and that nntp probe service processing continues.

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

- :doc:`Event ID 11096 <event-id-11096>`
