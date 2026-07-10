:orphan:

.. _mwagent-event-id-11091:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11091: SETP receiver: SETP operation raised an exception.
   :event-id: 11091
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: SETP receiver
   :event-reference: true

MonitorWare Agent Event ID 11091: SETP receiver: SETP operation raised an exception
===================================================================================

Answer
------

SETP receiver: SETP operation raised an exception. The product recorded this while processing setp receiver; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11091``
- **Severity:** Warning
- **Component:** SETP receiver
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** SETP receiver: SETP operation raised an exception. Additional detail: {event_detail}

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

- :doc:`Verify listener binding and Windows Firewall rules <../../shared/troubleshooting/event-id/network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :doc:`Verify TLS certificates, private keys, and permitted peers <../../shared/troubleshooting/event-id/tls-verify-certificate-chain-and-peer>` — Check validity, trust chain, key pairing, protocol mode, and peer authorization.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11091 does not recur and that setp receiver processing continues.

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

- :doc:`Event ID 11090 <event-id-11090>`
- :doc:`Event ID 11092 <event-id-11092>`
- :doc:`Event ID 11093 <event-id-11093>`
