.. index:: System Requirements

System Requirements
===================

The WinSyslog Service has minimal system requirements. The actual minimum
requirements depend on the type of installation. If the Client is installed,
they are higher. The service has very minimal requirements, enabling it to run
on a large variety of machines - even highly utilized ones.

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

* If the Rsyslog Windows Agent shall just monitor the local systems event log,
  impact on the monitored system is barely noticeable, if at all visible.

* If the Rsyslog Windows Agent acts as a central Syslog server receiving
  hundreds of messages per second, it needs many more resources. Even then, the
  actual load is depending on the actions carried out. As such, there is no
  single guideline for hardware sizing. It needs to be adapted to the expected
  workload. We have created an article on `performance optimization <https://www.adiscon.com/article/performance-optimizing-syslog-server/>`_
  for Syslog server operations, which you may want to read.

* Please note however, that the service is specifically optimized to handle
  high throughput including message bursts (for example received via syslog).

* If you expect high volume burst and carry out time consuming actions (for
  example database writes), we highly recommend adding additional memory to the
  machine. Please note that the 32Bit Service is limited to 2GB of usable
  memory. The 64Bit version does not have any limit. A typical Syslog message
  (including overhead) takes roughly 4-8 KB. With 1024 MB, you can buffer up to
  100,000-200,000 messages in 1024 MB.

* Please note that the Rsyslog Windows Agent is capable of storing such bursts
  temporarily in memory even if the machine would otherwise be too slow to
  process the messages.



Adiscon LogAnalyzer
-------------------

* Adiscon LogAnalyzer requires a local web server installed. Microsoft Internet
  Information Server (IIS) or Apache with PHP support is recommended as Adiscon
  LogAnalyzer is a PHP based application. Adiscon LogAnalyzer is an optional
  component and not mandatory. We recommend using it with modern PHP
  versions (PHP 8.0 or higher) on Apache or IIS with current XAMPP, WAMP,
  or similar web server packages.
