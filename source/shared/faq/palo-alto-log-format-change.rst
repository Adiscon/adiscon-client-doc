.. include:: ../supporting-labels.rst

.. _palo-alto-log-format-change:

Recommended Palo Alto Firewall Syslog Configuration
===================================================

This article provides configuration recommendations for Palo Alto firewalls to ensure consistent and reliable syslog message parsing by your syslog server.

Question
--------

What is the recommended syslog format configuration for Palo Alto firewalls when sending logs to a syslog server?

Answer
------

**We recommend configuring Palo Alto firewalls to use IETF** :doc:`RFC 5424 <../../glossaryofterms/rfc5424>` **syslog format instead of BSD (RFC 3164) format.** The IETF format provides a structured, unambiguous message format that ensures consistent parsing regardless of Palo Alto firmware version or spacing differences in log messages.

Why Use IETF (RFC 5424) Format?
--------------------------------

IETF format is recommended over BSD (RFC 3164) format for the following reasons:

1. **Structured format:** IETF format includes a required APP-NAME field that eliminates parsing ambiguity
2. **Consistent parsing:** The structured format ensures your syslog server parses messages consistently regardless of:
   * Palo Alto firmware version
   * Spacing differences in log messages
   * Future firmware updates that may change message formatting
3. **Better compatibility:** IETF format is the modern syslog standard and provides better support for SIEM systems and log analysis tools
4. **Prevents parsing issues:** BSD format relies on heuristics that can be affected by spacing changes, potentially causing fields like ``version=`` to be parsed incorrectly or missing from output

**Note:** If you're experiencing issues where the ``version=`` field is missing from syslog output after a Palo Alto upgrade, this is typically caused by BSD format parsing ambiguity due to spacing changes. Switching to IETF format resolves this issue.

Configuration Steps
-------------------

Step 1: Access Syslog Server Profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to the Palo Alto Networks firewall web interface
2. Navigate to: **Device > Server Profiles > Syslog**

   Reference: `Palo Alto Documentation - Configure Syslog Monitoring <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring>`_

3. Either:
   * Edit an existing syslog server profile, or
   * Click **Add** to create a new profile

Step 2: Configure Syslog Server Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each syslog server in the profile:

1. **Name:** Enter a unique name for the server (if creating new)
2. **Syslog Server:** Enter the IP address or FQDN of your syslog server
3. **Transport:**
   * **Important:** IETF format typically uses TCP or SSL (TLS)
   * Select **TCP** or **SSL** (not UDP)
   * If using SSL, ensure TLSv1.2 is supported

   Reference: `Palo Alto Documentation - Configure Syslog Server Profile <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring#configure-a-syslog-server-profile>`_

4. **Port:** Enter the port number (default TCP syslog port is 514, but verify with your syslog server configuration)
5. **Format:** Select **IETF** (this is the key setting)

   Reference: `Palo Alto Documentation - Configure Syslog Server Profile <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring#configure-a-syslog-server-profile>`_

6. **Facility:** Select the appropriate syslog facility value (default is LOG_USER)

Step 3: Verify Your Syslog Server Supports RFC 5424
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before applying the changes, ensure:

1. Your syslog server supports RFC 5424 format: Verify that your syslog server version has RFC 5424 parsing enabled

.. only:: winsyslog

   For WinSyslog, ensure RFC 5424 parsing is enabled in the Syslog Server service configuration.

.. only:: mwagent

   For MonitorWare Agent, ensure RFC 5424 parsing is enabled in the Syslog Server service configuration.

.. only:: rsyslog

   For Rsyslog, RFC 5424 support is built-in and enabled by default.

Step 4: Commit Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click **OK** to save the syslog server profile
2. Commit the configuration
3. Review the commit and click **Commit** again to confirm

   Reference: `Palo Alto Documentation - Commit Changes <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring#commit-your-changes-and-review-the-logs-on-the-syslog-server>`_

Step 5: Verify Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After committing:

1. Check syslog messages on your syslog server
2. Verify the format: Messages should now appear in IETF format:

   ``<14>1 2025-10-30T13:13:04.000Z e26secgw02 paloalto - - [meta version="11.2.6"] version=11.2.6|subtype=general|...``

3. Verify APP-NAME field: The ``paloalto`` field (APP-NAME) should be present and consistently parsed by your syslog server
4. Verify output format: Syslog server output should now consistently include the ``version=`` prefix

Expected Results
----------------

After configuring IETF format, you should see:

* **Consistent message format:** Messages appear in structured IETF format with the APP-NAME field (``paloalto``) consistently parsed
* **Reliable field extraction:** All fields, including ``version=``, are reliably extracted regardless of Palo Alto firmware version
* **Future-proof configuration:** The structured format ensures consistent behavior even after firmware upgrades
* **Better log analysis:** The structured format provides better support for SIEM systems and log analysis tools

Benefits Summary
----------------

Using IETF (RFC 5424) format provides:

* **Eliminates parsing ambiguity:** The structured format with required APP-NAME field ensures consistent parsing
* **Prevents version-related issues:** Spacing changes in firmware updates won't affect message parsing
* **Industry standard:** IETF format is the modern syslog standard recommended for enterprise environments
* **Better integration:** Improved compatibility with SIEM systems, log analysis tools, and centralized logging solutions

Technical Reference
-------------------

* RFC 3164 (BSD) - `IETF RFC 3164 <https://www.ietf.org/rfc/rfc3164.txt>`_
* :doc:`RFC 5424 (IETF) <../../glossaryofterms/rfc5424>`
* `Palo Alto Documentation - Configure Syslog Monitoring <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring>`_
* `Palo Alto Documentation - Syslog Field Descriptions <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions>`_
* `Palo Alto Documentation - Use Syslog for Monitoring <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring>`_

Additional Information
----------------------

For more information about syslog server configuration and RFC 5424 support, see the Syslog Server documentation in your product's manual.
