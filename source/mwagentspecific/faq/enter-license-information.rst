.. _mwagent-enter-license-information:

How Do I Enter MonitorWare Agent License Information?
=====================================================

Answer
------

Apply the ``license.alic`` file through **General** -> **License** ->
**License File** in the configuration client, save, and restart the service.

Details
-------

Current MonitorWare Agent builds require a ``license.alic`` file from Adiscon.

Default file location:

``%ProgramData%\\Adiscon\\MonitorWare\\license.alic``

Use the default location unless Adiscon support or your deployment process
requires another path.

Action path
-----------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the MonitorWare Agent Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab and apply ``license.alic``.
5. Save the configuration and restart the MonitorWare Agent service.

Related information
-------------------

* `MonitorWare Agent edition comparison <https://www.mwagent.com/product-info/edition-comparison/>`_
* :doc:`../../shared/sales/how-to-contact-sales`
