.. Configuration Program documentation master file, created by
   sphinx-quickstart on Fri Jul 26 10:43:58 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

About EventReporter
===================

**EventReporter is an integrated, modular, and distributed solution for system**
management.**

Microsoft Windows 10™, Windows 11™, Windows Server 2016™, Windows Server 2019™,
and Windows Server 2022™ are highly capable operating systems (we will call all of them
"Windows" in the following documentation). However, their standard event
reporting mechanisms are rather limited. Administrators seeking complete
control over their server environment need to regularly check the server event
logs. Adiscon's `EventReporter <https://www.EventReporter.com>`_ provides central notification of any events
logged to the Windows system event log. Messages can be delivered via email and
`syslog <https://www.adiscon.com/syslog/>`_ protocol.

The initial product - called EvntSLog - was specifically written with mixed
Windows and UNIX environments in mind. It supported the syslog protocol only.
It is currently in use by many large-scale commercial organizations,
universities, and government bodies (like the military) all around the world.
EventReporter empowers data center operators to integrate Windows event logs
into their central syslog setup. Administrative duties and exception
notification can easily be built via Unix-based scripting.

But small sized organizations also demanded relief from checking server logs.
As such, EventReporter allows delivery of Windows event notifications via
standard Internet email. Each server's events are gathered, filtered according
to rules set up by the administrator and - if they matter - forwarded to the
admin. Especially small sized organizations operating a single server can be
rest assured that they will not miss any important log entries.

`EventReporter <https://www.EventReporter.com>`_ can be teamed with other
MonitorWare line of products. In this scenario, it provides a totally
centralized and automated event log collection, monitoring, and analysis
solution. If you are looking for a solution that not only can forward event
information but also monitor additional system settings, you might want to have
a look at the `MonitorWare Agent <https://www.mwagent.com>`_.

EventReporter is also a great tool for computer resellers, consultants, and
other service providers in need to monitor their customer's systems.

The product is easy to install and configure, uses only minimal system
resources and is proven to be reliable. Furthermore, it is extremely `inexpensive <https://www.EventReporter.com/products-prices/>`_.


Manual
======

.. toctree::
   :maxdepth: 1

   eventreporterspecific/introduction
   eventreporterspecific/producttour
   eventreporterspecific/index
   eventreporterspecific/stepbystepguides
   eventreporterspecific/eventreporter
   eventreporterspecific/gettinghelp
   eventreporterspecific/purchasingeventreporter
   eventreporterspecific/articles
   eventreporterspecific/faq
   eventreporterspecific/references
   glossaryofterms/index
   copyrights



* :ref:`genindex`
