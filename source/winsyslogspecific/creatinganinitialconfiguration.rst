Creating an Initial Configuration
=================================

Once WinSyslog is installed, a working configuration needs to be created. The
reason is that WinSyslog does not perform any work without being instructed to
do so. To create some basic work, the following needs to be done:

• **Create a simple ruleset** - The most basic ruleset includes no criteria, which means all incoming messages will match. To get started, we recommend
  using just a single `"Write to File" <https://www.WinSyslog.com/step-by-step-guides/actions-related/file-logging-steps-mwa42/>`_
  action which will write the incoming messages to the local disk.

•**Create at least one syslog listener** - Be sure to associate the created ruleset with the `"Syslog Listener" <https://www.WinSyslog.com/articles/how-to-configure-a-syslog-server/>`_.

•**Start the WinSyslog service**
  Your system is now ready to accept and store incoming messages.
