:orphan:

.. _winsyslog-event-id-900:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 900: Invalid license key rejected.
   :event-id: 900
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 900: Invalid license key rejected
====================================================

Answer
------

The WinSyslog service does not start with the rejected key.

Event details
-------------

- **Event ID:** ``900``
- **Severity:** Error
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** WinSyslog rejected an invalid license key during startup. Additional detail: {event_detail}

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

Repeat or monitor the affected operation and confirm that Event ID 900 does not recur and that licensing processing continues.

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

- :ref:`Event ID 11005 <winsyslog-event-id-11005>`
- :ref:`Event ID 11043 <winsyslog-event-id-11043>`
- :ref:`Event ID 11044 <winsyslog-event-id-11044>`
