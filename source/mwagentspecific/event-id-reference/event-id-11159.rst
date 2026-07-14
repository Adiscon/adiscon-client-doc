:orphan:

.. _mwagent-event-id-11159:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11159: Corrupt log-rotation queue file could not be quarantined.
   :event-id: 11159
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Log rotation queue
   :event-reference: true

MonitorWare Agent Event ID 11159: Corrupt log-rotation queue file could not be quarantined
==========================================================================================

Answer
------

The product detected an unreadable or invalid durable log-rotation queue and could not rename it to a quarantine file. Pending rotation work in that file cannot be trusted or loaded.

Event details
-------------

- **Event ID:** ``11159``
- **Severity:** Warning
- **Component:** Log rotation queue
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`{reason} Path: {queue_path}`

Possible causes
---------------

- The queue file or its directory is locked.
- The service account lacks rename permission.
- The data volume is unavailable, read-only, or damaged.

Immediate checks
----------------

#. Preserve a copy of the queue file and its directory metadata.
#. Check rename permissions, file locks, and storage health under the product service account.
#. Do not edit the queue manually; collect evidence and contact support if pending archive work must be recovered.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the corrupt file is quarantined or replaced safely and new rotation jobs persist normally.

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
