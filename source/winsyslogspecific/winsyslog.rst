.. _winsyslog-configuration-overview:

Configuring
===========

This section explains how to configure WinSyslog after installation. Use it to
define input services, build rulesets and filter logic, configure actions, and
verify that the WinSyslog service is receiving and processing messages as
expected.

In this manual, **input** is the clearest plain-language concept for anything
that receives logs, while **service** remains the main operational term for the
configured WinSyslog object. Some GUI pages still use exact labels such as
``Syslog server`` or ``RELP Listener``. Those are specific current client
labels, not separate concepts. For the terminology mapping, see
:doc:`FAQ: What do "service", "listener", and "server" mean in WinSyslog? <faq/services-listeners-and-servers>`.

Recommended setup path
----------------------

1. Define input services under :doc:`Services <services>` and attach each
   service to a ruleset.
2. Build processing under :doc:`Filter conditions <filterconditions>` (rules,
   filters, order).
3. Add actions under :doc:`Actions <actions>` to store and/or forward the data.
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
