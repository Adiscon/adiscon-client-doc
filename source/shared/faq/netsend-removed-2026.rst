:orphan:

.. _netsend-removed-2026:

Why is Net Send no longer available in the configuration client?
================================================================

Question
--------

I cannot add a Net Send action in the configuration client. Where did it go?

Answer
------

Net Send was **removed from the configuration client** in the **2026.07** release
for WinSyslog, EventReporter, and MonitorWare Agent.

Details
-------

The Windows Messenger service (``net send``) is deprecated on modern Windows and
was unreliable for production alerting. The **2026.07** client no longer offers
Net Send in the action list.

Existing configurations that still reference Net Send may load with a skip or
warning depending on client version. You cannot create new Net Send actions from
the current client.

Action path
-----------

Use one of these alternatives in your ruleset:

- **Send Email** for operator notifications.

.. only:: winsyslog or winsyslog_j or eventreporter or mwagent

   - **HTTP REST Output** for webhooks and REST endpoints (see **Actions →
     Forwarding** in this manual).

- **Start Program** to invoke a custom script or notifier.
- Syslog or RELP forwarding to a central monitoring system.

Related information
-------------------

For the deprecated Net Send action reference and HTTP REST Output details, see
**Configuration → Actions** in the WinSyslog, EventReporter, or MonitorWare
Agent manual.
