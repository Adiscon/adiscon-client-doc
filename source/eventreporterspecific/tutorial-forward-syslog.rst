.. _eventreporter-tutorial-forward-syslog:

Tutorial: Forward Windows Events to a Syslog Server
===================================================

Use this tutorial when EventReporter should relay selected Windows events to a
remote syslog receiver.

Goal
----

At the end of this procedure, EventReporter will forward matching Windows event
log entries to a remote syslog server.

Prerequisites
-------------

- The destination host name or IP address
- The target port and transport mode expected by the receiver
- A ruleset that receives events from an Event Log Monitor service

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward Syslog <../mwagentspecific/a-forwardsyslogoptions>`
   action to that ruleset.
3. Configure the remote target.

   - Enter the destination host name or IP address.
   - Set the destination port.
   - Choose the transport mode that matches the receiver.

4. Keep protocol choices conservative.

   - Use UDP only if message loss is acceptable.
   - Prefer TCP-based modes when reliable delivery matters.

5. Save and apply the configuration.
6. Restart the EventReporter service if required.

Verification
------------

1. Trigger an event that matches the ruleset.
2. Confirm that the remote syslog server receives it.
3. If forwarding fails, verify host, port, protocol mode, and firewall rules on
   both sides.

Next step
---------

If forwarding works, continue with:

- :doc:`../mwagentspecific/a-forwardsyslogoptions`
- :doc:`store-and-forward`
