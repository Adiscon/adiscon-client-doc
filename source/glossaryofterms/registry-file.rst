
.. index:: Registry File

:orphan:

Registry File
=============

A **Registry File** (with .reg extension) is a text file that contains a snapshot
of Windows Registry entries. In the context of Adiscon products (WinSyslog,
EventReporter, MonitorWare Agent), registry files are used to export and import
complete product configurations.

Registry files enable:
- **Configuration backup** - Save your entire product configuration
- **Mass deployment** - Apply the same configuration to multiple systems
- **Configuration sharing** - Share configurations between team members
- **Disaster recovery** - Quickly restore configurations after system failures

The registry file can be created through the product's client interface using
the "Export Settings to Registry File" option, and imported silently using:
``regedit.exe /s configuration.reg``

This makes registry files an essential tool for enterprise deployments and
configuration management.
