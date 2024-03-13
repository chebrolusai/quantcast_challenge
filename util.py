import re
import os
import data_integrity
import time

ALLOWED_OPTIONS_CONSTANT     = {'d'}
MONTHS_WITH_30_DAYS_CONSTANT = {2,4,6,9,11}

def parse_command_line_arguments(aInputArguments) -> dict:
    # Strictly expects the format filespec -option date

    dParsedArguments = {}

    dParsedArguments['fileSpec'] = aInputArguments[0]
    dParsedArguments['option']   = aInputArguments[1][1:]
    dParsedArguments['date']     = aInputArguments[2]

    return dParsedArguments


def check_for_valid_input_options(aInputOptions):

    for option in aInputOptions:

        if option not in ALLOWED_OPTIONS_CONSTANT:

            data_integrity.failed(errorString="Invalid option. Program only supports option d",exitCode=2)



def check_if_filespec_exists(aFileSpecs):
    
    for fileSpec in aFileSpecs:

        if not os.path.exists(fileSpec):

            data_integrity.failed(errorString=f'Filepath "{fileSpec}" does not exist.',exitCode=1)

        elif os.path.isdir(fileSpec):

            data_integrity.failed(errorString=f'"{fileSpec}" is a directory.',exitCode=1)



def validate_date_format(date):
    # validates the date in the UTC format YYYY-MM-DD

    reMatch = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date)

    if reMatch:
        year , month, day = reMatch.groups()

        convertedyear  = int(year)
        convertedMonth = int(month)
        convertedDay   = int(day)

        if convertedMonth > 12 :
            data_integrity.failed(errorString="Invalid Month provided", exitCode=2)
        
        # Checks for month feb
        if convertedMonth == 2:
            
            if convertedDay > 29:

                data_integrity.failed(errorString="Invalid day for Feb provided", exitCode=2)
            
            if convertedDay == 29 and convertedyear % 4 != 0:

                data_integrity.failed(errorString="Invalid day for Feb provided", exitCode=2)
        
        # Validate days
        if convertedDay > 31 :

            data_integrity.failed(errorString="Invalid day provided",exitCode=2)
        
        if convertedDay == 31 and convertedMonth in MONTHS_WITH_30_DAYS_CONSTANT:

            data_integrity.failed(errorString="Invalid Day provided for the month", exitCode=2)
                
    
    else:
        data_integrity.failed(errorString="Please give a valid date in the format YYYY-MM-DD",exitCode=2)