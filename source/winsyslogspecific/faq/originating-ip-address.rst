.. _originating-ip-address-winsyslog:

Forwarding syslog messages with original IP address in WinSyslog
================================================================

This article explains why forwarded syslog messages show the forwarding
server's IP address instead of the original device's IP address and how
to preserve the original source information in WinSyslog.

Problem
-------

When WinSyslog receives a syslog message and forwards it to another
server, the forwarded message shows WinSyslog's IP address as the source
instead of the original device's IP address. This makes it difficult to
identify the true source of log messages in multi-hop forwarding
scenarios.

Root Cause
----------

This is a limitation of the traditional UDP-based syslog protocol
(RFC 3164). The IP header of a forwarded UDP packet always reflects the
address of the forwarding server, not the original sender. The syslog
protocol itself does not mandate that the original source address be
preserved in the message body, so the information is lost unless
additional steps are taken.

Solutions
---------

Option 1: Enable RFC 3164 parsing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the originating devices are RFC 3164 compliant, WinSyslog can extract
the hostname from the syslog message header rather than relying on the
IP header.

1. Open the WinSyslog Configuration Client.
2. Navigate to the Syslog Server service.
3. Enable **RFC 3164 Parsing**.
4. Save the configuration and allow WinSyslog to reload.

.. note::

   Many devices are not fully RFC 3164 compliant. Incorrectly
   formatted headers can result in wrong hostnames being parsed.

Option 2: Use the RELP protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

RELP (Reliable Event Logging Protocol) is a TCP-based protocol that
provides guaranteed delivery and preserves the original host
information.

1. Open the WinSyslog Configuration Client.
2. Navigate to your rule or create a new one.
3. Add a new action and select **Forward Via RELP**.
4. Configure the following settings:

   * **Remote Host:** IP address or hostname of the RELP server.
   * **Port:** 20514 (default RELP port).
   * Enable **Preserve Original Hostname** if available.
   * Enable **TLS/SSL** if secure transport is required.

5. Test the connection to verify the RELP handshake.
6. Save the configuration and restart the WinSyslog service.

Benefits of RELP:

* Guaranteed message delivery with acknowledgments.
* Automatic retry for failed transmissions.
* TLS encryption for secure transport.
* Cross-platform compatibility with Unix/Linux receivers.

Option 3: Use the SETP protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SETP (Secure Event Transfer Protocol) is a proprietary Adiscon protocol
designed for Windows-to-Windows log forwarding. It preserves all
message fields, including the original source.

1. Configure a SETP listener on the receiving WinSyslog instance.
2. On the forwarding WinSyslog instance, add a **Forward via SETP**
   action.
3. Enter the IP address and port of the receiving server.
4. Save the configuration and restart the WinSyslog service.

.. note::

   SETP requires both sender and receiver to be Adiscon products.
   It is best suited for internal Windows-to-Windows environments.

Option 4: Enable Include Original Host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a tag at the beginning of the forwarded message that contains the
original host information.

1. Open the WinSyslog Configuration Client.
2. Navigate to your syslog forwarding action.
3. Enable **Include Original Host**.
4. Save the configuration and allow WinSyslog to reload.

This adds a tag such as ``FromHost: <ip>`` at the start of the message.

.. note::

   This approach is not RFC 3164 compliant. The receiving server
   must be able to parse the additional tag to extract the original
   host.

Option 5: Forward in XML format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forwarding messages in XML format preserves all original metadata,
including the source IP.

1. Open the WinSyslog Configuration Client.
2. Navigate to your forwarding action.
3. Select **XML Format** as the output format.
4. Save the configuration and allow WinSyslog to reload.

.. note::

   XML-formatted messages are not standard syslog. The receiving
   system must support XML parsing.

Recommendations
---------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Scenario
     - Recommended Solution
   * - Production environments requiring guaranteed delivery
     - RELP protocol
   * - Internal Windows-to-Windows forwarding
     - SETP protocol
   * - RFC 3164 compliant network devices
     - Enable RFC 3164 parsing
   * - Quick compatibility fix for non-compliant devices
     - Include Original Host option
   * - Automated parsing systems
     - XML format forwarding
   * - Compliance and audit requirements
     - RELP with TLS encryption

Verification
------------

1. Forward a test syslog message through WinSyslog.
2. On the receiving server, verify that the original source IP or
   hostname appears instead of WinSyslog's IP address.
3. Check the Windows Application Event Log on the WinSyslog server for
   any forwarding errors.
4. If using RELP, confirm that the connection handshake completes and
   messages are acknowledged.
