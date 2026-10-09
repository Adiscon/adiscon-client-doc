TLS Send Progress Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  nTLSSendTimeout

**Description:**
  Maximum time without successful TLS send progress, in milliseconds. The
  default is 30000 (30 seconds). Valid values are 1 through 2147483647.
  Missing or invalid values use the default; zero does not disable the timeout.

  This setting applies when forwarding Syslog over TCP with TLS enabled,
  including persistent connections, reconnects, backup destinations, and
  diskqueue replay. It does not apply to UDP or unencrypted TCP forwarding.

  Each successful TLS write, including a partial write, restarts the inactivity
  interval. Socket readiness and TLS retry requests do not restart it. A send
  can therefore take longer than the configured interval while it continues
  making progress.
  Successful writes do not confirm that the destination has processed the
  message.

  TCP connection establishment and the TLS handshake share one total deadline
  with the same configured value. Progress during these steps does not restart
  that deadline. Name resolution is also bounded by the configured value,
  using a separate deadline before the connection attempt.

  On timeout, the failed connection is closed and the action uses its existing
  transmission-failure handling. If diskqueuing is enabled and persistence
  succeeds, unsent messages are retained for later replay. A timeout does not
  immediately trigger a reconnect or a backup attempt. Partially transmitted
  messages may be duplicated when replayed.

  Service stop and configuration reload cancel an active TLS network operation
  without waiting for this timeout. The Session Timeout setting
  (``nTimeoutValue``) instead controls closure of an idle TCP session; it does
  not bound an active TLS send.
