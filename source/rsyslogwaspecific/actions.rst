Actions
=======

Actions define what rsyslog Windows Agent does with an event after it matches a
rule.

There can be multiple actions for each rule. Actions are processed in the order
you configure them.

Forwarding actions
------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-sendrelp
   a-forwardsyslogoptions
   ../mwagentspecific/a-senddtls

Internal actions
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-callruleset
   ../mwagentspecific/a-computestatusvariable
   ../mwagentspecific/a-discard
   ../mwagentspecific/a-normalizeevent
   ../mwagentspecific/a-setproperty
   ../mwagentspecific/a-setstatus
