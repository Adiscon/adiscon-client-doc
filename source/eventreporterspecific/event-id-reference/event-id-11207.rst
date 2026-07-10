:orphan:

.. _eventreporter-event-id-11207:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11207: Product service: configuration reload state.
   :event-id: 11207
   :event-product: EventReporter
   :event-severity: Information
   :event-component: Product service
   :event-reference: true

EventReporter Event ID 11207: Product service: configuration reload state
=========================================================================

Answer
------

The product service reported an informational condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11207``
- **Severity:** Information
- **Component:** Product service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Configuration reloaded but service stopped during meantime.

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

Repeat or monitor the affected operation and confirm that Event ID 11207 does not recur and that product service processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :doc:`Event ID 11204 <event-id-11204>`
- :doc:`Event ID 11205 <event-id-11205>`
- :doc:`Event ID 11206 <event-id-11206>`
