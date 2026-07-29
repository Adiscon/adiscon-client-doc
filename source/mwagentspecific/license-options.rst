

License
=======

Licensing options are on **General** -> **License** in the configuration client.
Current builds use a ``license.alic`` license file.

License File
^^^^^^^^^^^^

Use this page to apply ``license.alic``.

.. only:: mwagent

   .. image:: ../images/generaloptions-license.png
      :width: 100%

.. only:: winsyslog or winsyslog_j

   .. image:: ../images/generaloptions-license-winsyslog.png
      :width: 100%

.. only:: eventreporter or rsyslog

   .. image:: ../images/generaloptions-license-shared.png
      :width: 100%

**File Configuration field:**
  szLicenseV2Path

**Description:**
  Optional path to the license file. When empty, the service uses the default
  location:

  .. only:: mwagent

     ``%ProgramData%\\Adiscon\\MonitorWare\\license.alic``

  .. only:: winsyslog or winsyslog_j

     ``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``

  .. only:: eventreporter

     ``%ProgramData%\\Adiscon\\EventReporter\\license.alic``

  .. only:: rsyslog

     ``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

  You can browse for the file, drag-and-drop it onto the client, or paste a
  file path. The license is validated and applied when you save the
  configuration.

  Current configuration clients use the license file path only. They do not
  read or save legacy registration-name or numeric license-key configuration
  values. Update an existing configuration to use ``szLicenseV2Path`` and a
  ``license.alic`` file.

  The main window status bar shows license status (for example, the licensed
  organization). A version mismatch between the license file and the installed
  service may show a warning banner until you apply a matching license.

Verify License
^^^^^^^^^^^^^^

Use this control to verify that the configured license is valid before or after
you save.

If a newly issued file reports that it is not active yet, wait until the
activation time shown by the client and then verify it again.
