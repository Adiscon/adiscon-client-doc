:orphan:

.. _winsyslog-event-id-11149:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11149: Event Log Monitor V2 service: general runtime error.
   :event-id: 11149
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Event Log Monitor V2 service
   :event-reference: true

WinSyslog Event ID 11149: Event Log Monitor V2 service: general runtime error
=============================================================================

Answer
------

The event log monitor v2 service reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11149``
- **Severity:** Warning
- **Component:** Event Log Monitor V2 service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcewevtmonitor run.

Possible causes
---------------

- The configured Windows Event Log channel is unavailable, inaccessible, or contains an unreadable record.
- Publisher metadata, locale data, or the saved monitor state could not be processed.

Troubleshooting
---------------

#. Read the channel, provider, and record details included in the event.
#. Confirm the channel exists and the product service account can read it.
#. Check nearby Windows Event Log service errors, correct the channel or permissions issue, and retry.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11149 does not recur and that event log monitor v2 service processing continues.

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

- :doc:`Event ID 11147 <event-id-11147>`
- :doc:`Event ID 11148 <event-id-11148>`
- :doc:`Event ID 11150 <event-id-11150>`
