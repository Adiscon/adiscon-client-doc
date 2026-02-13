.. _copying-configuration-winsyslog:


How to Copy the WinSyslog Configuration to Other Servers
========================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-02-13
   :updated: 2026-02-13
   :products: WinSyslog

Overview
--------

If you have multiple copies of WinSyslog and want to replicate the current
configuration across several servers, you can export the settings to a
registry file and distribute it. This saves time by avoiding manual
reconfiguration of services and rulesets on each machine.

Exporting the Configuration
----------------------------

1. Open the WinSyslog Configuration Client.
2. Go to the **Computer** menu and click **Export Settings to Registry File**
   (not binary).
3. Save the registry file to a convenient location, for example a shared
   network folder.

Importing the Configuration on Other Servers
---------------------------------------------

On each target server, double-click the exported registry file. This imports
all WinSyslog registry settings automatically. When you open the WinSyslog
Configuration Client on that machine, your configured rules and services
will be present.

See Also
--------

* :doc:`mass-rollout-deployment` - How to perform a mass rollout of WinSyslog
* :doc:`export-settings-support-call` - How to export WinSyslog settings for a
  support call
