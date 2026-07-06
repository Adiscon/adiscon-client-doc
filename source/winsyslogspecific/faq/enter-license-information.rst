.. _winsyslog-enter-license-information:

How Do I Enter WinSyslog License Information?
=============================================

Answer
------

On **WinSyslog 2026** and later, deploy the ``license.alic`` file through
**General** → **License** → **License File** in the configuration client, save,
and restart the service. On **pre-2026** majors, use **Legacy License** with
the registration name and numeric keys from Adiscon.

Details
-------

**2026 and later (License V2)**

WinSyslog 2026 requires a signed ``license.alic`` file from Adiscon. Legacy
registration name and numeric keys from WinSyslog 18.x do **not** authorize
the 2026 major.

Default file location:

``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``

You can set ``szLicenseV2Path`` to another path. See :ref:`license-v2` for the
full reference.

**Pre-2026 majors (legacy keys)**

``license.alic`` files **do not work** on WinSyslog 18.x and earlier. If you
must stay on a legacy major, contact Adiscon support or sales for a manually
issued legacy license.

Action Path (2026+)
--------------------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the WinSyslog Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab.
5. Browse for ``license.alic``, or drag-and-drop the file, or paste the file path.
6. Save the configuration and verify license status in the client.
7. Restart the WinSyslog service.

Action Path (legacy majors)
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

* :ref:`license-v2`
* :ref:`version-numbering-2026`
* :doc:`what-is-freeware-mode`
* :doc:`../installation`
* :doc:`../../shared/sales/how-to-contact-sales`
