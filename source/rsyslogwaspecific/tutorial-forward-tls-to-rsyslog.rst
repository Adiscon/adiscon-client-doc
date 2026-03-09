.. _rsyslogwa-tutorial-forward-tls-to-rsyslog:

Tutorial: Forward Windows Events via TLS to rsyslog
===================================================

Use this tutorial when rsyslog Windows Agent should forward selected Windows
Event Log records to an rsyslog receiver over encrypted syslog transport.

Goal
----

At the end of this procedure, rsyslog Windows Agent will forward matching
Windows events to an rsyslog server over TCP with TLS enabled.

Prerequisites
-------------

- The rsyslog receiver host name or IP address
- The TCP port used by the rsyslog TLS listener
- The framing mode expected by the receiver
- The CA certificate or client certificate files required by the receiver
- A ruleset that receives events from an Event Log Monitor service

Configure the rsyslog receiver
------------------------------

Configure the rsyslog server first so that it accepts TLS-protected syslog over
TCP. The examples below use RainerScript syntax and follow the local rsyslog
documentation under `../rsyslog2/doc/source/`.

Minimal TLS listener with anonymous authentication::

   global(
     defaultNetstreamDriver="gtls"
     defaultNetstreamDriverCAFile="/etc/rsyslog.d/certs/ca.pem"
     defaultNetstreamDriverCertFile="/etc/rsyslog.d/certs/server-cert.pem"
     defaultNetstreamDriverKeyFile="/etc/rsyslog.d/certs/server-key.pem"
   )

   module(
     load="imtcp"
     streamDriver.name="gtls"
     streamDriver.mode="1"
     streamDriver.authMode="anon"
   )

   input(
     type="imtcp"
     port="6514"
   )

Stricter listener with certificate validation and client name matching::

   global(
     defaultNetstreamDriver="gtls"
     defaultNetstreamDriverCAFile="/etc/rsyslog.d/certs/ca.pem"
     defaultNetstreamDriverCertFile="/etc/rsyslog.d/certs/server-cert.pem"
     defaultNetstreamDriverKeyFile="/etc/rsyslog.d/certs/server-key.pem"
   )

   module(
     load="imtcp"
     streamDriver.name="gtls"
     streamDriver.mode="1"
     streamDriver.authMode="x509/name"
   )

   input(
     type="imtcp"
     port="6514"
     permittedPeer=["windows-agent01.example.net"]
   )

Use `x509/name` when the receiver should validate the client certificate and
restrict accepted senders to the permitted certificate names. Use `anon` only
when that weaker trust model is acceptable in your environment. In both cases,
restart rsyslog after changing the listener configuration.

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward Syslog <a-forwardsyslogoptions>` action to that ruleset.
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

7. If the receiver requires certificate-based trust, provide the matching
   files.

   - Select the common CA PEM file used to validate the receiver.
   - If mutual authentication is required, also select the client certificate
     PEM and key PEM files.

8. Keep protocol settings modern.

   - Leave **SSL v3** disabled.
   - Leave **TLS v1.0** disabled.
   - Use **TLS v1.2** or **TLS v1.3** when the receiver supports them.

9. Save and apply the configuration.
10. Restart the rsyslog Windows Agent service if required in your environment.

Verification
------------

1. Trigger an event that matches the ruleset.
2. Confirm that the rsyslog receiver accepts the TLS connection and receives
   the forwarded event.
3. If forwarding fails, check:

   - target host and port
   - rsyslog `imtcp` listener configuration
   - TCP framing mode
   - CA, certificate, and key files
   - TLS version compatibility
   - `permittedPeer` entries on the rsyslog side when `x509/name` is used
   - firewall rules between rsyslog Windows Agent and rsyslog

Next step
---------

If forwarding works, continue with:

- :doc:`a-forwardsyslogoptions`
- :doc:`store-and-forward`
