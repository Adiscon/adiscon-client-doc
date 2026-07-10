:orphan:

.. _mwagent-event-id-11184:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11184: Service configuration: memory reserve could not be allocated.
   :event-id: 11184
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Service configuration
   :event-reference: true

MonitorWare Agent Event ID 11184: Service configuration: memory reserve could not be allocated
==============================================================================================

Answer
------

The service configuration reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11184``
- **Severity:** Warning
- **Component:** Service configuration
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Cservicemanager startupservices.

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

Repeat or monitor the affected operation and confirm that Event ID 11184 does not recur and that service configuration processing continues.

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

- :doc:`Event ID 11183 <event-id-11183>`
- :doc:`Event ID 11185 <event-id-11185>`
- :doc:`Event ID 11186 <event-id-11186>`
