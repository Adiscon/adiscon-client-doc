:orphan:

.. _version-numbering-2026:

Version numbering from version 26
=================================

Adiscon products use calendar-based version numbers starting with version 26.
In ``26.07``, ``26`` means the calendar year 2026 and ``07`` means July.

Version format
--------------

Customer-visible versions use four components:

``YY.MM.0.BUILD``

- **YY**: two-digit calendar year, for example ``26`` for 2026
- **MM**: calendar month, always two digits, for example ``07`` for July
- **Third component**: always ``0`` (reserved)
- **BUILD**: incrementing build number per release

The About dialog may insert spaces after dots, for example
``26. 07. 0. 785``.

Service and configuration client builds from the same release month share the
same ``YY.MM`` line, for example **26.07**.

Release cadence
---------------

Adiscon publishes regular monthly builds with fixes and improvements. The
first general-availability release in the version 26 line is **26.07**.

Earlier version mapping
-----------------------

The last product versions before the version 26 line are:

- **WinSyslog**: 18.x
- **EventReporter**: 19.x
- **MonitorWare Agent**: 15.x
- **rsyslog Windows Agent**: 8.x

Version 26 and later uses a ``license.alic`` file. See
:ref:`licensing-version-26-and-later`.

Version 26 release notes
------------------------

Each product website publishes upgrade guidance and release notes for version
26. Use those pages for the customer-facing upgrade story; use this manual for
configuration and technical reference.

- `WinSyslog version history <https://www.winsyslog.com/version-history/>`__
- `MonitorWare Agent version history <https://www.mwagent.com/version-history/>`__
- `EventReporter version history <https://www.eventreporter.com/version-history/>`__
- `rsyslog Windows Agent version history <https://www.rsyslog.com/windows-agent/about-rsyslog-windows-agent/>`__

Monthly build details are listed on each product's version-history page.
