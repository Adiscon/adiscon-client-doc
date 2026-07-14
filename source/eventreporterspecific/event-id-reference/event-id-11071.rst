:orphan:

.. _eventreporter-event-id-11071:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11071: Disk Space Monitor could not complete a disk-space check.
   :event-id: 11071
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Disk Space Monitor service
   :event-reference: true

EventReporter Event ID 11071: Disk Space Monitor could not complete a disk-space check
======================================================================================

Answer
------

The Disk Space Monitor service encountered an expected runtime error while checking one of its configured volumes. That polling cycle does not produce a valid disk-space result for the affected target.

Event details
-------------

- **Event ID:** ``11071``
- **Severity:** Error
- **Component:** Disk Space Monitor service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error in Disk Space Monitor: {error_detail}`

Possible causes
---------------

- A configured drive, mount point, or network path is unavailable.
- The product service account cannot query the target path.
- Windows returned a storage, path, or resource error during the check.

Immediate checks
----------------

#. Use the event detail and service configuration to identify the affected target.
#. Test that path while running as the product service account and translate any Windows error code.
#. Restore access or correct the target, then wait for the next polling cycle.

Detailed procedures
-------------------

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that a later polling cycle reports the expected disk-space state without another Event ID 11071.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
