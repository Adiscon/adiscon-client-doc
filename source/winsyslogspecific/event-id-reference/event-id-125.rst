:orphan:

.. _winsyslog-event-id-125:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 125: Freeware mode reminder.
   :event-id: 125
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 125: Freeware mode reminder
==============================================

Answer
------

Freeware-mode limits apply to the running WinSyslog service.

Event details
-------------

- **Event ID:** ``125``
- **Severity:** Information
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`WinSyslog is running in freeware mode; the event detail describes the active limitation. Additional detail: {event_detail}`

Possible causes
---------------

- The configured object is missing, invalid, unsupported by this product, or unavailable at runtime.
- Windows or a required provider returned the operation-specific error appended to the event.

Immediate checks
----------------

#. Identify the exact service, rule, filter, action, or setting named by the complete event detail.
#. Compare that object with the product reference and preserve the first related error in the same time window.
#. Correct only the identified setting or dependency, then run one controlled test.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 125 does not recur and that licensing processing continues.

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

- :ref:`Event ID 11005 <winsyslog-event-id-11005>`
- :ref:`Event ID 11043 <winsyslog-event-id-11043>`
- :ref:`Event ID 11044 <winsyslog-event-id-11044>`
