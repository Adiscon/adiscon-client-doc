:orphan:

.. _winsyslog-event-id-11016:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11016: SNMP action: runtime operation failed.
   :event-id: 11016
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: SNMP action
   :event-reference: true

WinSyslog Event ID 11016: SNMP action: runtime operation failed
===============================================================

Answer
------

SNMP action: runtime operation failed. The product recorded this while processing snmp action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11016``
- **Severity:** Warning
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

- :ref:`Verify an SNMP trap sender and receiver path <event-id-procedure-snmp-verify-trap-path>` — Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11016 does not recur and that snmp action processing continues.

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

- :ref:`Event ID 11038 <winsyslog-event-id-11038>`
