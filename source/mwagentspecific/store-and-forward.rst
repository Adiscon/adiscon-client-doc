Store and Forward
=================

After MonitorWare Agent collects and filters data, actions determine what
happens next.

Common destinations
-------------------

MonitorWare Agent commonly uses these actions:

- :doc:`Write to File <a-fileoptions>` for local archival or troubleshooting
- :doc:`Database logging <a-databaseoptions>` for structured storage and later
  analysis
- :doc:`Forward Syslog <a-forwardsyslogoptions>` for downstream syslog
  infrastructure
- :doc:`Forward SETP <a-forwardsetpoptions>` for reliable transfer to Adiscon
  systems
- :doc:`Mail <a-mailoptions>` or :doc:`Start Program <a-startprogram>` for
  alerting and operational response

Choosing the first destination
------------------------------

For first-time setup, writing to a file is usually the easiest verification
path. For production deployments, forwarding or database storage is often more
useful.

If reliable delivery across temporary outages matters, configure disk-backed
queues where the action supports them.
