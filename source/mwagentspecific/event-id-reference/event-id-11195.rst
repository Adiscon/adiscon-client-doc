:orphan:

.. _mwagent-event-id-11195:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11195: Disk queue: runtime data error.
   :event-id: 11195
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Disk queue
   :event-reference: true

MonitorWare Agent Event ID 11195: Disk queue: runtime data error
================================================================

Answer
------

The disk queue reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11195``
- **Severity:** Error
- **Component:** Disk queue
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Formatted runtime diagnostic.

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

Repeat or monitor the affected operation and confirm that Event ID 11195 does not recur and that disk queue processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

No safe general self-service repair is available for this event. Collect the evidence above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11196 <event-id-11196>`
- :doc:`Event ID 11197 <event-id-11197>`
