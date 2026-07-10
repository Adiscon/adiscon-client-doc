:orphan:

.. _rsyslog-event-id-11017:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11017: Forward Syslog action: action initialization failed.
   :event-id: 11017
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Forward Syslog action
   :event-reference: true

rsyslog Windows Agent Event ID 11017: Forward Syslog action: action initialization failed
=========================================================================================

Answer
------

Forward Syslog action: action initialization failed. The product recorded this while processing forward syslog action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11017``
- **Severity:** Error
- **Component:** Forward Syslog action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Forward Syslog action: action initialization failed. Additional detail: {event_detail}

Possible causes
---------------

- The destination or listener is unavailable, blocked, bound to another address or port, or configured for a different transport.
- TLS certificates, peer authorization, protocol settings, or sender and receiver configuration do not match.

Immediate checks
----------------

#. Record the endpoint, address family, port, transport, TLS mode, and complete runtime detail.
#. Verify DNS, route, listener ownership, firewall policy, and TCP or UDP reachability as applicable.
#. Send one unique test message and verify positive receipt and queue recovery.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11017 does not recur and that forward syslog action processing continues.

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

- :ref:`Event ID 11018 <rsyslog-event-id-11018>`
- :ref:`Event ID 11039 <rsyslog-event-id-11039>`
- :ref:`Event ID 11040 <rsyslog-event-id-11040>`
