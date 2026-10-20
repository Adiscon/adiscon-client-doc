:orphan:

.. only:: eventreporter and errata_preview

   .. _err-2026-006-eventreporter-default-license:

   ERR-2026-006: EventReporter may not find the default license file
   =================================================================

   **Status:** Scheduled

   **Publication:** Draft prepared for review

   **First published:** Pending publication

   Description
   -----------

   EventReporter can start in trial mode when its license file is stored as
   ``%ProgramData%\Adiscon\EventReporter\license.alic`` and no separate license
   file path is configured. The configuration client can show the file as valid
   even though the service does not load it on startup.

   Affected products
   -----------------

   This issue is confirmed in EventReporter service builds ``26.07.0.603``,
   ``26.08.0.608``, ``26.09.0.609``, and ``26.10.0.610`` when registry
   configuration is used with the default license path. Other versions and
   file-based configurations are not confirmed affected here.

   Impact
   ------

   The service may use trial mode instead of the purchased license. When the
   trial period ends, licensed processing can stop.

   How to determine whether you are affected
   -----------------------------------------

   Check the service startup status after applying the license. If it reports
   trial mode while the configuration client shows a valid license, check the
   startup debug log for ``reason=Missing``. Separately, inspect the license
   path field in General > License to see whether an explicit path is set.

   Workaround
   ----------

   Keep the license file contents unchanged. Make a copy in the same directory
   under a different filename, such as ``license_custom.alic``. In the
   EventReporter Configuration Client, open General > License and enter the
   copied file's full path in the license path field (or use the browse button
   beside that field). Save the configuration and restart the service. Confirm
   that it starts in licensed mode. Keep the original license file for
   recovery. The service restart briefly interrupts event processing; verify
   your normal event collection and forwarding after it starts.

   Resolution status
   -----------------

   A correction is being prepared. The exact fixed service build will be
   stated after release.

   Revision history
   ----------------

   - **October 20, 2026:** Draft prepared for review; not published.
