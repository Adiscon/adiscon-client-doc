:orphan:

.. _rsyslog-event-id-11043:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11043: A sender connection was refused by the permitted-senders limit.
   :event-id: 11043
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Client connection licensing
   :event-reference: true

rsyslog Windows Agent Event ID 11043: A sender connection was refused by the permitted-senders limit
====================================================================================================

Answer
------

The product refused the sender identified in the event because the configured permitted-senders limit had already been reached.

Event details
-------------

- **Event ID:** ``11043``
- **Severity:** Error
- **Component:** Client connection licensing
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Connection refused. Additional detail: {event_detail}`

Possible causes
---------------

- Permitted Senders is enabled and the configured number of sender entries is already in use.
- The connecting sender is not one of the currently permitted senders.
- The permitted-senders configuration no longer matches the intended sender inventory.

Immediate checks
----------------

#. Record the configured permitted-senders limit and whether the rejected sender should be allowed; do not publish the sender address.
#. Review the current permitted-senders entries and remove only entries that are confirmed obsolete.
#. If the intended sender count exceeds the configured or licensed allowance, update the authorized configuration or license before retrying.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Send one identifiable test from an authorized sender and confirm that it is accepted exactly once without Event ID 11043.

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

- :ref:`Event ID 11005 <rsyslog-event-id-11005>`
- :ref:`Event ID 11044 <rsyslog-event-id-11044>`
- :ref:`Event ID 118 <rsyslog-event-id-118>`
