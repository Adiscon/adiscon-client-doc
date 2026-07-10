:orphan:

.. _mwagent-event-id-11000:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11000: SETP connection closed by the receiver.
   :event-id: 11000
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: SETP sender
   :event-reference: true

MonitorWare Agent Event ID 11000: SETP connection closed by the receiver
========================================================================

Answer
------

The current SETP session is closed and will be recreated. Forwarding can continue after reconnect.

Event details
-------------

- **Event ID:** ``11000``
- **Severity:** Warning
- **Component:** SETP sender
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** SETP sender connection was closed by the remote side while waiting for a reply. Additional detail: {event_detail}

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
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Check validity, trust chain, key pairing, protocol mode, and peer authorization.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11000 does not recur and that setp sender processing continues.

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

- :ref:`Event ID 11001 <mwagent-event-id-11001>`
- :ref:`Event ID 11002 <mwagent-event-id-11002>`
- :ref:`Event ID 11003 <mwagent-event-id-11003>`
