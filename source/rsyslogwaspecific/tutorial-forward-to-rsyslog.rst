.. _rsyslogwa-tutorial-forward-to-rsyslog:

Tutorial: Forward Windows Events to rsyslog
===========================================

Use this tutorial when rsyslog Windows Agent should relay selected Windows
events to a remote rsyslog server.

Goal
----

At the end of this procedure, rsyslog Windows Agent will forward matching
Windows event log entries to a remote rsyslog receiver.

Prerequisites
-------------

- The destination host name or IP address
- The target port and transport mode expected by the receiver
- A ruleset that receives events from an Event Log Monitor service

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward Syslog <a-forwardsyslogoptions>` action to that ruleset.
3. Configure the remote target.

   - Enter the destination host name or IP address.
   - Set the destination port.
   - Choose the transport mode that matches the receiver.

4. Keep protocol choices conservative.

   - Use UDP only if message loss is acceptable.
   - Prefer TCP-based modes when reliable delivery matters.

5. Save and apply the configuration.
6. Restart the rsyslog Windows Agent service if required.

Verification
------------

1. Trigger an event that matches the ruleset.
2. Confirm that the remote rsyslog server receives it.
3. If forwarding fails, verify host, port, protocol mode, and firewall rules on
   both sides.

Next step
---------

If forwarding works, continue with:

- :doc:`tutorial-forward-tls-to-rsyslog`
- :doc:`a-forwardsyslogoptions`
