# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test fn_floss.component.function_floss"""
import unittest
import logging
import sys
import os
from fn_floss.lib.floss_util import extract_strings, get_floss_params

log = logging.getLogger(__name__)

TESTCASE_INPUT        = 'sample1.zip'
TESTCASE_EXPECTED_OUTPUT = 'sample1-zip-floss-output.txt'

class TestFunctionFloss(unittest.TestCase):
    def setUp(self):
        pass

    def testExtractString(self):
        """
        test extract strings from binary data
        :return:
        """
        # Get the filename path of the floss testcase file and the expected output.
        dirTestData = os.path.join(os.getcwd(), 'data')
        fileTestcase = os.path.join(dirTestData, TESTCASE_INPUT)
        fileExpected = os.path.join(dirTestData, TESTCASE_EXPECTED_OUTPUT)

        # Open and read the testcase file
        try:
            with open(fileTestcase, 'r') as fileInput:
                data = fileInput.read()
        except Exception as err:
            raise err

        # Use commandline args -q quiet mode, -s shellcode, -n 5 minimum characters 5
        str_floss_options = '-q,-s,-n 5'
        listStrings = extract_strings(str_floss_options, data)

        # Open and read the file containing the expected output from floss string extractor
        try:
            with open(fileExpected, 'r') as fileExpected:
                listExpectedStrings = fileExpected.read().splitlines()
        except Exception as err:
            raise err

        # Compare just computed output from floss on the testcase to known expected output.
        self.assertListEqual(listStrings, listExpectedStrings)

    def tearDown(self):
        pass

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger(__name__).setLevel( logging.DEBUG )
    unittest.main()
    
