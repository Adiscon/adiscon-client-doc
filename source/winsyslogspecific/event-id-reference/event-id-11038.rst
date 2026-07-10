:orphan:

.. _winsyslog-event-id-11038:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11038: SNMP action: runtime operation failed.
   :event-id: 11038
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: SNMP action
   :event-reference: true

WinSyslog Event ID 11038: SNMP action: runtime operation failed
===============================================================

Answer
------

SNMP action: runtime operation failed. The product recorded this while processing snmp action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11038``
- **Severity:** Error
- **Component:** SNMP action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** SNMP action: runtime operation failed. Additional detail: {event_detail}

Possible causes
---------------

- Sender and receiver transport, port, SNMP version, security or community, OID, or value type do not match.
- The receiver is not bound, a firewall drops the traffic, or the SNMP library returned the appended runtime error.

Immediate checks
----------------

#. Record transport, endpoint, SNMP version, security or community, OIDs, and the complete runtime detail.
#. Confirm the intended receiver process owns the configured endpoint and accepts a paced test trap.
#. Verify the received OID and value before changing filters or MIB settings.

Detailed procedures
-------------------

- :doc:`Verify an SNMP trap sender and receiver path <../../shared/troubleshooting/event-id/snmp-verify-trap-path>` — Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11038 does not recur and that snmp action processing continues.

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

- :doc:`Event ID 11016 <event-id-11016>`
