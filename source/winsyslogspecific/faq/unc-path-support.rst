.. _winsyslog-unc-path-support-faq:

Can WinSyslog Write to a UNC Path?
==================================

Question
--------

Can WinSyslog write log files to a UNC path such as
``\\server\share\logs``?

Answer
------

Yes, but not with the default service account. WinSyslog runs as a Windows
service, and the default Local System account normally cannot access network
shares. To use a UNC path, run the WinSyslog service under an account that has
permission to access the target share.

Details
-------

UNC path support itself is not the problem. The limiting factor is the Windows
security context under which the service runs.

Typical working setup:

* a domain or local service account is configured for the WinSyslog service
* that account has write permissions on the target share
* the share and underlying NTFS permissions both allow access

Typical non-working setup:

* the WinSyslog service still runs as Local System
* the target is a remote UNC share
* no explicit network permissions exist for the service account

Action path
-----------

1. Create or choose a service account that has access to the target share.
2. Grant that account the required share and NTFS permissions.
3. Open the Windows Services console.
4. Open the properties of the ``AdisconWINSyslog`` service.
5. Change the logon account from Local System to the chosen service account.
6. Restart the WinSyslog service.
7. Configure the file action to use the UNC path.
8. Send a test message and verify that the target file is created or updated.

Important notes
---------------

* Test the target path with the same account context that the service uses.
* Drive-letter mappings created in an interactive user session are usually not
  visible to Windows services. Use the UNC path directly.
* If possible, keep log storage local and use forwarding or downstream syncing
  for remote distribution. This is usually more robust than writing directly to
  a network share.

Related information
-------------------

* :doc:`../../mwagentspecific/a-fileoptions`
* :doc:`../tutorial-write-to-file`
