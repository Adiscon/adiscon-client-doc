.. _rsyslogwa-enter-license-information:

How Do I Enter rsyslog Windows Agent License Information?
=========================================================

Answer
------

Open the rsyslog Windows Agent Configuration Client, go to **General** ->
**License**, enter the registration name exactly as provided, import the
license key, save the configuration, and restart the service.

Details
-------

After you purchase rsyslog Windows Agent, Adiscon sends the license
information by email. That message contains:

- the registration name
- the license key

The registration name is case-sensitive and must match the delivered value
exactly.

For Event Log Monitor deployments, licensing is based on the source systems
whose Windows Event Logs are collected or forwarded. A license is required for
each monitored system, regardless of whether that source system is a physical
server, a workstation, or a virtual machine.

Action path
-----------

1. Open the rsyslog Windows Agent Configuration Client.
2. In the left pane, expand **General** and select **License**.
3. Copy the registration name from the delivery email into
   **Registration Name**.
4. Copy the full license key and click **Import from Clipboard**.
5. Save the configuration.
6. Restart the rsyslog Windows Agent service so the updated license state is
   applied.

Related information
-------------------

* :doc:`../installation`
* :doc:`../editioncomparison`
* :doc:`../../shared/sales/how-to-contact-sales`
