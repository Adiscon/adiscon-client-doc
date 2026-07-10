:orphan:

.. _winsyslog-event-id-11052:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11052: Network and TLS transport: TLS operation warning.
   :event-id: 11052
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Network and TLS transport
   :event-reference: true

WinSyslog Event ID 11052: Network and TLS transport: TLS operation warning
==========================================================================

Answer
------

Network and TLS transport: TLS operation warning. The product recorded this while processing network and tls transport; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11052``
- **Severity:** Warning
- **Component:** Network and TLS transport
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cwinsock initopensslserversession. Additional detail: {event_detail}

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
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11052 does not recur and that network and tls transport processing continues.

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

- :doc:`Event ID 11048 <event-id-11048>`
- :doc:`Event ID 11049 <event-id-11049>`
- :doc:`Event ID 11050 <event-id-11050>`
