.. _default-timevalues-explained-winsyslog:


Default Timevalues Setting in WinSyslog Explained
==================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-02-12
   :updated: 2026-02-12
   :products: WinSyslog

Overview
--------

This FAQ explains the Default Timevalues setting in WinSyslog and how it
affects time handling throughout the system.

What is the Default Timevalues Setting?
----------------------------------------

The General Options in WinSyslog contain a setting for "Default Timevalues".
This setting controls how timestamps are handled throughout the system.

Default Timevalues Options
---------------------------

You can set Default Timevalues to:

* **UTC (Universal Coordinated Time):** The default setting. All internal
  time calculations use UTC.
* **Localtime:** Uses the local time zone for certain output operations.

Why UTC is Used Internally
---------------------------

**Important:** Even when you select "Localtime", WinSyslog still calculates
internally with UTC time. This is necessary to:

* Maintain time accuracy when messages are sent via Syslog or SETP protocols
* Prevent unexpected time differences across time zones
* Ensure consistent timestamp handling in database operations
* Support reliable message forwarding between systems

Where Localtime Setting Has Effect
-----------------------------------

When Default Timevalues is set to "Localtime", it affects the following
operations:

+--------------------------+--------------------------------------------------+
| Action                   | Effect                                           |
+==========================+==================================================+
| Send Email Action        | Date in the email header uses localtime          |
+--------------------------+--------------------------------------------------+
| Start Program Action     | Time parameters in command line use localtime    |
+--------------------------+--------------------------------------------------+
| Write File Action        | Time properties in file names use localtime      |
+--------------------------+--------------------------------------------------+
| Filter Engine            | Filtering by weekday or time fields uses         |
|                          | localtime                                        |
+--------------------------+--------------------------------------------------+

Getting Localtime Output
-------------------------

For actions where you need localtime output in custom formats, you can use
property options:

Property Option: localtime
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts the output of any timestamp into localtime:

.. code-block:: text

   %timegenerated:::localtime%

This will display the time in the local time zone.

Property Option: uxLocalTimeStamp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same output as uxTimeStamp, but uses localtime instead of UTC:

.. code-block:: text

   %timereported:::uxLocalTimeStamp%

This generates a UNIX-style timestamp based on local time.

Examples
--------

**Using UTC timestamps (default):**

.. code-block:: text

   %timegenerated%
   %timereported:::uxTimeStamp%

**Using localtime timestamps:**

.. code-block:: text

   %timegenerated:::localtime%
   %timereported:::uxLocalTimeStamp%

Best Practices
--------------

* **Keep UTC as default:** For most scenarios, UTC is recommended for
  consistency
* **Use localtime option:** Apply the localtime property option only where
  needed
* **Database storage:** Store timestamps in UTC for accurate querying
  across time zones
* **Display purposes:** Convert to localtime when displaying to users
* **Log rotation:** Use localtime for file naming if you want daily
  rotations based on local business hours

Additional Notes
----------------

* The Default Timevalues setting affects defaults only - individual actions
  can override this
* UTC-based calculations ensure messages maintain accurate timestamps when
  forwarded
* Consider your environment's time zone distribution when choosing the
  default
* Most enterprise deployments prefer UTC for global consistency
