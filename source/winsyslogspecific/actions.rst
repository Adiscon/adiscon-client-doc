Actions
=======

Actions define what WinSyslog does after a rule matches an event. They are the
output and follow-up stage of processing.

A single rule can contain multiple actions. Actions run in listed order, so the
sequence can matter when one action changes data or affects later behavior.

Use the sections below to choose the right action type for storage,
forwarding, notification, or internal processing.

Storage actions
---------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-databaseoptions
   ../mwagentspecific/a-oledbdatabaseaction
   ../mwagentspecific/a-fileoptions

Forwarding and notification actions
-----------------------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-eventlogoptions
   ../mwagentspecific/a-mailoptions
   ../mwagentspecific/a-netsend
   ../mwagentspecific/a-sendtocommunicationsport
   ../mwagentspecific/a-sendmsqueue
   ../mwagentspecific/a-sendrelp
   ../mwagentspecific/a-forwardsetpoptions
   ../mwagentspecific/a-sendsnmptrap
   a-forwardsyslogoptions
   ../mwagentspecific/a-senddtls

Internal processing actions
---------------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-callruleset
   ../mwagentspecific/a-computestatusvariable
   ../mwagentspecific/a-discard
   ../mwagentspecific/a-normalizeevent
   ../mwagentspecific/a-postprocessevent
   ../mwagentspecific/a-resolvehostname
   ../mwagentspecific/a-setproperty
   ../mwagentspecific/a-setstatus

Other actions
-------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/a-playsound
   ../mwagentspecific/a-startprogram
