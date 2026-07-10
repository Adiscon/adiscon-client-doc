:orphan:

.. _rsyslog-event-id-11034:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11034: SETP sender: TLS client initialization failed.
   :event-id: 11034
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: SETP sender
   :event-reference: true

rsyslog Windows Agent Event ID 11034: SETP sender: TLS client initialization failed
===================================================================================

Answer
------

The setp sender reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11034``
- **Severity:** Error
- **Component:** SETP sender
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Cactionsendmiap doaction.

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

Repeat or monitor the affected operation and confirm that Event ID 11034 does not recur and that setp sender processing continues.

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

- :doc:`Event ID 11000 <event-id-11000>`
- :doc:`Event ID 11001 <event-id-11001>`
- :doc:`Event ID 11002 <event-id-11002>`
