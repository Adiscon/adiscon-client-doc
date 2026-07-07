:orphan:

.. _version-numbering-2026:

Version numbering from 2026
===========================

Adiscon products on the **2026** calendar-year major use a new version scheme
and monthly release cadence.

Version format
--------------

Customer-visible versions use four components:

``YEAR.MONTH.0.BUILD``

- **YEAR** — calendar year of the build (major version), for example ``2026``
- **MONTH** — calendar month of the release (minor version), always two digits
  zero-padded, for example ``07`` for July
- **Third component** — always ``0`` (reserved)
- **BUILD** — incrementing build number per release

The About dialog may insert spaces after dots (for example ``2026. 07. 0. 785``).

Service and configuration client builds from the same release month share the
same ``YEAR.MONTH`` line (for example **2026.07**).

Release cadence
---------------

- One **major** per calendar year (2026, 2027, …)
- **Minor** bumps with each calendar month within that year
- Regular monthly builds with fixes and improvements

The first general-availability minor for the 2026 announcement is **2026.07**.

Legacy major mapping
--------------------

**Last sequential majors** before the 2026 calendar-year line:

- **WinSyslog** — 18.x
- **EventReporter** — 19.x
- **MonitorWare Agent** — 15.x
- **rsyslog Windows Agent** — 8.x

Upgrading from any of these majors to **2026** requires a new License V2 file.
See :ref:`license-v2`.

2026 major release notes
------------------------

Each product website publishes upgrade guidance and release notes for the
2026 major. Use those pages for the customer-facing upgrade story; use this
manual for configuration and technical reference.

- `WinSyslog version history <https://www.winsyslog.com/version-history/>`__
- `MonitorWare Agent version history <https://www.mwagent.com/version-history/>`__
- `EventReporter version history <https://www.eventreporter.com/version-history/>`__
- `rsyslog Windows Agent version history <https://www.rsyslog.com/windows-agent/about-rsyslog-windows-agent/>`__

Monthly build details are listed on each product's version-history page.
