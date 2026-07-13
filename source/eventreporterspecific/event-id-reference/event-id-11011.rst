:orphan:

.. _eventreporter-event-id-11011:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11011: ODBC database action: database operation failed.
   :event-id: 11011
   :event-product: EventReporter
   :event-severity: Error
   :event-component: ODBC database action
   :event-reference: true

EventReporter Event ID 11011: ODBC database action: database operation failed
=============================================================================

Answer
------

ODBC database action: database operation failed. The product recorded this while processing odbc database action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11011``
- **Severity:** Error
- **Component:** ODBC database action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`ODBC database action: database operation failed. Additional detail: {event_detail}`

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

- :ref:`Test an ODBC connection in the product context <event-id-procedure-database-test-odbc-connection>` — Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11011 does not recur and that odbc database action processing continues.

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

- :ref:`Event ID 11010 <eventreporter-event-id-11010>`
- :ref:`Event ID 11029 <eventreporter-event-id-11029>`
- :ref:`Event ID 11030 <eventreporter-event-id-11030>`
