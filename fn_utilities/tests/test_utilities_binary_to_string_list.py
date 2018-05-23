# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import unittest
import logging
import sys
import os
from fn_utilities.components.utilities_binary_to_string_list_floss import extract_strings

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

        listStrings = extract_strings(data)

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