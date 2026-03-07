.. _winsyslog-tutorial-forward-syslog:

Tutorial: Forward Messages to Another Syslog Server
===================================================

Use this tutorial when WinSyslog should relay selected messages to another
syslog receiver.

Goal
----

At the end of this procedure, WinSyslog will forward matching messages from a
ruleset to a remote syslog server.

Prerequisites
-------------

- The destination host name or IP address
- The target port and transport mode expected by the receiver
- TLS details if the target requires encrypted transport

Steps
-----

1. Create or choose the ruleset whose messages should be forwarded.
2. Add a :doc:`Forward Syslog <a-forwardsyslogoptions>` action to that ruleset.
3. Configure the remote target.

   - Enter the destination host name or IP address.
   - Set the destination port.
   - Choose the transport mode that matches the receiver.

4. Keep protocol choices conservative.

   - Use UDP only if message loss is acceptable.
   - Prefer TCP-based modes when reliable delivery matters.
   - Enable TLS only when the target is configured for it.

5. Save the configuration and restart the WinSyslog service if required.

Verification
------------

1. Send a test message into WinSyslog.
2. Confirm that the target syslog server receives the forwarded event.
3. If forwarding fails, verify host, port, protocol mode, and TLS settings on
   both sides.

Next step
---------

If forwarding works, continue with:

- :doc:`a-forwardsyslogoptions`
- :doc:`producttour/store-and-forward`
- :doc:`faq/non-standard-syslog-format`
