:orphan:

.. _mwagent-event-id-11199:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11199: TCP and TLS listener: TLS server initialization failed.
   :event-id: 11199
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: TCP and TLS listener
   :event-reference: true

MonitorWare Agent Event ID 11199: TCP and TLS listener: TLS server initialization failed
========================================================================================

Answer
------

TCP and TLS listener: TLS server initialization failed. The product recorded this while processing tcp and tls listener; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11199``
- **Severity:** Warning
- **Component:** TCP and TLS listener
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Ctcpserver ssl connection initialization failed. Additional detail: {event_detail}`

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

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11199 does not recur and that tcp and tls listener processing continues.

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

- :ref:`Event ID 11198 <mwagent-event-id-11198>`
- :ref:`Event ID 11200 <mwagent-event-id-11200>`
- :ref:`Event ID 11201 <mwagent-event-id-11201>`
