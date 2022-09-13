# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_odbc_query.util import function_utils, odbc_utils

PACKAGE_NAME = "fn_odbc_query"
FN_NAME = "fn_odbc_query"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_odbc_query'"""

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
        sql_condition_value1 = getattr(fn_inputs, "sql_condition_value1", None)
        sql_condition_value2 = getattr(fn_inputs, "sql_condition_value2", None)
        sql_condition_value3 = getattr(fn_inputs, "sql_condition_value3", None)

        # Log parameers
        self.LOG.info(str(fn_inputs))

        sql_params = function_utils.prepare_sql_parameters(sql_condition_value1, sql_condition_value2,
                                                           sql_condition_value3)

        # Validate app.config settings
        validate_fields(["sql_connection_string"], self.options)

        sql_connection_string = self.options["sql_connection_string"]
        sql_restricted_sql_statements = self.options.get("sql_restricted_sql_statements", None)
        sql_autocommit = function_utils.str_to_bool(self.options.get("sql_autocommit", False))
        sql_query_timeout = int(self.options.get("sql_query_timeout")) \
            if self.options.get("sql_query_timeout") else None
        sql_database_type = self.options.get("sql_database_type").lower() \
            if self.options.get("sql_database_type") else None
        sql_number_of_records_returned = int(self.options["sql_number_of_records_returned"]) \
            if self.options.get("sql_number_of_records_returned") else None

        # Validate Data
        function_utils.validate_data(sql_restricted_sql_statements, sql_query)

        try:
            # Connect with ODBC
            odbc_connection = odbc_utils.OdbcConnection(sql_connection_string, sql_autocommit, sql_query_timeout)
            odbc_connection.configure_unicode_settings(sql_database_type)
            odbc_connection.create_cursor()

            # Check what SQL statement is executed, get the first word in sql_query
            sql_statement = function_utils.get_type_sql_statement(sql_query)

            if sql_statement == 'select':

                self.LOG.debug(u"Query: %s. Params: %s. Fetching %s records.",
                               sql_query, sql_params, sql_number_of_records_returned)

                rows = odbc_connection.execute_select_statement(sql_query, sql_params, sql_number_of_records_returned)
                results = function_utils.prepare_results(odbc_connection.get_cursor_description(), rows)
                self.LOG.info(json.dumps(str(results)))

                if results.get("entries") is None:
                    yield StatusMessage("No query results returned...")
                else:
                    yield StatusMessage("Result contains {} entries...".format(len(results.get("entries"))))

            elif sql_statement == 'update' or sql_statement == 'delete' \
                    or sql_statement == 'insert':

                self.LOG.debug(u"Query: %s. Params: %s.", sql_query, sql_params)

                # Return row count and set results to empty list
                row_count = odbc_connection.execute_odbc_query(sql_query, sql_params)
                results = function_utils.prepare_results(None, None)

                self.LOG.info(u"%s rows processed", row_count)
                yield StatusMessage("{} rows processed".format(row_count))

            else:
                self.LOG.error(u"SQL statement '%s' is not supported", sql_statement)
                raise ValueError("SQL statement '{}' is not supported".format(sql_statement))

        except Exception as err:
            raise IntegrationError(str(err))

        # Commit changes and tear down connection
        finally:
            yield StatusMessage("Closing ODBC connection...")

            if odbc_connection:
                odbc_connection.close_connections()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
