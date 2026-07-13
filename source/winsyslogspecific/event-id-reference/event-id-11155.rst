:orphan:

.. _winsyslog-event-id-11155:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11155: Cross-volume archive copy succeeded but source cleanup failed.
   :event-id: 11155
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

WinSyslog Event ID 11155: Cross-volume archive copy succeeded but source cleanup failed
=======================================================================================

Answer
------

The product copied the rotated log to an archive on another volume, but could not delete the original source file. Both copies may remain.

Event details
-------------

- **Event ID:** ``11155``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Cross-volume copy succeeded but source delete failed: {source_path}`

Possible causes
---------------

- The service account can read but cannot delete the source file.
- Another process reopened or locked the source file.
- The source volume became read-only or unavailable after the copy.

Immediate checks
----------------

#. Verify that the archive copy is complete before touching the source.
#. Test delete permission and inspect file locks on the source path.
#. After confirming the archive, remove the source through the organization's approved retention procedure.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that only the intended archive remains and a later cross-volume rotation completes without Event ID 11155.

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

- :ref:`Event ID 11153 <winsyslog-event-id-11153>`
- :ref:`Event ID 11154 <winsyslog-event-id-11154>`
- :ref:`Event ID 11156 <winsyslog-event-id-11156>`
