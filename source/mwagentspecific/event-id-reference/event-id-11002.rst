:orphan:

.. _mwagent-event-id-11002:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11002: SETP delivery delayed in the action cache.
   :event-id: 11002
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: SETP sender
   :event-reference: true

MonitorWare Agent Event ID 11002: SETP delivery delayed in the action cache
===========================================================================

Answer
------

Delivery is delayed while the action cache retries.

Event details
-------------

- **Event ID:** ``11002``
- **Severity:** Warning
- **Component:** SETP sender
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** SETP sender could not complete the send operation; the message was moved to the action cache for retry. Additional detail: {event_detail}

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

- :doc:`Resolve a destination and test its TCP port <../../shared/troubleshooting/event-id/network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :doc:`Verify TLS certificates, private keys, and permitted peers <../../shared/troubleshooting/event-id/tls-verify-certificate-chain-and-peer>` — Check validity, trust chain, key pairing, protocol mode, and peer authorization.
- :doc:`Verify sender, receiver, and queued-message recovery <../../shared/troubleshooting/event-id/transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11002 does not recur and that setp sender processing continues.

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

- :doc:`Event ID 11000 <event-id-11000>`
- :doc:`Event ID 11001 <event-id-11001>`
- :doc:`Event ID 11003 <event-id-11003>`
