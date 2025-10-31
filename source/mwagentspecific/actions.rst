Actions
=======

Actions tell the application that what to do with a given event. With actions,
you can forward events to a mail recipient or Syslog server, store it in a
file or database, or do many other things with it.

There can be multiple actions for each rule. Actions are processed in the order
they are configured.

However you can change the order of the actions by moving them Up or Down.

Storing Actions
---------------

.. toctree::
   :maxdepth: 1

   a-databaseoptions
   a-oledbdatabaseaction
   a-fileoptions
   a-syslogqueueaction

forwarding actions
------------------

.. toctree::
   :maxdepth: 1

   a-eventlogoptions
   a-mailoptions
   a-netsend
   a-sendtocommunicationsport
   a-sendmsqueue
   a-sendrelp
   a-forwardsetpoptions
   a-sendsnmptrap
   ../shared/actions/a-forwardsyslogoptions
   a-senddtls

internal actions
----------------

.. toctree::
   :maxdepth: 1

   a-callruleset
   a-computestatusvariable
   a-discard
   a-normalizeevent
   a-postprocessevent
   a-resolvehostname
   a-setproperty
   a-setstatus

other actions
-------------

.. toctree::
   :maxdepth: 1

   a-controlntservice
   a-httprequest


   a-playsound
   a-startprogram
