Tutorial: Write Events to a File
================================

Goal
----

Write events collected by MonitorWare Agent to a local file.

Prerequisites
-------------

- A ruleset that receives events from a MonitorWare Agent service
- A writable local output path

Steps
-----

1. Create or choose the ruleset whose events should be written.
2. Add a :doc:`Write to File <a-fileoptions>` action to that ruleset.
3. Configure the target directory and filename.
4. Save and apply the configuration.
5. Restart the service if required in your environment.

Verification
------------

Trigger a matching event and confirm that the output file is created or
updated.
