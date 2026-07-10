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

The snmp trap receiver reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11137``
- **Severity:** Warning
- **Component:** SNMP Trap Receiver
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcesnmptrap run.

Possible causes
---------------

- The runtime operation named in the event detail failed.
- A dependent Windows resource, configured endpoint, or product setting was unavailable or invalid.

Troubleshooting
---------------

#. Read the complete event detail and identify the operation, configured object, and Windows error code.
#. Check adjacent product events and the debug log for the first failure in the same time window.
#. Correct the reported configuration or dependency and repeat the operation.

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

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11138 <event-id-11138>`
- :doc:`Event ID 11139 <event-id-11139>`
- :doc:`Event ID 11140 <event-id-11140>`
