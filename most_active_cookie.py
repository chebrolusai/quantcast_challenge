import sys
import re
import util
import data_integrity

READ_ONLY_CONSTANT = 'r'

if sys.argv.__len__() < 4:
    
    data_integrity.failed("Specify the log file, and date with -d",2)

if sys.argv.__len__() > 4:
    
    data_integrity.failed("Invalid number of arguments passed",2)


# Parse input arguments
dParsedArguments = util.parse_command_line_arguments(sys.argv[1:])

# Check if file exists
util.check_if_filespec_exists([dParsedArguments.get('fileSpec')])

# Check for vaalid input option
util.check_for_valid_input_options([dParsedArguments.get('option')])

# Check for date format and if it is valid
util.validate_date_format(dParsedArguments['date'])



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