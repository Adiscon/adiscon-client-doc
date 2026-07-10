:orphan:

.. _winsyslog-event-id-900:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 900: Invalid license key rejected.
   :event-id: 900
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 900: Invalid license key rejected
====================================================

Answer
------

The WinSyslog service does not start with the rejected key.

Event details
-------------

- **Event ID:** ``900``
- **Severity:** Error
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** WinSyslog rejected an invalid license key during startup.

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

Repeat or monitor the affected operation and confirm that Event ID 900 does not recur and that licensing processing continues.

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

- :doc:`Event ID 11005 <event-id-11005>`
- :doc:`Event ID 11043 <event-id-11043>`
- :doc:`Event ID 11044 <event-id-11044>`
