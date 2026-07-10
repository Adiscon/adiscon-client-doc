:orphan:

.. _rsyslog-event-id-11110:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11110: Event Log Monitor service: licensed Event Log Monitor limit reached.
   :event-id: 11110
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Event Log Monitor service
   :event-reference: true

rsyslog Windows Agent Event ID 11110: Event Log Monitor service: licensed Event Log Monitor limit reached
=========================================================================================================

Answer
------

The event log monitor service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11110``
- **Severity:** Error
- **Component:** Event Log Monitor service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcenteventreport loadconfig.

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

Repeat or monitor the affected operation and confirm that Event ID 11110 does not recur and that event log monitor service processing continues.

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
- :doc:`Event ID 11098 <event-id-11098>`
- :doc:`Event ID 11099 <event-id-11099>`
