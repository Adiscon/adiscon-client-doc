.. _log-rotation-naming-convention-mwagent:

Log Rotation Naming Convention Change in MonitorWare Agent 15.x
================================================================

This article explains the change in rotated log file naming convention in MonitorWare Agent 15.x and later versions.

Question
--------

Why are my rotated log files named differently after upgrading to MonitorWare Agent 15.x?

Answer
------

MonitorWare Agent 15.x and later versions use a new naming convention for rotated log files. Instead of placing sequence numbers before the file extension (e.g., ``syslog1.csv``, ``syslog2.csv``), the new format appends sequence numbers after the file extension (e.g., ``syslog.csv.1``, ``syslog.csv.2``).

**This change is intentional and by design.** The new format follows Unix/POSIX conventions and provides better compatibility with common log management tools and scripts.

What Changed
------------

**Old Format (MonitorWare Agent versions before 15.x):**

* ``syslog.csv`` (active log file)
* ``syslog1.csv`` (first rotated file)
* ``syslog2.csv`` (second rotated file)
* ``syslog3.csv`` (third rotated file)

**New Format (MonitorWare Agent 15.x and later):**

* ``syslog.csv`` (active log file)
* ``syslog.csv.1`` (first rotated file)
* ``syslog.csv.2`` (second rotated file)
* ``syslog.csv.3`` (third rotated file)

Root Cause
----------

This change was intentionally implemented as part of improvements to the log rotation subsystem. The new format provides several benefits:

1. **Better compatibility:** Follows Unix/POSIX conventions used by standard log rotation utilities
2. **Improved reliability:** Enhanced thread safety in the log rotation mechanism
3. **Tool compatibility:** Works better with common log management tools and scripts
4. **Industry standard:** Aligns with widely-adopted log rotation naming practices

**Important:** The filename format change cannot be reverted through configuration settings.

Impact on Existing Workflows
-----------------------------

The naming convention change may affect:

* **Scripts that parse log filenames:** Scripts expecting the old format may fail to find rotated files
* **Monitoring tools:** Tools that reference specific filename patterns may need updates
* **Log management workflows:** Automated processes that depend on the old naming convention may break
* **Backup scripts:** File backup routines that filter by filename pattern may need adjustment

Solution
--------

Updating Scripts and Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have scripts, monitoring tools, or applications that parse or reference rotated log files, update them to work with the new format:

1. **Modify file parsing logic:**

   Update patterns to handle ``filename.ext.N`` format instead of ``filenameN.ext``

   Example (PowerShell):

   .. code-block:: powershell

      # Old pattern
      Get-ChildItem "syslog[0-9].csv"

      # New pattern
      Get-ChildItem "syslog.csv.[0-9]"

2. **Update hardcoded filename references:**

   Replace any hardcoded file paths in scripts to use the new naming convention

3. **Test compatibility:**

   Verify script functionality with the new naming convention in a test environment before deploying to production

Log Management Tool Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new format is compatible with most modern log rotation utilities:

* **Standard logrotate:** Fully compatible with the new format
* **Third-party tools:** Most log management tools support POSIX-style naming
* **Custom solutions:** May require updates to filename matching patterns

**Recommendation:** Verify that your log management tools support the POSIX-style naming convention. Most modern tools do, but older or custom solutions may need configuration updates.

Migration Best Practices
------------------------

When upgrading to MonitorWare Agent 15.x or later:

1. **Test in development:**

   * Deploy the new version in a development environment first
   * Run your log processing workflows and scripts
   * Verify all tools work correctly with the new naming format
   * Document any required changes

2. **Update automation:**

   * Modify scripts before deploying the new MonitorWare Agent version
   * Update monitoring tool configurations
   * Test all changes in the development environment

3. **Plan for transition:**

   * Consider running both old and new versions during a transition period
   * Update scripts to handle both naming conventions if needed during migration
   * Document the change in deployment procedures

4. **Verify backup processes:**

   * Ensure backup scripts include files with the new naming pattern
   * Test backup restoration to verify rotated files are included
   * Update retention policies if they depend on filename patterns

5. **Update documentation:**

   * Document the filename format change in maintenance procedures
   * Update runbooks and operational guides
   * Communicate changes to all stakeholders

Common Questions
----------------

**Can I configure MonitorWare Agent to use the old naming format?**

No. The new naming format is built into the log rotation subsystem and cannot be changed through configuration. This ensures consistent behavior and maintains the reliability and thread safety improvements.

**Will my existing rotated log files be renamed automatically?**

No. Existing rotated files retain their original names. The new naming convention applies only to files rotated after upgrading to MonitorWare Agent 15.x or later.

**What happens to old rotated files?**

Old rotated files (using the previous naming convention) remain unchanged. They coexist with newly rotated files that use the new convention. You may want to rename old files manually if consistency is important for your workflows, or simply let them age out according to your retention policy.

**Are there any performance implications?**

No. The naming convention change does not affect performance. In fact, the underlying improvements to the log rotation subsystem provide better reliability and thread safety.

Additional Information
----------------------

For more information about log rotation configuration, see the log file action documentation in the MonitorWare Agent manual.

If you need assistance updating scripts or tools to work with the new naming convention, contact Adiscon support at https://ticket.adiscon.com/
