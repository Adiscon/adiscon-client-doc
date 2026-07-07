.. _rsyslogwa-enter-license-information:

How Do I Enter rsyslog Windows Agent License Information?
=========================================================

Answer
------

On **rsyslog Windows Agent version 26** and later, apply the ``license.alic``
file through **General** -> **License** -> **License File** in the
configuration client, save, and restart the service.

Details
-------

rsyslog Windows Agent version 26 requires a ``license.alic`` file from Adiscon.

Default file location:

``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

See :ref:`licensing-version-26-and-later` for license file details and
troubleshooting.

Action path
-----------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the rsyslog Windows Agent Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab and apply ``license.alic``.
5. Save the configuration and restart the service.

Related information
-------------------

* :ref:`licensing-version-26-and-later`
* :ref:`version-numbering-2026`
* :doc:`../installation`
* :doc:`../../shared/sales/how-to-contact-sales`
