.. _mwagent-mass-rollout-deployment:

How Do I Perform a Mass Rollout Deployment?
===========================================

Answer
------

Use a prepared base configuration and deploy the MonitorWare Agent service to
multiple target systems in a controlled rollout process.

Details
-------

Mass rollout is a deployment pattern, not a first-run setup task. It is
most useful when the service configuration is already validated on a reference
system.

Action path
-----------

1. Build and validate the configuration on a reference system.
2. Decide whether the target systems need only the engine or the full client
   installation.
3. Roll out the package and configuration in a staged manner.
4. Verify that target systems start the service and apply the expected
   configuration.

Related information
-------------------

* :doc:`mass-update-rollout`
* :doc:`../understand-the-components`
