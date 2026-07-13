:orphan:

.. _eventreporter-event-id-11056:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11056: Network and TLS transport: TLS operation warning.
   :event-id: 11056
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Network and TLS transport
   :event-reference: true

EventReporter Event ID 11056: Network and TLS transport: TLS operation warning
==============================================================================

Answer
------

Network and TLS transport: TLS operation warning. The product recorded this while processing network and tls transport; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11056``
- **Severity:** Warning
- **Component:** Network and TLS transport
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Cwinsock initopensslserversession. Additional detail: {event_detail}`

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
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11056 does not recur and that network and tls transport processing continues.

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

- :ref:`Event ID 11048 <eventreporter-event-id-11048>`
- :ref:`Event ID 11049 <eventreporter-event-id-11049>`
- :ref:`Event ID 11050 <eventreporter-event-id-11050>`
