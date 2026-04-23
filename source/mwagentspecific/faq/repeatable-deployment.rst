.. _mwagent-repeatable-deployment:

How Do I Perform a Repeatable Deployment?
=========================================

Answer
------

Use a prepared reference configuration and deploy the MonitorWare Agent service
to multiple target systems in a controlled, repeatable process.

Details
-------

Repeatable deployment is a deployment pattern, not a first-run setup task. It
is most useful when the service configuration is already validated on a
reference system and must be applied to more than one target.

Action path
-----------

1. Build and validate the configuration on a reference system.
2. Decide whether the target systems need only the engine or the full client
   installation.
3. Deploy the package and configuration in a staged manner.
4. Verify that target systems start the service and apply the expected
   configuration.

Related information
-------------------

* :doc:`repeatable-update-deployment`
* :doc:`../understand-the-components`
