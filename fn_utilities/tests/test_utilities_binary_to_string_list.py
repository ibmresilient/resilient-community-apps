# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test fn_utilities.component.utilities_binary_to_string_list"""
import unittest
import logging
import sys
import os
from fn_utilities.lib.utilities_binary_to_string_list_util import extract_strings

log = logging.getLogger(__name__)

TESTCASE_INPUT        = 'sample1.zip'
TESTCASE_KNOWN_OUTPUT = 'sample1-zip-floss-output.txt'

class TestBinaryToStringList(unittest.TestCase):
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
        fileTestcaseKnown = os.path.join(dirTestData, TESTCASE_KNOWN_OUTPUT)

        # Open the read the testcase file
        try:
            fileInput = open(fileTestcase, 'r')
            data = fileInput.read()
        except Exception as err:
            raise err
        finally:
            fileInput.close()

        # Use commandline args -q quiet mode, -s shellcode, -n 5 minimum characters 5
        str_floss_options = '-q,-s,-n 5'
        listStrings = extract_strings(str_floss_options, data)

        # Open and read the file containing the expected output from floss string extractor
        try:
            fileKnownOutput = open(fileTestcaseKnown, 'r')
            listKnownStrings = fileKnownOutput.read().splitlines()
        except Exception as err:
            raise err
        finally:
            fileKnownOutput.close()

        # Compare just computed output from floss on the testcase to known expected output.
        self.assertListEqual(listStrings, listKnownStrings)

    def tearDown(self):
        pass

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger(__name__).setLevel( logging.DEBUG )
    unittest.main()