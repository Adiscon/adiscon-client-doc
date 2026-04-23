.. _repeatable-deployment:

Information for Repeatable Deployment
=====================================

A repeatable deployment in this context means deploying an Adiscon client (for
example MonitorWare Agent, EventReporter, or WinSyslog) to multiple systems by
reusing one validated reference configuration. The goal is to build and verify
the package once, then apply the same software and settings consistently across
each target machine. This method is useful whenever you need more than a
one-off manual install, including small pilot groups and broader staged
deployments.

For guidance on differentiating between initial and update deployments, see the
MWAgent FAQ section.

Preparing the Reference Configuration
-------------------------------------

#. Install the product on a single reference system and configure it exactly as
   desired. Verify that the configuration works before continuing.
#. Export the configuration to a :doc:`registry file
   <../../glossaryofterms/registry-file>` via the configuration client
   (``Computer`` → ``Export Settings``).
#. Gather the files required for an engine-only installation:

   * For MonitorWare Agent 8.1 and newer this is typically ``mwagent.exe`` and
     ``mwagent.pem``.
   * Older releases may also require the Visual C++ runtime and OpenSSL helper
     files (``Microsoft.VC90.CRT.manifest``, ``libeay32.dll``, ``ssleay32.dll``,
     ``msvcm90.dll``, ``msvcp90.dll``, ``msvcr90.dll``).

Repeatable Deployment Example
-----------------------------

Once the reference system is prepared, copy the required files to a network
share or removable media and automate the deployment with a script similar to
the following:

.. code-block:: bat

   copy \\server\share\mwagent.exe C:\some-local-dir
   copy \\server\share\mwagent.pem C:\some-local-dir
   cd C:\some-local-dir
   mwagent -i
   regedit /s \\server\share\configParams.reg
   net start "AdisconMonitorWareAgent"

``configParams.reg`` represents the registry export taken from the reference
system. Because this deployment ships only the engine files, the approach works
well for DMZ environments where RPC or file sharing cannot be opened.

.. note::

   ``mwagent -i`` (or the equivalent command-line switch for other Adiscon
   products) only registers the Windows service. It assumes the binaries already
   exist in the current directory, so copy the files before running the command.

Branch Office Deployments
-------------------------

For branch offices or semi-automated deployments, distribute the prepared
package and have the local administrator perform the following steps:

#. Create a directory on the target computer and copy the provided files into
   it.
#. Run ``mwagent -i`` from that directory to register the service.
#. Import the exported configuration by double-clicking the ``.reg`` file (or by
   running ``regedit /s`` from an elevated command prompt).
#. Start the Windows service via ``net start`` or the Services management
   console. Restarting the entire machine is not required.

.. important::

   The directory that hosts the engine files **is** the installation directory.
   Deleting it removes the binaries and effectively uninstalls the product.

Updating Existing Deployments
-----------------------------

To upgrade an engine-only installation, update the reference system first, export
the revised configuration, and distribute the refreshed files using the same
process. Uninstallation is unnecessary as long as you overwrite the files in
place, but always stop the Windows service before copying the new binaries. For
a walkthrough focused on update scenarios, refer to the MWAgent FAQ section.
