:orphan:

.. _glossary-mwconcepts-filterconditions:
.. supporting-labels-marker

Filter Conditions
=================

Filter conditions are used inside the rule engine. They help to decide when a
rule is to be carried out. Filter conditions are considered to match of the
outcome if the configured comparison operation is "TRUE". Available filter
conditions are listed down below:

* Global Conditions
* General Conditions
* Date / Time
* InformationUnit Type
* Syslog
* Event Log Monitor
* NT Service Monitor
* Disk Space Monitor
* SNMP Traps
* SerialPort Monitor
* Custom Property

Global Conditions
-----------------

Global Conditions apply to the rule as whole. They are automatically combined
with a logical "AND" with the conditions in the filter tree. These are:

* Treat not found Filters as TRUE*

If a property queried in a filter condition is not present in the event, the
respective condition normally returns "FALSE". However, there might be
situations where you would prefer if the rule engine would evaluate this to
"TRUE" instead. With this option, you can select the intended behavior. If you
check it, conditions with properties not found in the event evaluates to "TRUE.

* Fire only if Event occurs* - This is kind of the opposite of the "Minimum Wait

Time". Here, multiple events must come in before a rule fires. For example Ping
is not a very reliable protocol, so a single ping might be lost. Thus, it may
not be the best idea to restart some processes just because a single ping
failed. It would be much better to wait for repetitive pings to fail before
doing so.

Exactly this the "Fire only if Event occurs" filter condition is made for. It
waits until a configured amount of the same events occurs within a period. Only
if the count is reached, the filter condition matches and the rule can fire.

* Minimum Wait Time* - This filter condition can be used to prevent rules from

firing to often. For example, a rule might be created to check the status of a
port probe event. The port probe probes an :doc:`smtp <../glossaryofterms/smtp>` server. If the event is fired
and the rule detects it, it will spawn a process that tries to restart the
service. This process will take some time. Maybe the SMTP gateway need some
more time to fully start up so that the port probe might fail again while the
problem is already taken care of. The port probe as such will generate an
additional event. Setting a minimum wait time will prevent this second port
probe event to fire again if it is – let us say – within 5 minutes from the
original one. In this case, the minimum wait time is not yet reached and as
such, the rule will not match. If, however, the same event is generated 5 hours
later (with the mail gateway failing again), the rule will once again fire and
corrective action taken.

Date Conditions
---------------

Rule processing can be bound to a specific or the installation date. By default
a Rule will always be processed.

General Filter Conditions
-------------------------

This set includes filters which are related to Non-Event Log specific settings.
These are:

* Source System* - This is the system a message is originated from. It can be

used to check for authorized systems to pass messages to the MonitorWare Agent.

* Message Content* - The message content filter condition is very powerful. It

evaluates to true if the specified content is found anywhere in the message.
As there is implicit wildcarding, there is no need to specify extra wildcards.

* CustomerID* - CustomerID is provided for customer ease. For example if someone

monitors his customer's server, he can store different CustomerIDs in each agent.
This is user configurable.

* SystemID* - SystemID is of type integer and is to be used by our customer. In

addition, it is user configurable.

* Status Name and Value* - These filter type corresponds to :doc:`set status action <../mwagentspecific/a-setstatus>`.

Date / Time
-----------

This filter condition is used to check the time frame and / or day of week in
which an event occurred.

* Time* - This filter condition is used to check the period in which an event

occurred. For example, a syslog message from a Cisco router saying that it
dialed up is normal if it occurs during office hours. If it occurs at night,
so, it is an alerting signal and an administrator might receive notification of
this event (while he might otherwise decide to discard it). This can be done
with the time setting.

* Weekdays* - This is closely equivalent to the time filter condition, except that

it is applied on a per-day basis. So it can be used to detect for example
events occurring on weekends and act differently on them.

Information Unit Type
---------------------

This is based on the type of service that generated the information unit. So
with this setting rules can be created that act only on e.g. syslog messages or
NT event reports.

Syslog
------

Syslog related filters are grouped here:

* Syslog Facility* - For syslog information units, this is the actual syslog

facility. If that filter condition is used on non-syslog originated information
units, it will be a value mapped on a best effort basis to a syslog facility.


* Syslog Priority* - For syslog information units, this is the actual syslog

priority. If that filter condition is used on non-syslog originated information
units, it will be a value mapped on a best effort basis to a syslog priority.


* Syslog Tag* - The syslog tag value, is a short string. This is provided for

non-syslog messages based on configuration. In most cases, this is used for
filtering.

Event Log Monitor
-----------------

Event Log Monitor related filters are grouped here:

* Event ID* - For Event Log Monitor information units, this is the actual NT event

log ID. For others, this value is undefined. We recommend using it with Event
Log Monitor information units only.

* Event Type* - For Event Log Monitor information units, this is the actual NT

event log. If enabled, the event must have the configured event type or the
rule will not match. This filter condition should only be used with event log
information units only.

* Event Source* - For Event Log Monitor information units, this is the actual NT

event log source. For others, this value is undefined. We recommend using it
with Event Log Monitor information units only.

* Event Severity* - For Event Log Monitor information units, this is the actual NT

event log severity. For others, the value is mapped on a best effort basis or
not available. We recommend using it with Event Log Monitor information units
only.

* Event Category* - For Event Log Monitor information units, this is the actual NT

event log category. If enabled, the event must have the configured event
category or the rule will not match. This filter condition should only be used
with event log information units.

* Event Categoryname* - This value contains the Category value as string if it can

be resolved. Otherwise it will contain the category number.

* Event User* - For Event Log Monitor information units, this is the actual NT

event log user. If enabled, the event must have the configured event user or
the rule will not match. This filter condition should only be used with event
log information units.

NT Service Monitor
------------------

The NT Service Name is used to check if vital operating services are running
continuously. By default these services set to "automatic" startup. If the
value returned is not true then corrective measures can be taken e.g. alerts can
be generated.

DiskSpace Monitor
-----------------

A flexible dialog allows to generate filters on disk free space – both with
an absolute or relative value. Multiple comparisons can be done.

SNMP Traps
----------

Using SNMP Traps MonitorWare Agent can be used to manage and monitor all sorts
of equipment including computers, routers, wiring hubs etc. A trap is generated
when the device feels it should do so and it contains the information that the
device feels should be transmitted. Related filters are grouped here:

* Community* - It corresponds to the respective SNMP entity.

* Enterprise* - It corresponds to the respective SNMP entity.

* Generic name* - It corresponds to the respective SNMP entity.

* Version* - It corresponds to the respective SNMP entity.

* Uptime* - It corresponds to the respective SNMP entity.

Serial Port Monitor
-------------------

The serial port monitor allows you to monitor devices attached to local
communications ports.

Custom Property
---------------

As the name suggests it is a "Custom Property". Internally in MonitorWare Agent
all values are stored in properties. For example the main message is stored in
a property called "msg". By using this dialog you can access properties which
are dynamic (Like those from SNMP Trap Monitor when using v2 protocol).
