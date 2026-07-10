:orphan:

.. _winsyslog-event-id-11066:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11066: Database Monitor service: database operation failed.
   :event-id: 11066
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Database Monitor service
   :event-reference: true

WinSyslog Event ID 11066: Database Monitor service: database operation failed
=============================================================================

Answer
------

The database monitor service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11066``
- **Severity:** Error
- **Component:** Database Monitor service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cinfosourcedbmonitor checkmaxidvalue.

Possible causes
---------------

- The database is unavailable or rejected the connection.
- The configured data source, credentials, query, table, or field mapping is invalid.

Troubleshooting
---------------

#. Read the database error included in the event detail.
#. Test the configured data source and credentials from the product service account.
#. Verify the query, table, and field mappings, then retry the action or monitor.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11066 does not recur and that database monitor service processing continues.

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

- :doc:`Event ID 11067 <event-id-11067>`
- :doc:`Event ID 11068 <event-id-11068>`
- :doc:`Event ID 11069 <event-id-11069>`
