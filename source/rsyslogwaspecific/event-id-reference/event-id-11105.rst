:orphan:

.. _rsyslog-event-id-11105:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11105: Event Log Monitor service: Windows Event Log clear retry succeeded.
   :event-id: 11105
   :event-product: rsyslog Windows Agent
   :event-severity: Information
   :event-component: Event Log Monitor service
   :event-reference: true

rsyslog Windows Agent Event ID 11105: Event Log Monitor service: Windows Event Log clear retry succeeded
========================================================================================================

Answer
------

The event log monitor service reported an informational condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11105``
- **Severity:** Information
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

Repeat or monitor the affected operation and confirm that Event ID 11105 does not recur and that event log monitor service processing continues.

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

- :doc:`Event ID 11097 <event-id-11097>`
- :doc:`Event ID 11098 <event-id-11098>`
- :doc:`Event ID 11099 <event-id-11099>`
