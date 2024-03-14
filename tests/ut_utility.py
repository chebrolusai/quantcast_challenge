import unittest
import sys

sys.path.append(sys.path[0]+'/..')
from util import check_for_valid_input_options, validate_date_format, validate_utc_timestamp

class TestUtilityFunctions(unittest.TestCase):
    
    
    def test_input_options(self):

        aAllowedInputOptions   = ['d']
        aIncorrectInputOptions = ['d','a','p']

        self.assertTrue(check_for_valid_input_options(aAllowedInputOptions))

        self.assertFalse(check_for_valid_input_options(aIncorrectInputOptions))

    
    def test_valid_date(self):

        incorrectDateFormat   = '2024/15/15'

        incorrectDateFormatResult = validate_date_format(incorrectDateFormat)

        self.assertNotEqual(incorrectDateFormatResult,None)

        correctDateFormat   = '2024-07-05'

        correctDateFormatResult = validate_date_format(correctDateFormat)

        self.assertEqual(correctDateFormatResult,None)


        invalidDate = '2024/14/14'

        invalidDateResult = validate_date_format(invalidDate)

        self.assertNotEqual(invalidDateResult,None)

        validDate = '2024-02-29'

        validDateResult = validate_date_format(validDate)

        self.assertEqual(validDateResult,None)
    

    def test_valid_utc_timestamp(self):

        correctUtcDate = '2018-12-09T14:19:00+00:00'

        correctUtcDateResult = validate_utc_timestamp(correctUtcDate)

        self.assertTrue(correctUtcDateResult)

        incorrectUtcDate = '2018-12-0914:1900+00:00'

        incorrectUtcDateResult = validate_utc_timestamp(incorrectUtcDate)

        self.assertFalse(incorrectUtcDateResult)


if __name__ == '__main__':
    unittest.main()