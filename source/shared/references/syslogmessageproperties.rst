.. index:: Syslog Message Properties

Syslog Message Properties
=========================

**rawsyslogmsg**

The message as it was received from the wire (unparsed).

**syslogfacility**

The facility of a syslog message. For non-syslog messages, the value is
provided based on configuration. In essence, this is simply an integer value
that can be used for quick filtering inside your rules.

**syslogfacility_text**

The facility of a syslog message. This property is automatically created by
using the syslogfacility properly and set to these values: ``"Kernel", "User", "Mail", "Daemons", "Auth", "Syslog", "Lpr", "News", "UUCP", "Cron", "System0", "System1", "System2", "System3", "System4", "System5", "Local0", "Local1", "Local2", "Local3", "Local4", "Local5", "Local6", "Local7"``

**syslogpriority**

The severity of a syslog message. For non-syslog messages, this should be a
close approximation to what a syslog severity code means.

**syslogpriority_text**

The severity of a syslog message. This property is automatically created by
using the syslogpriority properly and set to these values: ``"Emergency", "Alert", "Critical", "Error", "Warning", "Notice", "Informational", "Debug"``

**syslogtag**

The syslog tag value, a short string. For non-syslog messages, this is provided
based on configuration. In most cases, this is used  for filtering.

**syslogver**

Contains the syslog version number which will be one or higher if a :doc:`rfc 5424 <../../glossaryofterms/rfc5424>`
valid message has been received, or 0 otherwise

**syslogappname**

Contains the appname header field, only available if the Syslog message was in
:doc:`rfc 5424 <../../glossaryofterms/rfc5424>` format. Otherwise, this field will be
emulated by the %syslogtag% property

**syslogprocid**

Contains the procid header field, only set if the Syslog message was in
:doc:`rfc 5424 <../../glossaryofterms/rfc5424>` format.

**syslogmsgid**

Contains the msgid  header field, only set if the Syslog message was in
:doc:`rfc 5424 <../../glossaryofterms/rfc5424>` format.

**syslogstructdata**

Contains the structdata header field (in raw format), only set if the Syslog
message was in :doc:`rfc 5424 <../../glossaryofterms/rfc5424>` format.

**syslogprifac**

Contains combined syslog facility and priority useful to build your own custom
syslog headers
