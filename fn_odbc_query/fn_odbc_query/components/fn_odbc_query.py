# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Resilient functions component to execute ODBC queries"""

# Set up:
# Destination: a Queue named "fn_odbc_query".
# Manual Action: Execute an ODBC query.

import logging
import pyodbc
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import json

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_odbc_query

    The Function executes an ODBC query and takes the following parameters:
        sql_query, sql_condition_value1, sql_condition_value2, sql_condition_value3

    An example of a set of query parameter might look like the following:

        sql_select: "SELECT incident_id, name, description FROM incidents WHERE incident_id = {sql_condition_value}"
        sql_condition_value1: artifact.value or custom condition value 1
        sql_condition_value2: condition value 2
        sql_condition_value3: condition value 3

    The ODBC query will return a result in JSON format with an entry consisting of sql query results.

        {
            'entries': [
                [u'sql_column_1', u'sql_column_2', u'sql_column_3', ...],
                [u'query_result_column_1_value', u'query_result_column_2_value', u'query_result_column_3_value', ...]
                [u'query_result_column_1_value', u'query_result_column_2_value', u'query_result_column_3_value', ...]
                ...
           ]
        }

    An example of a returned result:

        'entries': [
            [u'incident_id', u'name', u'description'],
            [1, u'Bad incident mysql', u'very bad incident']
        ]}

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
        sql_query: a SQL query with set parameters using a question mark as a place holder
        sql_condition_value1: value for the question mark - condition value 1
        sql_condition_value2: value for the question mark - condition value 2
        sql_condition_value3: value for the question mark - condition value 3

        """

        try:
            # Get the function parameters:
            sql_query = self.get_textarea_param(kwargs.get("sql_query"))  # text with value string: "SELECT incident_id, name, description FROM test.incidents WHERE incident_id = ?"
            sql_condition_value1 = kwargs.get("sql_condition_value1")  # text
            sql_condition_value2 = kwargs.get("sql_condition_value2")  # text
            sql_condition_value3 = kwargs.get("sql_condition_value3")  # text

            LOG.info("sql_query: %s", sql_query)
            LOG.info("sql_condition_value1: %s", sql_condition_value1)
            LOG.info("sql_condition_value2: %s", sql_condition_value2)
            LOG.info("sql_condition_value3: %s", sql_condition_value3)

            sql_args = []
            sql_args.extend(sql_condition_value1 if sql_condition_value1 is not None else [])
            sql_args.extend(sql_condition_value2 if sql_condition_value2 is not None else [])
            sql_args.extend(sql_condition_value3 if sql_condition_value3 is not None else [])

            yield StatusMessage("starting...")
            self.validate_data(sql_query, sql_args)

            yield StatusMessage("Opening ODBC connection...")
            self.setup_odbc_connection()

            yield StatusMessage("Executing an ODBC query...")
            results = self.execute_odbc_query(sql_query, sql_args)

            yield StatusMessage("done...")
            LOG.info(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as ex:
            LOG.error(str(ex))
            # Clean up here as well, yield FunctionError() will prevent executing finally block
            self.close_connections()
            yield FunctionError()

        # Clean up actions
        finally:
            yield StatusMessage("Closing ODBC connection...")
            self.close_connections()

    def validate_data(self, sql_query, sql_arg):
        """" Validate input data """
        # TODO test pyodbc sql injection scenarios, test select * "ALL", test multiple where clauses WHERE aa = ? AND bb = ?
        if "sql_allowed_statements" in self.options:
            sql_allowed_statements = self.options["sql_allowed_statements"]
        else:
            raise Exception("Mandatory config setting 'sql_allowed_statements' not set.")

        # Check if sql_query is one of the allowed statements from configuration file



    def setup_odbc_connection(self):
        """" Setup ODBC connection to a SQL server

        Setups up SQL server and connection objects using connection string obtained from the config file.

        """
        if "sql_connection_string" in self.options:
            sql_connection_string = self.options["sql_connection_string"]
        else:
            raise Exception("Mandatory config setting 'sql_connection_string' not set.")
        if "sql_connection_timeout" in self.options:
            sql_connection_timeout = self.options["sql_connection_timeout"]
        else:
            raise Exception("Mandatory config setting 'sql_connection_timeout' not set.")

        # ODBC connection pooling is turned ON by default.
        # Not all database drivers close connections on db_connection.close() to save round trips to the server.
        # Pooling should be set to False to close connection on db_connection.close().
        pyodbc.pooling = False

        try:
            # The connection string credentials, set in the config file
            self.db_connection = pyodbc.connect(sql_connection_string)

            # The connection timeout value, set in the config file
            self.db_connection.timeout = int(sql_connection_timeout)

            # This is just an example that works for PostgreSQL and MySQL, with Python 2.7.
            self.db_connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')

            # Create a cursor from the connection
            self.db_cursor = self.db_connection.cursor()

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not setup the ODBC connection, Exception %s", e)

    def execute_odbc_query(self, sql_query, sql_args):
        """"  Execute SQL statement

        Execute SQL statements using the Cursor execute() function.

        """
        if "sql_number_of_records_returned" in self.options:
            number_records = int(self.options["sql_number_of_records_returned"])

        try:
            # Execute query
            self.db_cursor.execute(sql_query, sql_args)

            # Fetch results
            if number_records is not None:
                rows = self.db_cursor.fetchmany(number_records)
            else:
                rows = self.db_cursor.fetchall()

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_query, e)

        try:
            rows
        except NameError:
            raise Exception("No query results returned")

        return self.prepare_results(rows)

    def prepare_results(self, rows):
        """"  Generate JSON from query results. """
        if rows is None:
            LOG.info("No query results returned")
            return {"entries": None}

        # List of column names from SQL result to use as dictionary keys
        dt_column_keys = [column[0] for column in self.db_cursor.description]

        # Build dictionary: key-value pairs consisting of column name - row value
        entries_data_list = []
        for row in rows:
            if row is None:
                break
            entries_data_list.append(dict(zip(dt_column_keys, row)))

        LOG.info("Result contains %s entries", len(entries_data_list))

        entries = {"entries": [entry for entry in entries_data_list]}

        return entries

    def close_connections(self):
        """"  Delete the cursor and close connection if they are defined. """
        if hasattr(self, 'db_cursor'):
            del self.db_cursor
        if hasattr(self, 'db_connection'):
            self.db_connection.close()
