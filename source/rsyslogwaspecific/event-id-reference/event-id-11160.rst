:orphan:

.. _rsyslog-event-id-11160:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11160: Corrupt log-rotation queue file was quarantined.
   :event-id: 11160
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Log rotation queue
   :event-reference: true

rsyslog Windows Agent Event ID 11160: Corrupt log-rotation queue file was quarantined
=====================================================================================

Answer
------

The product detected an invalid durable log-rotation queue and successfully renamed it for quarantine. The invalid queue is not loaded; new rotation work can use a new queue file.

Event details
-------------

- **Event ID:** ``11160``
- **Severity:** Warning
- **Component:** Log rotation queue
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`{reason} Renamed to: {quarantine_path}`

Possible causes
---------------

- The previous service run ended while queue state was being persisted.
- The queue file was externally modified or damaged.
- Storage or backup software produced incomplete queue contents.

Immediate checks
----------------

#. Preserve the quarantined file for analysis and record its path.
#. Check neighboring shutdown, storage, and file-system events.
#. Verify that a new queue file is created and inspect whether any rotated files from the quarantined jobs remain pending.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that new log rotations complete and durable queue state can be saved and reloaded.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :ref:`Event ID 11153 <rsyslog-event-id-11153>`
- :ref:`Event ID 11154 <rsyslog-event-id-11154>`
- :ref:`Event ID 11155 <rsyslog-event-id-11155>`
