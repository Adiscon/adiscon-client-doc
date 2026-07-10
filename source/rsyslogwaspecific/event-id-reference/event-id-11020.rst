:orphan:

.. _rsyslog-event-id-11020:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11020: Control Windows Service action: runtime operation failed.
   :event-id: 11020
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

rsyslog Windows Agent Event ID 11020: Control Windows Service action: runtime operation failed
==============================================================================================

Answer
------

The control windows service action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11020``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Cactioncontrolntservice doaction.

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

Repeat or monitor the affected operation and confirm that Event ID 11020 does not recur and that control windows service action processing continues.

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

- :doc:`Event ID 11216 <event-id-11216>`
- :doc:`Event ID 11217 <event-id-11217>`
- :doc:`Event ID 11218 <event-id-11218>`
