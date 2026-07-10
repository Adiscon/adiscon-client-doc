:orphan:

.. _winsyslog-event-id-11093:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11093: SETP receiver: SETP operation raised an exception.
   :event-id: 11093
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: SETP receiver
   :event-reference: true

WinSyslog Event ID 11093: SETP receiver: SETP operation raised an exception
===========================================================================

Answer
------

The setp receiver reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11093``
- **Severity:** Error
- **Component:** SETP receiver
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcemiap run.

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

Repeat or monitor the affected operation and confirm that Event ID 11093 does not recur and that setp receiver processing continues.

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

- :doc:`Event ID 11090 <event-id-11090>`
- :doc:`Event ID 11091 <event-id-11091>`
- :doc:`Event ID 11092 <event-id-11092>`
