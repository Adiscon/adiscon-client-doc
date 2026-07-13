:orphan:

.. _rsyslog-event-id-11148:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11148: Event Log Monitor could not create its saved bookmark.
   :event-id: 11148
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Event Log Monitor V2 service
   :event-reference: true

rsyslog Windows Agent Event ID 11148: Event Log Monitor could not create its saved bookmark
===========================================================================================

Answer
------

The product could not recreate the Event Log Monitor bookmark from its saved XML. It discards the temporary saved-state marker and creates an empty bookmark so monitoring can continue.

Event details
-------------

- **Event ID:** ``11148``
- **Severity:** Error
- **Component:** Event Log Monitor V2 service
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`EvtCreateBookmark failed with ErrorCode = '{error_code}'. An empty bookmark will be created.`

Possible causes
---------------

- The saved bookmark XML is invalid, incomplete, or incompatible.
- The monitored Windows channel or provider changed.
- Windows Event Log returned an error while creating the bookmark.

Immediate checks
----------------

#. Translate the Windows error code and export the affected service configuration and saved bookmark state.
#. Verify that the configured Windows Event Log channel exists and is accessible to the product service account.
#. Allow the service to create the empty bookmark, then verify the resulting start position and retention impact.

Detailed procedures
-------------------

- :ref:`Verify Event Log channel access and bookmark state <event-id-procedure-eventlog-verify-channel-access-and-bookmark>` — Confirm channel existence, enablement, account access, and collection position.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Write a uniquely identifiable test event and confirm that Event Log Monitor collects it and persists a valid new bookmark.

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

- :ref:`Event ID 11147 <rsyslog-event-id-11147>`
- :ref:`Event ID 11149 <rsyslog-event-id-11149>`
- :ref:`Event ID 11150 <rsyslog-event-id-11150>`
