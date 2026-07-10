:orphan:

.. _eventreporter-event-id-11137:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11137: SNMP Trap Receiver: SNMP operation raised an exception.
   :event-id: 11137
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: SNMP Trap Receiver
   :event-reference: true

EventReporter Event ID 11137: SNMP Trap Receiver: SNMP operation raised an exception
====================================================================================

Answer
------

SNMP Trap Receiver: SNMP operation raised an exception. The product recorded this while processing snmp trap receiver; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11137``
- **Severity:** Warning
- **Component:** SNMP Trap Receiver
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** SNMP Trap Receiver: SNMP operation raised an exception. Additional detail: {event_detail}

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
- :doc:`Verify a UDP path without assuming delivery <../../shared/troubleshooting/event-id/network-verify-udp-path>` — Confirm receiver binding, firewall policy, and positive receipt for a paced sample.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11137 does not recur and that snmp trap receiver processing continues.

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

- :doc:`Event ID 11138 <event-id-11138>`
- :doc:`Event ID 11139 <event-id-11139>`
- :doc:`Event ID 11140 <event-id-11140>`
