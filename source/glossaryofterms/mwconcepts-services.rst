:orphan:

.. _glossary-mwconcepts-services:
.. supporting-labels-marker

MonitorWare Agent - Services
============================

Services inside the MonitorWare Agent gather the data that is processed by
rules. Each service type reflects a specific set of code inside the MonitorWare
Agent. For example, a Syslog Service represents an instance of a Syslog server
and an NT Event Log Monitor Service represents an instance of an NT Log Monitor
(periodically pulling out log information).

Typically, there can be multiple instances of the same service running, as long
as their configuration parameters do not conflict. For example the syslog
service: there can be multiple syslog servers on a given system as long as they
listen to different ports. Consequently, there can be multiple instances of the
syslog service be created. For example, there could be three of them: two
listen to the default port of 514, but one with TCP and one with UDP, and a
third one listens to UDP port 10514. All three coexist and run at the same
time.


**The following services are supported:**

**Syslog server**

Implements a Syslog server. It can be set to listen to any valid port. UDP and
TCP communication is supported.

**Passive Syslog Listener**

The Passive Syslog Listener Service is a TCP based Listener Service that sends
messages from a Syslog Queue to any remote host, that connects to it.
Connections can be secured with TLS including certificate based authentication.
Additionally, a greeting and response message can be configured as well.


**RELP Listener**

Apart from the fact that a different communication protocol is used, the RELP
listener corresponds functionally to the syslog listener. The RELP listener
automatically monitors all available IP addresses, including IPv4 and IPv6.
This is due to the Librelp implementation method.


**SETP server**

Implements an SETP Server. It is used for reliable receiving event
notifications.

**Event Log Monitor**

Monitors Windows event logs. As soon as new events are detected, these are
forwarded to MonitorWare processing. This service is similar to the Adiscon
EventReporter functionality.

**Database Monitor**

The Database Monitor read a table from an ODBC data source and generates
InfoUnits out of it. These InfoUnits have properties (names by the table
fields) which are filled dynamically depending on which field your table has.
Each property can be used like other properties with in the MonitorWare Agent.

In short it is used to Monitor Database tables. It periodically checks a
database table for new records and if it finds them, generates an event from
each record. A table that shall be monitored by the Database Monitor must have
an integer ID field that auto-increments.

**SerialPort Monitor**

The SerialPort Monitor allows you to monitor devices attached to local
communications ports. Actually, this is not limited to serial (RS232) devices -
devices connected via e.g. LPT ports can also be monitored as long as the
device provides a proper interface to the port device.

For example - uses for the serial port monitor may be interfacing to data
loggers, "strange" log sources (e.g. PBX call logs) or out-of-band log
retrieval (e.g. setting a router to log to the serial port instead to the
network and then picking the data from that serial line). Out-of-band log
retrieval can also be used to hide the fact that logging is actually taking
place.

**SNMP Trap Receiver**

SNMP Trap Receiver allows you to receive SNMP messages. A rough description of
a Trap is that it is somewhat like a Syslog message, just over another protocol
(SNMP). A trap is generated when the device feels it should do so and it
contains the information that the device feels should be transmitted. It also
contains some (few) standard items, as the version, community etc.

**File monitor**

Monitors text files. As soon as new lines at the end of the file are detected,
these are forwarded to MonitorWare Agent for processing. They can be forwarded
either one line at a time or in fixed chunks as set by the administrator.

**Heartbeat**

This service generates a special information type. Its primary purpose is to
notify an upstream system that the MonitorWare Agent set for heart beating is
still alive. So the upstream system can be configured to raise alarms (or
corrective action) if it does not receive heartbeats from the downstream system.

**Ping Probe**

The ping probe pings a configured (remote) system on a schedule. If no ping
response (echo reply) is received within a configured interval, an event is
generated. This way, MonitorWare can check if a remote system is responding, at
least at the IP stack level.

**Port Probe**

This is similar to the ping probe, but works at the application level. It can
be used with any TCP based service. Basically, the MonitorWare Agent goes out
and periodically tries to connect to a specific TCP port on a specific (remote)
machine. If the connection request fails, an event is generated. As such,
failing services (like database or mail servers) can be detected.

Optionally, the port probe can send a single greeting string if the connection
was established and check if a response is sent by the remote system. For
example, a SMTP mail gateway can be probed by connecting to port 25 and then
sending a "HELO" sequence. The system should respond with a "HELO" message.
Many protocols have such command sequences. Thus, they can be very effectively
probed. Again, if the system does not provide the expected response, the port
probe will generate a notification event.

**NT Service Monitor**

The NT Service Monitor checks if vital system services and applications are
running and generates an alert if not.

**Disk Space Monitor**

Disk Space Monitor continuously checks all hard drives for available and used
space. It can be used to generate long term reports as well as alerts or
corrective action on low space conditions.

**Associated rulesets**

Each instance of a service has an associated ruleset. This allows easy
creation of customized rulesets on a per service basis. Of course, all
services can also operate on a common ruleset.

All services are executed as multiple threads inside the MonitorWare Agent.
From the operating point of view, there is only one system service called the
"MonitorWare Agent". If the service configuration of the MonitorWare Agent is
modified, the MonitorWare system service needs to be restarted in order to
activate the new configuration. Later releases will have some options to
automate this task.
