.. _licensing-version-26-and-later:

Licensing in version 26 and later
=================================

Question
--------

How does licensing work in Adiscon products from version 26 onward?

Answer
------

Starting with version 26, Adiscon provides a ``license.alic`` license file.
Apply this file through the configuration client's **License File** tab, save
the configuration, and verify the license status.

Details
-------

The file-based format is an operational licensing format, not a separate
product feature. Users normally only need to know where to place the license
file, how to apply it, and what to check if the product cannot read it.

**License file name:**
  ``license.alic``

**License file content:**
  A file containing the license details issued by Adiscon. Do not edit the file
  by hand.

**Configuration field:**
  ``szLicenseV2Path`` is the optional path to the license file. It expects a
  file path, not inline license text.

**Default locations** when ``szLicenseV2Path`` is empty:

- **WinSyslog**: ``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``
- **EventReporter**: ``%ProgramData%\\Adiscon\\EventReporter\\license.alic``
- **MonitorWare Agent**: ``%ProgramData%\\Adiscon\\MonitorWare\\license.alic``
- **rsyslog Windows Agent**:
  ``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

How to apply the license file
-----------------------------

1. Obtain ``license.alic`` from Adiscon for your product and edition.
2. Open the product's configuration client.
3. Open **General** -> **License** -> **License File**.
4. Browse for ``license.alic``, drag and drop the file, or paste the file path.
5. Save the configuration so the client applies the license file.
6. Restart the service if the product does not pick up the updated license
   automatically.
7. Reopen the license page or check the main window status bar and confirm that
   the license status is valid.

FAQ: Can I use an older product version?
----------------------------------------

Yes. Your license entitlement can cover older product versions. If the older
product version does not accept ``license.alic`` files, contact Adiscon support
or sales and request a free license key for that product version.

Troubleshooting license file problems
-------------------------------------

If the product does not accept the license file, check these items first:

- The file exists at the configured path or at the product's default location.
- The Windows service account can read the file and its parent directory.
- ``szLicenseV2Path`` points to the file itself, not only to a directory.
- The file was copied without changing its content or line endings.
- The file belongs to the correct product, edition, and product version.
- The installed service build and configuration client are from the expected
  product line.

Typical symptoms include file-not-found errors, permission errors, invalid or
broken file format messages, and version mismatch warnings. If these checks do
not explain the problem, contact Adiscon support and include the product name,
product version, configured license path, and the exact error message.

File-based configuration example
--------------------------------

.. code-block:: text

   general(name="License") {
    $szLicenseV2Path C:\\ProgramData\\Adiscon\\WinSyslog\\license.alic
   }

Adjust the path for your product and deployment layout.

Offline validation
------------------

Normal license checks do not require internet access.

Related information
-------------------

- :doc:`perpetual-license-and-upgradeinsurance`
- :doc:`air-gapped-environments`
- :doc:`../references/version-numbering-2026`
