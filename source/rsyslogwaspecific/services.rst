Services
========

Services are the input side of rsyslog Windows Agent. They collect or receive
events and send them into the assigned ruleset.

You must define at least one service. Without a service, the product does not
collect or receive any event data.

Defaults vs. active services
----------------------------

Service defaults are templates. They provide starting values for new services,
but they do not collect data by themselves. Actual processing only happens in
the active service instances you create under **Running Services**.

Basic services
--------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/heartbeat
   ../mwagentspecific/monitorwareechoreply

Network services
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/syslogserver

Windows and file monitoring
---------------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/eventlogmonitorv1
   ../mwagentspecific/eventlogmonitorv2
   ../mwagentspecific/filemonitor
