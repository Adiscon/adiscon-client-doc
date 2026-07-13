:orphan:

.. _mwagent-event-id-11215:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11215: A debug error was forwarded to the Windows Event Log.
   :event-id: 11215
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Diagnostic forwarding
   :event-reference: true

MonitorWare Agent Event ID 11215: A debug error was forwarded to the Windows Event Log
======================================================================================

Answer
------

The product produced an error-level internal diagnostic while forwarding of debug errors to Windows Event Log warnings was enabled. This Event ID is a container; the embedded detail identifies the originating operation.

Event details
-------------

- **Event ID:** ``11215``
- **Severity:** Warning
- **Component:** Diagnostic forwarding
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Debug Error Output. Additional detail: {error_detail}`

Possible causes
---------------

- Any component can produce an error-level debug diagnostic.
- A transient dependency or configuration problem triggered the originating debug error.
- The embedded detail may describe a product defect or an expected operational failure.

Immediate checks
----------------

#. Use the embedded detail and neighboring product events to identify the originating component and operation.
#. Follow a component-specific Event ID when one is present; do not troubleshoot Event ID 11215 in isolation.
#. Collect a bounded debug log and escalate when the detail cannot be mapped to a documented operation.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the originating operation succeeds and the same embedded debug error no longer appears in Event ID 11215.

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

- :ref:`Event ID 11152 <mwagent-event-id-11152>`
- :ref:`Event ID 11169 <mwagent-event-id-11169>`
- :ref:`Event ID 11194 <mwagent-event-id-11194>`
