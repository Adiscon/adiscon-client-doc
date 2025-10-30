.. _faq-odbc-mariadb-support:

MariaDB support with the ODBC database action
=============================================

**Question:** Is MariaDB supported by the ODBC action?

**Answer:** Yes. MariaDB is a drop-in, binary-compatible fork of MySQL and can be
used with the ODBC database action as a direct replacement for MySQL.

What this means
---------------

- MariaDB can be targeted by the ODBC action in WinSyslog, EventReporter, and
  MonitorWare Agent. It also applies to the Windows Agent variant of Rsyslog.
- Use a suitable MariaDB/MySQL ODBC driver (e.g., MariaDB Connector/ODBC or
  MySQL ODBC driver) and configure your DSN/connection string accordingly.
- Existing MySQL-based schemas and queries typically work unchanged due to the
  compatibility goals of MariaDB.

Quick setup tips
----------------

- Install a 64-bit ODBC driver if the service runs as 64-bit; match driver
  bitness to the service process.
- Create a System DSN for service use, or provide a full connection string in
  the action settings.
- Verify connectivity with the ODBC Data Source Administrator before enabling
  the action.

Background
----------

MariaDB was created by the original MySQL developers and is kept compatible
with MySQL while offering fully open-source licensing and ongoing independent
development. For the ODBC action, this equivalence means you can treat MariaDB
as a MySQL-compatible backend.


