:orphan:

.. _winsyslog-event-id-11100:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11100: Event Log Monitor service: runtime operation failed.
   :event-id: 11100
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Event Log Monitor service
   :event-reference: true

WinSyslog Event ID 11100: Event Log Monitor service: runtime operation failed
=============================================================================

Answer
------

Event Log Monitor service: runtime operation failed. The product recorded this while processing event log monitor service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11100``
- **Severity:** Warning
- **Component:** Event Log Monitor service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Nteventreport showevtlog. Additional detail: {event_detail}`

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

- :ref:`Verify Event Log channel access and bookmark state <event-id-procedure-eventlog-verify-channel-access-and-bookmark>` — Confirm channel existence, enablement, account access, and collection position.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11100 does not recur and that event log monitor service processing continues.

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

- :ref:`Event ID 11097 <winsyslog-event-id-11097>`
- :ref:`Event ID 11098 <winsyslog-event-id-11098>`
- :ref:`Event ID 11099 <winsyslog-event-id-11099>`
