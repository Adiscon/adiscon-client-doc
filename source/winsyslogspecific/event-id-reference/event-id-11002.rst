:orphan:

.. _winsyslog-event-id-11002:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11002: SETP delivery delayed in the action cache.
   :event-id: 11002
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: SETP sender
   :event-reference: true

WinSyslog Event ID 11002: SETP delivery delayed in the action cache
===================================================================

Answer
------

Delivery is delayed while the action cache retries.

Event details
-------------

- **Event ID:** ``11002``
- **Severity:** Warning
- **Component:** SETP sender
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** SETP sender could not complete the send operation; the message was moved to the action cache for retry.

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

Repeat or monitor the affected operation and confirm that Event ID 11002 does not recur and that setp sender processing continues.

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
- :doc:`Event ID 11003 <event-id-11003>`
