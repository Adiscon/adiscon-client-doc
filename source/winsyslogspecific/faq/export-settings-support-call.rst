.. _export-settings-support-call-winsyslog:


How to Export WinSyslog Settings for a Support Call
====================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-02-13
   :updated: 2026-02-13
   :products: WinSyslog

Overview
--------

When contacting Adiscon support, you may be asked to provide your WinSyslog
configuration. This FAQ explains how to export your WinSyslog settings to a
registry file and send them to the support team.

.. note::

   Do **not** use the binary registry file export option. Always use the
   text-based registry file export described below.

Step 1: Export Settings
-----------------------

Open the WinSyslog Configuration Client. Go to the **Computer** menu and click
**Export Settings to Registry File**.

Step 2: Save the Registry File
-------------------------------

After selecting the export option, a dialog appears where you can choose the
file name and location. Enter a descriptive name (for example,
``winsyslog-config.reg``) and save the file to a convenient location.

Step 3: Compress the File
--------------------------

Right-click on the saved registry file and compress (zip) it using your
preferred archiving tool. This reduces the file size for email transmission.

Step 4: Send the File
----------------------

Send the zipped registry file to the Adiscon support team via the
`Support Portal <https://ticket.adiscon.com/>`_.

Security Considerations
------------------------

The exported registry file contains your WinSyslog configuration, which may
include connection strings, server addresses, or other environment-specific
details. We recommend reviewing the contents of the registry file with a text
editor before sending it, so you can verify that no sensitive information is
included unintentionally.

See Also
--------

* :doc:`../installation` - WinSyslog installation documentation
