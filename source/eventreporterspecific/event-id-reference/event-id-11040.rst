:orphan:

.. _eventreporter-event-id-11040:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11040: Forward Syslog delivery failed without queue protection.
   :event-id: 11040
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Forward Syslog action
   :event-reference: true

EventReporter Event ID 11040: Forward Syslog delivery failed without queue protection
=====================================================================================

Answer
------

The Forward Syslog action could not deliver the current message, and the active transport or send mode did not place it in the supported action disk queue. The action is marked failed for this event.

Event details
-------------

- **Event ID:** ``11040``
- **Severity:** Error
- **Component:** Forward Syslog action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`WSError: {error_code} | Error sending syslog message: {error_detail}`

Possible causes
---------------

- The syslog destination is unavailable, refusing connections, or closing the session.
- DNS, routing, firewall, transport, or TLS settings prevent delivery.
- The selected send mode or transport is not using action disk-queue protection.

Immediate checks
----------------

#. Record the Winsock error, transport, send mode, and destination.
#. Test name resolution and the configured port from the product host.
#. Correct the destination or transport and send a new uniquely identifiable test message; evaluate queue protection if loss prevention is required.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the new test message arrives and Event ID 11040 does not recur.

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

- :ref:`Event ID 11017 <eventreporter-event-id-11017>`
- :ref:`Event ID 11018 <eventreporter-event-id-11018>`
- :ref:`Event ID 11039 <eventreporter-event-id-11039>`
