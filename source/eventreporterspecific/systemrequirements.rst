.. index:: System Requirements

System Requirements
===================

EventReporter is designed to run on current Windows client and server systems
with modest resource requirements.

Supported operating systems
---------------------------

The current product is intended for:

- Windows 10
- Windows 11
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows Server 2025
- newer compatible Windows releases

Do not assume that older end-of-life Windows versions are supported by current
EventReporter releases. If you need documentation for legacy platforms, use the
manual that matches the older product release.

Client requirements
-------------------

The EventReporter Configuration Client:

- runs on supported 32-bit and 64-bit Windows environments where the current
  product is supported
- uses Microsoft .NET components that the installer can add if required
- needs only modest disk space and memory for normal administration tasks

Service requirements
--------------------

The EventReporter service:

- runs as a Windows service in the background
- uses comparatively little memory and disk space in its base state
- consumes additional resources depending on queue size, action types, and
  event volume

Operational notes
-----------------

- Database logging performance depends more on the database and DSN setup than
  on the EventReporter core service.
- Large queues, heavy filtering, or verbose debug logging will increase
  resource use.
- Additional Windows event channels available on server editions can also be
  monitored when the operating system exposes them.
