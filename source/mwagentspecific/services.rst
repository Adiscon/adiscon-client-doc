Services
========

Use this section to configure how MonitorWare Agent collects data. Services are
the product inputs. They gather events or measurements and pass them to the
ruleset assigned to that service.

For example, the Syslog Server service accepts incoming syslog messages and
Event Log Monitor extracts Windows Event Log data. Multiple service instances
can run at the same time when their settings do not conflict.

You must define at least one enabled service, otherwise the product does not
collect any data and cannot do useful work.

Do not confuse configured services with **service defaults** in the tree view.
Service defaults are templates. They provide default properties for new
services but do not run and do not collect data by themselves.

Test mode is available for selected services, including Event Log Monitor and
File Monitor. Use it only for testing, because it can replay the same events
or files repeatedly.

Basic Services
--------------

.. toctree::
   :maxdepth: 1

   heartbeat
   monitorwareechoreply
   monitorwareechorequest

network services
----------------

.. toctree::
   :maxdepth: 1

   passivesysloglistener
   relplistener
   setpserver
   smtplistener
   snmpmonitor
   snmptrapreceiver
   syslogserver

probe services
--------------

.. toctree::
   :maxdepth: 1

   ftpprobe
   httpprobe
   imapprobe
   nntpprobe
   pingprobe
   pop3probe
   portprobe
   smtpprobe

file system monitoring
----------------------

.. toctree::
   :maxdepth: 1

   cpumonitor
   diskspacemonitor
   eventlogmonitorv1
   eventlogmonitorv2
   filemonitor
   ntservicemonitor

other services
--------------

.. toctree::
   :maxdepth: 1

   databasemonitor
   serialportmonitor
