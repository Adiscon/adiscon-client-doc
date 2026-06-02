.. index:: System Requirements

System Requirements
===================

The actual requirements depend on whether you install only the background
service or the full product including the Configuration Client.

Supported Windows platforms
---------------------------

Current rsyslog Windows Agent releases are intended for modern Windows
versions, including Windows 10, Windows 11, Windows Server 2016, Windows Server
2019, Windows Server 2022, Windows Server 2025, and newer compatible releases.

Client
------

- The Configuration Client supports both 32-bit and 64-bit Windows
  environments.
- The Configuration Client requires Microsoft .NET Framework 4.7.2 or a newer
  .NET Framework 4.x release, such as .NET Framework 4.8 or 4.8.1.
- .NET Framework 4.x and .NET Core / .NET 5+ are different runtime families,
  so .NET Core and .NET 5+ do not satisfy this requirement.
- The installer can add the required .NET Framework components if they are not
  yet present.
- The client itself requires only modest memory and disk space beyond normal
  Windows requirements.

This requirement applies to systems where the Configuration Client is
installed. An engine-only target does not require the Configuration Client.

Service
-------

- The service has lower overhead than the full UI installation.
- Runtime requirements depend mostly on which services are enabled and how much
  data the system processes.
- Forwarding large event volumes, using reliable queues, or buffering temporary
  outages requires more memory and disk than a basic event-forwarding setup.
- If the agent only monitors local Windows Event Logs and forwards selected
  events, system impact is typically low.

Sizing guidance
---------------

Resource needs vary with:

- event volume
- number of enabled services
- filter complexity
- forwarding protocol and queue settings
- outage tolerance and disk queue sizing

If you expect sustained high event volume or long queue retention windows,
allocate additional memory and disk space on the monitored system.
