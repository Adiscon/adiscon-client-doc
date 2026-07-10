:orphan:

.. _mwagent-event-id-11095:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11095: NNTP Probe service: probe operation raised an exception.
   :event-id: 11095
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: NNTP Probe service
   :event-reference: true

MonitorWare Agent Event ID 11095: NNTP Probe service: probe operation raised an exception
=========================================================================================

Answer
------

The nntp probe service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11095``
- **Severity:** Error
- **Component:** NNTP Probe service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcenntpprobe.

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

Repeat or monitor the affected operation and confirm that Event ID 11095 does not recur and that nntp probe service processing continues.

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

- :doc:`Event ID 11096 <event-id-11096>`
