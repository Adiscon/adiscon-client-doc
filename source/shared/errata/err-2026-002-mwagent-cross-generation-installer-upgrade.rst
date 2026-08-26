:orphan:

.. only:: mwagent

   .. _err-2026-002-mwagent-cross-generation-installer-upgrade:

   ERR-2026-002: MonitorWare Agent update reports success but program files are not upgraded correctly
   ====================================================================================================

   **Status:** Workaround available

   **First published:** August 26, 2026

   Description
   -----------

   A direct MonitorWare Agent update across product generations can finish
   with a successful setup message while one or more program features remain
   incomplete. The installed product identity may look current, but the
   MonitorWare Agent client, service, or selected feature files can still be
   from the older release. A later repair can then appear to do nothing
   because Windows Installer still considers the affected features installed
   or otherwise satisfied.

   This is an installer registration and feature-state problem. It does not,
   by itself, indicate that the MonitorWare Agent configuration was deleted.
   A newer setup can change package contents without changing the installed
   product identity, leaving the recorded feature state out of sync with the
   files on disk.

   Affected products and versions
   ------------------------------

   This notice applies to MonitorWare Agent. The behavior has been confirmed
   on direct updates from the 13.x generation to the 15.x generation. The
   same failure mode can also appear on other direct paths when the symptoms
   described below are present. Older starting versions may also be affected;
   this notice does not claim that every historic version is proven to fail.

   When an intermediate release is available, adjacent MonitorWare Agent
   upgrades such as 14.x to 15.x usually work and are the preferred in-place
   path. They are not a guarantee, so verify the result after every update.
   A fresh installation of the target release on a clean machine is outside
   the typical scope of this notice.

   Impact
   ------

   The setup wizard can display a normal completion page even though the
   installed MonitorWare Agent client or service still runs older binaries.
   Modify or Custom Setup can show an unexpected state, such as no selected
   subfeatures or zero required disk space. The About dialog or file
   properties can disagree with the version shown by setup or Programs and
   Features. A service or locked file can also cause a reboot prompt during
   recovery.

   How to determine whether this applies
   --------------------------------------

   Check for all or most of the following:

   * the issue follows a direct in-place MonitorWare Agent update between
     product generations
   * setup reports that the installation completed successfully
   * the running MonitorWare Agent client, service, or file properties still
     show an older version
   * Modify or Custom Setup shows an incomplete feature state, such as
     ``0 of 1 subfeatures selected`` or ``0 KB``
   * an ordinary repair does not replace the older files

   Record the client version, service version, selected features, and file
   versions before and after recovery. Preserve the verbose installer logs if
   further support is needed.

   Workarounds
   -----------

   1. Export or back up the MonitorWare Agent configuration before changing
      the installation.
   2. If a staged update is practical, update 13.x to 14.x and then to 15.x,
      verifying the client, service, features, and configuration after each
      hop. A staged path reduces the size of the generation change; it is not
      a guarantee of success.
   3. If the installation remains inconsistent, use the MonitorWare Agent
      clean-install procedure after exporting the configuration. Uninstalling
      removes program files, so confirm the configuration and license after
      installing the target release and re-import configuration data if
      required.
   4. If the symptoms already match this notice, run the following as two
      separate elevated setup runs from the folder containing the
      MonitorWare Agent installer. Close the Configuration Client and stop
      the MonitorWare Agent service manually before each run. This can avoid a
      reboot request caused by locked service files, although it cannot avoid
      every reboot request.

      First run: mark every setup feature as locally installed.

      .. code-block:: text

         mwaremax.exe /v"ADDLOCAL=ALL /L*v %TEMP%\mwagent-addlocal.log"

      Second run: force a refresh of the installed files and registration
      data.

      .. code-block:: text

         mwaremax.exe /v"REINSTALL=ALL REINSTALLMODE=amus /L*v %TEMP%\mwagent-reinstall.log"

      Let the wizard finish after each command. Do not combine the two
      property sets into one command for this recovery path. If the first
      command opens a resume page, continue through the wizard. After the
      second run, check Modify or Custom Setup, then verify the About dialog,
      file versions, service state, and configuration before normal use.

   Resolution status
   -----------------

   The workaround is available while the installer behavior is being
   investigated. A corrected setup build and its exact affected-version scope
   are not stated here until they are publicly confirmed. This notice will be
   revised when a corrected MonitorWare Agent setup is published.

   Revision history
   ----------------

   * August 26, 2026: Initial publication for MonitorWare Agent, with the
     two-stage repair workaround and cross-version symptom guidance.

   Related information
   --------------------

   * `MonitorWare Agent cross-generation installer FAQ
     <../../mwagentspecific/faq/cross-upgrade-v13-to-v15-installer.html>`_
