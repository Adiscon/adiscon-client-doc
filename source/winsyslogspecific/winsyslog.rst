.. _winsyslog-configuration-overview:

Configuring
===========

This section explains how to configure WinSyslog after installation. Use it to
define inputs, build rulesets and filter logic, configure actions, and verify
that the WinSyslog service is receiving and processing messages as expected.

Recommended setup path
----------------------

1. Define inputs under :doc:`Services <services>` and bind each service to a ruleset.
2. Build processing under :doc:`Filter conditions <filterconditions>` (rules, filters, order).
3. Add outputs under :doc:`Actions <actions>` (store and/or forward).
4. Verify reception with :ref:`Send Syslog Test Message <winsyslog-send-test-message>` and a temporary "write to file" action.

.. toctree::
   :maxdepth: 2

   winsyslogconcepts
   configuringwinsyslog
   multiple-rulesets-rules-actions
   ../mwagentspecific/clientoptions
   ../mwagentspecific/clienttools
   ../mwagentspecific/usingfilebasedconfiguration
   generaloptions
   services
   filterconditions
   actions
