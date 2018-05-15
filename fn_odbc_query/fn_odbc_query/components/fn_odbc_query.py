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
import re

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

    The ODBC query will return a result in JSON format with an entry consisting of key value pairs.

        {
            'entries': [
                {u'sql_column_1': "query_result_column_1_value, u'sql_column_2': u'query_result_column_2_value', ...},
                {u'sql_column_1': query_result_column_1_value, u'sql_column_2': u'query_result_column_2_value', ...}
                ...
            ]
        }

    An example of a returned result:

        "entries": [
            {"sql_column_1": 3, "sql_column_2": "MariaBD"},
            {"sql_column_1": 4, "sql_column_2": "MariaBD"},
            {"sql_column_1": 5, "sql_column_2": "MariaBD"}
            ]

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

            LOG.info(u"sql_query: %s", sql_query)
            LOG.info(u"sql_condition_value1: %s", sql_condition_value1)
            LOG.info(u"sql_condition_value2: %s", sql_condition_value2)
            LOG.info(u"sql_condition_value3: %s", sql_condition_value3)

            yield StatusMessage("Starting...")
            sql_params = self.prepare_sql_parameters(sql_condition_value1, sql_condition_value2, sql_condition_value3)
            self.validate_data(sql_query, sql_params)

            yield StatusMessage("Opening ODBC connection...")
            db_connection = self.setup_odbc_connection()

            yield StatusMessage("Executing an ODBC query...")
            results = self.execute_odbc_query(db_connection, sql_query, sql_params)

            if results.get("entries") is None:
                yield StatusMessage("No query results returned.")

            yield StatusMessage("Done...")
            LOG.info(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as ex:
            LOG.error(str(ex))
            # Clean up here as well, yield FunctionError() will prevent executing finally block
            self.close_connections(db_connection)
            yield FunctionError()

        # Clean up actions
        finally:
            yield StatusMessage("Closing ODBC connection...")
            self.close_connections(db_connection)

    @staticmethod
    def prepare_sql_parameters(sql_condition_value1, sql_condition_value2, sql_condition_value3):
        """" Prepare a list with non None parameters

        Prepare a list of non None value or blank "Falsy" parameters.

        """
        sql_params = []

        if sql_condition_value1:
            sql_params.append(sql_condition_value1)
        if sql_condition_value2:
            sql_params.append(sql_condition_value2)
        if sql_condition_value3:
            sql_params.append(sql_condition_value3)

        return sql_params

    def validate_data(self, sql_query, sql_args):
        """" Validate input data

        Validate if query is allowed.

        """
        # TODO test select * "ALL", test multiple where clauses WHERE aa = ? AND bb = ?
        if "sql_not_allowed_statements" in self.options:
            sql_not_allowed_statements = self.options["sql_not_allowed_statements"]

        # Check if sql_query is one of the NOT allowed statements from configuration file

        if re.search("delete", sql_query.lower()):
            raise Exception("User does not have permission to perform %s SQL statement", sql_query)

    def setup_odbc_connection(self):
        """" Setup ODBC connection to a SQL server

        Setup ODBC connection to a SQL server using connection string obtained from the config file.

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
            db_connection = pyodbc.connect(sql_connection_string)
            db_connection.timeout = int(sql_connection_timeout)

            # This is just an example that works for PostgreSQL and MySQL, with Python 2.7.
            db_connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
            db_connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')

        # Catch any additional errors not specifically checked for
        except Exception as e:
            db_connection = None
            raise Exception("Could not setup the ODBC connection, Exception %s", e)

        return db_connection

    def execute_odbc_query(self, db_connection, sql_query, sql_args):
        """"  Execute SQL statement

        Execute SQL statements using the Cursor execute() function.

        """
        if "sql_number_of_records_returned" in self.options:
            number_records = int(self.options["sql_number_of_records_returned"])

        try:
            db_cursor = db_connection.cursor()
            db_cursor.execute(sql_query, sql_args)

            rows = None
            if number_records is not None:
                rows = db_cursor.fetchmany(number_records)
            else:
                rows = db_cursor.fetchall()

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_query, e)

        return self.prepare_results(db_cursor.description, rows)

    @staticmethod
    def prepare_results(cursor_description_list, rows):
        """"  Generate result

        Generate result in JSON format with an entry consisting of key value pairs.

        """
        if rows is None or len(rows) == 0:
            LOG.info("No query results returned")
            return {"entries": None}

        # List of column names from SQL result to use as dictionary keys
        dt_column_keys = [column[0] for column in cursor_description_list]

        # Build dictionary: key-value pairs consisting of column name - row value
        entries_data_list = []
        for row in rows:
            if row is None:
                break
            entries_data_list.append(dict(zip(dt_column_keys, row)))

        LOG.info("Result contains %s entries", len(entries_data_list))

        entries = {"entries": [entry for entry in entries_data_list]}

        return entries

    @staticmethod
    def close_connections(db_connection):
        """"  Clean up

        Close connection if they are defined.

        """
        if db_connection is not None:
            db_connection.close()
