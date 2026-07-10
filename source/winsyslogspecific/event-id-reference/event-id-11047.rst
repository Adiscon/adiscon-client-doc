:orphan:

.. _winsyslog-event-id-11047:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11047: Configuration: invalid host or IP address.
   :event-id: 11047
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Configuration
   :event-reference: true

WinSyslog Event ID 11047: Configuration: invalid host or IP address
===================================================================

Answer
------

The configuration reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11047``
- **Severity:** Error
- **Component:** Configuration
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Invalid hostname.

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

Repeat or monitor the affected operation and confirm that Event ID 11047 does not recur and that configuration processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.
