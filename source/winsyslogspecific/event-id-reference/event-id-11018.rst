:orphan:

.. _winsyslog-event-id-11018:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11018: A queued Forward Syslog message could not be delivered.
   :event-id: 11018
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Forward Syslog disk queue
   :event-reference: true

WinSyslog Event ID 11018: A queued Forward Syslog message could not be delivered
================================================================================

Answer
------

The product could not deliver a message being replayed from the Forward Syslog action's disk queue. The queue position is moved back so delivery can be retried.

Event details
-------------

- **Event ID:** ``11018``
- **Severity:** Warning
- **Component:** Forward Syslog disk queue
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error sending syslog message '{error_detail}' - error '{error_code}'`

Possible causes
---------------

- The configured syslog destination is unreachable or not listening.
- DNS, routing, firewall, TCP, TLS, or peer settings prevent delivery.
- The destination closed or rejected the connection.

Immediate checks
----------------

#. Record the embedded error code and the affected Forward Syslog destination.
#. Resolve the destination and test the configured transport and port from the product host.
#. Correct the destination or transport problem and monitor queued replay.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the queued backlog decreases and a controlled message arrives at the configured syslog destination.

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

- :ref:`Event ID 11017 <winsyslog-event-id-11017>`
- :ref:`Event ID 11039 <winsyslog-event-id-11039>`
- :ref:`Event ID 11040 <winsyslog-event-id-11040>`
