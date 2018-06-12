#
# Unit tests for fn_odbc_query/util/function_utils.py
#
#  	100% code coverage
#
#
import unittest
from fn_odbc_query.util.function_utils import str_to_bool, prepare_sql_parameters, validate_data, get_type_sql_statement, prepare_results


class TestFunctionUtils(unittest.TestCase):

    def test_str_to_bool(self):
        print("Testing casting string to boolean....")

        result = str_to_bool("true")
        self.assertEqual(result, True)

        result = str_to_bool("True")
        self.assertEqual(result, True)

        result = str_to_bool("false")
        self.assertEqual(result, False)

        result = str_to_bool("Foo")
        self.assertEqual(result, False)

    def test_prepare_sql_parameters(self):
        print("Testing preparing SQL params....")

        param1 = "p1"
        param2 = "p2"
        param3 = "p3"

        # Test for all None params
        result = prepare_sql_parameters(None, None, None)
        self.assertEqual(result, [])

        # Test for non None params
        result = prepare_sql_parameters(param1, param2, param3)
        self.assertEqual(result, [param1, param2, param3])

        # Test for None params
        result = prepare_sql_parameters(None, param2, param3)
        self.assertEqual(result, [param2, param3])

        result = prepare_sql_parameters(param1, None, param3)
        self.assertEqual(result, [param1, param3])

        result = prepare_sql_parameters(param1, param2, None)
        self.assertEqual(result, [param1, param2])

    def test_validate_data(self):
        print("Testing validating data....")

        sql_query = "Delete from mock_data where id=3"

        # Test for wrong config settings ValueError
        # Not valid json
        # JSONDecodeError exception contains extra information, test if the err contains (assertIn) general error msg
        with self.assertRaises(ValueError) as cm:
            validate_data("insert", sql_query)
        err = cm.exception
        self.assertIn("Restricted SQL statements must be defined in valid JSON format.", str(err))

        with self.assertRaises(ValueError) as cm:
            validate_data("[insert]", sql_query)
        err = cm.exception
        self.assertIn("Restricted SQL statements must be defined in valid JSON format.", str(err))

        with self.assertRaises(ValueError) as cm:
            validate_data("\"insert\"", sql_query)
        err = cm.exception
        self.assertEqual(str(err), "Restricted SQL statements must be defined in valid JSON format as a list using square brackets.")

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
        err = cm.exception
        self.assertEqual(str(err), "User does not have permission to perform delete action.")

    def test_get_type_sql_statement(self):
        """ sql_query cannot be None or empty string, validation in fn_odbc_query_function()"""

        print("Testing getting type of sql statement....")

        sql_query = "Delete from mock_data where id=3"

        result = get_type_sql_statement(sql_query)

        self.assertEqual(result, "delete")

    def test_prepare_results(self):
        print("Testing preparing results....")

        cursor_description = (('sql_column_1', None, 10, 10, 0, True),
                                ('sql_column_2', None, 50, 50, 0, True),
                                ('sql_column_3', None, 50, 50, 0, True))

        rows = [(6, 'Titus', 'Leggon')]

        result = prepare_results(cursor_description, rows)
        self.assertEqual(result, {"entries": [{'sql_column_1': 6, 'sql_column_2': 'Titus', 'sql_column_3': 'Leggon'}]})

        # test None and empty list rows value
        result = prepare_results(cursor_description, None)
        self.assertEqual(result, {"entries": None})

        result = prepare_results(cursor_description, [])
        self.assertEqual(result, {"entries": None})

if __name__ == '__main__':
    unittest.main()

