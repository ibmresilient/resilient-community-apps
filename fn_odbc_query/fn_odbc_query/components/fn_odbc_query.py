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
        sql_select, sql_condition_value

    An example of a set of query parameter might look like the following:

        sql_select: "SELECT incident_id, name, description FROM incidents WHERE incident_id = {sql_condition_value}"
        sql_condition_value: artifact.value

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
        """Resilient Function: A function that makes ODBC queries.

        Inputs:
        sql_select: a query with parameters
        sql_condition_value: condition value

        """

        try:
            # Get the function parameters:
            sql_select = self.get_select_param(kwargs.get("sql_select"))  # select, values: "SELECT incident_id, name, description FROM test.incidents WHERE incident_id = ?"
            sql_condition_value = kwargs.get("sql_condition_value")  # text

            LOG.info("sql_select: %s", sql_select)
            LOG.info("sql_condition_value: %s", sql_condition_value)

            self.search_params = {'sql_select': sql_select,
                                  'sql_condition_value': sql_condition_value}

            yield StatusMessage("starting...")
            self.validate_data()

            yield StatusMessage("Opening ODBC connection...")
            self.setup_odbc_connection()

            yield StatusMessage("Executing an ODBC query...")
            results = self.execute_odbc_query()

            yield StatusMessage("done...")
            LOG.info(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            self.close_connections()
            yield FunctionError()

        # Clean up actions
        finally:
            yield StatusMessage("Closing ODBC connection...")
            self.close_connections()

    def validate_data(self):
        """" Validate input data, allow SELECT statements only """
        # TODO test pyodbc sql injection scenarios, test select * "ALL", test multiple where clauses WHERE aa = ? AND bb = ?
        sql_select = self.search_params.get("sql_select")
        sql_args = self.search_params.get("sql_condition_value")


    def setup_odbc_connection(self):
        """" Setup ODBC connection to a server database

        Setups up server database and connection objects using credentials obtained from the config file.
        Method also specifies the ODBC driver based on the sql_db_type from the config file.

        For testing purposes I'm connecting to MariaDB that lives on my Docker.

        """
        if "sql_server_url" in self.options:
            sql_server_url = self.options["sql_server_url"]
        else:
            raise Exception("Mandatory config setting 'sql_server_url' not set.")

        if "sql_db_type" in self.options:
            sql_db_type = self.options["sql_db_type"]
        else:
            raise Exception("Mandatory config setting 'sql_db_type' not set.")

        if "sql_port" in self.options:
            sql_port = self.options["sql_port"]
        else:
            raise Exception("Mandatory config setting 'sql_port' not set.")

        if "sql_uid" in self.options:
            sql_uid = self.options["sql_uid"]
        else:
            raise Exception("Mandatory config setting 'sql_uid' not set.")

        if "sql_pwd" in self.options:
            sql_pwd = self.options["sql_pwd"]
        else:
            raise Exception("Mandatory config setting 'sql_pwd' not set.")

        if "sql_connection_timeout" in self.options:
            sql_connection_timeout = self.options["sql_connection_timeout"]
        else:
            raise Exception("Mandatory config setting 'sql_connection_timeout' not set.")

        # FIXME hardcoded, set driver based on the sql_db_type
        sql_database_driver = "MariaDB ODBC 3.0 Driver"

        """ ODBC connection pooling is turned on by default.
        Connections to the SQL server are not closed by default. 
        Some database drivers do not close connections when close() is called in order to save round-trips to the server.
        To close your connection when you call close() you should set pooling to False.
        """
        pyodbc.pooling = False

        try:
            connection_string = "DRIVER={{{}}};SERVER={};PORT={};UID={};PWD={};".format(sql_database_driver,
                                                                                            sql_server_url, sql_port,
                                                                                            sql_uid, sql_pwd)

            self.db_connection = pyodbc.connect(connection_string)

            # The connection timeout value, set in the config file
            self.db_connection.timeout = int(sql_connection_timeout)

            # This is just an example that works for PostgreSQL and MySQL, with Python 2.7.
            self.db_connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')

            # Create a cursor from the connection
            self.db_cursor = self.db_connection.cursor()

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not setup the ODBC connection to %s, Exception %s", sql_server_url, e)

    def execute_odbc_query(self):
        """"  Execute SQL statement

        Execute SQL statements using the Cursor execute() function. Using prepared SQL statements, where clause/
        condition value is passed to the database separately, protecting against SQL injections.

        """
        if "sql_number_of_records_returned" in self.options:
            number_records = int(self.options["sql_number_of_records_returned"])

        try:
            sql_select = self.search_params.get("sql_select")
            sql_args = self.search_params.get("sql_condition_value")

            self.db_cursor.execute(sql_select, [sql_args])


            if number_records is not None:
                rows = self.db_cursor.fetchmany(number_records)
            else:
                rows = self.db_cursor.fetchall()

        # Catch some specific exceptions
        except pyodbc.DatabaseError as err:
            raise err

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_select, e)

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

        # add query result column names to result entries to be displayed as a row in Resilient datatable
        entries_data_list = [[column[0] for column in self.db_cursor.description]]

        # add rows to the result entries
        entries_data_list.extend([list(row) for row in rows])

        LOG.info("Result contains %s entries", len(entries_data_list))

        entries = {"entries": [entry for entry in entries_data_list]}

        return entries

    def close_connections(self):
        """"  Delete the cursor and close connection if they are defined. """
        if hasattr(self, 'db_cursor'):
            del self.db_cursor
        if hasattr(self, 'db_connection'):
            self.db_connection.close()
