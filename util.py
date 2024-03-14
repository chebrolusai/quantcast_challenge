import re
import os

ALLOWED_OPTIONS_CONSTANT     = {'d'}
MONTHS_WITH_30_DAYS_CONSTANT = {2,4,6,9,11}

def parse_command_line_arguments(aInputArguments) -> dict:
    # Strictly expects the format,  filespec -option date

    dParsedArguments = {}

    dParsedArguments['fileSpec'] = aInputArguments[0]
    dParsedArguments['option']   = aInputArguments[1][1:]
    dParsedArguments['date']     = aInputArguments[2]

    return dParsedArguments


def check_for_valid_input_options(aInputOptions) -> bool:
    # Checks if the option provided to the program is valid and expected

    for option in aInputOptions:

        if option not in ALLOWED_OPTIONS_CONSTANT:

           return False
    
    return True



def check_if_filespec_exists(fileSpec) -> bool:

    if not os.path.exists(fileSpec):

        return False

    elif os.path.isdir(fileSpec):

        return False

    return True

def validate_date_format(date) -> bool:
    # validates the date in the UTC format YYYY-MM-DD

    reMatch = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date)

    if reMatch:
        
        year , month, day = reMatch.groups()

        convertedyear  = int(year)
        convertedMonth = int(month)
        convertedDay   = int(day)

        if convertedMonth > 12 :
            
            return "Invalid Month provided"
        
        # Checks for month feb
        if convertedMonth == 2:
            
            if convertedDay > 29:

                return "Invalid day for Feb provided"
            
            if convertedDay == 29 and convertedyear % 4 != 0:

                return "Invalid day for Feb provided"
        
        # Validate days
        if convertedDay > 31 :

            return "Invalid day provided"
        
        if convertedDay == 31 and convertedMonth in MONTHS_WITH_30_DAYS_CONSTANT:

            return "Invalid Day provided for the month"
                
    
    else:
        return "Please give a valid date in the format YYYY-MM-DD"



def validate_utc_timestamp(timeStamp) -> bool:
    # validates timestamp in the UTC format

    if re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', timeStamp):
        
        return True
    
    else:
        
        return False