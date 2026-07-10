:orphan:

.. _mwagent-event-id-11000:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11000: SETP connection closed by the receiver.
   :event-id: 11000
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: SETP sender
   :event-reference: true

MonitorWare Agent Event ID 11000: SETP connection closed by the receiver
========================================================================

Answer
------

The current SETP session is closed and will be recreated. Forwarding can continue after reconnect.

Event details
-------------

- **Event ID:** ``11000``
- **Severity:** Warning
- **Component:** SETP sender
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** SETP sender connection was closed by the remote side while waiting for a reply.

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

Repeat or monitor the affected operation and confirm that Event ID 11000 does not recur and that setp sender processing continues.

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

- :doc:`Event ID 11001 <event-id-11001>`
- :doc:`Event ID 11002 <event-id-11002>`
- :doc:`Event ID 11003 <event-id-11003>`
