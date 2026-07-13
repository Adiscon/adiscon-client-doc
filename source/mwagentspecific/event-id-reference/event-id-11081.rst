:orphan:

.. _mwagent-event-id-11081:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11081: File Monitor service: file monitoring operation failed.
   :event-id: 11081
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: File Monitor service
   :event-reference: true

MonitorWare Agent Event ID 11081: File Monitor service: file monitoring operation failed
========================================================================================

Answer
------

File Monitor service: file monitoring operation failed. The product recorded this while processing file monitor service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11081``
- **Severity:** Error
- **Component:** File Monitor service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`File Monitor service: file monitoring operation failed. Additional detail: {event_detail}`

Possible causes
---------------

- The monitored path, wildcard expansion, sharing mode, encoding, line ending, or saved position does not match the source file.
- The service account cannot read the file, or the producer has replaced, truncated, or locked it unexpectedly.

Immediate checks
----------------

#. Record the resolved source path, file size and time, encoding, delimiter, and saved-position behavior.
#. Confirm that the service account can open the source while the producer is writing.
#. Append one unique record through the producer and verify that it is emitted once.

Detailed procedures
-------------------

- :ref:`Verify File Monitor source state and encoding <event-id-procedure-filemonitor-verify-source-state-and-encoding>` — Check source path, sharing, encoding, line endings, and read position.
- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11081 does not recur and that file monitor service processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11074 <mwagent-event-id-11074>`
- :ref:`Event ID 11075 <mwagent-event-id-11075>`
- :ref:`Event ID 11076 <mwagent-event-id-11076>`
