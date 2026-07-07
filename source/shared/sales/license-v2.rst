.. _license-v2:

License V2 (2026 and later)
===========================

Starting with the **2026** calendar-year major release, Adiscon products use
**License V2**: a cryptographically signed license file instead of a
registration name plus five numeric keys.

This page is the canonical reference for License V2 in the documentation set.
Product-specific steps are in each manual's license FAQ; the customer-facing
upgrade story is on each product website's 2026 major-release article.

Who needs License V2
--------------------

- **2026 and later majors** require a valid ``license.alic`` file. Legacy
  registration name and numeric key fields do **not** authorize these builds.
- **Pre-2026 majors** do **not** accept ``license.alic`` files. If you must
  stay on a legacy major, contact Adiscon support or sales for a manually issued
  legacy license (registration name and keys). There is no self-service
  conversion from License V2 back to legacy keys.

License file basics
-------------------

**File name:** ``license.alic``

**Format:** A single-line signed token issued by Adiscon. Do not edit the file
by hand.

**Configuration field:** ``szLicenseV2Path`` — path to the license file only,
not inline license text.

**Default locations** (when ``szLicenseV2Path`` is empty):

- **WinSyslog** — ``%ProgramData%\\Adiscon\\WinSyslog\\license.alic``
- **EventReporter** — ``%ProgramData%\\Adiscon\\EventReporter\\license.alic``
- **MonitorWare Agent** — ``%ProgramData%\\Adiscon\\MonitorWare\\license.alic``
- **rsyslog Windows Agent** — ``%ProgramData%\\Adiscon\\RSyslogAgent\\license.alic``

You may place the file elsewhere and set ``szLicenseV2Path`` to that location.

Configuration client
--------------------

In the configuration client, open **General** → **License**.

**License File tab (2026+):**

- Browse for ``license.alic``, drag-and-drop the file, or paste a file path.
- Verify and deploy the license when you save the configuration.
- The status bar shows license status (for example, licensed organization name).

**Legacy License tab:**

- Retained for reference and for deployments still on pre-2026 majors.
- On 2026+ service builds, legacy key fields are **not** used for authorization.

Major-version binding
---------------------

A license lists the calendar years it authorizes (for example, 2026). A build
from a year that is not covered by your license file is rejected or shows a
major-version mismatch warning until you deploy a matching license.

Evaluation and trial
--------------------

When no valid ``license.alic`` is present, the product may enter a time-limited
evaluation mode. Cryptographically invalid or rejected license files do **not**
qualify for that fallback.

For evaluation or licensing questions, contact Adiscon support or sales. This
documentation does not specify internal trial durations or countdown behavior.

Feature entitlements
--------------------

On 2026+ builds, configured services and actions must match the entitlements
in your license file. If a feature is not licensed, the service may refuse to
run that configuration until you adjust the setup or obtain an updated license.

Migrating to 2026
-----------------

1. Request a 2026 ``license.alic`` from Adiscon for your product and edition.
2. Place the file at the default path or set ``szLicenseV2Path``.
3. Install or upgrade to the 2026 major service build.
4. Open the configuration client, verify license status on the **License File**
   tab, and save the configuration.
5. Restart the service.

Migrating or staying on a legacy major
--------------------------------------

``license.alic`` files **do not work** on pre-2026 product versions. Contact
Adiscon support or sales if you need a legacy registration name and numeric
keys for an older major.

File-based configuration example
--------------------------------

.. code-block:: text

   general(name="License") {
    $szLicenseV2Path C:\\ProgramData\\Adiscon\\WinSyslog\\license.alic
   }

Adjust the path for your product and deployment layout.

Offline validation
------------------

License V2 is validated **offline** using keys embedded in the product. Normal
operation does not require internet activation.

Related information
-------------------

- :doc:`perpetual-license-and-upgradeinsurance`
- :doc:`air-gapped-environments`
- :doc:`../references/version-numbering-2026`
