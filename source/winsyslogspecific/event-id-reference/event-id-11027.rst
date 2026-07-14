:orphan:

.. _winsyslog-event-id-11027:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11027: Configured action raised an unknown exception at its retry limit.
   :event-id: 11027
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Rule engine action
   :event-reference: true

WinSyslog Event ID 11027: Configured action raised an unknown exception at its retry limit
==========================================================================================

Answer
------

An action raised an exception that did not contain a normal diagnostic error object when its attempt count was at or beyond the configured retry limit. The Event ID cannot identify the action-specific root cause.

Event details
-------------

- **Event ID:** ``11027``
- **Severity:** Error
- **Component:** Rule engine action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`An unknown exception occurred while applying a configured action at or beyond its configured retry limit.`

Possible causes
---------------

- An action or one of its providers raised an unexpected exception.
- A resource, driver, or third-party component failed outside the action's normal error path.
- The affected action encountered a product defect.

Immediate checks
----------------

#. Record the action name from neighboring debug and configuration context.
#. Collect a bounded debug log and Windows Error Reporting data from one controlled reproduction.
#. Do not repeatedly retry a state-changing action; collect evidence and escalate if the exception is reproducible.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the affected action completes a controlled test successfully and Event ID 11027 does not recur.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11014 <winsyslog-event-id-11014>`
- :ref:`Event ID 11019 <winsyslog-event-id-11019>`
- :ref:`Event ID 11021 <winsyslog-event-id-11021>`
