.. _mysql-update-winsyslog:

Troubleshooting MySQL 4.x Database Connectivity in WinSyslog
=============================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-02-13
   :updated: 2026-02-13
   :products: WinSyslog

Question
--------

I am facing a problem while writing to a MySQL 4.x database using the
Write to Database action in WinSyslog. What should I do?

Answer
------

This issue is related to the MySQL authentication protocol introduced in
MySQL 4.1 and above. The protocol uses a password hashing algorithm that
is not compatible with the one used by older clients and stores passwords
differently compared to older versions. If you upgrade your MySQL server
to 4.x and try to connect with an older client, the connection may fail.

You can resolve this by using one of the following options.

Option 1: Upgrade Client Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upgrade all client programs to use the 4.1.1 or newer client library.
This ensures compatibility with the new authentication protocol used by
MySQL 4.x servers.

Option 2: Use Pre-4.1 Style Passwords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The ``OLD_PASSWORD()`` function uses a less secure hashing algorithm
   than the MySQL 4.1+ method. Upgrading your client libraries
   (Option 1) is the preferred solution from a security standpoint.

If you need to continue using a pre-4.1 client program with WinSyslog,
reset the MySQL user password using the ``OLD_PASSWORD()`` function.

**Using SET PASSWORD:**

.. code-block:: sql

   SET PASSWORD FOR
   'someuser_abc'@'somehost_xyz' = OLD_PASSWORD('somenewpwd');

**Using UPDATE and FLUSH PRIVILEGES:**

.. code-block:: sql

   UPDATE mysql.user SET Password = OLD_PASSWORD('somenewpwd')
   WHERE Host = 'somehost_xyz' AND User = 'someuser_abc';
   FLUSH PRIVILEGES;

Replace ``somenewpwd`` with the password you want to use. You cannot
retrieve your old password from MySQL, so select a new one.

Option 3: Configure the Server for Older Password Hashing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure your MySQL server to use the older password hashing algorithm:

1. Start ``mysqld`` with the ``--old-passwords`` option.

2. Identify accounts that have updated their passwords to the longer
   4.1 format using the following query:

   .. code-block:: sql

      SELECT host, user, password FROM mysql.user
      WHERE LENGTH(Password) > 16;

3. Reset the password for the accounts returned by the query using
   the ``OLD_PASSWORD()`` function. You can use either
   ``SET PASSWORD`` or ``UPDATE`` as described in Option 2.
