:orphan:

.. _rsyslog-event-id-11225:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11225: RELP listener shutdown wake fallback.
   :event-id: 11225
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: RELP listener
   :event-reference: true

rsyslog Windows Agent Event ID 11225: RELP listener shutdown wake fallback
==========================================================================

Answer
------

The immediate local wake could not be delivered, so shutdown uses the bounded listener fallback.

Event details
-------------

- **Event ID:** ``11225``
- **Severity:** Warning
- **Component:** RELP listener
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`The RELP listener loopback wake failed; shutdown is using the bounded external-library fallback. Additional detail: {event_detail}`

Possible causes
---------------

- Local socket creation or loopback connection failed because of resource pressure or address-family configuration.

Immediate checks
----------------

#. Check local socket resource usage and the configured RELP listener address and port.

Detailed procedures
-------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Stop an idle RELP listener and confirm that Event ID 11225 does not recur and shutdown completes promptly.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry.
- The RELP listener address family, bind address, port, and debug log.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11223 <rsyslog-event-id-11223>`
