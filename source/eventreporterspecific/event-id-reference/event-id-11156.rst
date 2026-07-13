:orphan:

.. _eventreporter-event-id-11156:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11156: Rotated log could not be moved to its archive destination.
   :event-id: 11156
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

EventReporter Event ID 11156: Rotated log could not be moved to its archive destination
=======================================================================================

Answer
------

The product exhausted its normal move and cross-volume copy handling for a rotated log. The event identifies the source, destination, and Windows error.

Event details
-------------

- **Event ID:** ``11156``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`source='{source_path}' dest='{destination_path}' err={error_code}`

Possible causes
---------------

- The archive directory is unavailable or cannot be created.
- Permissions, file locks, path length, or free space prevent the move.
- The source or destination volume returned a Windows storage error.

Immediate checks
----------------

#. Translate the Windows error and preserve the source rotated file.
#. Test directory creation and file move access under the product service account.
#. Correct the path, permission, lock, or storage condition and allow recovery to retry.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the source file is moved to the intended archive and Event ID 11156 no longer recurs.

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

- :ref:`Event ID 11153 <eventreporter-event-id-11153>`
- :ref:`Event ID 11154 <eventreporter-event-id-11154>`
- :ref:`Event ID 11155 <eventreporter-event-id-11155>`
