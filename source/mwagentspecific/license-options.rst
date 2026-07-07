

License
=======

Licensing options are on **General** → **License** in the configuration client.
From the 2026 major onward, MonitorWare Agent uses **License V2** (a signed
``license.alic`` file). See :ref:`license-v2` for the canonical reference.

License File (2026 and later)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the **License File** tab to deploy ``license.alic``.

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
  Optional path to the License V2 file. When empty, the service uses the
  default location:

  .. only:: mwagent

     ``%ProgramData%\\Adiscon\\MonitorWare\\license.alic``

  .. only:: winsyslog or winsyslog_j

     ``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``

  .. only:: eventreporter

     ``%ProgramData%\\Adiscon\\EventReporter\\license.alic``

  .. only:: rsyslog

     ``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

  You can browse for the file, drag-and-drop it onto the client, or paste a
  file path. The license is validated and deployed when you save the
  configuration.

  The main window status bar shows license status (for example, the licensed
  organization). A major-version mismatch between the license file and the
  installed service may show a warning banner until you deploy a matching
  license.

Legacy License (pre-2026 majors)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Legacy License** tab retains the registration name and numeric key fields
for deployments on pre-2026 majors. On 2026+ service builds, these fields are
**not** used for authorization.

.. only:: mwagent

   .. image:: ../images/license-legacy-tab.png
      :width: 100%

.. only:: winsyslog or winsyslog_j

   .. image:: ../images/license-legacy-tab-winsyslog.png
      :width: 100%

.. only:: eventreporter or rsyslog

   .. image:: ../images/license-legacy-tab-shared.png
      :width: 100%

``license.alic`` files do **not** work on pre-2026 product versions. Contact
Adiscon if you need a legacy license for an older major.

Registration Name
^^^^^^^^^^^^^^^^^

**File Configuration field:**
  szlicense

**Description**
  The user chooses the registration name. It should correspond to your
  organization name, e.g. a company called "AA Carpenters, Inc." should not
  choose "AA" as registration name. This can easily be mistaken and most
  probably be rejected by Adiscon for that reason. With the above scenario,
  we recommend using the full company name "AA Carpenters, Inc.".

  Please note: The registration name is case sensitive. It must be entered
  exactly as given. Leading and trailing spaces are also part of the
  registration name, so be sure to enter none.


Registration number
^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  nLicenseKey1, nLicenseKey2, nLicenseKey3, nLicenseKey4, nLicenseKey5

**Description**
  Adiscon provides this number. It is valid for a specific registration name.
  Be sure to enter the correct registration number. Each block of the license
  key must be filled into one of the key fields. Alternatively, you can use
  the "Import from Clipboard" button. The client detects invalid registration
  numbers and reports the corresponding error.


Import from Clipboard
^^^^^^^^^^^^^^^^^^^^^

If the key has been copied to the clipboard it can be imported with this button.


Verify License
^^^^^^^^^^^^^^

Use this control to verify that the configured license is valid before or after
you save.
