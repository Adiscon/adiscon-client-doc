.. _mariadb-odbc-support:

Is MariaDB supported by the ODBC action?
=========================================

This article explains MariaDB support in ODBC database actions.

Question
--------

Is MariaDB supported by the ODBC action?

Answer
------

Yes, MariaDB is fully supported by the ODBC action and can be used as a direct replacement for MySQL.

Background
----------

MariaDB is a free and open-source alternative to MySQL. It is a fork of MySQL, initiated by the original MySQL developers after Oracle acquired Sun Microsystems (the former owner of MySQL). MariaDB was designed to be binary-compatible with MySQL, which generally makes switching from MySQL to MariaDB very easy.

Key characteristics of MariaDB:

* **Open Source:** MariaDB is consistently Open Source under a license that guarantees free use and further development
* **Binary Compatibility:** Designed to be binary-compatible with MySQL, making migration straightforward
* **Independent Development:** Continuous, independent development separate from MySQL
* **Performance:** Often preferred as an alternative due to sometimes better performance characteristics

Configuration
-------------

To use MariaDB with the ODBC action:

1. **Install MariaDB ODBC Driver:**
   - Download and install the `MariaDB Connector/ODBC driver <https://mariadb.org/connector-odbc/all-releases/>`_ from the official MariaDB website
   - Ensure you install the correct version (32-bit or 64-bit) to match your Adiscon product installation

2. **Configure System DSN:**
   - Open the ODBC Data Source Administrator (use the 32-bit version if your product runs in 32-bit mode)
   - Create a new System DSN
   - Select the MariaDB ODBC driver
   - Configure the connection settings (server, database, credentials)

3. **Configure Database Action:**
   - In your Adiscon product configuration, select the ODBC Database action
   - Choose the MariaDB System DSN you created
   - Test the connection using the "Verify Database" button
   - Create the database tables if needed using the "Create Database" button

**Note:** The configuration process is identical to configuring MySQL, as MariaDB uses MySQL-compatible drivers and protocols.

Additional Information
-----------------------

For more information about database actions, see the ODBC Database Options documentation in your product's manual.

For MariaDB-specific information, visit the `official MariaDB website <https://mariadb.org/>`_.

