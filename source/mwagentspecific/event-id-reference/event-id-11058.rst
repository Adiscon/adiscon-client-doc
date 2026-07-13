:orphan:

.. _mwagent-event-id-11058:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11058: Filter engine: regular expression initialization failed.
   :event-id: 11058
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Filter engine
   :event-reference: true

MonitorWare Agent Event ID 11058: Filter engine: regular expression initialization failed
=========================================================================================

Answer
------

Filter engine: regular expression initialization failed. The product recorded this while processing filter engine; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11058``
- **Severity:** Error
- **Component:** Filter engine
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Cfilterlistentry cfilterlistentry. Additional detail: {event_detail}`

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

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11058 does not recur and that filter engine processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
