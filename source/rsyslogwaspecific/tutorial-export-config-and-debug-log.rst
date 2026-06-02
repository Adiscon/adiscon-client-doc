.. _rsyslogwa-tutorial-export-config-and-debug-log:

Tutorial: Export the Configuration and Create a Debug Log
=========================================================

Use this tutorial when you need rsyslog Windows Agent configuration data and a
debug log for troubleshooting or for a support case.

Goal
----

At the end of this procedure, you will have:

- a text-based export of the rsyslog Windows Agent configuration
- a debug log file that captures service behavior

Prerequisites
-------------

- Access to the rsyslog Windows Agent Configuration Client
- Permission to restart the rsyslog Windows Agent service if needed
- A writable location for the exported settings and debug log

Steps
-----

1. Export the configuration.

   - Open the rsyslog Windows Agent Configuration Client.
   - Go to **Computer -> Export Settings to Registry File**.
   - Export the settings as a text-based registry file.

2. Save the export to a known location.

   - Use a descriptive file name such as ``rsyslogwa-config.reg``.
   - Do not use the binary export format.

3. Enable debug logging.

   - Open :doc:`Debug <../mwagentspecific/debug-options>` under **General**.
   - Enable debug output into file.
   - Set a full path and file name for the debug log.
   - Start with **Errors & Warnings** and **Minimum Debug Output** unless
     support asks for a higher level.

4. Restart the rsyslog Windows Agent service if required.
5. Reproduce the problem or run the test scenario.
6. Disable debug logging again after capture.

   - Debug logging increases system load and should not stay enabled during
     normal operation.

7. Package the files for review or support.

   - Compress the exported registry file and the debug log file into one ZIP
     archive.

Verification
------------

1. Confirm that the registry export file exists and is readable as text.
2. Confirm that the debug log file exists and contains recent entries from the
   test period.
3. If the debug log stays empty, verify that the service was restarted after
   enabling debug output.

Next step
---------

If you need to send the data to Adiscon, continue with:

- :doc:`faq/export-settings-support-call`
- :doc:`../../shared/sales/how-to-contact-sales`
