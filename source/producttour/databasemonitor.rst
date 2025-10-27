Database Monitor
================

The Database Monitor is used to monitor database tables. It periodically checks
a database table for new records and if it finds them, generates an event from
each record. A table that shall be monitored by the Database Monitor must have
an integer ID field that auto-increments. For example, this monitor can act as
a database-to-syslog forwarder.


.. image:: ../images/databasemonitor.png
   :width: 100%

* Database Monitor*


Further details can be found here: :doc:`database monitor <../mwagentspecific/databasemonitor>`.
