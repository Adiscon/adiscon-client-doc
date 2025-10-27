.. index:: Standard Properties

Standard Properties
===================

As outlined under Event Properties, these are properties present in all types
of events. Some event types have only these standard properties. Others have
additional properties. Those with additional properties are documented in the
other sections. If there is no specific documentation for a specific event
type, this means that it supports the standard properties, only.


**msgPropertyDescribed**

A human-readable representation of the message text. While this is generally
available, the exact contents largely depends on the source of the information.
For example, for a file monitor it contains the file line and for a syslog
message it contains the parsed part of the syslog message.

**source**

The source system the message originated from. This can be in various
representations (e.g. IP address or DNS name) depending on configuration
settings.

**localhostname**

On service startup it is automatically set to the local system computer name. It is read only and can be used if source property is not usable. E.g. if the Source property cannot be translated to IP format because the event log entry was recorded with an old computer name that no longer exists.

**resource**

A user-assigned numerical value. Does not have any specific meaning. Primarily
intended for quick filtering.

**CustomerID**

A user-assigned numerical value. Does not have any specific meaning. Primarily
intended for quick filtering.

**SystemID**

A user-assigned numerical value. Does not have any specific meaning. Primarily
intended for quick filtering.

**timereported**

The time the originator tells us when this message was reported. For example,
for syslog this is the timestamp from the syslog message (if not configured
otherwise). Please note that timereported eventually is incorrect or
inconsistent with local system time - as it depends on external devices, which
may not be properly synchronized.

For Windows Event Log events, timereported contains the timestamp from the
event log record.

**timegenerated**

The time the event was recorded by the service. If messages are forwarded via
SETP, this timestamp remains intact.

**importance**

Reserved for future use.

**iut**

Indicates the type of the event. Possible values are:

.. code-block:: text

  1- syslog message
  2- heartbeat
  3- Windows Event Log Entry
  4- SNMP trap message
  5- file monitor
  8- ping probe
  9- port probe
  10- Windows service monitor
  11- disk space monitor
  12- database monitor
  13- serial device monitor

**iuvers**

Version of the event record (info unit). This is a monitorware internal version
identifier.
