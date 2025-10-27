Features
========

Centralized Logging
-------------------

This is the key feature. WinSyslog gathers all Syslog messages send from
different sources and stores them locally on the Windows system. Event source
can be any Syslog enabled device. Today, virtually all devices can use Syslog.
Prominent examples are Cisco routers.

Ease of Use
-----------

Using the new WinSyslog Client interface, the product is very easy to set up and
customize. We also support full documentation and support for large-scale
unattended installations.

Powerful Actions
----------------

Each message received is processed by WinSyslog's powerful and extremely
flexible rule engine. Each rule defines which actions to carry out (e. g. send
an email message or store event log to a database) when the message matches the
rule's filter condition. Among others, filter conditions are string matches
inside the message or Syslog facility or priority. There are an unlimited
number of filter conditions and actions per rule available.

Interactive Server
------------------

Use the Interactive Syslog server to interactively display messages as they
arrive. Message buffer size is configurable and only limited by the amount of
memory installed in the machine.

Send Syslog Test Message
------------------------

WinSyslog client comes with "Send Syslog Test Message" facility. It can be
accessed via the "Tools" menu. This option enables to check if syslog messages
being sent properly to the destination or not.

Please note that the "Send Syslog Test Message" sends :doc:`udp <../glossaryofterms/udp>` syslog, only! It does
not at all send :doc:`rfc 3195 <../glossaryofterms/rfc3195>`, or syslog/tcp!

Freeware Mode
-------------

We care for the home user! WinSyslog can operate as freeware in so-called
"freeware mode" without a valid license. It supports a scrolling interactive
display of the 60 most current messages for an unlimited time. This feature is
most commonly requested for home environments. And: even our free copies come
with Adiscon's great support!

Standards Compatible
--------------------

WinSyslog is compatible with the Syslog :doc:`rfc 3164 <../glossaryofterms/rfc3164>`. It operates as an original
sender (device), server and relay. All specified operation modes are supported.
Non-RFC compliance can be configured by the administrator to fine-tune
WinSyslog to the local environment (e.g. timestamps can be taken from the local
system instead of the reporting device in case the device clocks are
unreliable).

WinSyslog Web Access
--------------------

Never need to look at plain text files! WinSyslog comes with a fully functional
ASP application that will display the contents of WinSyslog generated database
entries. The ASP pages are in full source code and can easily be customized.

Syslog Hierarchy
----------------

WinSyslog supports cascaded configurations most commonly found in larger
organizations. In a cascaded configuration, there are local WinSyslog instances
running at department or site level which report important events to a central
WinSyslog in the headquarter. There is no limit on the number of levels in a
cascaded system.

Email Notifications
-------------------

WinSyslog emails receive events based on the user defined ruleset. Email
notifications can be sent to any standard Internet email address, which allows
forwarding not only to typical email clients but also pager and cellular
phones. The email subject line is fully customizable and can be set to include
the original message. That way, pagers can receive full event information.

Store Messages Persistently
---------------------------

The WinSyslog server process stores all messages persistently. It helps to
audit and review important system events later on without any hard effort.
Messages can be written to flat ASCII files, ODBC data sources, and the Windows
event log.

Multiple Instances
------------------

WinSyslog supports running multiple Syslog servers on the same machine. Each
instance can listen to a different Syslog port, either via :doc:`tcp <../glossaryofterms/tcp>`
or :doc:`udp <../glossaryofterms/udp>`
and can be bound to a different ruleset for execution.

Full Logging
------------

WinSyslog logs the received Syslog message together with its priority and
facility code, as well as the sender's system IP address and date. It is also
able to log abnormally formatted packages (without or with invalid priority /
facility), so no message is lost.

Robustness
----------

WinSyslog is written to perform robust even under unusual circumstances. Its
reliability has been proven at customers sites since 1996.

Minimal Resource Usage
----------------------

WinSyslog has no noticeable impact on system resources. It was specifically
written with minimal resource usage in mind. In typical scenarios, its
footprint is barely traceable. This ensures it can also be installed on heavily
loaded servers.

Firewall Support
----------------

Does your security policy enforce you to use a non-standard Syslog port?
WinSyslog can be configured to listen on any :doc:`tcp <../glossaryofterms/tcp>`/IP port for Syslog messages.

Windows Service
---------------

The WinSyslog service is implemented as a native multithreaded Windows service.
It can be controlled via the control panel services applet or the computer
management MMC.

IPv6
----

Support for IPv6 is available in all network related facilities of the engine.
All network related actions will automatically detect :doc:`ipv6 <../glossaryofterms/ipv6>` and IPv4 target
addresses if configured. You can also use DNS resolution to resolve valid IPv6
addresses. Network related Services can either use IPv4 or IPv6 as internet
protocol. In order to support both protocols, you will need to create two
services. The only exception is the RELP Listener, which uses IPv4 and IPv6
automatically if available.

Multi-Language Client
---------------------

The WinSyslog Client comes with multiple languages ready to go. Out of the box
English, German, and Japanese are supported. Languages can be switched instantly.
Language settings are specific to a user.

Additional languages can be easily integrated using Adiscon's XML based
localization technology. We ask customers interested in an additional language
for a little help with the translation work (roughly 1 hour of work). Adiscon
will than happily create a new version. This service is free!

Friendly and Customizable User Interface
----------------------------------------

New Cloning feature added to the WinSyslog Client. In short you can now clone a
Ruleset, a Rule, an Action, or a Service with one mouse click.

Move up and Move down function has been added for actions in the WinSyslog
Client.

The WinSyslog Client Wizards has been enhanced for creating Actions, Services
and RuleSets. And other minute changes!

Multiple RuleSets - Rules - Actions
-----------------------------------

With WinSyslog as many "RuleSets", "Rules" and "Actions" as necessary can be
defined.

:doc:`multiple rulesets - rules - actions <../winsyslogspecific/multiple-rulesets-rules-actions>`

Handling for low-memory cases
-----------------------------

MWAgent allocates some emergency memory on startup. If the system memory limit
is reached, it releases the emergency memory and locks the queue. That means
not more items can be queued, this prevents a crash of the Agent and the queue
is still being processed. Many other positions in the code have been hardened
against out-of-memory scenarios.

Runs on a large Variety of Windows Systems
------------------------------------------

Windows 2019/2016/2012/10/8/2008 (R2)/7/Vista/2008/2003/2003 (R2)/XP/2000;
Workstation or Server – MonitorWare Agent runs on all of them.

Support for End-of-Life operating systems is only partially
available. Only a minimal service installation may be possible. More details:
:doc:`information for a mass rollout <../shared/gettingstarted/informationforamassrollout>`
