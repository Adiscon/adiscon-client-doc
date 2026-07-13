:orphan:

.. _eventreporter-event-id-11202:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11202: TCP listener could not assign an accepted socket.
   :event-id: 11202
   :event-product: EventReporter
   :event-severity: Error
   :event-component: TCP and TLS listener
   :event-reference: true

EventReporter Event ID 11202: TCP listener could not assign an accepted socket
==============================================================================

Answer
------

The TCP listener accepted or prepared a connection but could not assign its socket to a connection handler. At least that connection is lost, while the listener continues accepting later connections.

Event details
-------------

- **Event ID:** ``11202``
- **Severity:** Error
- **Component:** TCP and TLS listener
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not assign an accepted socket; at least one connection was lost. The server will continue.`

Possible causes
---------------

- The process or operating system exhausted socket, handle, thread, or memory resources.
- A connection-handler allocation failed.
- A transient Windows networking or product error prevented socket assignment.

Immediate checks
----------------

#. Check product process handles, memory, worker state, and connection rate at the event time.
#. Review neighboring Windows resource and networking events and reduce abnormal connection bursts if present.
#. Send a controlled TCP message and collect a bounded debug log if assignment failures recur.

Detailed procedures
-------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Interpret a Windows or Winsock error code <event-id-procedure-windows-interpret-error-code>` — Translate a numeric code without losing its operation or subsystem context.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that later TCP connections are accepted and controlled messages are processed without Event ID 11202.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11198 <eventreporter-event-id-11198>`
- :ref:`Event ID 11199 <eventreporter-event-id-11199>`
- :ref:`Event ID 11200 <eventreporter-event-id-11200>`
