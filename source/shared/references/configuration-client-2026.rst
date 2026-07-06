:orphan:

.. _configuration-client-2026:

Configuration client (2026 release line)
========================================

The **2026.07** installer ships two configuration clients:

- **Established configuration client** — the WinForms client documented in this
  manual (primary reference for setup steps and screenshots).
- **Next-generation Configuration Client Preview** — a WinUI-based workbench
  (``adiscon-client-ng``), shipped as a **preview** alongside the classic client.

The preview is optional. The classic client supports License V2 deployment and
full configuration editing for the 2026 major. See your product website's 2026
major-release **Upgrade** article for the customer-facing preview description.

Service toolbar
---------------

The main window toolbar provides service control:

- **Start**, **Stop**, and **Restart** with clearer status text when an action
  is unavailable (for example, during configuration reload).
- **Kill** — ends an orphan service process when the service manager state is
  inconsistent.
- **Open Windows Services** — opens ``services.msc`` for Windows Service
  management.

When the service is **paused** during configuration reload, stop and restart
may be disabled until reload completes.

Reset to default
----------------

The context menu and toolbar provide **Reset** on a selected service or action
to restore that item's settings to factory defaults. This is separate from
**Reset Changes** on an open property form, which discards unsaved edits only.

Event Viewer
------------

After start, stop, or configuration reload, service-management events are
prepended in the Event Viewer so recent control actions appear at the top.

File formats
------------

The **File** menu supports:

- **Adiscon YAML Config Format** (``.yaml``) — import and export
- **Adiscon Legacy Format** (``.cfg``) — legacy text configuration

See the file-based configuration chapter in your product manual and
:ref:`unsupported-configuration-blocks`.

Related information
-------------------

- :ref:`license-v2`
- :ref:`version-numbering-2026`
