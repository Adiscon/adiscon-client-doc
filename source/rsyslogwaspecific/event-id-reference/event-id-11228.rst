:orphan:

.. _rsyslog-event-id-11228:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11228: Action disk queue flush failed during shutdown.
   :event-id: 11228
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Action persistence
   :event-reference: true

rsyslog Windows Agent Event ID 11228: Action disk queue flush failed during shutdown
====================================================================================

Answer
------

The runtime could not force the affected retry queue data to stable storage at the shutdown boundary.

Event details
-------------

- **Event ID:** ``11228``
- **Severity:** Error
- **Component:** Action persistence
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`An action disk queue could not be flushed during shutdown; retryable work may be lost. Additional detail: {event_detail}`

Possible causes
---------------

- The disk is full or unavailable, the queue path is inaccessible, or the storage device returned an I/O error.

Immediate checks
----------------

#. Check free space, storage health, queue-directory permissions, and the Windows system log.
#. Preserve the queue files before restarting if recovery is required.

Detailed procedures
-------------------

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Stop the service again and confirm that Event ID 11228 does not recur and the action queue remains recoverable.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry.
- The action queue path, storage free space, permissions, and debug log.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11223 <rsyslog-event-id-11223>`
- :ref:`Event ID 11224 <rsyslog-event-id-11224>`
