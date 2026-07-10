:orphan:

.. _eventreporter-event-id-11014:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11014: Action processing: action initialization failed.
   :event-id: 11014
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Action processing
   :event-reference: true

EventReporter Event ID 11014: Action processing: action initialization failed
=============================================================================

Answer
------

The action processing reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11014``
- **Severity:** Error
- **Component:** Action processing
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Cactionconfigpostprocess loadsettings.

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

Repeat or monitor the affected operation and confirm that Event ID 11014 does not recur and that action processing processing continues.

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

- :doc:`Event ID 11019 <event-id-11019>`
- :doc:`Event ID 11021 <event-id-11021>`
- :doc:`Event ID 11022 <event-id-11022>`
