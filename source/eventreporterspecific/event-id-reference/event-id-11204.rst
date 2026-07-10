:orphan:

.. _eventreporter-event-id-11204:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11204: Product service: invalid worker-thread count was corrected.
   :event-id: 11204
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Product service
   :event-reference: true

EventReporter Event ID 11204: Product service: invalid worker-thread count was corrected
========================================================================================

Answer
------

The product service reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11204``
- **Severity:** Warning
- **Component:** Product service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Loadstate.

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

Repeat or monitor the affected operation and confirm that Event ID 11204 does not recur and that product service processing continues.

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

- :doc:`Event ID 11205 <event-id-11205>`
- :doc:`Event ID 11206 <event-id-11206>`
- :doc:`Event ID 11207 <event-id-11207>`
