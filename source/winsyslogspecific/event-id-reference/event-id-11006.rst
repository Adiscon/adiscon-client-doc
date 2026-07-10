:orphan:

.. _winsyslog-event-id-11006:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11006: Action callruleset configured ruleset was not found.
   :event-id: 11006
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Call Ruleset action
   :event-reference: true

WinSyslog Event ID 11006: Action callruleset configured ruleset was not found
=============================================================================

Answer
------

The call ruleset action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11006``
- **Severity:** Error
- **Component:** Call Ruleset action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Action callruleset configured ruleset was not found.

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

Repeat or monitor the affected operation and confirm that Event ID 11006 does not recur and that call ruleset action processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.
