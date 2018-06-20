# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Resilient functions component to execute ODBC queries"""

# Set up:
# Destination: a Queue named "fn_odbc_query".
# Manual Action: Execute an ODBC query.

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_odbc_query.util import function_utils, odbc_utils


LOG = logging.getLogger(__name__)
SQL_PYODBC_TIMEOUT_ERROR_STATE = 'HY000'


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_odbc_query'

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
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_odbc_query", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_odbc_query", {})

    @function("fn_odbc_query")
    def _fn_odbc_query_function(self, event, *args, **kwargs):
        """Resilient Function: A function that makes ODBC queries

        Using prepared SQL statements, where parameters are passed to the database separately,
        protecting against SQL injection attacks.

        Inputs:
        Inputs: sql_query: a SQL query with set parameters using a question mark as a place holder,
            SQL statements SELECT, INSERT, UPDATE and DELETE are supported
        sql_condition_value1: value for the question mark - condition value 1
        sql_condition_value2: value for the question mark - condition value 2
        sql_condition_value3: value for the question mark - condition value 3

        """
        odbc_connection = None

        try:
            # Get the function parameters:
            if "sql_query" not in kwargs or kwargs.get("sql_query") == '':
                LOG.error(u"Required field sql_query is missing or empty")
                raise ValueError("Required field sql_query is missing or empty")

            sql_query = self.get_textarea_param(kwargs.get("sql_query"))  # textarea

            LOG.info(u"sql_query: %s", sql_query)

            # ------------------------------------------------------
            # When adding more condition input fields to the function, you need to load them here
            # and pass the new variable/s to the function_utils.prepare_sql_parameters().
            # ------------------------------------------------------
            sql_condition_value1 = kwargs.get("sql_condition_value1")  # text
            sql_condition_value2 = kwargs.get("sql_condition_value2")  # text
            sql_condition_value3 = kwargs.get("sql_condition_value3")  # text

            LOG.info(u"sql_condition_value1: %s", sql_condition_value1)
            LOG.info(u"sql_condition_value2: %s", sql_condition_value2)
            LOG.info(u"sql_condition_value3: %s", sql_condition_value3)

            sql_params = function_utils.prepare_sql_parameters(sql_condition_value1, sql_condition_value2,
                                                               sql_condition_value3)

            # Read configuration settings:
            if "sql_connection_string" in self.options:
                sql_connection_string = self.options["sql_connection_string"]
            else:
                LOG.error(u"Mandatory config setting 'sql_connection_string' not set.")
                raise ValueError("Mandatory config setting 'sql_connection_string' not set.")

            sql_restricted_sql_statements = self.options["sql_restricted_sql_statements"] \
                if "sql_restricted_sql_statements" in self.options else None

            sql_autocommit = function_utils.str_to_bool(self.options["sql_autocommit"]) \
                if "sql_autocommit" in self.options else False

            sql_query_timeout = int(self.options["sql_query_timeout"]) \
                if "sql_query_timeout" in self.options else None

            sql_database_type = self.options["sql_database_type"].lower() \
                if "sql_database_type" in self.options else None

            sql_number_of_records_returned = int(self.options["sql_number_of_records_returned"]) \
                if "sql_number_of_records_returned" in self.options else None

            sql_pyodbc_timeout_error_state = self.options["sql_pyodbc_timeout_error_state"] \
                if "sql_pyodbc_timeout_error_state" in self.options else SQL_PYODBC_TIMEOUT_ERROR_STATE

            yield StatusMessage("Starting...")

            yield StatusMessage("Validating...")
            function_utils.validate_data(sql_restricted_sql_statements, sql_query)

            yield StatusMessage("Opening ODBC connection...")
            odbc_connection = odbc_utils.OdbcConnection(sql_connection_string, sql_autocommit,
                                                        sql_query_timeout, sql_pyodbc_timeout_error_state)
            odbc_connection.configure_unicode_settings(sql_database_type)
            odbc_connection.create_cursor()

            yield StatusMessage("Executing an ODBC query...")
            # Check what SQL statement is executed, get the first word in sql_query
            sql_statement = function_utils.get_type_sql_statement(sql_query)

            if sql_statement == 'select':

                LOG.debug(u"Query: %s. Params: %s. Fetching %s records.",
                         sql_query, sql_params, sql_number_of_records_returned)

                rows = odbc_connection.execute_select_statement(sql_query, sql_params, sql_number_of_records_returned)
                results = function_utils.prepare_results(odbc_connection.get_cursor_description(), rows)
                LOG.info(json.dumps(results))

                if results.get("entries") is None:
                    yield StatusMessage("No query results returned...")
                else:
                    yield StatusMessage("Result contains {} entries...".format(len(results.get("entries"))))

            elif sql_statement == 'update' or sql_statement == 'delete' \
                    or sql_statement == 'insert':

                LOG.debug(u"Query: %s. Params: %s.", sql_query, sql_params)

                # Return row count and set results to empty list
                row_count = odbc_connection.execute_odbc_query(sql_query, sql_params)
                results = function_utils.prepare_results(None, None)

                LOG.info(u"%s rows processed", row_count)
                yield StatusMessage("{} rows processed".format(row_count))

            else:
                LOG.error(u"SQL statement '%s' is not supported", sql_statement)
                raise ValueError("SQL statement '{}' is not supported".format(sql_statement))

            yield StatusMessage("Done...")
            yield FunctionResult(results)

        except Exception as err:
            LOG.error(str(err))
            raise FunctionError(str(err))

        # Commit changes and tear down connection
        finally:
            yield StatusMessage("Closing ODBC connection...")

            if odbc_connection:
                odbc_connection.close_connections()

