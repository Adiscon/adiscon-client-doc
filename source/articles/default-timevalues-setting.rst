Default Timevalues Setting in EventReporter/MonitorWare Agent/WinSyslog explained
=================================================================================

- Created: 2008-01-24 Andre Lorbach
- Updated: 2020-10-05 adisconteam

The general options of each product (EventReporter, MonitorWare Agent and
WinSyslog) contain a setting for the "Default Timevalues". This setting can be
set to Localtime and UTC (Universal Coordinated Time) which is default.

**If you switch this setting to Localtime, you may wonder why output timevalues still are in UTC.**

Internally we need to calculate with UTC time. This is needed
in order to maintain the time values if they are send via Syslog or SETP. If
we wouldn't do this, this could result to unexpected time differences.

**So where does this setting have an effect?**

* Send Email Action: The date in the email header is affected
* Start Program Action: Time parameters in the command line are affected
* Write File Action: Time properties in the file name are affected
* Filter Engine: If you filter by weekday or time fields, localtime does affect
  the filter result

**But how can I get localtime output?**

We added two additional options into the property engine which can be applied
on time based values for this purpose.

Property Option: **localtime** = converts the output of the timestamp into localtime:

``Sample: %variable:::localtime%``

Property Option: **uxLocalTimeStamp** = same output as uxTimeStamp, but
localtime is used

``Sample: %variable:::uxLocalTimeStamp%``
