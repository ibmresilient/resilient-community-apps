# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Resilient functions component to execute ODBC queries"""

# Set up:
# Destination: a Queue named "fn_odbc_query".
# Manual Action: Execute an ODBC query.

import logging
import pyodbc
import json
import sys
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_odbc_query.util import function_utils

SINGLE_ENCODING_DATABASES = ["mariadb", "postgresql", "mysql"]
SQL_ATTR_CONNECTION_TIMEOUT = 113
LOG = logging.getLogger(__name__)

""" Unicode objects don’t exist in python 3.6. """
if sys.version_info >= (3, 0):
    unicode = str


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
        db_connection = None
        db_cursor = None

        try:
            # Get the function parameters:
            if "sql_query" not in kwargs or kwargs.get("sql_query") == '':
                raise ValueError("Required field sql_query is missing or empty")

            sql_query = self.get_textarea_param(kwargs.get("sql_query"))  # textarea
            sql_condition_value1 = kwargs.get("sql_condition_value1")  # text
            sql_condition_value2 = kwargs.get("sql_condition_value2")  # text
            sql_condition_value3 = kwargs.get("sql_condition_value3")  # text

            LOG.info(u"sql_query: %s", sql_query)
            LOG.info(u"sql_condition_value1: %s", sql_condition_value1)
            LOG.info(u"sql_condition_value2: %s", sql_condition_value2)
            LOG.info(u"sql_condition_value3: %s", sql_condition_value3)

            # Read configuration settings:
            sql_restricted_sql_statements = self.options["sql_restricted_sql_statements"] \
                if "sql_restricted_sql_statements" in self.options else None

            yield StatusMessage("Starting...")

            yield StatusMessage("Validating...")
            sql_params = function_utils.prepare_sql_parameters(sql_condition_value1,
                                                               sql_condition_value2, sql_condition_value3)
            function_utils.validate_data(sql_restricted_sql_statements, sql_query)

            yield StatusMessage("Opening ODBC connection...")
            db_connection = self.setup_odbc_connection() #fixme mock
            self.configure_unicode_settings(db_connection) #fixme mock
            db_cursor = self.create_cursor(db_connection) #fixme test exception

            yield StatusMessage("Executing an ODBC query...")
            # Check what SQL statement is executed, get the first word in sql_query
            sql_statement = function_utils.get_type_sql_statement(sql_query)

            if sql_statement == 'select':
                rows = self.execute_select_statement(db_cursor, sql_query, sql_params)
                results = function_utils.prepare_results(db_cursor.description, rows)

                if results.get("entries") is None:
                    yield StatusMessage("No query results returned...")
                else:
                    yield StatusMessage("Result contains {} entries...".format(len(results.get("entries"))))

            elif sql_statement == 'update' or sql_statement == 'delete' \
                    or sql_statement == 'insert':
                # Return row count and set results to empty list
                row_count = self.execute_odbc_query(db_connection, db_cursor, sql_query, sql_params)
                results = function_utils.prepare_results(None, None)

                yield StatusMessage("{} rows processed".format(row_count))

            else:
                raise ValueError("SQL statement '{}' is not supported".format(sql_statement))

            yield StatusMessage("Done...")
            LOG.info(json.dumps(results))

            yield FunctionResult(results)

        except Exception:
            raise FunctionError()

        # Commit changes and tear down connection
        finally:
            yield StatusMessage("Closing ODBC connection...")
            self.close_connections(db_connection, db_cursor)

    def setup_odbc_connection(self):
        """" Setup ODBC connection to a SQL server

        Setup ODBC connection to a SQL server using connection string obtained from the config file.
        Set autocommit and query timeout values based on the information in config file.

        """
        if "sql_connection_string" in self.options:
            sql_connection_string = self.options["sql_connection_string"]
        else:
            raise ValueError("Mandatory config setting 'sql_connection_string' not set.")

        # ODBC connection pooling is turned ON by default.
        # Not all database drivers close connections on db_connection.close() to save round trips to the server.
        # Pooling should be set to False to close connection on db_connection.close().
        pyodbc.pooling = False

        try:
            db_connection = pyodbc.connect(sql_connection_string)

            if "sql_autocommit" in self.options:
                sql_autocommit = self.options["sql_autocommit"].lower()

                # As per the Python DB API, the default value is False
                if sql_autocommit == "true":
                    db_connection.autocommit = True

            if "sql_query_timeout" in self.options:
                sql_query_timeout = self.options["sql_query_timeout"]

                # Some odbc drivers might throw an error while setting db_connection.timeout:
                # ('HY000', u"[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")
                # SQL_ATTR_CONNECTION_TIMEOUT represents value 113,
                # this constant can be found in ODBC specification file "sqlext.h".
                # SQL_ATTR_CONNECTION_TIMEOUT appears not be supported by the psqlodbc driver (PostgreSQL).
                # Try to catch a pyodbc.Error and pass.
                try:
                    # Query statement timeout defaults to 0, which means "no timeout"
                    db_connection.timeout = int(sql_query_timeout)

                except pyodbc.Error as e:
                    sql_state = e.args[0]
                    error_message = e.args[1]
                    if sql_state == 'HY000' and str(SQL_ATTR_CONNECTION_TIMEOUT) in error_message:
                        pass
                    else:
                        raise Exception("Could not setup the ODBC connection, Exception %s", e)

        except Exception as e:
            raise Exception("Could not setup the ODBC connection, Exception %s", e)

        return db_connection

    def configure_unicode_settings(self, db_connection):
        """"  Configure unicode settings

        Pyodbc recommends configurating connection's encoding and decoding.
        "By default, pyodbc uses UTF-16 assuming native byte-order and SQL_C_WCHAR for reading and writing
        all Unicode as recommended in the ODBC specification.
        Unfortunately many drivers behave differently so connections may need to be configured."

        Configure unicode settings based on the type of SQL database server.

        """
        if "sql_database_type" in self.options:
            sql_database_type = self.options["sql_database_type"].lower()

            # These databases tend to use a single encoding and do not differentiate between
            # "SQL_CHAR" and "SQL_WCHAR". Therefore you must configure them to encode Unicode
            # data as UTF-8 and to decode both C buffer types using UTF-8.
            # https://github.com/mkleehammer/pyodbc/wiki/Unicode
            if sql_database_type in SINGLE_ENCODING_DATABASES:
                db_connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
                db_connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
                if sys.version_info[0] == 3: # Python 3.x
                    db_connection.setencoding(encoding='utf-8')
                else:
                    db_connection.setencoding(str, encoding='utf-8')
                    db_connection.setencoding(unicode, encoding='utf-8')

        return db_connection

    @staticmethod
    def create_cursor(db_connection):
        """"  Create cursor """
        try:
            db_cursor = db_connection.cursor()

        except Exception as e:
            raise Exception("Could not execute SQL statement, Exception %s", e)

        return db_cursor

    @staticmethod
    def execute_odbc_query(db_connection, db_cursor, sql_query, sql_args):
        """"  Execute SQL DELETE, UPDATE, INSERT statement

        Execute SQL statements using the Cursor execute() function.

        """
        try:
            db_cursor.execute(sql_query, sql_args)

            if not db_connection.autocommit:
                db_connection.commit()

        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_query, e)

        return db_cursor.rowcount

    def execute_select_statement(self, db_cursor, sql_query, sql_args):
        """"  Execute SQL SELECT statement

        Execute SQL statements using the Cursor execute() function.

        """
        number_records = None

        if "sql_number_of_records_returned" in self.options:
            sql_number_of_records_returned = self.options["sql_number_of_records_returned"]
            number_records = int(sql_number_of_records_returned)

        try:
            db_cursor.execute(sql_query, sql_args)

            if number_records is not None:
                rows = db_cursor.fetchmany(number_records)
            else:
                rows = db_cursor.fetchall()

        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_query, e)

        return rows

    @staticmethod
    def close_connections(db_cursor, db_connection):
        """"  Tear down

        Close connections if they're defined.

        """
        if db_connection is not None:
            db_connection.close()

        if db_cursor is not None:
            db_cursor.close()
