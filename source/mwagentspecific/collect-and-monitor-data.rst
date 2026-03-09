Collect and Monitor Data
========================

MonitorWare Agent can collect both event data and operational monitoring data.
That breadth is one of the main differences between MonitorWare Agent and the
more specialized manuals in this doc set.

Typical input sources
---------------------

MonitorWare Agent commonly starts with one or more of these service types:

- :doc:`Event Log Monitor V2 <eventlogmonitorv2>` for Windows Event Log
  channels
- :doc:`Syslog Server <syslogserver>` for network devices and applications that
  send syslog
- :doc:`SETP Server <setpserver>` for reliable structured forwarding between
  Adiscon products
- :doc:`File Monitor <filemonitor>` for text-based application logs
- probe and monitor services such as :doc:`pingprobe`, :doc:`portprobe`,
  :doc:`diskspacemonitor`, :doc:`cpumonitor`, and :doc:`ntservicemonitor`

A practical first design
------------------------

For a first working deployment, keep the design small:

1. Choose one service that collects the data you care about first.
2. Attach that service to a dedicated ruleset.
3. Add one simple action, such as write to file or forward via syslog.
4. Verify that the expected events arrive.

This produces a baseline that is easy to test before you add more services,
filters, and destinations.
