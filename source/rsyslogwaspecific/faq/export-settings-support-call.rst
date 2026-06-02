.. _export-settings-support-call-rsyslogwa:

How to Export rsyslog Windows Agent Settings for a Support Call
===============================================================

Question
--------

How do I export the rsyslog Windows Agent configuration so I can send it to
Adiscon support?

Answer
------

Open the rsyslog Windows Agent Configuration Client, export the settings as a
text-based registry file, compress the exported file, and submit it through the
`Support Portal <https://ticket.adiscon.com/>`_.

Details
-------

Do **not** use the binary registry export format. Use the text-based export so
support can inspect the configuration.

Action path
-----------

1. Open the rsyslog Windows Agent Configuration Client.
2. Go to **Computer -> Export Settings to Registry File**.
3. Save the file to a known location.
4. Compress the exported ``.reg`` file.
5. Send the ZIP archive through the support portal.

Related information
-------------------

* :doc:`../tutorial-export-config-and-debug-log`
