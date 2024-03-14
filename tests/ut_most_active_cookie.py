import unittest
import sys
import subprocess


class TestMostActiveCookie(unittest.TestCase):

    def test_most_active_cookie_1(self):
        
        # Test case 1 (success case): valid file, valid option, valid date
        print("------ Test case 1 (success) -------")
        print("# Test case 1 (success case): valid file, valid option, valid date")

        scriptCommand = f"python3 {sys.path[0]}/../most_active_cookie.py ./tests/mock_data/cookie_tokens.csv -d 2018-12-09"

        expectedOutput = "AtY0laUfhglK3lC7\n"

        print("\n"+'SCRIPT_COMMAND: ' + scriptCommand)
        print("\n"+'EXPECTED_OUTPUT: ' + "\n" + expectedOutput)

        output = subprocess.check_output(scriptCommand,shell=True,universal_newlines=True)

        self.assertEqual(output,expectedOutput)

        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ output)

    def test_most_active_cookie_2(self):
    
        # Test case 2 (failure case): valid file, invalid content
        print("------ Test case 2 (success) -------")
        print("# Test case 2 (success case): valid file, some invalid content")

        scriptCommand = f"python3 {sys.path[0]}/../most_active_cookie.py ./tests/mock_data/invalid_format.csv -d 2018-12-08"

        expectedOutput = "4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n"


        print("\n"+'SCRIPT_COMMAND: ' + scriptCommand)
        print("\n"+'EXPECTED_OUTPUT: ' + "\n" + expectedOutput)

        output = subprocess.check_output(scriptCommand,shell=True,universal_newlines=True)

        self.assertCountEqual(output,expectedOutput)

        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ output)

    
    def test_most_active_cookie_3(self):
    
        # Test case 3 (failure case): valid file, valid option, invalid date
        print("------ Test case 3 (failure) -------")
        print("# Test case 3 (failure case): valid file, valid option, invalid date")

        scriptCommand = f"python3 {sys.path[0]}/../most_active_cookie.py ./tests/mock_data/cookie_tokens.csv -d 2023-02-29"


        print("\n"+'SCRIPT_COMMAND: ' + scriptCommand)
        print("\n"+'EXPECTED_OUTPUT: ' + "\n" + 'Error Message')

        output      = ''
        return_code = None

        try:
            output = subprocess.check_output(scriptCommand,shell=True,universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output      = e.output
            return_code = e.returncode


        self.assertNotEqual(return_code,0)

        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ output)

    
    def test_most_active_cookie_4(self):
    
        # Test case 4 (failure case): valid file, invalid option, valid date
        print("------ Test case 4 (failure) -------")
        print("# Test case 4 (failure case): valid file, invalid option, valid date")

        scriptCommand = f"python3 {sys.path[0]}/../most_active_cookie.py ./tests/mock_data/cookie_tokens.csv -s 2023-04-19"


        print("\n"+'SCRIPT_COMMAND: ' + scriptCommand)
        print("\n"+'EXPECTED_OUTPUT: ' + "\n" + 'Error Message')

        output      = ''
        return_code = None

        try:
            output = subprocess.check_output(scriptCommand,shell=True,universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output      = e.output
            return_code = e.returncode


        self.assertNotEqual(return_code,0)

        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ output)
    
    def test_most_active_cookie_5(self):
    
        # Test case 5 (failure case): multiple valid file, valid option, valid date 
        print("------ Test case 5 (failure) -------")
        print("# Test case 5 (failure case): multiple valid files, invalid option, valid date")

        scriptCommand = f"python3 {sys.path[0]}/../most_active_cookie.py ./tests/mock_data/cookie_tokens.csv ./tests/mock_data/cookie_tokens.csv -d 2023-04-19"


        print("\n"+'SCRIPT_COMMAND: ' + scriptCommand)
        print("\n"+'EXPECTED_OUTPUT: ' + "\n" + 'Error Message')

        output      = ''
        return_code = None

        try:
            output = subprocess.check_output(scriptCommand,shell=True,universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output      = e.output
            return_code = e.returncode


        self.assertNotEqual(return_code,0)

        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ output)
    
    
    
    def test_most_active_cookie_6(self):
        
        # Test case 5 (success case): valid file, valid option, valid date - multiple results
        print("------ Test case 6 (success) -------")
        print("# Test case 6 (success case): valid file, valid option, valid date - multiple results")

        scriptCommand = f"python3 {sys.path[0]}/../most_active_cookie.py ./tests/mock_data/cookie_tokens.csv -d 2018-12-08"

        expectedOutput = "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n"

        print("\n"+'SCRIPT_COMMAND: ' + scriptCommand)
        print("\n"+'EXPECTED_OUTPUT: ' + "\n" + expectedOutput)

        output = subprocess.check_output(scriptCommand,shell=True,universal_newlines=True)

        self.assertCountEqual(output,expectedOutput)

        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ output)


if __name__ == '__main__':
    sys.stdout = sys.__stdout__
    unittest.main()