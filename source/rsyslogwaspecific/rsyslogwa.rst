.. _rsyslogwa-configuration-overview:

Configuration
=============

Use this section to configure how rsyslog Windows Agent collects Windows
events, processes them through rules, and forwards the results.

If you are new to the product, start with ``Getting Started`` for the first
working setup and return here for the detailed configuration pages.

In this manual, **input** is the clearest plain-language concept for anything
that collects or receives events, while **service** remains the operational
term for the configured rsyslog Windows Agent object.

Recommended setup path
----------------------

1. Define input services under :doc:`Services <services>` and bind each service to a
   ruleset.
2. Build processing under :doc:`Filter Conditions <filterconditions>`.
3. Add forwarding or internal processing under :doc:`Actions <actions>`.
4. Verify end-to-end delivery with a simple forwarding action before refining
   the filters.

.. toctree::
   :maxdepth: 2

   core-concepts
   configuringrsyslogwa
   multiple-rulesets-rules-actions
   ../mwagentspecific/clientoptions
   ../mwagentspecific/clienttools
   ../mwagentspecific/usingfilebasedconfiguration
   ../mwagentspecific/generaloptions
   services
   filterconditions
   actions
