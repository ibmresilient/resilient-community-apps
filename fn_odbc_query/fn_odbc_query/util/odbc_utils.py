# -*- coding: utf-8 -*-
#
# Copyright IBM Corp. - Confidential Information
#
# Util classes for ODBC
#
import pyodbc
import sys

SQL_ATTR_CONNECTION_TIMEOUT = 113
SINGLE_ENCODING_DATABASES = ["mariadb", "postgresql", "mysql"]

""" Unicode objects don’t exist in python 3.6. """
if sys.version_info >= (3, 0):
    unicode = str


class OdbcConnection(object):
    # member variables
    db_connection = None
    db_cursor = None

    def __init__(self, sql_connection_string, sql_autocommit, sql_query_timeout, sql_pyodbc_timeout_error_state):
        self.db_connection = self.setup_odbc_connection(sql_connection_string, sql_autocommit,
                                                        sql_query_timeout, sql_pyodbc_timeout_error_state)

    @staticmethod
    def setup_odbc_connection(sql_connection_string, sql_autocommit, sql_query_timeout, sql_pyodbc_timeout_error_state):
        """
        Setup ODBC connection to a SQL server using connection string obtained from the config file.
        Set autocommit and query timeout values based on the information in config file.
        :param sql_connection_string: config setting
        :param sql_autocommit: config setting
        :param sql_query_timeout: config setting
        :param sql_pyodbc_timeout_error_state: config setting
        :return: pyodbc Connection
        """
        # ODBC connection pooling is turned ON by default.
        # Not all database drivers close connections on db_connection.close() to save round trips to the server.
        # Pooling should be set to False to close connection on db_connection.close().
        pyodbc.pooling = False

        # This fixes incorrect locale setting issue that causes
        # pyodbc.connect to abort on macOS with ODBC Driver 17 for SQL Server (msodbcsql17) working in Python 3.6.
        import locale
        locale.setlocale(locale.LC_ALL, "")

        try:
            db_connection = pyodbc.connect(sql_connection_string)

            # As per the Python DB API, the default value is False
            if sql_autocommit:
                db_connection.autocommit = True

            if sql_query_timeout:
                # Some ODBC drivers might throw an error while setting db_connection.timeout:
                # ('HY000', u"[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")
                # The connection timeout period is set through SQLSetConnectAttr, SQL_ATTR_CONNECTION_TIMEOUT.
                # SQL_ATTR_CONNECTION_TIMEOUT represents value 113,
                # this constant can be found in ODBC specification file "sqlext.h".

                # SQL_ATTR_CONNECTION_TIMEOUT appears not be supported by the psqlodbc driver (PostgreSQL).
                # Psqlodbc throws a general error 'HY000' for which there was no specific SQLSTATE and for which no
                # implementation-specific SQLSTATE was defined.
                # Try to catch a pyodbc.Error, verify if it includes 'HY000' and '113' and pass.
                try:
                    # Query statement timeout defaults to 0, which means "no timeout"
                    db_connection.timeout = sql_query_timeout

                except pyodbc.Error as e:
                    sql_state = e.args[0]
                    error_message = e.args[1]
                    if sql_state == sql_pyodbc_timeout_error_state and str(SQL_ATTR_CONNECTION_TIMEOUT) in error_message:
                        pass
                    else:
                        raise Exception("Could not setup the ODBC connection, Exception %s", e)

        except Exception as e:
            raise Exception("Could not setup the ODBC connection, Exception %s", e)

        return db_connection

    def configure_unicode_settings(self, sql_database_type):
        """
        Configure unicode settings based on the type of SQL database server.
        Pyodbc recommends configurating connection's encoding and decoding, since many drivers behave differently.
        :param sql_database_type: config setting
        """
        if sql_database_type:
            # MariaDB, PostgreSQL, MySQL databases tend to use a single encoding and do not differentiate between
            # "SQL_CHAR" and "SQL_WCHAR". Therefore you must configure them to encode Unicode
            # data as UTF-8 and to decode both C buffer types using UTF-8.
            # https://github.com/mkleehammer/pyodbc/wiki/Unicode
            if sql_database_type in SINGLE_ENCODING_DATABASES:
                self.db_connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
                self.db_connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
                if sys.version_info[0] == 3:  # Python 3.x
                    self.db_connection.setencoding(encoding='utf-8')
                else:
                    self.db_connection.setencoding(str, encoding='utf-8')
                    self.db_connection.setencoding(unicode, encoding='utf-8')

            # Pyodbc Wiki page states recent MS SQL Server drivers match the specification,
            # no additional Unicode configuration is necessary. Using the pyodbc defaults is recommended.

    def set_db_cursor(self, db_cursor):
        self.db_cursor = db_cursor

    def create_cursor(self):
        """  Create cursor """
        try:
            db_cursor = self.db_connection.cursor()
            self.set_db_cursor(db_cursor)

        except Exception as e:
            raise Exception("Could not execute SQL statement, Exception %s", e)

    def execute_select_statement(self, sql_query, sql_params, sql_number_of_records_returned):
        """
        Execute SQL SELECT statement using the Cursor execute() function.
        :param sql_query: sql statement
        :param sql_params: function parameters
        :param sql_number_of_records_returned: config setting
        :return: list of rows
        """
        try:
            self.db_cursor.execute(sql_query, sql_params)

            if sql_number_of_records_returned is not None:
                rows = self.db_cursor.fetchmany(sql_number_of_records_returned)
            else:
                rows = self.db_cursor.fetchall()

        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_query, e)

        return rows

    def get_cursor_description(self):
        """
        Returns cursor_description a tuple with query result columns.
        :return: tuple
        """
        return self.db_cursor.description

    def execute_odbc_query(self, sql_query, sql_params):
        """
        Execute SQL DELETE, UPDATE, INSERT statements using the Cursor execute() function.
        :param sql_query: sql statement
        :param sql_params: function parameters
        """
        try:
            self.db_cursor.execute(sql_query, sql_params)

            if not self.db_connection.autocommit:
                self.db_connection.commit()

        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_query, e)

        return self.db_cursor.rowcount

    def close_connections(self):
        """  Tear down. Close connections if they're defined."""
        if self.db_cursor is not None:
            self.db_cursor.close()

        if self.db_connection is not None:
            self.db_connection.close()
