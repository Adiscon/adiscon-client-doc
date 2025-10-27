.. index:: Windows Event Log Properties

Windows Event Log Properties
============================

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

**NTEventLogType**

The name of the Windows Event Log this event is from (for example "System" or
"Security").

**bdata**

Windows Event Log records sometimes contain binary data. The Event Log Monitor
service can be set to include this binary data into the event, if it is
present. If it is configured to do so, the binary data is put into the "bdata"
property. Every byte of binary data is represented by two hexadecimal
characters.

Please note that it is likely for bdata not to be present. This is because the
binary data is seldom used and very performance-intense.
(%id%) - "%msg%"%$CRLF%
