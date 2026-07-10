:orphan:

.. _rsyslog-event-id-11067:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11067: Database Monitor service: database operation failed.
   :event-id: 11067
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Database Monitor service
   :event-reference: true

rsyslog Windows Agent Event ID 11067: Database Monitor service: database operation failed
=========================================================================================

Answer
------

Database Monitor service: database operation failed. The product recorded this while processing database monitor service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11067``
- **Severity:** Error
- **Component:** Database Monitor service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Database Monitor service: database operation failed. Additional detail: {event_detail}

Possible causes
---------------

- The configured provider, DSN, server, database, or authentication setting is unavailable or invalid.
- The service account lacks database rights, or the provider returned a timeout, TLS, schema, or query error.

Immediate checks
----------------

#. Preserve the complete provider error and identify the configured database action or monitor.
#. Confirm provider or DSN bitness, server and database names, authentication mode, and service-account context.
#. Run a minimal read-only connection test before retrying one product event.

Detailed procedures
-------------------

- :doc:`Test an ODBC connection in the product context <../../shared/troubleshooting/event-id/database-test-odbc-connection>` — Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
- :doc:`Test an OLE DB connection in the product context <../../shared/troubleshooting/event-id/database-test-oledb-connection>` — Verify OLE DB provider, architecture, authentication, connectivity, and a minimal query.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11067 does not recur and that database monitor service processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11066 <event-id-11066>`
- :doc:`Event ID 11068 <event-id-11068>`
- :doc:`Event ID 11069 <event-id-11069>`
