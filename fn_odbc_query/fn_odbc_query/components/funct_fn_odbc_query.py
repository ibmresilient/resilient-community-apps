# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from json import dumps

from fn_odbc_query.util import function_utils, odbc_utils
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                StatusMessage, app_function)
from resilient_lib import IntegrationError, str_to_bool, validate_fields

PACKAGE_NAME = "fn_odbc_query"
FN_NAME = "fn_odbc_query"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_odbc_query'

    The Function executes an ODBC query and takes the following parameters:
        sql_query, sql_condition_value1, sql_condition_value2, sql_condition_value3

    An example of query parameters might look like the following:

        sql_select:
        SELECT id AS sql_column_1, first_name AS sql_column_2, last_name AS sql_column_3
            FROM mock_data WHERE id = ?
        DELETE from mock_data WHERE id = ?
        INSERT into mock_data (id, first_name, last_name) values (?, ?, ?)
        UPDATE mock_data SET id = ? WHERE email = ?

        sql_condition_value1: custom condition value 1 | artifact.value | artifact.description | etc
        sql_condition_value2: custom condition value 2 | artifact.value | artifact.description | etc
        sql_condition_value3: custom condition value 3 | artifact.value | artifact.description | etc

    The ODBC query will return a result in JSON format with an entry consisting of key value pairs.

        {
            'entries': [
                {u'sql_column_1': "query_result_column_1_value, u'sql_column_2': u'query_result_column_2_value', ...},
                {u'sql_column_1': query_result_column_1_value, u'sql_column_2': u'query_result_column_2_value', ...}
                ...
            ]
        }
    """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that runs ODBC queries. Parameters are passed to the database separately, protecting against SQL injection attacks.
        Inputs:
        sql_query: a SQL query with set parameters using a question mark as a place holder, SQL statements SELECT, INSERT, UPDATE and DELETE are supported
        sql_condition_value1: value for the question mark - condition value 1
        sql_condition_value2: value for the question mark - condition value 2
        sql_condition_value3: value for the question mark - condition value 3
        Inputs:
            -   fn_inputs.sql_query
            -   fn_inputs.sql_condition_value3
            -   fn_inputs.sql_condition_value1
            -   fn_inputs.sql_condition_value2
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate function parameters
        validate_fields(["sql_query"], fn_inputs)

        # Get the function parameters:
        sql_query = fn_inputs.sql_query
        sql_params = [getattr(fn_inputs, f"sql_condition_value{num}", None) for num in range(1, len(fn_inputs))]

        # Log parameers
        self.LOG.info(str(sql_params))

        # Validate app.config settings
        validate_fields(["sql_connection_string"], self.options)

        sql_connection_string = self.options["sql_connection_string"]
        sql_restricted_sql_statements = self.options.get("sql_restricted_sql_statements", None)
        sql_autocommit = str_to_bool(self.options.get("sql_autocommit", 'False'))
        sql_query_timeout = int(self.options.get("sql_query_timeout")) \
            if self.options.get("sql_query_timeout") else None
        sql_database_type = self.options.get("sql_database_type").lower() \
            if self.options.get("sql_database_type") else None
        sql_number_of_records_returned = int(self.options["sql_number_of_records_returned"]) \
            if self.options.get("sql_number_of_records_returned") else None

        # Validate sql query
        function_utils.validate_data(sql_restricted_sql_statements, sql_query)

        try:
            # Connect with ODBC
            odbc_connection = odbc_utils.OdbcConnection(sql_connection_string, sql_autocommit, sql_query_timeout)
            odbc_connection.configure_unicode_settings(sql_database_type)
            odbc_connection.create_cursor()

            # Check what SQL statement is executed, get the first word in sql_query
            sql_statement = sql_query.split(None, 1)[0].lower()

            if sql_statement == 'select':

                self.LOG.debug(f"Query: {sql_query}. Params: {sql_params}. Fetching {sql_number_of_records_returned} records.")

                rows = odbc_connection.execute_select_statement(sql_query, sql_params, sql_number_of_records_returned)
                results = function_utils.prepare_results(odbc_connection.get_cursor_description(), rows)
                self.LOG.info(dumps(str(results)))

                if results.get("entries"):
                    yield StatusMessage(f"Result contains {len(results.get('entries'))} entries...")
                else:
                    yield StatusMessage("No query results returned...")

            elif sql_statement in ['update', 'delete', 'insert']:
                self.LOG.debug(f"Query: {sql_query}. Params: {sql_params}.")

                # Return row count and set results to empty list
                row_count = odbc_connection.execute_odbc_query(sql_query, sql_params)
                results = {"entries": None}

                self.LOG.info(f"{row_count} rows processed")
                yield StatusMessage(f"{row_count} rows processed")

            else:
                raise ValueError(f"SQL statement '{sql_statement}' is not supported")

        except Exception as err:
            raise IntegrationError(str(err))

        # Commit changes and tear down connection
        finally:
            yield StatusMessage("Closing ODBC connection...")
            if odbc_connection:
                odbc_connection.close_connections()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
