.. _eventreporter-cross-upgrade-v17-to-v19-installer:

Why did my EventReporter update report success when the files were not upgraded correctly?
===========================================================================================

Question
--------

Why can an in-place EventReporter update report success while the installed
client, service, or selected features still contain files from the older
release?

Answer
------

This can happen when Windows Installer retains an incomplete feature state
while processing a cross-generation update. The setup wizard can finish and
report success even though a later maintenance operation still sees features
as advertised, unavailable, or otherwise not fully installed. The product
configuration is normally not deleted; the problem is that the expected
program files were not refreshed.

Details
-------

This behavior has been confirmed for direct EventReporter updates from the
17.x generation to the 19.x generation. It can also affect other direct paths,
including 18.x to 19.4 and 16.x to 19.4, when the same symptoms are present.
The source version alone does not prove that an update path is safe or
affected.

The underlying mechanism is consistent with Windows Installer feature-state
handling. A newer setup package can be accepted as an update without changing
the installed product identity, but Windows Installer still evaluates the
feature and component state recorded for the previous installation. A change
between product generations can leave a feature only partially selected or
advertised. ``ADDLOCAL=ALL`` explicitly requests all features locally, while
``REINSTALL=ALL`` only refreshes features that Windows Installer considers
installed. This is why a two-stage repair is useful for this symptom.

Look for this combination:

* the setup wizard displays a successful completion page
* the EventReporter About dialog or file properties still show an older
  client or service version
* Modify or Custom Setup shows an unexpected state such as ``0 of 1
  subfeatures selected`` or ``0 KB``
* a normal repair does not replace the older files
* the installer requests a reboot because a service or file is still in use

.. include:: ../../shared/partials/cross-upgrade-installer-evidence.rst

Action path
-----------

1. Export or back up the EventReporter configuration before changing the
   installation.
2. Close the EventReporter Configuration Client and stop the EventReporter
   service manually before each setup run. Stopping the service first can
   avoid a reboot request caused by locked service files, but it cannot avoid
   every reboot request.
3. If a staged update is practical, use a tested intermediate release, such
   as 17.x to 18.x to 19.4, and verify the client, service, features, and
   configuration after each hop. Do not assume that an adjacent version path
   is safe without verification.
4. If the installation remains inconsistent, use the clean-install procedure
   for EventReporter after exporting the configuration.
5. If you are already working from the folder that contains the installer,
   run the following as two separate elevated setup runs. Substitute
   ``evtrptjp.exe`` when using the Japanese setup.

   First run: mark every setup feature as locally installed.

   .. code-block:: text

      evtrpt.exe /v"ADDLOCAL=ALL /L*v %TEMP%\eventreporter-addlocal.log"

   Second run: force a refresh of the installed files and registration data.

   .. code-block:: text

      evtrpt.exe /v"REINSTALL=ALL REINSTALLMODE=amus /L*v %TEMP%\eventreporter-reinstall.log"

   Let the wizard finish after each command. Do not combine the two property
   sets into one command for this recovery path. If the first command opens a
   resume page, continue through the wizard. After the second run, check
   Modify or Custom Setup, then verify the About dialog and the file versions
   before starting the service.

Related information
--------------------

* :ref:`err-2026-002-eventreporter-cross-generation-installer-upgrade`
* :doc:`../installation`
* `Microsoft Windows Installer ADDLOCAL property <https://learn.microsoft.com/en-us/windows/win32/msi/addlocal>`_
* `Microsoft Windows Installer REINSTALL property <https://learn.microsoft.com/en-us/windows/win32/msi/reinstall>`_
* `Microsoft Windows Installer REINSTALLMODE property <https://learn.microsoft.com/en-us/windows/win32/msi/reinstallmode>`_
* `Microsoft Windows Installer system reboots <https://learn.microsoft.com/en-us/windows/win32/msi/system-reboots>`_
