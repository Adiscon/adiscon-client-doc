Actions
=======

Actions tell the application that what to do with a given event. With actions,
you can forward events to a mail recipient or Syslog server, store it in a
file or database, or do many other things with it.


There can be multiple actions for each rule.
Actions are processed in the order they are configured.
However you can change the order of the actions by moving them Up or Down.

Storing Actions
---------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-databaseoptions
   ../mwagentspecific/a-oledbdatabaseaction
   ../mwagentspecific/a-fileoptions

forwarding actions
------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-eventlogoptions
   ../mwagentspecific/a-mailoptions
   ../mwagentspecific/a-netsend
   ../mwagentspecific/a-forwardsetpoptions
   ../shared/actions/a-forwardsyslogoptions
   ../mwagentspecific/a-senddtls

internal actions
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-callruleset
   ../mwagentspecific/a-computestatusvariable
   ../mwagentspecific/a-discard
   ../mwagentspecific/a-resolvehostname
   ../mwagentspecific/a-setproperty
   ../mwagentspecific/a-setstatus

other actions
-------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-playsound
   ../mwagentspecific/a-startprogram
