# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# Unit tests for fn_odbc_query/util/function_utils.py
import unittest
from fn_odbc_query.util.function_utils import validate_data, prepare_results

class TestFunctionUtils(unittest.TestCase):

    def test_validate_data(self):
        sql_query = "Delete from mock_data where id=3"

        # Test for wrong config settings ValueError
        # Not valid json
        # JSONDecodeError exception contains extra information, test if the err contains (assertIn) general error msg
        with self.assertRaises(ValueError) as cm:
            validate_data("insert", sql_query)
        self.assertIn("Restricted SQL statements must be defined in valid JSON format.", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            validate_data("[insert]", sql_query)
        self.assertIn("Restricted SQL statements must be defined in valid JSON format.", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            validate_data("\"insert\"", sql_query)
        self.assertEqual(str(cm.exception), "Restricted SQL statements must be defined in valid JSON format as a list using square brackets.")

        # Test for config settings that pass
        validate_data(None, sql_query)

        validate_data("", sql_query)

        validate_data("[]", sql_query)

        validate_data("[\" insert \"]", sql_query)

        validate_data("[\"INSERT\"]", sql_query)

        validate_data("[\"insert\", \"update\"]", sql_query)

        # Test for NOT allowed statement exception
        with self.assertRaises(Exception) as cm:
            validate_data("[\"delete\"]", sql_query)
        self.assertEqual(str(cm.exception), "User does not have permission to perform delete action.")

    def test_get_type_sql_statement(self):
        """ sql_query cannot be None or empty string, validation in fn_odbc_query_function()"""

        sql_query = "Delete from mock_data where id=3"

        result = sql_query.split(None, 1)[0].lower()

        self.assertEqual(result, "delete")

    def test_prepare_results(self):

        cursor_description = (('sql_column_1', None, 10, 10, 0, True),
                              ('sql_column_2', None, 50, 50, 0, True),
                              ('sql_column_3', None, 50, 50, 0, True))

        result = prepare_results(cursor_description, [(6, 'Titus', 'Leggon')])
        self.assertEqual(result, {"entries": [{'sql_column_1': 6, 'sql_column_2': 'Titus', 'sql_column_3': 'Leggon'}]})

        # test None and empty list rows value
        result = prepare_results(cursor_description, None)
        self.assertEqual(result, {"entries": None})

        result = prepare_results(cursor_description, [])
        self.assertEqual(result, {"entries": None})

if __name__ == '__main__':
    unittest.main()
