
About WinSyslog
===============

**WinSyslog is an enhanced syslog server for Windows. It serves the same purpose as a Unix Syslog daemon. It is an integrated, modular, and distributed solution
for system management.**

Network administrators can continuously monitor their systems and receive
alarms as soon as important events occur.

`Syslog <https://www.adiscon.com/syslog>`_  is a standard protocol for centralized reporting of system events. Its
roots are in the UNIX environment, but most modern devices (e. g. Cisco
routers) use the Syslog protocol. They report important events, operating
parameters, and even debug messages via Syslog. Unfortunately Microsoft Windows
does not include a Syslog server (a Syslog server is called "Syslog daemon" or
- short - Syslogd under UNIX).

Adiscon's `WinSyslog <https://www.WinSyslog.com>`_ fills this gap. Prior to version 3.0, WinSyslog was known
under the name of "NTSLog". WinSyslog is the first and original Syslog server
available on the Windows platform. Its initial version was created in 1996 just
to receive Cisco routers status messages. The product has been continuously
developed during the past years. Version 3 represented a major stepping stone.
That was the main reason we decided to rename the product.

WinSyslog can also be used in conjunction with Adiscon's `MonitorWare Agent <https://www.mwagent.com>`_,
and `EventReporter <https://www.EventReporter.com>`_ to build a totally centralized Windows
event log monitoring tool. More information on centrally monitoring Windows
operating systems can be found at www.monitorware.com

Most customers use WinSyslog to gather events reported from Syslog enabled
devices (routers, switches, firewalls, and printers to name a few) and store
them persistently on their Windows system. WinSyslog can display Syslog
messages interactively on-screen but also store them in flat ASCII files, ODBC
databases, or the Windows event log. The product runs as a reliable background
service and needs no operator intervention once it is configured and running.
As a service, it can start up automatically during Windows boot.

The improvised services and rules introduced in version 4 allow very flexible
configuration of WinSyslog. WinSyslog detects conditions like string matches in
the incoming messages and can actively act on them. For example, an email
message can be sent if a high priority message is detected. There can also be
multiple Syslog servers running at the same time, each one listening to
different ports.

For a complete overview over the MonitorWare line of products, please visit
`https://www.adiscon.com <https://www.adiscon.com/products>`_.


Manual
======

.. toctree::
   :maxdepth: 1


   winsyslogspecific/introduction
   winsyslogspecific/producttour
   winsyslogspecific/index
   winsyslogspecific/stepbystepguides
   ../interactivesyslogviewer/index
   winsyslogspecific/winsyslog-j
   winsyslogspecific/gettinghelp
   winsyslogspecific/winsyslogconcepts
   winsyslogspecific/purchasingwinsyslog
   winsyslogspecific/articles
   winsyslogspecific/faq

   winsyslogspecific/references
   winsyslogspecific/glossaryofterms
   copyrights



* :ref:`genindex`
