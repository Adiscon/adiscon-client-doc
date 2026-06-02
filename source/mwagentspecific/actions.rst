Actions
=======

Use this section to configure what MonitorWare Agent does after a rule matches.
Actions can forward events, store them, enrich them, or trigger follow-up
processing.

There can be multiple actions in one rule. They run in the order configured,
and you can change that order by moving actions up or down.

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
   a-forwardsyslogoptions
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
