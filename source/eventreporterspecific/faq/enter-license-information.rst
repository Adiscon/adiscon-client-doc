.. _eventreporter-enter-license-information:

How Do I Enter EventReporter License Information?
=================================================

Answer
------

On **EventReporter version 26** and later, apply the ``license.alic`` file
through **General** -> **License** -> **License File** in the configuration
client, save, and restart the service.

Details
-------

EventReporter version 26 requires a ``license.alic`` file from Adiscon.

Default file location:

``%ProgramData%\\Adiscon\\EventReporter\\license.alic``

For Event Log Monitor deployments, licensing is based on the source systems
whose Windows Event Logs are collected or forwarded. See your edition
comparison for product limits.

Action path
-----------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the EventReporter Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab and apply ``license.alic``.
5. Save the configuration and restart the EventReporter service.

Related information
-------------------

* :ref:`version-numbering-2026`
* :doc:`../installation`
* :doc:`../editioncomparison`
* :doc:`../../shared/sales/how-to-contact-sales`
