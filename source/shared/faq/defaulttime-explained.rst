:orphan:

.. _shared-defaulttime-explained:

How Do Default Time Values Work?
================================

Answer
------

The **Default Timevalues are based on** setting controls whether generated time
values use UTC or local time in places where the product formats or interprets
time-dependent output.

Details
-------

This setting affects multiple areas, including:

- email header dates
- time parameters passed to Start Program actions
- time properties used in file names
- filter results when weekday or time-based conditions are evaluated

UTC is the safer default for consistent cross-system processing. Local time can
be more convenient when output is primarily reviewed by administrators in one
time zone.

Action path
-----------

1. Open **General** -> **General Options**.
2. Locate **Default Timevalues are based on**.
3. Choose `UTC` or `Localtime` according to your operational need.
4. Save and apply the configuration.
