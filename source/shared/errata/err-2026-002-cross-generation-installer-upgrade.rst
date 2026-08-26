:orphan:

.. only:: winsyslog or winsyslog_j or mwagent or eventreporter or rsyslog

   .. _err-2026-002-cross-generation-installer-upgrade:

   ERR-2026-002: In-place update reports success but program files are not upgraded correctly
   ===========================================================================================

   **Status:** Workaround available

   **First published:** August 26, 2026

   Description
   -----------

   A direct in-place update across product generations can finish with a
   successful setup message while one or more program features remain
   incomplete. The installed product identity may look current, but the
   client, service, or selected feature files can still be from the older
   release. A later repair can then appear to do nothing because Windows
   Installer still considers the affected features installed or otherwise
   satisfied.

   This is an installer feature-state and file-refresh problem. It does not,
   by itself, indicate that the product configuration was deleted. The exact
   source version is not sufficient to rule the behavior in or out.

   Affected products and versions
   ------------------------------

   * **EventReporter:** Confirmed on direct updates from 17.x to 19.x. Other
     direct paths can also be affected, including 18.x to 19.4 and 16.x to
     19.4 when the same symptoms occur.
   * **WinSyslog:** Confirmed on direct updates from 16.x to 18.x. Other
     direct source versions can also be affected.
   * **MonitorWare Agent:** Confirmed on direct updates from 13.x to 15.x.
     Other direct source versions can also be affected.
   * **rsyslog Windows Agent:** Confirmed on direct updates from 6.x to 8.x.
     Other direct source versions can also be affected.

   These are affected-version examples, not a guarantee that every install in
   a range fails. No adjacent source-version path should be treated as safe
   without checking the result. Fresh installations are outside the typical
   scope of this notice.

   Impact
   ------

   The setup wizard can display a normal completion page even though the
   installed client or service still runs older binaries. Custom Setup can
   show an unexpected state, such as no selected subfeatures or zero required
   disk space. The About dialog or file properties can disagree with the
   version shown by the setup or installed-program entry. A service or locked
   file can also cause a reboot prompt during recovery.

   How to determine whether this applies
   --------------------------------------

   Check for all or most of the following:

   * the issue follows a direct in-place update between product generations
   * setup reports that the installation completed successfully
   * the running client, service, or file properties still show an older
     version
   * Modify or Custom Setup shows an incomplete feature state
   * an ordinary repair does not replace the older files

   Record the client version, service version, selected features, and file
   versions before and after the recovery. Preserve the verbose installer logs
   if further support is needed.

   Workarounds
   -----------

   1. Export or back up the product configuration before changing the
      installation.
   2. Close the configuration client and stop the product service manually
      before each setup run. This can avoid a reboot request caused by locked
      service files, although it cannot avoid every reboot request.
   3. Where practical, use a tested staged update through an intermediate
      release and verify every hop. A staged path reduces the size of the
      generation change; it is not a guarantee of success.
   4. If the installation remains inconsistent, use the product's clean-install
      procedure after exporting the configuration.
   5. For the specific incomplete-feature symptom, run the two following
      commands as separate elevated setup runs from the directory containing
      the installer. Let the first wizard finish before starting the second.
      Substitute the Japanese setup executable where applicable.

      EventReporter (``evtrpt.exe`` or ``evtrptjp.exe``):

      .. code-block:: text

         evtrpt.exe /v"ADDLOCAL=ALL /L*v %TEMP%\eventreporter-addlocal.log"
         evtrpt.exe /v"REINSTALL=ALL REINSTALLMODE=amus /L*v %TEMP%\eventreporter-reinstall.log"

      WinSyslog (``wnsyslog.exe`` or ``wnsyslogjp.exe``):

      .. code-block:: text

         wnsyslog.exe /v"ADDLOCAL=ALL /L*v %TEMP%\winsyslog-addlocal.log"
         wnsyslog.exe /v"REINSTALL=ALL REINSTALLMODE=amus /L*v %TEMP%\winsyslog-reinstall.log"

      MonitorWare Agent (``mwaremax.exe``):

      .. code-block:: text

         mwaremax.exe /v"ADDLOCAL=ALL /L*v %TEMP%\mwagent-addlocal.log"
         mwaremax.exe /v"REINSTALL=ALL REINSTALLMODE=amus /L*v %TEMP%\mwagent-reinstall.log"

      rsyslog Windows Agent (``rsyslogwa.exe``):

      .. code-block:: text

         rsyslogwa.exe /v"ADDLOCAL=ALL /L*v %TEMP%\rsyslogwa-addlocal.log"
         rsyslogwa.exe /v"REINSTALL=ALL REINSTALLMODE=amus /L*v %TEMP%\rsyslogwa-reinstall.log"

      Do not combine the two property sets into one command for this recovery
      path. After the second run, verify that Modify or Custom Setup shows all
      intended features, then check the About dialog, file versions, service
      state, and configuration.

   Resolution status
   -----------------

   The workaround is available while the installer behavior is being
   investigated. A corrected setup build and its exact affected-version scope
   are not stated here until they are publicly confirmed. This notice will be
   revised when a corrected build is available.

   Revision history
   ----------------

   * August 26, 2026: Initial publication with the two-stage repair workaround
     and expanded cross-version scope.
