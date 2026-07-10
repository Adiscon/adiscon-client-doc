:orphan:

.. _winsyslog-event-id-11119:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11119: POP3 Probe service: probe operation raised an exception.
   :event-id: 11119
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: POP3 Probe service
   :event-reference: true

WinSyslog Event ID 11119: POP3 Probe service: probe operation raised an exception
=================================================================================

Answer
------

The pop3 probe service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11119``
- **Severity:** Error
- **Component:** POP3 Probe service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcepop3probe.

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

Repeat or monitor the affected operation and confirm that Event ID 11119 does not recur and that pop3 probe service processing continues.

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

- :doc:`Event ID 11120 <event-id-11120>`
