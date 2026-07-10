:orphan:

.. _eventreporter-event-id-11001:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11001: SETP TLS session closed.
   :event-id: 11001
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: SETP sender
   :event-reference: true

EventReporter Event ID 11001: SETP TLS session closed
=====================================================

Answer
------

The TLS-backed SETP session is closed and will be recreated.

Event details
-------------

- **Event ID:** ``11001``
- **Severity:** Warning
- **Component:** SETP sender
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** SETP sender TLS session was closed while waiting for a reply.

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

Repeat or monitor the affected operation and confirm that Event ID 11001 does not recur and that setp sender processing continues.

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
- :doc:`Event ID 11002 <event-id-11002>`
- :doc:`Event ID 11003 <event-id-11003>`
