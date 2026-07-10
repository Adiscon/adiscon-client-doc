:orphan:

.. _mwagent-event-id-101:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 101: The service was removed.
   :event-id: 101
   :event-product: MonitorWare Agent
   :event-severity: Information
   :event-component: Windows service lifecycle
   :event-reference: true

MonitorWare Agent Event ID 101: The service was removed
=======================================================

Answer
------

The Windows service registration was removed.

Event details
-------------

- **Event ID:** ``101``
- **Severity:** Information
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** The service was removed.

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

Repeat or monitor the affected operation and confirm that Event ID 101 does not recur and that windows service lifecycle processing continues.

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

- :doc:`Event ID 100 <event-id-100>`
- :doc:`Event ID 102 <event-id-102>`
- :doc:`Event ID 103 <event-id-103>`
