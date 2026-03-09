.. _mass-rollout-deployment-eventreporter:

How to Perform a Mass Rollout of EventReporter
==============================================

Question
--------

How can I deploy EventReporter to many systems efficiently?

Answer
------

Use one system as the reference build, export its configuration, and automate
distribution of the installer or service files plus the exported configuration
through your normal software deployment tooling.

Details
-------

A mass rollout is appropriate when many systems should use the same or nearly
the same EventReporter setup. The exact deployment mechanism depends on your
environment, but the overall pattern stays the same:

- create and test one reference configuration
- export that configuration
- distribute the software and configuration together
- adjust only host-specific values where needed

Action path
-----------

1. Install EventReporter on a reference system.
2. Configure and test the required services, rulesets, filters, and actions.
3. Export the configuration as a text-based registry file.
4. Package the EventReporter software and the exported configuration for your
   deployment tool.
5. Deploy to target systems by using your standard automation platform such as
   Group Policy, SCCM, PowerShell, or another software distribution tool.
6. Import the configuration on the target systems.
7. Start the EventReporter service and verify that event collection and
   forwarding work as expected.

Important notes
---------------

- Review machine-specific settings such as file paths, service accounts,
  credentials, and target addresses.
- Test on a non-production system before broad rollout.
- Keep the configuration export in text form so it can be reviewed and tracked.

Related information
-------------------

* :doc:`copying-configuration`
* :doc:`../installation`
