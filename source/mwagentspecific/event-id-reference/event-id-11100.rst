:orphan:

.. _mwagent-event-id-11100:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11100: A corrupted Windows Event Log record was skipped.
   :event-id: 11100
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Event Log Monitor service
   :event-reference: true

MonitorWare Agent Event ID 11100: A corrupted Windows Event Log record was skipped
==================================================================================

Answer
------

The legacy Event Log Monitor encountered a corrupted record and, as configured, advanced its persisted position past that record. The corrupted record is not processed.

Event details
-------------

- **Event ID:** ``11100``
- **Severity:** Warning
- **Component:** Event Log Monitor service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The Event Log '{channel_name}' is corrupted at entry {record_number}. Corruption handling is configured to ignore corrupted events, so processing continues.`

Possible causes
---------------

- The Windows Event Log channel contains a damaged record.
- The underlying event-log file or storage was corrupted.
- An external restore or maintenance operation left an unreadable record.

Immediate checks
----------------

#. Record the channel and record number from the event.
#. Use Windows Event Viewer or native event-log tools to verify the channel and export it before repair.
#. Review the configured corruption-handling policy and repair or clear the Windows channel only under the organization's retention procedure.

Detailed procedures
-------------------

- :ref:`Verify Event Log channel access and bookmark state <event-id-procedure-eventlog-verify-channel-access-and-bookmark>` — Confirm channel existence, enablement, account access, and collection position.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that monitoring advances to later records and that newly written test events are collected from the channel.

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

- :ref:`Event ID 11097 <mwagent-event-id-11097>`
- :ref:`Event ID 11098 <mwagent-event-id-11098>`
- :ref:`Event ID 11099 <mwagent-event-id-11099>`
