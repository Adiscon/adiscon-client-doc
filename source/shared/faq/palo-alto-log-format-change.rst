.. include:: ../supporting-labels.rst

.. _palo-alto-log-format-change:

Why does the log output format change after a Palo Alto firewall upgrade?
=========================================================================

This article explains why Palo Alto firewall log format changes after upgrades can cause parsing issues and how to resolve them by switching to IETF (RFC 5424) format.

Question
--------

After upgrading a Palo Alto firewall, the syslog output format from the syslog server has changed. Specifically, the ``version=`` field that was previously included in the output is now missing. Why does this happen and how can it be fixed?

Answer
------

This issue occurs because Palo Alto firewalls use BSD (RFC 3164) syslog format, which has an optional TAG field. After upgrades, Palo Alto may change spacing in syslog messages, which causes parsing ambiguity in RFC 3164 format. The recommended solution is to configure Palo Alto to use IETF (:doc:`RFC 5424 <../../glossaryofterms/rfc5424>`) format instead, which eliminates parsing ambiguity.

Root Cause
----------

The issue occurs because:

1. **Missing TAG field:** Palo Alto syslog messages use BSD (RFC 3164) format without the optional TAG field
2. **Spacing changes:** After upgrades, Palo Alto may change spacing (e.g., from 2 spaces to 1 space) before fields like ``version=``
3. **Parser ambiguity:** Without a TAG field, RFC 3164 parsers must use heuristics to determine where the message content begins. The spacing difference triggers different parsing behavior:
   - **Old format (2 spaces):** The parser extracts ``version`` as the syslogtag → Output: ``version=10.2.7-h12|...``
   - **New format (1 space):** The parser does not extract ``version`` as syslogtag → Output: ``11.2.6|...`` (missing ``version=``)

Solution: Switch to IETF (RFC 5424) Format
-------------------------------------------

The recommended solution is to configure Palo Alto to use IETF (RFC 5424) syslog format instead of BSD format. The IETF format includes a required APP-NAME field that eliminates parsing ambiguity, ensuring consistent behavior regardless of spacing.

Why IETF Format Solves the Problem
-----------------------------------

* APP-NAME is required (unlike BSD's optional TAG field)
* Structured format eliminates parsing ambiguity
* Consistent parsing regardless of spacing differences
* Better for SIEM systems and log analysis tools

Configuration Steps for Palo Alto
----------------------------------

Step 1: Access Syslog Server Profile Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to the Palo Alto Networks firewall web interface
2. Navigate to: **Device > Server Profiles > Syslog**

   Reference: `Palo Alto Documentation - Configure Syslog Monitoring <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring>`_

3. Either:
   * Edit an existing syslog server profile, or
   * Click **Add** to create a new profile

Step 2: Configure Server Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Step 3: Verify Syslog Server Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before applying the changes, ensure:

1. Your syslog server supports RFC 5424 format: Verify that your syslog server version has RFC 5424 parsing enabled

.. only:: winsyslog

   For WinSyslog, ensure RFC 5424 parsing is enabled in the Syslog Server service configuration.

.. only:: mwagent

   For MonitorWare Agent, ensure RFC 5424 parsing is enabled in the Syslog Server service configuration.

.. only:: rsyslog

   For Rsyslog, RFC 5424 support is built-in and enabled by default.

Step 4: Apply Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Click **OK** to save the syslog server profile
2. Commit the configuration
3. Review the commit and click **Commit** again to confirm

   Reference: `Palo Alto Documentation - Commit Changes <https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring#commit-your-changes-and-review-the-logs-on-the-syslog-server>`_

Step 5: Verify the Change
~~~~~~~~~~~~~~~~~~~~~~~~~~

After committing:

1. Check syslog messages on your syslog server
2. Verify the format: Messages should now appear in IETF format:

   ``<14>1 2025-10-30T13:13:04.000Z e26secgw02 paloalto - - [meta version="11.2.6"] version=11.2.6|subtype=general|...``

3. Verify APP-NAME field: The ``paloalto`` field (APP-NAME) should be present and consistently parsed by your syslog server
4. Verify output format: Syslog server output should now consistently include the ``version=`` prefix

Expected Result
---------------

After switching to IETF format:

* **Consistent parsing:** The syslog server will consistently extract the APP-NAME field (``paloalto``)
* **No spacing issues:** The structured format eliminates ambiguity caused by spacing differences
* **Reliable output:** Output format will be consistent regardless of Palo Alto version or spacing

IETF format is the recommended long-term solution as it eliminates parsing ambiguity and provides better structure for log analysis.

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
