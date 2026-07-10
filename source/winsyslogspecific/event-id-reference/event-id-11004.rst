:orphan:

.. _winsyslog-event-id-11004:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11004: SETP session restored.
   :event-id: 11004
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: SETP sender
   :event-reference: true

WinSyslog Event ID 11004: SETP session restored
===============================================

Answer
------

Forwarding can continue.

Event details
-------------

- **Event ID:** ``11004``
- **Severity:** Information
- **Component:** SETP sender
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** SETP sender session has been restored.

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

Repeat or monitor the affected operation and confirm that Event ID 11004 does not recur and that setp sender processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :doc:`Event ID 11000 <event-id-11000>`
- :doc:`Event ID 11001 <event-id-11001>`
- :doc:`Event ID 11002 <event-id-11002>`
