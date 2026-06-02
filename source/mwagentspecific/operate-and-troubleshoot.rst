Operate and Troubleshoot
========================

Once the first configuration works, operating MonitorWare Agent becomes a
repeatable cycle of checking service health, confirming event flow, and
reviewing action results.

Operational checks
------------------

Use these checks first:

- confirm the MonitorWare Agent service is running
- confirm the expected service instances are enabled
- confirm the correct ruleset is assigned to each service
- confirm actions can reach their target path, server, or database

When something does not work
----------------------------

Work from input to output:

1. verify that the service can collect or receive the data
2. verify that the ruleset assignment is correct
3. verify that the filter condition is not excluding the event
4. verify that the action target is reachable and correctly configured

Support-oriented tasks
----------------------

For escalation or support transfer, the most useful artifacts are usually:

- exported configuration
- debug log output
- a short description of the expected and actual result

See also:

- :doc:`../stepbystepguides`
- :doc:`faq/export-settings-support-call`
