.. _repeatable_deployment_vs_repeatable_update_deployment:

Differences Between Repeatable Deployment and Repeatable Update Deployment
=========================================================================

While repeatable deployment and repeatable update deployment are closely
related, there are important distinctions in how they are planned and carried
out for Adiscon products. Understanding these differences helps you choose the
right method for the target systems you are preparing.

1.  Repeatable Deployment (Initial Deployment)
----------------------------------------------

A **repeatable deployment**, also known as an initial deployment, refers to the
**first-time installation** of software on multiple target systems where the
application **does not currently exist**.

* **Primary Goal:** To establish the software and its baseline
  configuration on new machines.

* **Target System State:** The software is **not installed** yet.
* **Key Steps:**
    #.  Perform an initial, full installation on a reference system.
    #.  Create and thoroughly test the **baseline configuration**.
    #.  Export this baseline configuration to a :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Package the product's executable files (e.g., ``winsyslg.exe``, ``mwagent.exe``) and associated DLLs along with the
        exported :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Distribute and execute a script that will:

        * Copy the product files to the target machine's desired installation directory.
        * **Install** the product as a Windows service (e.g., using ``winsyslg -i`` or ``mwagent -i``).
        * Import the baseline configuration from the ``.reg`` file.
        * **Start** the newly installed service.

* **Focus:** Establishing a functional, standardized installation from a clean slate.

2.  Repeatable Update Deployment
--------------------------------

A **repeatable update deployment** involves the **planned upgrade or patching**
of an application that is **already installed** on the target systems to a
newer version.

* **Primary Goal:** To update the software and potentially its
    configuration to a newer version, while ensuring minimal
    downtime and maintaining operational continuity.

* **Target System State:** The software is **already installed** and
    likely running.

* **Key Steps:**
    #.  Perform an **in-place upgrade** of the software on a reference system to the new version.
    #.  Adjust and refine the configuration for the new version, if
        necessary, and thoroughly test it.
    #.  Export the **updated configuration** to a :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Package the **new product files** (executables, DLLs) and the
        updated :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Distribute and execute a script that will:

        * **Stop** the existing, running service on the target machine.
        * Copy the new files to the existing installation directory,
          **overwriting** the old executables.
        * Import the updated configuration from the ``.reg`` file,
          applying changes to the existing registry entries.
        * **Restart** the service.

* **Focus:** Updating existing installations with minimal disruption.

3.  Key Differences at a Glance
-------------------------------

.. rubric:: Comparison of Deployment Types

**Repeatable Deployment (Initial):**

* **Target State:** Software **not installed**.
* **Core Action:** First-time installation, provisioning.
* **Service Handling:** Service is **installed and started**.
* **File Copying:** Copying **new** files for initial setup.
* **Configuration:** Import of a **baseline configuration**.
* **Complexity:** Generally simpler, no running service to manage.

**Repeatable Update Deployment:**

* **Target State:** Software **already installed**.
* **Core Action:** Upgrade, patch, version migration.
* **Service Handling:** Existing service is **stopped, then restarted**.
* **File Copying:** Copying **new** files to **overwrite old ones**.
* **Configuration:** Import of an **updated configuration**
    (changes applied to existing).
* **Complexity:** Slightly more complex, requires service
    management and compatibility checks.
