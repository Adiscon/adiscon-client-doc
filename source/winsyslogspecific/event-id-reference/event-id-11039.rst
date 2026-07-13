:orphan:

.. _winsyslog-event-id-11039:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11039: Forward Syslog delivery failed and the message was queued.
   :event-id: 11039
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Forward Syslog action
   :event-reference: true

WinSyslog Event ID 11039: Forward Syslog delivery failed and the message was queued
===================================================================================

Answer
------

A TCP Forward Syslog transmission failed while the supported disk-queue mode was enabled. The product queued the message for later delivery and scheduled recovery processing.

Event details
-------------

- **Event ID:** ``11039``
- **Severity:** Warning
- **Component:** Forward Syslog action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`WSError: {error_code} | Error sending syslog message: {error_detail}`

Possible causes
---------------

- The syslog destination is unavailable or refusing the configured TCP connection.
- DNS, routing, firewall, or TLS settings prevent delivery.
- The peer closed the session or stopped accepting messages.

Immediate checks
----------------

#. Record the Winsock error and confirm that the action queue accepted the message.
#. Test the configured destination, transport, and port from the product host.
#. Restore delivery and monitor the queue until it drains.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the destination receives a controlled message and the queued backlog decreases without another Event ID 11039.

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
- :ref:`Event ID 11018 <winsyslog-event-id-11018>`
- :ref:`Event ID 11040 <winsyslog-event-id-11040>`
