import sys
import re
import util
import data_integrity

READ_ONLY_CONSTANT = 'r'

if sys.argv.__len__() < 4:
    
    data_integrity.failed("Specify both the log file, and date with -d",2)

if sys.argv.__len__() > 4:
    
    data_integrity.failed("Too many number of arguments passed. Specify only the log filespec, and date with -d ",2)


# Parse input arguments
dParsedArguments = util.parse_command_line_arguments(sys.argv[1:])

# Check if file exists
if not util.check_if_filespec_exists(dParsedArguments.get('fileSpec')):

    data_integrity.failed(errorString="Please provide a valid filepath.",exitCode=2)

# Check for vaalid input option
if not util.check_for_valid_input_options([dParsedArguments.get('option')]):

     data_integrity.failed(errorString="Invalid option. Program only supports option d",exitCode=2)

# Check for date format and if it is valid
dateValidation = util.validate_date_format(dParsedArguments['date'])

if dateValidation is not None:

    data_integrity.failed(errorString=dateValidation, exitCode=2)



dFileOutputObject  = {}
dMaxOccurance      = {}

DATE_MATCH_CONSTANT = re.compile(dParsedArguments['date'])

# Parse files - currently would contain only 1 file
for eachFile in [dParsedArguments.get('fileSpec')]:

    with open(eachFile, READ_ONLY_CONSTANT) as file:

        for line in file:

            if not line.strip():
                continue

            aCommaSeparatedValues = line.strip().split(',')
            
            if len(aCommaSeparatedValues) != 2:

                data_integrity.failed(errorString="Invalid file format",exitCode=2)
            
            
            token, timeStamp = aCommaSeparatedValues

            if util.validate_utc_timestamp(timeStamp) and DATE_MATCH_CONSTANT.match(timeStamp):
                
                if eachFile not in dFileOutputObject:
                    dFileOutputObject[eachFile] = {}
                
                if token not in dFileOutputObject[eachFile]:
                    dFileOutputObject[eachFile][token] = {'count': 0} 
                    dMaxOccurance[eachFile] = 1

                dFileOutputObject[eachFile][token]['count'] += 1

                if dFileOutputObject[eachFile][token]['count'] > dMaxOccurance[eachFile]:
                    dMaxOccurance[eachFile] = dFileOutputObject[eachFile][token]['count']


for file in dFileOutputObject:

    for token in dFileOutputObject[file]:

        if dFileOutputObject[file][token]['count']  == dMaxOccurance[file]:

            print(token)