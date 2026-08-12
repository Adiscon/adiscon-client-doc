:orphan:

.. _eventreporter-event-id-11226:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11226: SNMP listener shutdown wake fallback.
   :event-id: 11226
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: SNMP trap listener
   :event-reference: true

EventReporter Event ID 11226: SNMP listener shutdown wake fallback
==================================================================

Answer
------

The local wake descriptor could not be used, so shutdown uses a bounded receive wait.

Event details
-------------

- **Event ID:** ``11226``
- **Severity:** Warning
- **Component:** SNMP trap listener
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`The SNMP listener wake descriptor is unavailable; shutdown is using the bounded select fallback. Additional detail: {event_detail}`

Possible causes
---------------

- Local UDP socket setup or send failed, or the descriptor set reached its capacity.

Immediate checks
----------------

#. Check local socket resource usage and descriptor pressure, then restart the service.

Detailed procedures
-------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Stop an idle SNMP trap listener and confirm that Event ID 11226 does not recur and shutdown completes promptly.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry.
- The SNMP listener configuration and debug log covering shutdown.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11223 <eventreporter-event-id-11223>`
