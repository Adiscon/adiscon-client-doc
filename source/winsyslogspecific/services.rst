Services
========

Services gather events data. For example, the Syslog server service accepts
incoming Syslog messages and the Event Log Monitor extracts Windows Event Log
data. There can be unlimited multiple services. Depending on the service type,
there can also be multiple instances running, each one with different settings.

You must define at least one service, otherwise the product does not gather
event data and hence does not perform any useful work at all. Sometimes,
services are mistaken with service defaults those are pre-existing in the tree
view. Service defaults are just the templates that carry the default properties
assigned to a service, when one of the respective type is to be created.
Service defaults are NOT executed and thus cannot gather any data.

Added a test mode for Services, currently EventLog Monitor V1 & V2 and File
Monitor are supported. When enabling the testmode for a certain service, it
will process it's Events/Files over and over again. So only use this setting
for testing purposes.

Basic Services
--------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/heartbeat
   ../mwagentspecific/monitorwareechoreply

network services
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/relplistener
   ../mwagentspecific/setpserver
   ../mwagentspecific/snmptrapreceiver
   ../mwagentspecific/syslogserver
