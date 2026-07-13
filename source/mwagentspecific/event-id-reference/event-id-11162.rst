:orphan:

.. _mwagent-event-id-11162:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11162: Log-rotation jobs cannot be persisted because the data directory is unset.
   :event-id: 11162
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Log rotation queue
   :event-reference: true

MonitorWare Agent Event ID 11162: Log-rotation jobs cannot be persisted because the data directory is unset
===========================================================================================================

Answer
------

During a runtime settings change, the product had detached rotation jobs but no data directory in which to persist them. The jobs remain in memory and are re-queued, but they are not durable across a service stop or crash.

Event details
-------------

- **Event ID:** ``11162``
- **Severity:** Warning
- **Component:** Log rotation queue
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Data directory unset: in-memory detached rotation jobs re-queued without persistence.`

Possible causes
---------------

- The product data directory is empty or invalid.
- Configuration reload temporarily removed the data-directory setting.
- The data directory could not be resolved during startup or reload.

Immediate checks
----------------

#. Avoid stopping the service while in-memory jobs remain pending.
#. Correct the product data-directory setting and verify service-account access.
#. Reload once and monitor the rotation queue until pending jobs complete.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the queue file is persisted in the configured data directory and pending rotations survive a controlled reload.

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

- :ref:`Event ID 11153 <mwagent-event-id-11153>`
- :ref:`Event ID 11154 <mwagent-event-id-11154>`
- :ref:`Event ID 11155 <mwagent-event-id-11155>`
