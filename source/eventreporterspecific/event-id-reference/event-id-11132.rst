:orphan:

.. _eventreporter-event-id-11132:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11132: SNMP Monitor service: SNMP operation raised an exception.
   :event-id: 11132
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: SNMP Monitor service
   :event-reference: true

EventReporter Event ID 11132: SNMP Monitor service: SNMP operation raised an exception
======================================================================================

Answer
------

The snmp monitor service reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11132``
- **Severity:** Warning
- **Component:** SNMP Monitor service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcesnmpmonitor run.

Possible causes
---------------

- The service received an invalid setting or could not initialize a configured component.
- Windows denied a required service, registry, file, or operating-system operation.

Troubleshooting
---------------

#. Read this event together with adjacent product events that contain the detailed failure.
#. Validate the recently changed configuration and the product service account permissions.
#. Correct the reported setting or operating-system condition, then restart or reload the service.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11132 does not recur and that snmp monitor service processing continues.

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

- :doc:`Event ID 11133 <event-id-11133>`
- :doc:`Event ID 11134 <event-id-11134>`
- :doc:`Event ID 11135 <event-id-11135>`
