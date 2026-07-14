:orphan:

.. _eventreporter-event-id-11153:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11153: Existing archive file was renamed before log rotation.
   :event-id: 11153
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

EventReporter Event ID 11153: Existing archive file was renamed before log rotation
===================================================================================

Answer
------

The intended archive destination already existed. The product preserved it under a timestamped backup name before retrying the move of the newly rotated log.

Event details
-------------

- **Event ID:** ``11153``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Existing archive file renamed to make room for rotated log: {backup_path}`

Possible causes
---------------

- An archive file with the same generated name already exists.
- Archive naming or retention settings produce collisions.
- A previous rotation left an unexpected destination file.

Immediate checks
----------------

#. Confirm that both the renamed backup and newly rotated file exist in the archive location.
#. Review archive naming and retention settings for repeated collisions.
#. Check free space and permissions before the next rotation.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Perform or observe a controlled rotation and confirm that the new archive is created without overwriting an existing file.

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

- :ref:`Event ID 11154 <eventreporter-event-id-11154>`
- :ref:`Event ID 11155 <eventreporter-event-id-11155>`
- :ref:`Event ID 11156 <eventreporter-event-id-11156>`
