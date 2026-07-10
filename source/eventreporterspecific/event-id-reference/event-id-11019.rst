:orphan:

.. _eventreporter-event-id-11019:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11019: Action processing: runtime operation failed.
   :event-id: 11019
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Action processing
   :event-reference: true

EventReporter Event ID 11019: Action processing: runtime operation failed
=========================================================================

Answer
------

The action processing reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11019``
- **Severity:** Error
- **Component:** Action processing
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Cactionconfigsyslogqueue loadsettings.

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

Repeat or monitor the affected operation and confirm that Event ID 11019 does not recur and that action processing processing continues.

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

- :doc:`Event ID 11014 <event-id-11014>`
- :doc:`Event ID 11021 <event-id-11021>`
- :doc:`Event ID 11022 <event-id-11022>`
