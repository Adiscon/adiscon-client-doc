:orphan:

.. _eventreporter-event-id-11042:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11042: WinSyslog file action: runtime operation failed.
   :event-id: 11042
   :event-product: EventReporter
   :event-severity: Error
   :event-component: WinSyslog file action
   :event-reference: true

EventReporter Event ID 11042: WinSyslog file action: runtime operation failed
=============================================================================

Answer
------

The winsyslog file action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11042``
- **Severity:** Error
- **Component:** WinSyslog file action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Writefile.

Possible causes
---------------

- The remote endpoint is unavailable or the network path was interrupted.
- The listener, protocol, TLS settings, certificate, or permitted-peer configuration does not match.

Troubleshooting
---------------

#. Use the event detail to identify the endpoint and failing protocol operation.
#. Verify name resolution, routing, firewall rules, listening port, and remote service state.
#. For TLS connections, verify certificates, trust, protocol versions, and permitted-peer settings before retrying.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11042 does not recur and that winsyslog file action processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.
