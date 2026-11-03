:orphan:

.. only:: (winsyslog or winsyslog_j or mwagent or rsyslog) and errata_preview

   .. _err-2026-020-product-default-license:

   ERR-2026-020: A service may not find its default license file
   =============================================================

   **Status:** Draft; partial correction scheduled

   **Publication:** Draft prepared for review

   **First published:** Pending publication

   Description
   -----------

   In registry configuration mode, the classic configuration client can
   install a license at its product-specific default location while the
   service looks for the default license in a different directory. If the
   service cannot find a valid license there, it may run in trial mode despite
   the installed license.

   Affected products
   -----------------

   The behavior has been identified for the following client and service
   version combinations:

   - **WinSyslog:** client ``26.10.0.793`` and service ``26.10.0.775``
   - **MonitorWare Agent:** client ``26.10.0.1773`` and service ``26.10.0.690``
   - **rsyslog Windows Agent:** client ``26.10.0.443`` and service
     ``26.10.0.354``

   The issue requires an empty configured license path, a valid license at the
   client default location, and no valid license at the different location
   used by the service. The service location can depend on its configured data
   directory. Other versions may also be affected. This list does not
   establish the earliest affected version.

   Impact
   ------

   The service may enter trial mode despite an installed license. Installing
   the license in the client's default location alone does not establish
   licensed service operation.

   How to determine whether you are affected
   -----------------------------------------

   1. Check the service and classic client versions and confirm that registry
      configuration is in use.
   2. Check whether the configured license path is empty. The default path
      displayed by the client does not establish that an explicit path is
      configured or that the service uses that location.
   3. Check the configured data directory and compare the client's license
      location with the service's default location. For the 26.10 service
      versions listed above, an empty license path selects ``license.alic``
      in the configured data directory, or in the directory containing the
      service program if the data directory is empty. Confirm whether a
      valid license exists only at the client location. For the scheduled
      26.11 behavior, see the resolution status below.
   4. Check the service's license status. Trial status alone does not confirm
      this issue; the path and license conditions above must also apply.

   Workaround
   ----------

   Copy the unchanged valid license to a different filename in the same
   folder. Select that file as the explicit license path in the classic
   client, save the configuration and restart the service. Ensure that the
   service account can read the file, then verify that the service reports
   licensed operation and processes messages as expected. A restart briefly
   interrupts service operation; follow your usual controlled restart
   procedure and retain the original license.

   Resolution status
   -----------------

   For registry configurations with an empty license path and no configured
   data directory, a correction is scheduled for version 26.11. The target
   service builds are WinSyslog ``26.11.0.778``, MonitorWare Agent
   ``26.11.0.693``, and rsyslog Windows Agent ``26.11.0.357``. These target
   builds do not confirm that a corrected release is available.

   With no configured data directory, the scheduled correction first checks
   the product-specific default license location under the Windows common
   application data directory, if Windows can provide that directory. If
   that license file or its containing path is missing, the service retains
   the fallback to ``license.alic`` beside the service program. An unreadable
   or invalid license at the product-specific location does not trigger that
   fallback.

   The scheduled correction does not cover configurations with a different
   data directory. The service continues to use that directory for its
   default license path, so the mismatch may remain. Use the explicit-path
   workaround above and verify licensed operation.

   Revision history
   ----------------

   - **November 3, 2026:** Draft prepared for review; not published.

