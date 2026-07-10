:orphan:

.. _mwagent-event-id-11016:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11016: SNMP action: runtime operation failed.
   :event-id: 11016
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: SNMP action
   :event-reference: true

MonitorWare Agent Event ID 11016: SNMP action: runtime operation failed
=======================================================================

Answer
------

The snmp action reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11016``
- **Severity:** Warning
- **Component:** SNMP action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Cactionconfigsendsnmp loadconfig.

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

Repeat or monitor the affected operation and confirm that Event ID 11016 does not recur and that snmp action processing continues.

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

- :doc:`Event ID 11038 <event-id-11038>`
