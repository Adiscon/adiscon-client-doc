:orphan:

.. _mwagent-event-id-11028:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11028: Configured action raised an unknown exception below its retry limit.
   :event-id: 11028
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Rule engine action
   :event-reference: true

MonitorWare Agent Event ID 11028: Configured action raised an unknown exception below its retry limit
=====================================================================================================

Answer
------

An action raised an exception that did not contain a normal diagnostic error object while its attempt count was below the configured retry limit. Another attempt occurs only when retry processing is enabled and the failure remains retryable.

Event details
-------------

- **Event ID:** ``11028``
- **Severity:** Error
- **Component:** Rule engine action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`An unknown exception occurred while applying a configured action below its configured retry limit.`

Possible causes
---------------

- An action or one of its providers raised an unexpected exception.
- A transient resource or third-party component failed outside the action's normal error path.
- The affected action encountered a product defect.

Immediate checks
----------------

#. Record whether a later retry succeeds and identify the affected action from neighboring events.
#. If retries continue to fail, collect a bounded debug log and Windows Error Reporting data.
#. Avoid changing unrelated action settings; escalate a reproducible unknown exception with the collected evidence.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that a later retry or controlled test completes successfully and Event ID 11028 stops recurring.

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

- :ref:`Event ID 11014 <mwagent-event-id-11014>`
- :ref:`Event ID 11019 <mwagent-event-id-11019>`
- :ref:`Event ID 11021 <mwagent-event-id-11021>`
