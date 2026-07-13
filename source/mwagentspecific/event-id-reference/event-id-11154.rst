:orphan:

.. _mwagent-event-id-11154:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11154: Log rotation was deferred because an archive destination could not be renamed.
   :event-id: 11154
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

MonitorWare Agent Event ID 11154: Log rotation was deferred because an archive destination could not be renamed
===============================================================================================================

Answer
------

An archive destination already existed and the product could not rename it out of the way. The rotated file remains pending for a later attempt.

Event details
-------------

- **Event ID:** ``11154``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not rename blocking destination; rotate move deferred: {destination_path}`

Possible causes
---------------

- The service account lacks rename or delete permission in the archive directory.
- Another process has the destination file open.
- The archive path is unavailable, read-only, or out of space.

Immediate checks
----------------

#. Preserve the pending rotated file and identify the blocking destination from the event.
#. Test rename access under the product service account and check file locks and free space.
#. Remove the blocking condition and allow log-rotation recovery to retry.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the pending rotated file reaches the archive destination and Event ID 11154 stops recurring.

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
- :ref:`Event ID 11155 <mwagent-event-id-11155>`
- :ref:`Event ID 11156 <mwagent-event-id-11156>`
