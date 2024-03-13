import sys
import os
import util
import re
import data_integrity


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