:orphan:

.. _mwagent-event-id-11008:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11008: Action configuration: configured action feature is unavailable.
   :event-id: 11008
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Action configuration
   :event-reference: true

MonitorWare Agent Event ID 11008: Action configuration: configured action feature is unavailable
================================================================================================

Answer
------

Action configuration: configured action feature is unavailable. The product recorded this while processing action configuration; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11008``
- **Severity:** Warning
- **Component:** Action configuration
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Action configuration: configured action feature is unavailable. Additional detail: {event_detail}

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

- :doc:`Collect evidence for an escalation-only runtime event <../../shared/troubleshooting/event-id/runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11008 does not recur and that action configuration processing continues.

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

- :doc:`Event ID 11007 <event-id-11007>`
- :doc:`Event ID 11009 <event-id-11009>`
