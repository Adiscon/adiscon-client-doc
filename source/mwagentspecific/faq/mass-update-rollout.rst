.. _mwagent-mass-update-rollout:

How Do I Perform a Mass Update Rollout?
=======================================

Answer
------

Use mass update rollout when MonitorWare Agent is already deployed and you need
to distribute an updated configuration or package revision to many systems.

Details
-------

Mass update rollout differs from initial mass rollout because the target
systems already exist in production and may already process data.

Action path
-----------

1. Validate the updated package or configuration on a non-production system.
2. Plan restart timing and rollback expectations.
3. Deploy the update in stages.
4. Confirm that services restart cleanly and continue to process data.

Related information
-------------------

* :doc:`mass-rollout-deployment`
* :doc:`diff-massroll-massupdateroll`
