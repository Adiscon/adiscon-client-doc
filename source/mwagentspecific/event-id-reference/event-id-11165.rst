:orphan:

.. _mwagent-event-id-11165:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11165: Email action: SMTP recipient address is missing.
   :event-id: 11165
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Email action
   :event-reference: true

MonitorWare Agent Event ID 11165: Email action: SMTP recipient address is missing
=================================================================================

Answer
------

Email action: SMTP recipient address is missing. The product recorded this while processing email action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11165``
- **Severity:** Error
- **Component:** Email action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Cmailrcptlist setrecipients. Additional detail: {event_detail}`

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

- :ref:`Verify SMTP connectivity and mail delivery <event-id-procedure-mail-verify-smtp-delivery>` — Separate DNS, TCP, TLS, authentication, relay, recipient, and downstream delivery.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11165 does not recur and that email action processing continues.

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

- :ref:`Event ID 11164 <mwagent-event-id-11164>`
