:orphan:

.. _winsyslog-event-id-11031:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11031: OLE DB action: database operation failed.
   :event-id: 11031
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: OLE DB action
   :event-reference: true

WinSyslog Event ID 11031: OLE DB action: database operation failed
==================================================================

Answer
------

The ole db action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11031``
- **Severity:** Error
- **Component:** OLE DB action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Cactionoledb doaction.

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

Repeat or monitor the affected operation and confirm that Event ID 11031 does not recur and that ole db action processing continues.

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

- :doc:`Event ID 11012 <event-id-11012>`
- :doc:`Event ID 11013 <event-id-11013>`
- :doc:`Event ID 11032 <event-id-11032>`
