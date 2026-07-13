:orphan:

.. _winsyslog-event-id-11161:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11161: Configuration reload kept the existing log-rotation workers.
   :event-id: 11161
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

WinSyslog Event ID 11161: Configuration reload kept the existing log-rotation workers
=====================================================================================

Answer
------

Active log-rotation work did not finish within the reload timeout. The product keeps the current worker pool and skips replacing it so detached work retains a valid owner.

Event details
-------------

- **Event ID:** ``11161``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Configuration reload kept the existing asynchronous log rotation worker pool because active detached work did not drain before the bounded stop timeout.`

Possible causes
---------------

- A rotation move, compression, or archive operation is slow or blocked.
- The archive destination is unavailable or under heavy load.
- The configured reload timeout is shorter than active rotation work requires.

Immediate checks
----------------

#. Inspect pending and active rotation work without terminating the service.
#. Check archive availability, file locks, compression load, and free space.
#. Let active work finish, then perform one controlled configuration reload.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that active rotations complete and a later reload applies the intended rotation-worker settings without Event ID 11161.

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
- :ref:`Event ID 11155 <winsyslog-event-id-11155>`
