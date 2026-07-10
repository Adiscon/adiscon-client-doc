:orphan:

.. _rsyslog-event-id-11194:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11194: Product runtime: message compression failed.
   :event-id: 11194
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Product runtime
   :event-reference: true

rsyslog Windows Agent Event ID 11194: Product runtime: message compression failed
=================================================================================

Answer
------

The product runtime reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11194``
- **Severity:** Warning
- **Component:** Product runtime
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Csyslogclient send udp.

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

Repeat or monitor the affected operation and confirm that Event ID 11194 does not recur and that product runtime processing continues.

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

- :doc:`Event ID 11152 <event-id-11152>`
- :doc:`Event ID 11169 <event-id-11169>`
