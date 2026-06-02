:orphan:

.. _faq-dotnet-framework-vs-dotnet-core-and-dotnet:

Do the configuration clients require .NET Framework, or is .NET Core or .NET 5+ enough?
==========================================================================================

Question
--------

Can the Windows configuration clients run with only the newer .NET runtime
installed, such as .NET Core, .NET 8, or .NET 10?

Answer
------

No. The Windows configuration clients require **Microsoft .NET Framework
4.7.2 or a newer .NET Framework 4.x release**.

``.NET Framework 4.x`` is a Windows-only runtime family. ``.NET Core`` and
``.NET 5+`` are a different cross-platform runtime family.

``.NET 5+`` continues the ``.NET Core`` line under a new name. It is not a
newer version of ``.NET Framework 4.x``.

Installing only ``.NET Core`` or ``.NET 5+`` does not satisfy a
``.NET Framework`` requirement.

Details
-------

For these products, the requirement applies to the **Windows configuration
client**. The background service is a separate component.

If you deploy only the background service on a target system, the
Configuration Client is not required on that system. In that case, this
``.NET Framework`` requirement applies where the Configuration Client is
installed and used, not to the service-only target.

The following satisfy this requirement:

- ``.NET Framework 4.7.2``
- ``.NET Framework 4.8``
- ``.NET Framework 4.8.1``

The following do not satisfy this requirement on their own:

- ``.NET Core 3.x``
- ``.NET 5``
- ``.NET 6``
- ``.NET 8``
- ``.NET 10``

Action path
-----------

1. Check whether the system has ``.NET Framework 4.7.2`` or a newer
   ``.NET Framework 4.x`` release installed.
2. If it is missing, install ``.NET Framework`` separately or allow the
   product installer to add the required Framework components.
3. If the system only has ``.NET Core`` or ``.NET 5+``, do not assume that
   the configuration client can run.

Related information
-------------------

- Microsoft documentation on .NET Framework versions and dependencies:
  https://learn.microsoft.com/en-us/dotnet/framework/install/versions-and-dependencies
- Microsoft documentation on installing .NET on Windows:
  https://learn.microsoft.com/en-us/dotnet/core/install/windows
