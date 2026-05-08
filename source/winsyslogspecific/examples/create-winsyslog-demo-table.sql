IF DB_ID(N'WinSyslogDemo') IS NULL
BEGIN
    CREATE DATABASE WinSyslogDemo;
END
GO

USE WinSyslogDemo;
GO

IF OBJECT_ID(N'dbo.WinSyslogIncoming', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.WinSyslogIncoming (
        received_at datetime2(0) NOT NULL,
        source_host nvarchar(255) NOT NULL,
        facility_text nvarchar(32) NULL,
        severity_text nvarchar(32) NULL,
        app_name nvarchar(128) NULL,
        raw_message nvarchar(max) NULL,
        message_text nvarchar(max) NOT NULL
    );
END
GO
