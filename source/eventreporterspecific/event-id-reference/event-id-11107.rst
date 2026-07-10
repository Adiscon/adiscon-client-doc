:orphan:

.. _eventreporter-event-id-11107:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11107: Windows Event Log cleared.
   :event-id: 11107
   :event-product: EventReporter
   :event-severity: Information
   :event-component: Event Log Monitor service
   :event-reference: true

EventReporter Event ID 11107: Windows Event Log cleared
=======================================================

Answer
------

The Event Log Monitor cleared the configured Windows Event Log.

Event details
-------------

- **Event ID:** ``11107``
- **Severity:** Information
- **Component:** Event Log Monitor service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcenteventreport showevtlog.

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

Repeat or monitor the affected operation and confirm that Event ID 11107 does not recur and that event log monitor service processing continues.

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

- :doc:`Event ID 11106 <event-id-11106>`
