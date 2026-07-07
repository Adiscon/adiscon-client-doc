.. _winsyslog-enter-license-information:

How Do I Enter WinSyslog License Information?
=============================================

Answer
------

Apply the ``license.alic`` file through **General** -> **License** ->
**License File** in the configuration client, save, and restart the service.

Details
-------

Current WinSyslog builds require a ``license.alic`` file from Adiscon.

Default file location:

``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``

You can set ``szLicenseV2Path`` to another path if you do not use the default
location.

Action path
-----------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the WinSyslog Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab.
5. Browse for ``license.alic``, or drag-and-drop the file, or paste the file path.
6. Save the configuration and verify license status in the client.
7. Restart the WinSyslog service.

Verification
------------

After the service restart, reopen the license page and confirm that license
status is shown without validation errors.

Related information
-------------------

* :doc:`what-is-freeware-mode`
* :doc:`../installation`
* :doc:`../../shared/sales/how-to-contact-sales`
