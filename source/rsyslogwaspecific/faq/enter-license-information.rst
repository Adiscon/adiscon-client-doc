.. _rsyslogwa-enter-license-information:

How Do I Enter rsyslog Windows Agent License Information?
=========================================================

Answer
------

On **rsyslog Windows Agent version 26** and later, apply the ``license.alic`` file
through **General** → **License** → **License File** in the configuration
client, save, and restart the service. On **pre-26** versions, use **Legacy
License** with the registration name and numeric keys from Adiscon.

Details
-------

**Version 26 and later (license file)**

rsyslog Windows Agent version 26 requires a ``license.alic`` file from
Adiscon. Legacy keys from rsyslog Windows Agent 8.x do **not** authorize the
version 26 release line.

Default file location:

``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

See :ref:`licensing-version-26-and-later` for license file details and
troubleshooting.

**Pre-26 versions (legacy keys)**

``license.alic`` files **do not work** on rsyslog Windows Agent 8.x and
earlier. Contact Adiscon support or sales for a legacy license key if you must
remain on an older version. Current licenses can cover older versions, but older
builds need the legacy key format.

Action path (version 26+)
-------------------------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the rsyslog Windows Agent Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab and apply ``license.alic``.
5. Save the configuration and restart the service.

Action path (legacy versions)
-----------------------------

1. Open the rsyslog Windows Agent Configuration Client.
2. Expand **General** and select **License**.
3. Open the **Legacy License** tab.
4. Enter the registration name and import the license key.
5. Save the configuration and restart the service.

Related information
-------------------

* :ref:`licensing-version-26-and-later`
* :ref:`version-numbering-2026`
* :doc:`../installation`
* :doc:`../../shared/sales/how-to-contact-sales`
