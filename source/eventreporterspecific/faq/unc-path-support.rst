.. _eventreporter-unc-path-support-faq:

Can EventReporter Write to a UNC Path?
======================================

Question
--------

Can EventReporter write log files to a UNC path such as
``\\server\share\logs``?

Answer
------

Yes, but not with the default Local System account. To use a UNC path, run the
EventReporter service under an account that has permission to access the target
share.

Details
-------

UNC path support itself is not the limiting factor. The important part is the
Windows security context under which the service runs.

Action path
-----------

1. Create or choose a service account that has access to the target share.
2. Grant that account the required share and NTFS permissions.
3. Open the Windows Services console.
4. Open the properties of the EventReporter service.
5. Change the logon account from Local System to the chosen service account.
6. Restart the EventReporter service.
7. Configure the file action to use the UNC path.
8. Trigger a test event and verify that the target file is created or updated.

Related information
-------------------

* :doc:`../../mwagentspecific/a-fileoptions`
* :doc:`../tutorial-write-to-file`
