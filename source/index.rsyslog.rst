
About Rsyslog Windows Agent
===========================

**The Rsyslog Windows Agent is designed to work closely with Rsyslog for Linux.**
It is designed to provide a tight integration of both environments. Log
consolidation at its best.  In addition, it can be easily integrated into an
environment, where Adiscon's MonitorWare Line of products is already present.**

**The Rsyslog Windows Agent relies on Adiscon's knowledge in reliable logging**
environments for both Linux and Windows. It provides the possibility to
consolidate logs from a Windows machine on a central Linux repository through
Rsyslog.**

Rsyslog Windows Agent runs on the systems to be monitored and provides the core
functionality. It can gather the data from various sources, like the Windows
event log, routers, switches, firewalls, and many more. It supports very
flexible and powerful local filtering and processing of these gathered events
based on a powerful rule processor, events can be forwarded, acted on, or
discarded - all at the discretion of the system administrator. Even a
stand-alone Rsyslog Windows Agent can play a vital role in network management
by performing a role like generating alert emails at the occurrences of
specific events.

Larger environments consolidate Rsyslog Windows Agent data in a central
repository like the MonitorWare event database or combined log files. Database
is the source of information for all reporting and analysis modules of the
MonitorWare system. By default, database can be created with MySQL, Microsoft
Access, or Microsoft SQL Server (also available as cost-free MSDE). As standard
SQL and ODBC are being used, it is easily adaptable to other database systems.
For example, we know that many customers use it successfully with Oracle
databases.

A number of different modules work on this consolidated database or the log
files to carry out various activities. These modules include scheduled
reporting facilities like for analysis, a web interface, or reporting via
`Adiscon LogAnalyzer <https://loganalyzer.adiscon.com>`_.

Rsyslog Windows Agent can also integrate with other network monitoring and
management related Adiscon products like `EventReporter <https://www.EventReporter.com>`_, `WinSyslog <https://www.WinSyslog.com>`_ and
`MonitorWare Agent <https://www.mwagent.com>`_. In fact, it uses common terms and methods wherever possible,
so upgrading from these solutions to the full MonitorWare system is easy.

For a complete overview over the MonitorWare line of products, please visit
`https://www.adiscon.com <https://www.adiscon.com/products>`_.


Manual
======

.. toctree::
   :maxdepth: 1

   rsyslogwaspecific/introduction
   rsyslogwaspecific/index
   rsyslogwaspecific/commonuses
   rsyslogwaspecific/rsyslogwa
   rsyslogwaspecific/gettinghelp
   rsyslogwaspecific/purchasingrsyslogwa
   rsyslogwaspecific/articles
   rsyslogwaspecific/faq
   rsyslogwaspecific/references
   rsyslogwaspecific/glossaryofterms
   copyrights



* :ref:`genindex`
