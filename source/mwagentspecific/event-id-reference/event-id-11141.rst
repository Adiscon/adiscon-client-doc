:orphan:

.. _mwagent-event-id-11141:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11141: Syslog listener: BEEP listener option could not be applied.
   :event-id: 11141
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Syslog listener
   :event-reference: true

MonitorWare Agent Event ID 11141: Syslog listener: BEEP listener option could not be applied
============================================================================================

Answer
------

Syslog listener: BEEP listener option could not be applied. The product recorded this while processing syslog listener; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11141``
- **Severity:** Error
- **Component:** Syslog listener
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Infosourcesyslog. Additional detail: {event_detail}

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
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11141 does not recur and that syslog listener processing continues.

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

- :doc:`Event ID 11112 <event-id-11112>`
- :doc:`Event ID 11113 <event-id-11113>`
- :doc:`Event ID 11114 <event-id-11114>`
