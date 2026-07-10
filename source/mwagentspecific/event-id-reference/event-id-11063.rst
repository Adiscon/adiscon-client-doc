:orphan:

.. _mwagent-event-id-11063:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11063: MonitorWare Echo service: MonitorWare Echo operation raised an unknown exception.
   :event-id: 11063
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: MonitorWare Echo service
   :event-reference: true

MonitorWare Agent Event ID 11063: MonitorWare Echo service: MonitorWare Echo operation raised an unknown exception
==================================================================================================================

Answer
------

MonitorWare Echo service: MonitorWare Echo operation raised an unknown exception. The product recorded this while processing monitorware echo service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11063``
- **Severity:** Error
- **Component:** MonitorWare Echo service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** MonitorWare Echo service: MonitorWare Echo operation raised an unknown exception. Additional detail: {event_detail}

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
- :doc:`Verify sender, receiver, and queued-message recovery <../../shared/troubleshooting/event-id/transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11063 does not recur and that monitorware echo service processing continues.

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

- :doc:`Event ID 11060 <event-id-11060>`
- :doc:`Event ID 11061 <event-id-11061>`
- :doc:`Event ID 11062 <event-id-11062>`
