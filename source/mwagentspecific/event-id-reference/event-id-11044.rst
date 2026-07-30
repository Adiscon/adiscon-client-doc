:orphan:

.. _mwagent-event-id-11044:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11044: A sender connection exceeded the licensed client limit.
   :event-id: 11044
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Client connection licensing
   :event-reference: true

MonitorWare Agent Event ID 11044: A sender connection exceeded the licensed client limit
========================================================================================

Answer
------

The product refused the sender identified in the event because accepting it would exceed the client-connection allowance of the installed edition or license.

Event details
-------------

- **Event ID:** ``11044``
- **Severity:** Error
- **Component:** Client connection licensing
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Client license limit exceeded. Additional detail: {event_detail}`

Possible causes
---------------

- More distinct senders are connecting than the installed edition or license permits.
- A changed sender address causes an existing device to be counted as an additional client.
- The installed license is not the intended license for this product or system.

Immediate checks
----------------

#. Confirm the running product, edition, displayed license status, and client allowance without copying license data.
#. Compare the intended sender inventory with the currently accepted senders and identify address changes or unintended sources.
#. Remove unintended senders or install an authorized license with sufficient client capacity, then retry one controlled sender test.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Send one identifiable test from the intended sender and confirm that it is accepted exactly once without Event ID 11044.

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

- :ref:`Event ID 11005 <mwagent-event-id-11005>`
- :ref:`Event ID 11043 <mwagent-event-id-11043>`
- :ref:`Event ID 118 <mwagent-event-id-118>`
