Actions
=======

Actions tell EventReporter what to do with an event after a rule matches.
They store, forward, transform, or trigger follow-up behavior.

Important behavior
------------------

- A rule can contain multiple actions.
- Actions run in the order they are configured.
- Start with one simple output action during initial setup so the event path is
  easy to verify.

Storing actions
---------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-databaseoptions
   ../mwagentspecific/a-oledbdatabaseaction
   ../mwagentspecific/a-fileoptions

Forwarding actions
------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-eventlogoptions
   ../mwagentspecific/a-mailoptions
   ../mwagentspecific/a-netsend
   ../mwagentspecific/a-forwardsetpoptions
   ../mwagentspecific/a-forwardsyslogoptions
   ../mwagentspecific/a-senddtls

Internal actions
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-callruleset
   ../mwagentspecific/a-computestatusvariable
   ../mwagentspecific/a-discard
   ../mwagentspecific/a-resolvehostname
   ../mwagentspecific/a-setproperty
   ../mwagentspecific/a-setstatus

Other actions
-------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-playsound
   ../mwagentspecific/a-startprogram
