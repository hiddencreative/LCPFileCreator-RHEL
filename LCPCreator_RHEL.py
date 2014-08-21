__author__ = 'josefweiss'

# Get data from user

print '\n','This script will generate the required XML output for a RHEL LCP file.','\n'
logDirectory = raw_input('Type LCE client log directory location, or hit enter to accept default: [/opt/lce/client/]:')
if logDirectory == '':
    logDirectory = '/opt/lce/client/'
processAccounting = raw_input('Monitor process accounting and BSM auditing?  Saying yes will enable process accounting. [Y/n]:')
if processAccounting == 'y':
    processAccountingDirectory = raw_input('Type accounting file location, or hit enter to accept default: [/var/account/pacct]:')
    if processAccountingDirectory == '':
        processAccountingDirectory = '/var/account/pacct'
    else:
        processAccounting == 'n'
tailMessages = raw_input('Monitor messages log [Y/n]:')
if tailMessages == 'y':
    messagesDirectory = raw_input('Type messages log location, or hit enter to accept default: [/var/log/messages]:')
    if messagesDirectory == '':
        messagesDirectory = '/var/log/messages'
    else:
        tailMessages = 'n'
tailSecure = raw_input('Monitor secure log [Y/n]:')
if tailSecure == 'y': secureDirectory = raw_input('Type secure log location, or hit enter to accept default: [/var/log/secure]:')
if secureDirectory == '': secureDirectory = '/var/log/secure'
tailAnother = raw_input('Monitor another log file? [Y/n]:')
if tailAnother == 'y': tailAnotherDirectory = raw_input('Type log file location, Example: [/var/log/mylogfile.log]:')
tailAllLogFiles = raw_input('Tail all log files [Y/n]:')
if tailAllLogFiles == 'y': tailAllLogFilesDirectory = raw_input('Type log files directory, or hit enter to accept default: [/var/log/*.log]:')
tailAllLogFilesDirectory = '/var/log/*.log'
tailSecurityLogs = raw_input('Tail all security logs [Y/n]:')
if tailSecurityLogs == 'y': tailSecurityLogsDirectory = raw_input('Type secure log files directory, or hit enter to accept default: [/security_logs/*]:')
tailSecurityLogsDirectory = 'security_logs/*'
reportFileOwnershipChanges= raw_input('Report ownership changes during integrity monitoring? [Y/n]:')
if reportFileOwnershipChanges == 'y': reportOwnershipChanges = 'yes'
else: reportOwnershipChanges = 'no'
reportFilePermissionChanges = raw_input('Report permissions changes during integrity monitoring? [Y:n]')
if reportFilePermissionChanges == 'y': reportPermissionChanges = 'yes'
else: reportPermissionChanges = 'no'
modificationCheckFrequency = raw_input('Enter the time in minutes to re-scan directories for modifications, or hit enter to accept the default: [60]:')
if modificationCheckFrequency == '': modificationCheckFrequency = '60'
scanFrequency = raw_input('Enter the scan frequency for monitoring, or hit enter to accept the default: [60]:')
if scanFrequency == '': scanFrequency ='60'
hearbeatFrequency = raw_input('Enter the hearbeat frequency, or hit enter to accept the default: [300]:')
if hearbeatFrequency == '': hearbeatFrequency = '300'
sendCompressedEvents = raw_input('Do you want to send client events compressed: [Y/n]:')
if sendCompressedEvents == 'y': sendCompressedEvents = '1'
else:
    sendCompressedEvents = '0'

# Create the XML File

print '\n','Generating XML...','\n'
print '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
print '<options xmlns:xi="http://www.w3.org/2003/XInclude">'
print '\t<!-- This LCE Client file created by LCPCreator -->\n'

print '\t<!-- LCE client log messages are written to a file named according to the date in the directory specified below. -->'
print '\t<log-directory>', logDirectory, '</log-directory>\n'

print '\n\t<!-- monitors process accounting and BSM auditing for process execution -->\n'
if processAccounting =='y': print '\t<accounting-file>' + processAccountingDirectory + '</accounting-file>'

print '\n\t<!-- The files specified below are tailed. -->\n'
if tailMessages == 'y': print '\t<tail-dir>' + messagesDirectory + '</tail-dir>'
if tailSecure == 'y': print '\t<tail-dir>'+ secureDirectory + '</tail-dir>'
if tailAnother == 'y': print '\t<tail-dir>'+ tailAnotherDirectory +'<tail-dir>'
if tailAllLogFiles == 'y': print '\t<tail-dir>'+ tailAllLogFilesDirectory +'</tail-dir>'
if tailSecurityLogs == 'y': print '\t<tail-dir>'+ tailSecurityLogsDirectory +'</tail-dir>'

print '\n\t<!-- When the following options are enabled, changes to ownership and permissions will be reported for the above monitored files and directories. -->\n'
print '\t<report-ownership-changes>'+ reportOwnershipChanges +'</report-ownership-changes>'
print '\t<report-permissions-changes>'+ reportPermissionChanges +'</report-permissions-changes>'

print '\n\t<!-- The next setting determines the frequency, in minutes, with which monitored files and directories will be re-scanned for changes. -->\n'
print '\t<modification-check-frequency>'+ modificationCheckFrequency +'</modification-check-frequency>'
print '\t<scan-frequency>'+ scanFrequency +'</scan-frequency>'
print '\t<heartbeat-frequency>'+ hearbeatFrequency +'</heartbeat-frequency>'
print '\t<compress-events>'+ sendCompressedEvents +'</compress-events>'
print '\n','Done'








