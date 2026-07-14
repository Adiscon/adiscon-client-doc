:orphan:

.. _mwagent-event-id-11183:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11183: Configuration reload was skipped because the log-rotation scheduler did not stop.
   :event-id: 11183
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Configuration reload
   :event-reference: true

MonitorWare Agent Event ID 11183: Configuration reload was skipped because the log-rotation scheduler did not stop
==================================================================================================================

Answer
------

The product could not stop the existing log-rotation scheduler within the reload timeout. It keeps the current scheduler owner alive and does not apply the requested configuration reload.

Event details
-------------

- **Event ID:** ``11183``
- **Severity:** Warning
- **Component:** Configuration reload
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Configuration reload skipped because the log rotation scheduler did not stop before its bounded timeout.`

Possible causes
---------------

- A rotation, compression, or archive operation is still active or blocked.
- The archive destination is slow or unavailable.
- The bounded stop timeout expired before scheduler shutdown completed.

Immediate checks
----------------

#. Confirm that the current configuration remains active.
#. Inspect pending rotation work, archive availability, file locks, and storage performance.
#. Allow the scheduler to finish and perform one controlled reload.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the later reload succeeds and the intended configuration becomes active without Event ID 11183.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11184 <mwagent-event-id-11184>`
- :ref:`Event ID 11185 <mwagent-event-id-11185>`
- :ref:`Event ID 11186 <mwagent-event-id-11186>`
