:orphan:

.. _shared-loganalyzer-setup-and-use:

Set up and use Adiscon LogAnalyzer
==================================

Use this guide when you want to review stored log or event data with Adiscon
LogAnalyzer.

What LogAnalyzer does
---------------------

Adiscon LogAnalyzer is a browser-based analysis component for stored data. It
works after another product has already written messages or events to a file or
database.

Deployment model
----------------

In a typical setup:

1. The logging product writes data into a database.
2. LogAnalyzer runs on a web server with PHP support.
3. LogAnalyzer connects to the database and reads the stored rows.
4. Users open the LogAnalyzer web interface in a browser.

Recommended integration path
----------------------------

The most stable integration path in the current documentation set is
database-backed storage:

1. Configure the product to write data into a database.
2. Point LogAnalyzer at that database.
3. Review the stored data in the browser.

File-based review is also possible, but parser and format details depend on the
exact file layout. This guide therefore focuses on the database-backed path.

Prerequisites
-------------

- A working Adiscon product configuration that can store data in a database
- A reachable database server with the required credentials
- A web server host where LogAnalyzer will be deployed
- A supported PHP runtime on that web server
- The LogAnalyzer application files on the web server
- Database connection information for the LogAnalyzer source

Required components
-------------------

To make LogAnalyzer usable, you need all of the following:

- **Upstream logging product**:
  EventReporter, WinSyslog, or MonitorWare Agent configured to write data into
  a database
- **Database server**:
  a database that stores the rows written by the product, for example MariaDB,
  MySQL, or Microsoft SQL Server
- **Web server**:
  a host that serves the LogAnalyzer application over HTTP or HTTPS, for
  example Microsoft IIS or Apache HTTP Server
- **PHP runtime**:
  LogAnalyzer is a PHP application and requires a working PHP environment on
  the web server. PHP 8.0 or higher is the current recommended baseline in
  this documentation set.
- **LogAnalyzer files**:
  the application files must be deployed on the web server so the browser can
  open the interface
- **Database administration tool (optional)**:
  a tool such as phpMyAdmin or another SQL administration interface can make
  initial setup and verification easier, but it is not mandatory

Typical deployment options
--------------------------

Common ways to provide the required web and PHP components include:

- **Windows web stack**:
  Microsoft IIS with PHP
- **Apache on Windows**:
  Apache HTTP Server with PHP
- **Packaged Windows stack**:
  XAMPP, WAMP, or a similar Windows package that already combines Apache, PHP,
  and a database server
- **Linux web stack**:
  a LAMP-style deployment with Linux, Apache, MariaDB or MySQL, and PHP

These component combinations are known to work together for this type of
deployment. The manuals do not require one specific stack, but they do assume
that you provide a working combination of web server, PHP runtime, and
database access before configuring LogAnalyzer itself.

Recommended setup order
-----------------------

1. Prepare the database server and confirm that it accepts connections.
2. Configure the logging product so it writes matching data into that
   database.
3. Prepare the web server and PHP runtime for LogAnalyzer.
4. Deploy the LogAnalyzer files on the web server.
5. Open the LogAnalyzer interface and configure the database source.
6. Verify end-to-end that newly written rows appear in LogAnalyzer.

Basic setup
-----------

1. Prepare the web server.

   - Install or verify a web server such as Microsoft IIS or Apache HTTP
     Server.
   - Install or verify PHP on that server.
   - If you prefer a packaged setup, install XAMPP, WAMP, or a comparable
     package instead of configuring the components separately. A LAMP-style
     deployment is also a valid known-working option on Linux.

2. Prepare the database side.

   - Make sure the database server is running.
   - Make sure the database already contains rows written by the upstream
     product or is ready to receive them.
   - If helpful, use a database administration tool such as phpMyAdmin or a
     native SQL administration tool to inspect the database during setup.

3. Deploy the LogAnalyzer files on the web server.
4. Confirm that the database server is reachable from the LogAnalyzer host.
5. Open the LogAnalyzer web interface in a browser.

Connect the data source
-----------------------

1. Create or select a LogAnalyzer source that points to the database written by
   the product.
2. Enter the database connection details for that source.
3. Save the source configuration.
4. Open the source and verify that rows can be read.

Verification
------------

1. Trigger one new event or message in the upstream product.
2. Confirm that the product writes the row to the configured database table.
3. Refresh the LogAnalyzer view.
4. Verify that the new row appears in LogAnalyzer.

Troubleshooting notes
---------------------

- If LogAnalyzer opens but shows no data, first verify that the upstream
  product is actually writing new rows.
- If the database connection fails, verify server access, credentials,
  and table permissions.
- If the web interface is not reachable, check the web server and PHP setup
  before troubleshooting the logging product.

Related information
-------------------

Use one of the product-specific LogAnalyzer tutorials to prepare the upstream
data source before configuring LogAnalyzer itself.
