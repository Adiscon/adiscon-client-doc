:orphan:

.. _winsyslog-event-id-11111:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11111: Windows Service Monitor: Windows Service Monitor raised an exception.
   :event-id: 11111
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Windows Service Monitor
   :event-reference: true

WinSyslog Event ID 11111: Windows Service Monitor: Windows Service Monitor raised an exception
==============================================================================================

Answer
------

The windows service monitor reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11111``
- **Severity:** Error
- **Component:** Windows Service Monitor
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcentservicemonitor doaction.

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

Repeat or monitor the affected operation and confirm that Event ID 11111 does not recur and that windows service monitor processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.
