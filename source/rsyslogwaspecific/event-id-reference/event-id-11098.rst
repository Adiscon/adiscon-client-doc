:orphan:

.. _rsyslog-event-id-11098:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11098: Event Log Monitor service: Windows Event Log could not be opened.
   :event-id: 11098
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Event Log Monitor service
   :event-reference: true

rsyslog Windows Agent Event ID 11098: Event Log Monitor service: Windows Event Log could not be opened
======================================================================================================

Answer
------

The event log monitor service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11098``
- **Severity:** Error
- **Component:** Event Log Monitor service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
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

Repeat or monitor the affected operation and confirm that Event ID 11098 does not recur and that event log monitor service processing continues.

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

- :doc:`Event ID 11097 <event-id-11097>`
- :doc:`Event ID 11099 <event-id-11099>`
- :doc:`Event ID 11100 <event-id-11100>`
