:orphan:

.. _eventreporter-event-id-11116:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11116: Syslog listener: runtime operation failed.
   :event-id: 11116
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Syslog listener
   :event-reference: true

EventReporter Event ID 11116: Syslog listener: runtime operation failed
=======================================================================

Answer
------

The syslog listener reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11116``
- **Severity:** Error
- **Component:** Syslog listener
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcepassivesyslog run.

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

Repeat or monitor the affected operation and confirm that Event ID 11116 does not recur and that syslog listener processing continues.

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

- :doc:`Event ID 11112 <event-id-11112>`
- :doc:`Event ID 11113 <event-id-11113>`
- :doc:`Event ID 11114 <event-id-11114>`
