Actions
=======

Actions tell the application that what to do with a given event. With actions,
you can forward events to a mail recipient or Syslog server, store it in a
file or database or do many other things with it.

There can be multiple actions for each rule. Actions are processed in the order
they are configured. However you can change the order of the actions by moving
them Up or Down.



Forwarding Actions
------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-sendrelp
   a-forwardsyslogoptions
   ../mwagentspecific/a-senddtls

internal actions
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-callruleset
   ../mwagentspecific/a-computestatusvariable
   ../mwagentspecific/a-discard
   ../mwagentspecific/a-normalizeevent
   ../mwagentspecific/a-setproperty
   ../mwagentspecific/a-setstatus
