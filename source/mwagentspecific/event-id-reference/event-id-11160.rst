:orphan:

.. _mwagent-event-id-11160:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11160: Log rotation: runtime operation failed.
   :event-id: 11160
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

MonitorWare Agent Event ID 11160: Log rotation: runtime operation failed
========================================================================

Answer
------

Log rotation: runtime operation failed. The product recorded this while processing log rotation; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11160``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Logrotationsubsystem. Additional detail: {event_detail}

Possible causes
---------------

- The configured path is unavailable, full, or not writable by the service account.
- Rotation naming, retention, timing, or another process holding the file prevents the required operation.

Immediate checks
----------------

#. Record the resolved path, file name, rotation trigger, and service-account context.
#. Check existence, ACLs, free space, current file sizes, and recent timestamps.
#. Perform one controlled write or rotation and verify that active output continues.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11160 does not recur and that log rotation processing continues.

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

- :ref:`Event ID 11153 <mwagent-event-id-11153>`
- :ref:`Event ID 11154 <mwagent-event-id-11154>`
- :ref:`Event ID 11155 <mwagent-event-id-11155>`
