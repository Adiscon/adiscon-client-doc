:orphan:

.. _winsyslog-event-id-11042:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11042: Write to File action has an invalid output format.
   :event-id: 11042
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Write to File action
   :event-reference: true

WinSyslog Event ID 11042: Write to File action has an invalid output format
===========================================================================

Answer
------

The action's stored output-format value is not supported by the installed product build. The current event is not written by this action.

Event details
-------------

- **Event ID:** ``11042``
- **Severity:** Error
- **Component:** Write to File action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Invalid file format {format_id} for Write to File action; nothing was written.`

Possible causes
---------------

- The configuration was imported from an incompatible version.
- A manual configuration edit supplied an invalid format value.
- The action configuration is damaged.

Immediate checks
----------------

#. Export and back up the affected Write to File action.
#. Open it in the installed Configuration Client and select a supported output format.
#. Reload the configuration and write a controlled test event.

Detailed procedures
-------------------

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the test event appears in the intended file using the selected format and Event ID 11042 does not recur.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
