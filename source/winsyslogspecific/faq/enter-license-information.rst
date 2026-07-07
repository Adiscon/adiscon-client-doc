.. _winsyslog-enter-license-information:

How Do I Enter WinSyslog License Information?
=============================================

Answer
------

On **WinSyslog version 26** and later, apply the ``license.alic`` file through
**General** → **License** → **License File** in the configuration client, save,
and restart the service. On **pre-26** versions, use **Legacy License** with
the registration name and numeric keys from Adiscon.

Details
-------

**Version 26 and later (license file)**

WinSyslog version 26 requires a ``license.alic`` file from Adiscon. Legacy
registration name and numeric keys from WinSyslog 18.x do **not** authorize
version 26.

Default file location:

``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``

You can set ``szLicenseV2Path`` to another path. See
:ref:`licensing-version-26-and-later` for license file details and troubleshooting.

**Pre-26 versions (legacy keys)**

``license.alic`` files **do not work** on WinSyslog 18.x and earlier. If you
must stay on an older version, contact Adiscon support or sales for a legacy
license key. Current licenses can cover older versions, but older builds need
the legacy key format.

Action Path (version 26+)
-------------------------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the WinSyslog Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab.
5. Browse for ``license.alic``, or drag-and-drop the file, or paste the file path.
6. Save the configuration and verify license status in the client.
7. Restart the WinSyslog service.

Action Path (legacy versions)
-----------------------------

1. Open the WinSyslog Configuration Client.
2. Expand **General** and select **License**.
3. Open the **Legacy License** tab.
4. Enter the registration name exactly as provided.
5. Import the license key blocks or use **Import from Clipboard**.
6. Save the configuration and restart the service.

Verification
------------

After the service restart, reopen the license page and confirm that license
status is shown without validation errors.

Related Information
-------------------

* :ref:`licensing-version-26-and-later`
* :ref:`version-numbering-2026`
* :doc:`what-is-freeware-mode`
* :doc:`../installation`
* :doc:`../../shared/sales/how-to-contact-sales`
