:orphan:

.. _mariadb-odbc-support:

Is MariaDB supported by the ODBC action?
========================================

This article explains MariaDB support in the ODBC database action for Adiscon products.

Background
----------

MariaDB is a free and open-source database management system that serves as a direct replacement for MySQL. It was created as a fork of MySQL by the original MySQL developers after Oracle acquired Sun Microsystems (the former owner of MySQL).

MariaDB is designed to be binary-compatible with MySQL, which makes switching from MySQL to MariaDB straightforward. MariaDB is consistently Open Source under a license that guarantees free use and further development, and is often preferred as an alternative due to its continuous, independent development and sometimes better performance.

Support Status
--------------

**Yes, MariaDB is fully supported by the ODBC action.**

MariaDB can be used as a direct replacement for MySQL with the ODBC database action. Since MariaDB maintains binary compatibility with MySQL, it works seamlessly with existing MySQL ODBC drivers and configurations.

Using MariaDB
-------------

To use MariaDB with the ODBC action:

1. **Install MariaDB** on your system or connect to an existing MariaDB server
2. **Install the MySQL ODBC driver** (MariaDB is compatible with MySQL ODBC drivers)
3. **Configure a System DSN** using the ODBC Data Source Administrator
4. **Select the DSN** in your product's ODBC Database action configuration

The configuration process is identical to using MySQL, as MariaDB maintains binary compatibility with MySQL connectors and drivers.

Additional Information
----------------------

.. only:: not syslogviewer

   For more information about configuring the ODBC database action, see the :doc:`database logging <../../glossaryofterms/database>` documentation.

.. only:: mwagent

   See also :doc:`ODBC Database Options <../references/a-databaseoptions>` for MonitorWare Agent-specific configuration details.

For details about MariaDB itself, visit the `MariaDB Foundation website <https://mariadb.org/>`_.

