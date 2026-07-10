:orphan:

.. _eventreporter-event-id-11041:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11041: Start Program action: runtime operation failed.
   :event-id: 11041
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Start Program action
   :event-reference: true

EventReporter Event ID 11041: Start Program action: runtime operation failed
============================================================================

Answer
------

Start Program action: runtime operation failed. The product recorded this while processing start program action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11041``
- **Severity:** Error
- **Component:** Start Program action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Start Program action: runtime operation failed. Additional detail: {event_detail}

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

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11041 does not recur and that start program action processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
