<h1 align="center">Unit Testing</h1>

A directory which contains the script for unit testing the components in most_active_cookie.py and util file

### About

##### ut_utility.py

This will test some of the functions in the util python file such as validation for date, timestamp and input options. It consists of both success and failed test cases to verify the expected behaviour.

##### ut_most_active_cookie.py

This tests the functionality of the most active cookie. It attempts to give various types of arguments to the script. It then verifies the script output to the actual expected output. It covers both success and failed test cases to verify the expected behaviour.

##### mock_data

A sub directory which has mock files to verify the behaviour of the program.

- <b>cookie_tokens.csv</b>: which follows the expected format.
- <b>invalid_format.txt</b>: which has minor alterations in the timestamps and csv values which are meant to be ignored by the program.

### Usage

Depending on the Operating System:

```sh
python3 <ut_utility or ut_most_active_cookie>.py
```

or

```sh
python <ut_utility or ut_most_active_cookie>.py
```
