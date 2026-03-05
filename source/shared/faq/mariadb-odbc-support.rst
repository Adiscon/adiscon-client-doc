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

Modern Deployment Recommendations
---------------------------------

For current MariaDB deployments, we recommend the following:

1. **Use a current MariaDB server and connector**
   - Use currently supported MariaDB server releases
   - Use a current MariaDB Connector/ODBC package from the official source

2. **Use a dedicated database account**
   - Create a dedicated user for the Adiscon product
   - Grant only the required privileges on the target database/schema

3. **Enable secure transport for remote database connections**
   - Use TLS between the Adiscon host and MariaDB server when traffic crosses networks
   - Configure certificate settings in the DSN/driver according to your security policy

4. **Use UTF-8 consistently**
   - Prefer UTF-8/``utf8mb4`` settings for server, database, and connector
   - This prevents character conversion issues in international log messages

5. **Validate end-to-end before production rollout**
   - Use "Verify Database" in the ODBC action
   - Insert sample messages and verify they are written and readable as expected

Common Modern Troubleshooting Checks
------------------------------------

If connection tests fail, verify:

* Driver architecture matches the product runtime (32-bit vs 64-bit)
* Host, port, database name, and credentials in the DSN are correct
* MariaDB user authentication method is supported by the installed connector
* TLS requirements (if enabled) match server and connector configuration
* Firewall rules allow database traffic

Additional Information
-----------------------

For more information about database actions, see the ODBC Database Options documentation in your product's manual.

For MariaDB-specific information, visit the `official MariaDB website <https://mariadb.org/>`_.
