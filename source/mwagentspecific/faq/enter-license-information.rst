.. _mwagent-enter-license-information:

How Do I Enter MonitorWare Agent License Information?
=====================================================

Answer
------

On **MonitorWare Agent 2026** and later, deploy the ``license.alic`` file
through **General** → **License** → **License File** in the configuration
client, save, and restart the service. On **pre-2026** majors, use **Legacy
License** with the registration name and numeric keys from Adiscon.

Details
-------

**2026 and later (License V2)**

MonitorWare Agent 2026 requires a signed ``license.alic`` file from Adiscon.
Legacy keys from MonitorWare Agent 15.x do **not** authorize the 2026 major.

Default file location:

``%ProgramData%\\Adiscon\\MonitorWare\\license.alic``

See :ref:`license-v2` for the full reference.

**Pre-2026 majors (legacy keys)**

``license.alic`` files **do not work** on MonitorWare Agent 15.x and earlier.
Contact Adiscon support or sales for a manually issued legacy license if you
must remain on a legacy major.

Action path (2026+)
--------------------

1. Obtain ``license.alic`` from Adiscon for your edition.
2. Open the MonitorWare Agent Configuration Client.
3. Expand **General** and select **License**.
4. Open the **License File** tab and deploy ``license.alic``.
5. Save the configuration and restart the MonitorWare Agent service.

Action path (legacy majors)
-----------------------------

1. Open the MonitorWare Agent Configuration Client.
2. Expand **General** and select **License**.
3. Open the **Legacy License** tab.
4. Enter the registration name and import the license key.
5. Save the configuration and restart the service.

Related information
-------------------

* :ref:`license-v2`
* :ref:`version-numbering-2026`
* `MonitorWare Agent edition comparison <https://www.mwagent.com/product-info/edition-comparison/>`_
* :doc:`../../shared/sales/how-to-contact-sales`
