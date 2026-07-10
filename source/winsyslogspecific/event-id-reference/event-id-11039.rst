:orphan:

.. _winsyslog-event-id-11039:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11039: Forward Syslog action: runtime operation failed.
   :event-id: 11039
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Forward Syslog action
   :event-reference: true

WinSyslog Event ID 11039: Forward Syslog action: runtime operation failed
=========================================================================

Answer
------

The forward syslog action reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11039``
- **Severity:** Warning
- **Component:** Forward Syslog action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cactionsendsyslog doaction.

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

Repeat or monitor the affected operation and confirm that Event ID 11039 does not recur and that forward syslog action processing continues.

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

- :doc:`Event ID 11017 <event-id-11017>`
- :doc:`Event ID 11018 <event-id-11018>`
- :doc:`Event ID 11040 <event-id-11040>`
