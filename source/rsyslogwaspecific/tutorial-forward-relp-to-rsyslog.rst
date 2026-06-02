.. _rsyslogwa-tutorial-forward-relp-to-rsyslog:

Tutorial: Forward Windows Events via RELP to rsyslog
====================================================

Use this tutorial when rsyslog Windows Agent should forward selected Windows
Event Log records to an rsyslog receiver with RELP.

Goal
----

At the end of this procedure, rsyslog Windows Agent will forward matching
Windows events to an rsyslog server through RELP.

Prerequisites
-------------

- The rsyslog receiver host name or IP address
- The RELP port used by the receiver
- Any TLS or certificate files required by the receiver
- A ruleset that receives events from an Event Log Monitor service

This tutorial assumes the rsyslog side is already configured to accept RELP.

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Send RELP <../mwagentspecific/a-sendrelp>` action to that
   ruleset.
3. Configure the target host and RELP port.
4. Keep the default RELP port unless the receiver uses a different one.
5. If the receiver expects TLS, enable SSL / TLS encryption and provide the
   matching CA or client certificate files.
6. If reliable delivery across temporary outages matters, enable disk-backed queues
   for the action.
7. Save and apply the configuration.
8. Restart the rsyslog Windows Agent service if required.

Verification
------------

1. Trigger an event that matches the ruleset.
2. Confirm that the rsyslog receiver accepts the RELP connection and receives
   the event.
3. If forwarding fails, check host, port, TLS settings, and receiver-side RELP
   listener configuration.

Next step
---------

If RELP forwarding works, continue with:

- :doc:`../mwagentspecific/a-sendrelp`
- :doc:`store-and-forward`
