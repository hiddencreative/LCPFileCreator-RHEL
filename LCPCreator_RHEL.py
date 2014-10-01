__author__ = 'josefweiss'

# Set default values
#logDirectoryInput = 'n'
#processAccountingInput = 'y'
#tailMessagesInput = 'y'


# Print description of what this script will do.

print '\n','This script will generate the required XML output for a RHEL LCP file.'
print 'The default choice for each question is in capital letters.  To accept the default you may simply hit [Enter]','\n'

# Get log directory location
logDirectoryInput = raw_input('The LCE client log directory will be set to default location of: [/opt/lce/client/], Change it? [y/N]:')
if logDirectoryInput == '':
    logDirectory = '/opt/lce/client/'
else:
    logDirectory = raw_input('Enter full LCE client log directory location, with backslash, such as [/opt/lce/client/]:')

# Set up process accounting directory information
processAccountingInput = raw_input('Monitor process accounting and BSM auditing?  Saying yes will enable process accounting. [y/N]:')
if processAccountingInput == 'y':
    processAccountingDirectory = raw_input('Accounting file location, will be set to default: [/var/account/pacct], Change it: [y/N]:')
    if processAccountingDirectory == '':
        processAccountingDirectory = '/var/account/pacct'
    else:
        processAccountingDirectory = raw_input('Enter location of process accounting file, such as [/var/account/paccr];')
else:
    processAccountingInput == 'n'

# Set up monitoring of messages log
tailMessagesInput = raw_input('Monitor messages log [y/N]:')
if tailMessagesInput == 'y':
    messagesDirectory = raw_input('Type messages log location, or hit enter to accept default: [/var/log/messages]:')
    if messagesDirectory == '':
        messagesDirectory = '/var/log/messages'
    else:
        tailMessages = 'n'

# Set up monitoring of secure log
tailSecureInput = raw_input('Monitor secure log [y/N]:')
if tailSecureInput == 'y':
    secureDirectory = raw_input('Type secure log location, or hit enter to accept default: [/var/log/secure]:')
    if secureDirectory =='':
        secureDirectory = '/var/log/secure'
    else:
        secureDirectory = 'n'

# Set a definition here to allow multiple entries of additional log files.
#tailAnother = raw_input('Monitor another log file? [Y/n]:')
#if tailAnother =='y':
#    tailAnotherDirectory = raw_input('Type log file location, Example: [/var/log/mylogfile.log]:')


tailAllLogFilesInput = raw_input('Tail all log files [Y/n]:')
if tailAllLogFilesInput == 'y':
    tailAllLogFilesDirectory = raw_input('Type log files directory, or hit enter to accept default: [/var/log/*.log]:')
    if tailAllLogFilesDirectory == '':
        tailAllLogFilesDirectory = '/var/log/*.log'
    else:
        tailAllLogFilesDirectory = tailAllLogFilesDirectory
else:
    tailAllLogFilesInput =='n'



tailSecurityLogs = raw_input('Tail all security logs [Y/n]:')
if tailSecurityLogs == 'y': tailSecurityLogsDirectory = raw_input('Type secure log files directory, or hit enter to accept default: [/security_logs/*]:')
tailSecurityLogsDirectory = 'security_logs/*'



reportFileOwnershipChangesInput= raw_input('Report ownership changes during integrity monitoring? [Y/n]:')
if reportFileOwnershipChangesInput == 'y': reportOwnershipChanges = 'yes'
else:
    reportOwnershipChanges = 'no'


reportFilePermissionChangesInput = raw_input('Report permissions changes during integrity monitoring? [Y:n]')
if reportFilePermissionChangesInput == 'y': reportPermissionChanges = 'yes'
else:
    reportPermissionChanges = 'no'


modificationCheckFrequencyInput = raw_input('Enter the time in minutes to re-scan directories for modifications, or hit enter to accept the default: [60]:')
if modificationCheckFrequencyInput == '': modificationCheckFrequency = '60'
else:
    modificationCheckFrequency = modificationCheckFrequencyInput

scanFrequencyInput = raw_input('Enter the scan frequency for monitoring, or hit enter to accept the default: [60]:')
if scanFrequencyInput == '': scanFrequency ='60'
else:
    scanFrequency = scanFrequencyInput

hearbeatFrequencyInput = raw_input('Enter the hearbeat frequency, or hit enter to accept the default: [300]:')
if hearbeatFrequencyInput == '': hearbeatFrequency = '300'
else:
    hearbeatFrequency = hearbeatFrequencyInput

sendCompressedEvents = raw_input('Do you want to send client events compressed: [Y/n]:')
if sendCompressedEvents == 'y': sendCompressedEvents = '1'
else:
    sendCompressedEvents = '0'


def createXMLfile():

    print '\n','Generating XML...','\n'
    print '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
    print '<options xmlns:xi="http://www.w3.org/2003/XInclude">'
    print '\t<!-- This LCE Client file created by LCPCreator -->\n'

    print '\t<!-- LCE client log messages are written to a file named according to the date in the directory specified below. -->'
    print '\t<log-directory>', logDirectory, '</log-directory>\n'

    print '\n\t<!-- monitors process accounting and BSM auditing for process execution -->\n'
    if processAccountingInput =='y': print '\t<accounting-file>' + processAccountingDirectory + '</accounting-file>'

    print '\n\t<!-- The files specified below are tailed. -->\n'
    if tailMessagesInput == 'y': print '\t<tail-dir>' + messagesDirectory + '</tail-dir>'
    if tailSecureInput == 'y': print '\t<tail-dir>'+ secureDirectory + '</tail-dir>'
    if tailAnotherInput == 'y': print '\t<tail-dir>'+ tailAnotherDirectory +'<tail-dir>'
    if tailAllLogFilesInput == 'y': print '\t<tail-dir>'+ tailAllLogFilesDirectory +'</tail-dir>'
    if tailSecurityLogsInput == 'y': print '\t<tail-dir>'+ tailSecurityLogsDirectory +'</tail-dir>'

    print '\n\t<!-- When the following options are enabled, changes to ownership and permissions will be reported for the above monitored files and directories. -->\n'
    print '\t<report-ownership-changes>'+ reportOwnershipChanges +'</report-ownership-changes>'
    print '\t<report-permissions-changes>'+ reportPermissionChanges +'</report-permissions-changes>'

    print '\n\t<!-- The next setting determines the frequency, in minutes, with which monitored files and directories will be re-scanned for changes. -->\n'
    print '\t<modification-check-frequency>'+ modificationCheckFrequency +'</modification-check-frequency>'
    print '\t<scan-frequency>'+ scanFrequency +'</scan-frequency>'
    print '\t<heartbeat-frequency>'+ hearbeatFrequency +'</heartbeat-frequency>'
    print '\t<compress-events>'+ sendCompressedEvents +'</compress-events>'
    print '\n','Done'



print createXMLfile()







