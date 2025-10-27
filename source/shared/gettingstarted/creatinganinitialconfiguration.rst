Creating an Initial Configuration
=================================

MonitorWare Agent actually contains the features of five products in it. In
order to get MonitorWare Agent running be sure to go through the :doc:`tutorial <monitorwareagenttutorial>`
section, once you have read this section.

MonitorWare Agent can work as:


**Data gatherer**

Here, it gathers event data from important sources like Windows event logs, text
files, ping and port probes, and the like.


**Real Time Alerter**

Alert conditions can be detected in real time and alerts can be issued. Alerts
can be sent via email and various other means. Alerts based on data collected by
the data gatherers can be configured with respect to different parameters.


**Automatic Admin Actions**

Depending on certain events, administrative actions can be automatically
initiated, for example the deletion of temporary files in a low-disk space
condition.


**Relay Server**

MonitorWare Agent can be used to build, highly scalable, complex systems with
relay servers between locations or networks. As a relay server, it forwards
incoming events to another instance of MonitorWare Agent or a Syslog daemon.


**Event Repository**

All gathered event data can be stored in a repository. The repository is a
database providing the base for all other MonitorWare products. Events can also
be stored in text files. With a specific configuration, a secure log repository
can be created for auditing purposes.

MonitorWare Agent can perform any mix of the five functions on a given machine.
There are no limits inside the product. Right after installation, however, it is
not configured for any of the above functions. So in order to have it do some
useful work, it needs to be configured.
