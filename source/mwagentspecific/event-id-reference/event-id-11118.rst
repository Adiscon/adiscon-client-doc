:orphan:

.. _mwagent-event-id-11118:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11118: Ping Probe service: runtime operation failed.
   :event-id: 11118
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Ping Probe service
   :event-reference: true

MonitorWare Agent Event ID 11118: Ping Probe service: runtime operation failed
==============================================================================

Answer
------

The ping probe service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11118``
- **Severity:** Error
- **Component:** Ping Probe service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Pingprobe.

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

Repeat or monitor the affected operation and confirm that Event ID 11118 does not recur and that ping probe service processing continues.

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

- :doc:`Event ID 11117 <event-id-11117>`
