:orphan:

.. _microsoft-365-oauth-mail:

Microsoft 365 OAuth for email alerts
====================================

.. only:: mwagent or winsyslog or eventreporter

   This guide configures a **Send Email** action in MonitorWare Agent,
   WinSyslog, or EventReporter to submit alert messages to Exchange Online
   using Microsoft 365 OAuth with application permissions. Follow it only
   when the installed Adiscon User Interface offers **Microsoft 365 OAuth
   (application)** in the **SMTP authentication** list. The product service
   that runs the action must also support application OAuth; a client option
   alone does not prove that the installed service build supports it. Check
   both installed components and their release information. This guide does
   not assign a product version or claim general availability.
   The client steps cover the classic Adiscon WinForms interface only; they
   do not cover WinSyslog-ng or another client interface.

   The steps use the Exchange Online application-permission method: the Entra
   application receives the Office 365 Exchange Online application permission
   ``SMTP.SendAsApp``, and Exchange grants the application's service principal
   access to one mailbox. This is SMTP client submission with an app-only
   token. It does not use Microsoft Graph mail permissions or delegated
   ``SMTP.Send`` sign-in, and it does not fall back to username and password.
   This is a customer configuration guide. You do not need access to an
   Adiscon developer environment, development scripts, or a sample VBS file.

   Goal
   ----

   Send one alert through ``smtp.office365.com`` from a dedicated, licensed
   user mailbox such as ``alerts@example.com``. The SMTP username and sender
   address must be that same mailbox. The recipient is a separate address,
   such as ``operations@example.com``.

   Before you start
   ----------------

   Ask the Microsoft 365 administrator to confirm these prerequisites:

   - An existing licensed user mailbox is available, or the administrator
     creates one for alerts. In the Microsoft 365 admin center, open **Users**
     > **Active users** and either select **Add a user** or open the existing
     user. Assign a license that includes Exchange Online, then confirm the
     primary SMTP address. This guide uses ``alerts@example.com`` as the
     example mailbox. Use its primary SMTP address consistently.
   - A Microsoft Entra administrator can register or manage the application,
     add an Exchange Online application permission, and grant tenant-wide
     admin consent. Use an administrator role authorized by your tenant for
     those actions.
   - An Exchange Online administrator has permission to register the
     application's service principal and grant the mailbox permissions shown
     below. In many tenants, this is a member of the **Organization
     Management** role group or a delegated role group with the required
     Exchange commands.
   - The alert recipient is known. It can be a distribution list or another
     mailbox; it is not the SMTP username unless it is intentionally the same
     address.
   - The service machine can reach the Microsoft identity token endpoint over
     HTTPS (typically TCP port 443) and Exchange Online SMTP submission over
     TCP port 587.

   If the selector is not present, stop and check the installed build's release
   information or contact Adiscon support. Do not infer availability from this
   guide or from an unreleased runtime change.

   1. Prepare the Microsoft Entra application
   ------------------------------------------

   In the Microsoft Entra admin center, open **Identity** > **Applications** >
   **App registrations**. Select **New registration**, enter a name, choose
   **Accounts in this organizational directory only**, and select **Register**.
   This app-only setup does not need a redirect URI. You can use an existing
   application registered in your own tenant instead. On the app's
   **Overview** page, record the **Directory (tenant) ID** and **Application
   (client) ID** as GUIDs.

   To find the Exchange service principal Object ID, open **Enterprise
   applications**, search for the application by its **Application (client)
   ID**, and open its **Overview** page. Record the **Object ID** from that
   Enterprise application page. Do not use the App registrations Object ID.

   In the app registration, open **Certificates & secrets** > **Client
   secrets** > **New client secret**. Enter a description, choose an expiration
   that follows your organization's secret lifetime policy, and select **Add**.
   Copy the secret's **Value** while it is visible. The secret's **ID** is not
   the secret value and cannot be used in the Adiscon field. Record the
   expiration date and schedule rotation before expiry. Do not put the secret
   value in a command, script, command-line argument, or support log. You will
   enter it only in the Adiscon password field later.

   2. Add the Exchange SMTP application permission
   -----------------------------------------------

   In the app registration, open **API permissions** > **Add a permission** >
   **APIs my organization uses**. Search for and select **Office 365 Exchange
   Online**, choose **Application permissions**, then select
   ``SMTP.SendAsApp`` and add the permission. Do not choose Microsoft Graph or
   delegated ``SMTP.Send`` for this application-only setup.

   .. figure:: ../../images/m365-oauth-consent-required.png
      :alt: Exchange Online SMTP.SendAsApp application permission awaiting administrator consent
      :width: 100%

      Before administrator consent: adding ``SMTP.SendAsApp`` alone is
      insufficient. This German-language example still shows **Not granted**.
      The visible Microsoft Graph ``User.Read`` permission is unrelated and is
      not required for this SMTP setup.

   Select **Grant admin consent for <your tenant>** and confirm the prompt.
   Before continuing, verify that the permission appears with status
   **Granted for <your tenant>** in the app's API permissions list. A
   permission listed as pending or not granted is not
   ready for Exchange configuration.

   3. Register the application in Exchange Online and grant one mailbox
   --------------------------------------------------------------------

   Use Exchange Online PowerShell from an administrator workstation. Replace
   the application (client) ID and **Object ID from the Enterprise applications
   entry** for this application. The Enterprise application Object ID is not
   the Object ID on the App registrations page. The tenant ID is entered in
   the Adiscon client later; it is not needed by these Exchange commands. No
   client secret is used in these commands.

   The commands below are examples for an administrator to review and run in
   their tenant. They do not run from this guide. The service-principal lookup
   stops if the application ID is already registered more than once, creates
   it only when no match exists, and stops if the registered object ID differs
   from the Enterprise application Object ID supplied above.

   .. code-block:: powershell

      $AppId = '<application (client) ID GUID>'
      $EnterpriseAppObjectId = '<Enterprise application Object ID GUID>'
      $Mailbox = 'alerts@example.com'

      if (-not (Get-Module -ListAvailable -Name ExchangeOnlineManagement)) {
          Install-Module -Name ExchangeOnlineManagement -Scope CurrentUser -ErrorAction Stop
      }
      Import-Module ExchangeOnlineManagement -ErrorAction Stop
      Connect-ExchangeOnline -UserPrincipalName '<administrator UPN>' `
          -ErrorAction Stop

      $servicePrincipals = @(Get-ServicePrincipal -ErrorAction Stop |
          Where-Object { $_.AppId -eq $AppId })
      if ($servicePrincipals.Count -gt 1) {
          throw 'More than one Exchange service principal has this application ID. ' +
              'Stop and resolve the duplicate.'
      }
      if ($servicePrincipals.Count -eq 0) {
          New-ServicePrincipal -AppId $AppId -ObjectId $EnterpriseAppObjectId -ErrorAction Stop
          $servicePrincipals = @(Get-ServicePrincipal -ErrorAction Stop |
              Where-Object { $_.AppId -eq $AppId })
      }
      if ($servicePrincipals.Count -ne 1) {
          throw 'The Exchange service principal was not created or cannot be ' +
              'uniquely identified.'
      }
      $exoServicePrincipal = $servicePrincipals[0]
      if ($exoServicePrincipal.ObjectId -ne $EnterpriseAppObjectId) {
          throw 'The Exchange service principal Object ID does not match the ' +
              'Enterprise application Object ID.'
      }

      $mailboxPermissions = @(Get-MailboxPermission -Identity $Mailbox `
          -User $exoServicePrincipal.Identity -ErrorAction Stop)
      if (@($mailboxPermissions | Where-Object {
          $_.AccessRights -contains 'FullAccess' -and $_.Deny
      }).Count -gt 0) {
          throw 'A FullAccess deny permission exists for this mailbox. ' +
              'Stop and have the administrator review it.'
      }
      $fullAccessPermission = @($mailboxPermissions | Where-Object {
          $_.AccessRights -contains 'FullAccess' -and -not $_.Deny
      })
      if ($fullAccessPermission.Count -eq 0) {
          Add-MailboxPermission -Identity $Mailbox `
              -User $exoServicePrincipal.Identity `
              -AccessRights FullAccess -ErrorAction Stop
      }

      $recipientPermissions = @(Get-RecipientPermission -Identity $Mailbox `
          -Trustee $exoServicePrincipal.Identity -ErrorAction Stop | Where-Object {
          $_.AccessRights -contains 'SendAs'
      })
      if (@($recipientPermissions | Where-Object {
          $_.AccessControlType -eq 'Deny'
      }).Count -gt 0) {
          throw 'A SendAs deny permission exists for this mailbox. Resolve it before continuing.'
      }
      $sendAsPermission = @($recipientPermissions | Where-Object {
          $_.AccessControlType -eq 'Allow'
      })
      if ($sendAsPermission.Count -eq 0) {
          Add-RecipientPermission -Identity $Mailbox `
              -Trustee $exoServicePrincipal.Identity `
              -AccessRights SendAs -ErrorAction Stop
      }

      Get-ServicePrincipal -ErrorAction Stop |
          Where-Object { $_.AppId -eq $AppId } |
          Format-List AppId,ObjectId,Identity,DisplayName
      Get-MailboxPermission -Identity $Mailbox -User $exoServicePrincipal.Identity `
          -ErrorAction Stop | Where-Object {
          $_.AccessRights -contains 'FullAccess'
      } | Format-Table User,AccessRights,Deny
      Get-RecipientPermission -Identity $Mailbox `
          -Trustee $exoServicePrincipal.Identity -ErrorAction Stop |
          Format-List Trustee,AccessRights,AccessControlType,IsInherited

   Review each command with your Exchange administrator before running it.
   The permission checks make repeated runs skip grants already present. Keep
   the service principal's ``Identity`` value for both mailbox permission
   commands; do not substitute the App ID or Entra Object ID there. The
   verification output must show exactly one Exchange service principal with
   the expected App ID and matching Enterprise application Object ID, a
   ``FullAccess`` row with ``Deny`` set to ``False``, and a ``SendAs`` row
   with ``AccessControlType`` set to ``Allow``. If any expected row is missing
   or the IDs do not match, stop and recheck the permissions before configuring
   the client.

   4. Check SMTP AUTH policy for the mailbox
   -----------------------------------------

   SMTP AUTH must be allowed for the selected Exchange Online mailbox. Check
   its mailbox setting and the organization setting:

   .. code-block:: powershell

      Get-CASMailbox -Identity 'alerts@example.com' -ErrorAction Stop |
          Format-List SmtpClientAuthenticationDisabled
      Get-TransportConfig -ErrorAction Stop |
          Format-List SmtpClientAuthenticationDisabled

   For the mailbox setting, ``False`` means SMTP AUTH is enabled for that
   mailbox, ``True`` means it is disabled, and a blank value means it inherits
   the organization setting. A mailbox value of ``False`` overrides an
   organization-wide disabled value for that mailbox. If your administrator
   approves enabling SMTP AUTH for this mailbox, the per-mailbox command is:

   .. code-block:: powershell

      Set-CASMailbox -Identity 'alerts@example.com' `
          -SmtpClientAuthenticationDisabled $false -ErrorAction Stop
      Get-CASMailbox -Identity 'alerts@example.com' -ErrorAction Stop |
          Format-List SmtpClientAuthenticationDisabled

   After an approved change, the mailbox query should show ``False``. If it
   shows ``True`` or blank, stop and ask the administrator to recheck the
   setting and applicable policies before testing.

   Do not enable SMTP AUTH organization-wide as a setup shortcut. If Security
   Defaults or another administrator policy blocks SMTP AUTH, stop and ask the
   administrator to decide whether an approved policy change is appropriate.
   Do not disable Security Defaults automatically. Microsoft documents these
   organization and mailbox settings in `Enable or disable authenticated
   client SMTP submission
   <https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission>`_.

   5. Prepare a trusted SMTP CA bundle on the service machine
   ----------------------------------------------------------

   The Adiscon SMTP connection validates the Exchange server certificate using
   a PEM CA file. The Microsoft identity token request uses Windows HTTPS
   certificate validation separately; it does not use this SMTP CA file.

   On the Windows machine that runs the Adiscon service, download the current
   PEM bundle from the `curl CA Extract page
   <https://curl.se/docs/caextract.html>`_ over HTTPS. The page links to
   ``https://curl.se/ca/cacert.pem`` and publishes the current file's SHA-256
   checksum. Compare that checksum with the downloaded file's result from:

   .. code-block:: powershell

      Get-FileHash '<downloaded cacert.pem path>' -Algorithm SHA256

   Download it to a temporary location first. After the hash matches, use File
   Explorer to create ``C:\ProgramData\Adiscon\certs`` on the service machine.
   Save the verified file there as ``cacert.pem``. If the configuration is edited on a
   remote computer, this path still refers to the service machine, not the
   computer running the client. To identify the service account without
   changing or stopping the service, open ``services.msc``, find the Adiscon
   product service, and view **Properties** > **Log On**. In the folder's
   **Properties** > **Security** > **Advanced** permissions, keep existing
   inherited entries, including **SYSTEM**. Add **Read & execute** access for
   the service account and ensure Administrators retain **Modify** access. Do
   not remove or reduce existing SYSTEM permissions. The certificate bundle is
   a list of trusted
   certificate authorities; do not place the Exchange SMTP server's leaf
   certificate in this field. Do not disable certificate or hostname
   verification to work around a trust error.

   6. Configure the Send Email action
   ----------------------------------

   In the classic Adiscon WinForms client, expand **Rules/Rule Sets**, select
   the rule, open **Actions**, then choose **Add Action** > **Send Email**.
   Create or edit that action and use these values in **Mail Server Options**:

   - **Mailserver**: ``smtp.office365.com``
   - **Mailserver port**: ``587``
   - **SMTP authentication**: **Microsoft 365 OAuth (application)**
   - **SMTP Username**: the primary SMTP address of the licensed mailbox, for
     example ``alerts@example.com``
   - **Tenant ID (GUID)**: the Entra tenant ID
   - **Application ID (GUID)**: the Entra application (client) ID
   - **Application client secret**: the client secret **Value**, not its ID
   - **SMTP trusted CA file (PEM)**: the verified CA bundle path on the service
     machine
   - **Use a secure connection (SSL) to the mail server**: enabled
   - **Use STARTTLS SMTP Extension**: enabled

   In **Mail Format Options**, set **Sender Emailaddress** to the same primary
   mailbox address used for **SMTP Username**. Set **Recipient Emailaddress**
   to the destination address, such as ``operations@example.com``. Keep the
   sender and recipient roles separate unless your recipient is intentionally
   the sender mailbox.

   The client masks the secret in its password field and stores it using the
   existing reversible credential encoding. This is not strong encryption.
   Restrict access to the configuration, registry data, exported settings, and
   their backups to administrators and the service account. Rotate the secret
   before expiry and update the action. Do not include the secret or access
   tokens in support evidence.

   7. Save, apply, and send one test event
   ---------------------------------------

   Add the action to a rule that matches one deliberate test event. Use the
   product's normal configuration save and apply workflow. If your deployment
   requires a service restart for configuration changes, follow your normal
   change process before testing.

   For a concrete test, use one known event collected by the selected product.
   For example, send one controlled syslog test event from
   ``test-host.example.com`` with warning priority and message
   ``[TEST] Backup job DailyBackup finished with warnings: simulated file skipped.``.
   Configure the action's subject and body with event properties rather than
   hard-coded test text:

   .. code-block:: text

      Subject: [TEST] %source%: %msg%
      Body:
      Source: %source%
      Message: %msg%
      Priority: %syslogpriority%

   Use the client's **Insert Property** control to confirm that each property
   is available for the event type you chose. ``%syslogpriority%`` applies to
   syslog events; for Windows events, use the available event properties and
   omit the priority line if it is not listed. In EventReporter, choose one
   actual Windows event rather than a syslog event. Save and apply the
   configuration using the normal operator workflow, then trigger the rule
   once and check the intended recipient mailbox.

   A successful OAuth authentication response such as SMTP ``235`` confirms
   authentication only. SMTP ``250`` after the message ``DATA`` command means
   the server accepted the message for processing; it does not confirm inbox
   delivery. Check message trace, quarantine, and non-delivery reports before
   repeating a test, so a delayed message is not sent twice.

   Troubleshooting
   ---------------

   1. **Entra application and secret**: for missing-token or ``535`` errors,
      verify the tenant ID, application ID, secret **Value**, and expiration.
      Do not copy the secret ID into the client.
   2. **Consent and Exchange identity**: verify that ``SMTP.SendAsApp`` has
      tenant admin consent. Confirm there is exactly one Exchange service
      principal for the App ID and its Object ID matches the Enterprise
      application Object ID. A duplicate or mismatch needs administrator
      review.
   3. **Mailbox authorization**: confirm ``FullAccess`` and ``SendAs`` are
      allowed for the Exchange service principal on the same mailbox used as
      SMTP username and sender. Stop for administrator review if an explicit
      deny exists.
   4. **SMTP AUTH and secure connection**: if SMTP AUTH is rejected, check the
      mailbox's ``SmtpClientAuthenticationDisabled`` value and the tenant
      setting. ``True`` blocks SMTP AUTH; blank inherits the tenant value.
      Ask an administrator to review Security Defaults and other policies.
      For a connection failure before OAuth, check outbound TCP port 587,
      STARTTLS, the PEM path and service-account read access, and certificate
      chain and hostname validation. Windows HTTPS trust for token requests is
      separate from the SMTP PEM bundle.
   5. **Service, event, and delivery**: check that the installed service
      supports the option, then check its startup/configuration log and
      whether the rule matched the test event. A startup failure before an
      event is processed does not prove OAuth authentication failed. SMTP
      ``235`` confirms authentication only. SMTP ``250`` after ``DATA`` means
      the server accepted the message for processing, not that it reached the
      inbox. Check message trace, quarantine, and non-delivery reports before
      repeating a test to avoid duplicate messages.

   Microsoft also documents an Exchange Online **application RBAC** method for
   SMTP. It uses the Exchange role ``Application SMTP.SendAsApp`` and a scoped
   role assignment, without adding the Entra SMTP application permission or
   granting the mailbox ``FullAccess`` and ``SendAs`` permissions shown in
   this guide. These are separate authorization models; do not combine their
   steps. See Microsoft's `SMTP onboarding to app RBAC
   <https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/smtp-app-rbac-onboarding>`_
   for that alternative. The Adiscon setup described here follows the
   application-permission model.

   Microsoft documents a different OAuth flow for `shared mailbox access
   <https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#sasl-xoauth2-authentication-for-shared-mailboxes-in-office-365>`_.
   That guidance obtains a token on behalf of a user. Adiscon has not tested
   that shared-mailbox flow with this application-only configuration; this
   guide uses a licensed user mailbox.

   Related information
   -------------------

   - `Microsoft: Authenticate SMTP using OAuth
     <https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth>`_
   - `Microsoft: Enable or disable authenticated client SMTP submission
     <https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission>`_
   - `Microsoft: Connect-ExchangeOnline
     <https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/connect-exchangeonline?view=exchange-ps>`_
   - `curl: CA Extract
     <https://curl.se/docs/caextract.html>`_
