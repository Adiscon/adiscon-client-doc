:orphan:

.. _mwagent-event-id-11163:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11163: Persisted log-rotation queue file could not be read.
   :event-id: 11163
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Log rotation queue
   :event-reference: true

MonitorWare Agent Event ID 11163: Persisted log-rotation queue file could not be read
=====================================================================================

Answer
------

At startup, the product found the durable log-rotation queue but could not read it. Persisted rotation jobs from the previous run are not loaded by this attempt.

Event details
-------------

- **Event ID:** ``11163``
- **Severity:** Warning
- **Component:** Log rotation queue
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not read persisted log rotation queue file: {queue_path}`

Possible causes
---------------

- The service account lacks read access to the queue file.
- The queue file is locked, unavailable, or damaged.
- The data directory points to an inaccessible location.

Immediate checks
----------------

#. Preserve the queue file and record its permissions, size, and timestamp.
#. Test read access under the product service account and check storage health and file locks.
#. Collect evidence before replacing the queue when pending archive work may need recovery.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the queue file can be loaded and pending rotations resume or that new queue persistence works after approved recovery.

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

- :ref:`Event ID 11153 <mwagent-event-id-11153>`
- :ref:`Event ID 11154 <mwagent-event-id-11154>`
- :ref:`Event ID 11155 <mwagent-event-id-11155>`
