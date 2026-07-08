.. _rsyslogwa-enter-license-information:

How Do I Enter rsyslog Windows Agent License Information?
=========================================================

Answer
------

Apply the ``license.alic`` file through **General** -> **License** in the
configuration client, save, and restart the service.

Details
-------

Current rsyslog Windows Agent builds require a ``license.alic`` file from
Adiscon.

Default file location:

``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

Use the default location unless Adiscon support or your deployment process
requires another path.

Action path
-----------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the rsyslog Windows Agent Configuration Client.
3. Expand **General** and select **License**.
4. Browse for ``license.alic``, drag-and-drop the file, or paste the file path.
5. Save the configuration and restart the service.

Related information
-------------------

* :doc:`../installation`
* :doc:`../../shared/sales/how-to-contact-sales`
