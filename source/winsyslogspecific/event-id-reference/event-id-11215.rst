:orphan:

.. _winsyslog-event-id-11215:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11215: Debug error output was forwarded to the Windows Event Log.
   :event-id: 11215
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Product runtime
   :event-reference: true

WinSyslog Event ID 11215: Debug error output was forwarded to the Windows Event Log
===================================================================================

Answer
------

A debug-level error message was emitted while Event Log warning forwarding was enabled.

Event details
-------------

- **Event ID:** ``11215``
- **Severity:** Warning
- **Component:** Product runtime
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Debug error output was forwarded to the Windows Event Log. Additional detail: {event_detail}

Possible causes
---------------

- The product service, dependency, service account, or required Windows resource is unavailable or incorrectly configured.
- Windows returned the appended startup, shutdown, permission, timeout, or resource error.

Immediate checks
----------------

#. Record the affected service or component, service account, state, dependencies, and complete runtime detail.
#. Check recent Service Control Manager and neighboring product events for the first failure.
#. Correct the specific dependency, account, permission, or resource condition and perform one controlled retry.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11215 does not recur and that product runtime processing continues.

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

- :ref:`Event ID 11152 <winsyslog-event-id-11152>`
- :ref:`Event ID 11169 <winsyslog-event-id-11169>`
- :ref:`Event ID 11194 <winsyslog-event-id-11194>`
