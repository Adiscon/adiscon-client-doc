.. index:: Registry Paths

Registry Paths
==============

Here are some more details regarding registry paths.

Since 64bit Windows re-routes all registry keys for 32bit programs
automatically
``(HKEY_LOCAL_MACHINE\SOFTWARE\ to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node)``, Adiscon decided in the course of development that the 32bit as well as 64bit
registry keys of the service should use the``„HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node“`` subkey.


But for your case, this is rather problematic since you need a registry file
for 32bit and for 64bit systems. Thus we decided to use a workaround, namely
to use the parameters key in the service area. In the services subkey of the
registry is no automatic mapping for Win32/64 applications and thus you can
use the same registry file for all systems.
