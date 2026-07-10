:orphan:

.. _rsyslog-event-id-11008:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11008: Action configuration: configured action feature is unavailable.
   :event-id: 11008
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Action configuration
   :event-reference: true

rsyslog Windows Agent Event ID 11008: Action configuration: configured action feature is unavailable
====================================================================================================

Answer
------

The action configuration reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11008``
- **Severity:** Warning
- **Component:** Action configuration
- **Windows Event Log source:** ``RSyslogWindowsAgent``
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

Repeat or monitor the affected operation and confirm that Event ID 11008 does not recur and that action configuration processing continues.

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

- :doc:`Event ID 11007 <event-id-11007>`
- :doc:`Event ID 11009 <event-id-11009>`
