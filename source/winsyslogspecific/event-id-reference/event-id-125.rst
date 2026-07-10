:orphan:

.. _winsyslog-event-id-125:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 125: Freeware mode reminder.
   :event-id: 125
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 125: Freeware mode reminder
==============================================

Answer
------

Freeware-mode limits apply to the running WinSyslog service.

Event details
-------------

- **Event ID:** ``125``
- **Severity:** Information
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** WinSyslog is running in freeware mode; the event detail describes the active limitation.

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

Repeat or monitor the affected operation and confirm that Event ID 125 does not recur and that licensing processing continues.

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

- :doc:`Event ID 11005 <event-id-11005>`
- :doc:`Event ID 11043 <event-id-11043>`
- :doc:`Event ID 11044 <event-id-11044>`
