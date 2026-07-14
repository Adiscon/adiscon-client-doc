:orphan:

.. _rsyslog-event-id-11157:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11157: Existing archive could not be renamed to prevent overwrite.
   :event-id: 11157
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

rsyslog Windows Agent Event ID 11157: Existing archive could not be renamed to prevent overwrite
================================================================================================

Answer
------

The product found an archive-name collision but could not rename the existing archive to the protected fallback name. It does not intentionally overwrite the existing file.

Event details
-------------

- **Event ID:** ``11157``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Prevent archive overwrite rename failed: {archive_path}`

Possible causes
---------------

- The archive file is locked by another process.
- The service account lacks rename permission.
- The archive directory is unavailable, read-only, or out of space.

Immediate checks
----------------

#. Identify and preserve the existing archive file.
#. Check file locks, directory permissions, and free space under the product service account.
#. Remove the blocking condition and perform a controlled rotation.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that archive-name collisions are resolved without overwriting files and Event ID 11157 does not recur.

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

- :ref:`Event ID 11153 <rsyslog-event-id-11153>`
- :ref:`Event ID 11154 <rsyslog-event-id-11154>`
- :ref:`Event ID 11155 <rsyslog-event-id-11155>`
