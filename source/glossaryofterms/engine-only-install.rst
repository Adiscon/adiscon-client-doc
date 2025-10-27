.. index:: engine only install

:orphan:

Engine Only Install
===================

An **Engine Only Install** refers to a deployment method where only the core
service executable (e.g., ``winsyslg.exe``, ``mwagent.exe``, ``evtlog.exe``)
and its essential dependencies are installed, without the full client application
and user interface components. This type of installation is particularly useful for:

* **Mass deployments** where you want to minimize the installation footprint
* **Server environments** where GUI components are not needed
* **Automated deployments** where configuration is managed via registry files
* **Security-conscious environments** where you want to reduce the attack surface

In an engine-only install, the service runs with the configuration stored in the
Windows Registry, which can be exported from a master installation and imported
during deployment. This allows for consistent configuration across multiple systems
without requiring the full installation package.

Key characteristics:
- Smaller disk footprint (typically just a few MB)
- No GUI components or client tools
- Configuration via registry import/export
- Suitable for headless/server deployments
- Can be updated by simply replacing the executable files

This approach is commonly used in enterprise environments where hundreds or
thousands of systems need to be monitored with consistent configuration.
