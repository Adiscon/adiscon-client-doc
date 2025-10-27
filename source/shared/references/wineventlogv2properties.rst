.. index:: Windows Event Log V2 Properties

Windows Event Log V2 Properties
===============================

**id**

Windows Event ID

**severity**

severity as indicated in the event log. This is represented in string form.
Possible values are:

.. code-block:: text

  [INF] - informational
  [AUS] - Audit Success
  [AUF] - Audit failure
  [WRN] - Warning
  [ERR] - Error
  [NON] - Success (called "NON" for historical reasons)

**severityid**

The severity encoded as a numerical entity (like in Windows API)

**sourceproc**

The process that wrote the event record (called "source" in Windows event
viewer).

**category**

The category ID from the Windows Event Log record. This is a numerical value.
The actual value is depending on the event source.

**catname**

The category name from the Windows Event Log record. This is a string value.
The actual value is depending on the event source. This value is a textual
representation from the Category ID. This property could contain line feeds,
which can be removed by activating the option "Remove Control Characters from
String Parameters" in the advanced options of the EventLog Monitor Service.

**user**

The user name that was recorded in the Windows Event Log. This is "N\A" if no
user was recorded.

**nteventlogtype**

The name of the Windows Event Log this event is from (for example "System" or
"Security").

**channel**

The channel property for event log entries, for classic Event logs they match
the ``%nteventlogtype%`` property, for new event logs, they match the "Event Channel".

**sourceraw**

This contains the full internal name of the event source for new event logs,
for classic event logs it contains the same value as in %sourceproc%.

**level**

Textual representation of the event log level (which is stored as a number in ``%severityid%``). This property is automatically localized by the system.

**categoryid**

Internal category id as number.

**keyword**

Textual representation of the event keyword. This property is automatically
localized by the system.

**user_sid**

If available, contains the raw SID of the username (``%user%``) property.

**recordnum**

Contains the internal event record number. Please note that if the event log
has been truncated before, it may not start with 0 or 1 but a higher number.
