.. _eventreporter-tutorial-forward-tls-to-rsyslog:

Tutorial: Forward Windows Events via TLS to rsyslog
===================================================

Use this tutorial when EventReporter should forward selected Windows Event Log
records to an rsyslog receiver over encrypted syslog transport.

Goal
----

At the end of this procedure, EventReporter will forward matching Windows
events to an rsyslog server over TCP with TLS enabled.

Prerequisites
-------------

- The rsyslog receiver host name or IP address
- The TCP port used by the rsyslog TLS listener
- The framing mode expected by the receiver
- The CA certificate or client certificate files required by the receiver
- A ruleset that receives events from an Event Log Monitor service

This tutorial assumes the rsyslog side is already configured to accept syslog
over TLS. EventReporter must use the same port, TLS trust model, and
certificate files expected by that receiver.

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward Syslog <../mwagentspecific/a-forwardsyslogoptions>`
   action to that ruleset.
3. Configure the target host and port.

   - Enter the rsyslog server host name or IP address.
   - Set the TCP port used by the rsyslog TLS listener.

4. Select a TCP-based syslog transport mode.

   - Prefer **TCP (octet-count based framing)** when the receiver supports it.
   - Otherwise use the TCP framing mode that matches the rsyslog listener.

5. Open the TLS settings for the action and enable **SSL / TLS Encryption**.
6. Select the TLS mode that matches the receiver configuration.

   - Use the default anonymous mode only if the receiver is configured for it.
   - Use certificate-based mode when the receiver expects CA validation or a
     client certificate.

7. If the receiver requires certificate-based trust, provide the matching files.

   - Select the common CA PEM file used to validate the receiver.
   - If mutual authentication is required, also select the client certificate
     PEM and key PEM files.

8. Keep protocol settings modern.

   - Leave **SSL v3** disabled.
   - Leave **TLS v1.0** disabled.
   - Use **TLS v1.2** or **TLS v1.3** when the receiver supports them.

9. Save and apply the configuration.
10. Restart the EventReporter service if required in your environment.

Verification
------------

1. Trigger an event that matches the ruleset.
2. Confirm that the rsyslog receiver accepts the TLS connection and receives
   the forwarded event.
3. If forwarding fails, check:

   - target host and port
   - TCP framing mode
   - CA, certificate, and key files
   - TLS version compatibility
   - firewall rules between EventReporter and rsyslog

Next step
---------

If forwarding works, continue with:

- :doc:`../mwagentspecific/a-forwardsyslogoptions`
- :doc:`store-and-forward`
