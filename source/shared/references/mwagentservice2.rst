.. index:: The MonitorWare Agent Service 2.x

The MonitorWare Agent Service 2.x
=================================

The service operates in the background while your computer is running. The
MonitorWare Agent 2.x (i.e. MonitorWare Agent 2.0, 2.1,...) is installed as a
system service during setup. It typically runs on each machine being monitored.
However, some machines can also be dedicated to run it for housekeeping
functions (for example log consolidation).

The MonitorWare Agent can be :doc:`engine only <../gettingstarted/informationforamassrollout>`. In this case, only the
service is installed onto a machine. It can be customized either by directly
editing the registry or by copying a registry snapshot from a machine with
installed client. Please note that "Engine Only" installs need a full
MonitorWare Agent license.

The MonitorWare Agent service 2.x program is called "mwagent.exe". It is the
sole executable that needs to be distributed for mass rollouts.

**The Service Account** - NT Services must utilize an NT logon account in order to

perform their intended tasks. The MonitorWare Agent service is no different.
The account initially used by the service is "local system". We recommend
retaining this setting.

If for any reason you would like to change the service account, you can do so
via the control panel "services" applet (or the "Computer Management" MMC under
modern Windows). However, you need to make sure that the new account has
sufficient permissions.

**Command Line Switches** - The MonitorWare Agent 2.x supports a limited set of command line switches. These are primarily used for unattended installations or

"engine only" installs. These are:

.. code-block:: text

  mwagent –h    Help, displays a short usage notice
  mwagent –I    Installs the service
  mwagent –u    Removes (uninstalls) the service
  mwagent –v    Displays version information as well as whether or not
                the service is installed.

**Please Note:** If you are opting for "Engine Only" install then there are two new
dll's located in the MointorWare Agent 2.x directory which are needed (used for
SETP over SSL):

* libeay32.dll
* ssleay32.dll

Copy these dll's either in System32 or in the MonitorWare Agent 2.x directory.
They are statically linked into the program, so these dll's are necessary (even
if they are not used in your configuration). If these aren't there then you
would definitely face problems!
