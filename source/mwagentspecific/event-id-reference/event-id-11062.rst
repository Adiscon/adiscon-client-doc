:orphan:

.. _mwagent-event-id-11062:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11062: MonitorWare Echo service: MonitorWare Echo operation raised an exception.
   :event-id: 11062
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: MonitorWare Echo service
   :event-reference: true

MonitorWare Agent Event ID 11062: MonitorWare Echo service: MonitorWare Echo operation raised an exception
==========================================================================================================

Answer
------

The monitorware echo service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11062``
- **Severity:** Error
- **Component:** MonitorWare Echo service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcealivemonecho run.

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

Repeat or monitor the affected operation and confirm that Event ID 11062 does not recur and that monitorware echo service processing continues.

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

- :doc:`Event ID 11060 <event-id-11060>`
- :doc:`Event ID 11061 <event-id-11061>`
- :doc:`Event ID 11063 <event-id-11063>`
