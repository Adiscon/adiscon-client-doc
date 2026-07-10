:orphan:

.. _eventreporter-event-id-11188:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11188: Service configuration: configured service feature is unavailable.
   :event-id: 11188
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Service configuration
   :event-reference: true

EventReporter Event ID 11188: Service configuration: configured service feature is unavailable
==============================================================================================

Answer
------

The service configuration reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11188``
- **Severity:** Warning
- **Component:** Service configuration
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Runtime diagnostic.

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

Repeat or monitor the affected operation and confirm that Event ID 11188 does not recur and that service configuration processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

No safe general self-service repair is available for this event. Collect the evidence above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11183 <event-id-11183>`
- :doc:`Event ID 11184 <event-id-11184>`
- :doc:`Event ID 11185 <event-id-11185>`
