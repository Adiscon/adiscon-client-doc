.. index:: System Requirements

System Requirements
===================

EventReporter requires very limited resources of the machine to run optimally.
The actual minimum requirements to run the application depend on the type of
installation. If only the client is installed, they are a bit higher otherwise
the service needs a few enabling it to run on a large variety of machines –
even the highly utilized ones.

Client
------

* The client can be installed on Windows 10, Windows 11, and Windows Server
  2016/2019/2022. The operating system variant (Workstation, Server …) is
  irrelevant. Note: For legacy systems (Windows XP, Server 2003), older versions
  are available - contact Adiscon for details.

* The client is suited for 32bit and 64bit operating systems. It runs
  automatically on each platform in 32Bit or 64Bit mode.

* The client uses Microsoft .Net Framework technology. The Installer will
  automatically install the necessary .Net Framework components before
  installation. A network connection maybe required in order to download
  additional components.

* The client requires roughly 8 MB RAM in addition to the operating system
  minimum requirements. It also needs around 5 MB of disk space.

Service
-------

* The service has fewer requirements.

* It works under the same operating system versions.

* At runtime, the base service requires 5 MB of main memory and less than 5 MB
  of disk space. However, the actual resources used by the agent largely depend
  on the services configured.

* Please note that the 32Bit Service is limited to 2GB of usable memory. The
  64Bit version does not have any limit. A typical Syslog message (including
  overhead) takes roughly 4-8 KB. With 1024 MB, you can buffer up to
  100,000-200,000 messages in 1024 MB.

* On Windows Server editions, additional event logs (such as "DNS Server", "File
  Replication Service", and "Directory Service") are automatically supported.
