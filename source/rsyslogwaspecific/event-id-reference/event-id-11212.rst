:orphan:

.. _rsyslog-event-id-11212:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11212: System exception while compiling an NT Event Log expression.
   :event-id: 11212
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Event Log Monitor service
   :event-reference: true

rsyslog Windows Agent Event ID 11212: System exception while compiling an NT Event Log expression
=================================================================================================

Answer
------

A protected system exception handler caught a Windows exception in this path.

Event details
-------------

- **Event ID:** ``11212``
- **Severity:** Error
- **Component:** Event Log Monitor service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** System exception while compiling an NT Event Log expression. Additional detail: {event_detail}

Possible causes
---------------

- The configured Windows Event Log channel is missing, disabled, inaccessible, or no longer matches the saved collection position.
- The service account cannot read the channel or provider metadata, or the channel was cleared or recreated.

Immediate checks
----------------

#. Identify the exact channel, collection mode, saved position, and service account.
#. Confirm that Windows reports the channel enabled and readable in the service-account context.
#. Use one safe test event to verify collection before resetting any saved position.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11212 does not recur and that event log monitor service processing continues.

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

- :ref:`Event ID 11097 <rsyslog-event-id-11097>`
- :ref:`Event ID 11098 <rsyslog-event-id-11098>`
- :ref:`Event ID 11099 <rsyslog-event-id-11099>`
