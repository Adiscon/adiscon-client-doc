.. index:: Features

Features
========

Complete Windows Event Monitoring
---------------------------------

Rsyslog Windows Agent automatically monitors Windows Event Logs. All Event Logs
including modern Windows specific extensions are fully processed. Application
log file monitoring provides support for virtually any application that logs to
a text file like Web server log files, Oracle error logs files or Windows
application log files (like the DHCP log files).

External Events
---------------

Events are accepted via a standard Syslog server and hence all of the
Syslog-enabled devices can be included. This includes popular devices like
routers and switches as well as printers and a large number of UNIX / Linux
based systems and applications. Virtually all currently existing network
devices support Syslog – so the Rsyslog Windows Agent can act as a relay host
for them.

To reach an even broader device range, Rsyslog Windows Agent not only supports
standard compatible Syslog but also it supports popular extensions like Syslog
over.

Powerful Event Processing
-------------------------

Rsyslog Windows Agent is powerful and flexible rule engine processes all events
based on a configured set of actions. An unlimited number of rules and actions
allows tailoring to the specific needs.

Zero-Impact Monitoring
----------------------

Rsyslog Windows Agent has no noticeable impact on system resources. It is
specifically written with minimal resource usage in mind. In typical scenarios,
its footprint is barely traceable. This ensures it can also be installed on
heavily loaded servers.

Robustness
----------

Rsyslog Windows Agent is written to perform robust even under unusual
circumstances. The reliability of the product is proven due to its technology
since 1996.

Ease of Use
-----------

Rsyslog Windows Agent is easy to install and configure. Comprehensive
step-by-step guides and wizards help administrators with setting up even
complex systems.

Firewall Support
----------------

Does your security policy enforce you to use non-standard ports? Rsyslog
Windows Agent can be configured to send/listen on any TCP/IP port for Syslog
messages.

Syslog Support
--------------

Windows Event Messages can be forwarded using standard Syslog protocol. Windows
severity classes are mapped to the corresponding Syslog classes. Codes are
fully supported.

Send Syslog Test Message
------------------------

The Rsyslog Agent client comes with "Send Syslog Test Message". This option
enables you to check if Syslog Messages being sent properly to the destination
or not.

IPv6
----

Support for IPv6 is available in all network related facilities of the engine.
All network related actions will automatically detect IPv6 and IPv4 target
addresses if configured. You can also use DNS resolution to resolve valid IPv6
addresses. Network related Services can either use IPv4 or IPv6 as internet
protocol. In order to support both protocols, you will need to create two
services.

Runs on a large Variety of Windows Systems
------------------------------------------

Windows 2019/2016/2012/10/8/2008 (R2)/7/Vista/2008/2003/2003 (R2)/XP/2000;
Workstation or Server – MonitorWare Agent runs on all of them.

Support for End-of-Life operating systems is only partially
available. Only a minimal service installation may be possible. More details:
:doc:`information for a mass rollout <../shared/gettingstarted/informationforamassrollout>`

Multi-Language Client
---------------------

The Rsyslog Windows Agent client comes with multiple languages ready to go. Out
of the box English, Japanese and German are supported. Languages can be switched
instantly. Language settings are user-specific; so multiple users on the same
machine can use different languages.

Friendly and Customizable User Interface
----------------------------------------

New Skinning feature has been added to Rsyslog Windows Agent Client. New
Cloning feature added to Rsyslog Windows Agent Client helps to clone a Ruleset,
a Rule, an Action or a Service with one mouse click. Move up and Move down
function has been added for Actions in the Rsyslog Windows Agent Client.
Wizards have been enhanced for creating Actions, Services and RuleSets. And
other minute changes!

Handling for low-memory cases
-----------------------------

Rsyslog Windows Agent allocates some emergency memory on startup. If the system
memory limit is reached, it releases the emergency memory and locks the queue.
That means not more items can be queued, this prevents a crash of the Agent and
the queue is still being processed. Many other positions in the code have been
hardened against out of memory scenarios.

Multithreaded Queue Engine
--------------------------

The Action processing engine is multi-thread enabled, which means that the
overall processing performance will increase in larger environments and Rsyslog
Windows Agent will benefit from SMP machines.
