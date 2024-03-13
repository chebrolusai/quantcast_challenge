ERROR_CONSTANT = 'ERROR: '

def failed(errorString="Unknown error", exitCode=1):

    print(ERROR_CONSTANT + errorString)
    exit(exitCode)