# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.import unittest
import logging
import sys
from fn
_utilities.components.utilities_binary_to_string_list_floss import extract_strings

log = logging.getLogger(__name__)

TESTCASE_INPUT        = './data/sample1.zip'
TESTCASE_KNOWN_OUTPUT = './data/sample1-zip-floss-output.txt'

class TestBinaryToStringList(unittest.TestCase):
    def setUp(self):
        pass

    def testExtractString(self):
        """
        test extract strings from binary data
        :return:
        """
        try:
            fileInput = open(TESTCASE_INPUT, 'r')
            data = fileInput.read()
        except Exception as err:
            raise err
        finally:
            fileInput.close()

        listStrings = extract_strings(data)

        try:
            fileKnownOutput = open(TESTCASE_KNOWN_OUTPUT, 'r')
            listKnownStrings = fileKnownOutput.read().splitlines()
        except Exception as err:
            raise err
        finally:
            fileKnownOutput.close()

        self.assertListEqual(listStrings, listKnownStrings)

    def tearDown(self):
        pass

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger(__name__).setLevel( logging.DEBUG )
    unittest.main()