import re
import os
import data_integrity
import time

ALLOWED_OPTIONS_CONSTANT     = {'d'}

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


