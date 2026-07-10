:orphan:

.. _winsyslog-event-id-11068:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11068: Database Monitor service: database monitor ID field warning.
   :event-id: 11068
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Database Monitor service
   :event-reference: true

WinSyslog Event ID 11068: Database Monitor service: database monitor ID field warning
=====================================================================================

Answer
------

Database Monitor service: database monitor ID field warning. The product recorded this while processing database monitor service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11068``
- **Severity:** Warning
- **Component:** Database Monitor service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Database Monitor service: database monitor ID field warning. Additional detail: {event_detail}

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

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11068 does not recur and that database monitor service processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11066 <winsyslog-event-id-11066>`
- :ref:`Event ID 11067 <winsyslog-event-id-11067>`
- :ref:`Event ID 11069 <winsyslog-event-id-11069>`
