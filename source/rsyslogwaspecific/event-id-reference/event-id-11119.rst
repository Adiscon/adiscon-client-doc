:orphan:

.. _rsyslog-event-id-11119:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11119: POP3 Probe service: probe operation raised an exception.
   :event-id: 11119
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: POP3 Probe service
   :event-reference: true

rsyslog Windows Agent Event ID 11119: POP3 Probe service: probe operation raised an exception
=============================================================================================

Answer
------

POP3 Probe service: probe operation raised an exception. The product recorded this while processing pop3 probe service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11119``
- **Severity:** Error
- **Component:** POP3 Probe service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** POP3 Probe service: probe operation raised an exception. Additional detail: {event_detail}

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

- :ref:`Verify a monitored remote service <event-id-procedure-probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11119 does not recur and that pop3 probe service processing continues.

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

- :ref:`Event ID 11120 <rsyslog-event-id-11120>`
