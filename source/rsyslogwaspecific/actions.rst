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

.. note::

   Send DTLS requires the Professional or Enterprise edition. It is also
   available during the trial period. The Basic edition does not include
   Send DTLS. See :doc:`editioncomparison`.

Internal actions
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-callruleset
   ../mwagentspecific/a-computestatusvariable
   ../mwagentspecific/a-discard
   ../mwagentspecific/a-normalizeevent
   ../mwagentspecific/a-resolvehostname
   ../mwagentspecific/a-messageringbuffer
   ../mwagentspecific/a-setproperty
   ../mwagentspecific/a-setstatus
