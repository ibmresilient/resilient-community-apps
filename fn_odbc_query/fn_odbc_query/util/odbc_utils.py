# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# Util classes for ODBC
from logging import getLogger
import pyodbc

SINGLE_ENCODING_DATABASES = ["mariadb", "postgresql", "mysql"]
LOG = getLogger(__name__)

class OdbcConnection(object):

    db_connection = None
    db_cursor = None

    def __init__(self, sql_connection_string, sql_autocommit=False, sql_query_timeout=30):
        self.db_connection = self.setup_odbc_connection(sql_connection_string, sql_autocommit, sql_query_timeout)

    @staticmethod
    def setup_odbc_connection(sql_connection_string, sql_autocommit=False, sql_query_timeout=30):
        """
        Setup ODBC connection to a SQL server using connection string obtained from the config file.
        Set autocommit and query timeout values based on the information in config file.
        :param sql_connection_string: config setting
        :param sql_autocommit: config setting
        :param sql_query_timeout: config setting
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
            db_connection.autocommit = sql_autocommit

            # Some ODBC drivers do not implement the connection timeout and will throw pyodbc.Error while trying
            # to set it.
            #
            # The connection timeout period is set through SQLSetConnectAttr, SQL_ATTR_CONNECTION_TIMEOUT.
            #
            # SQL_ATTR_CONNECTION_TIMEOUT appears not be supported by the psqlodbc driver (PostgreSQL).
            # Psqlodbc throws a general error 'HY000' for which no implementation-specific SQLSTATE was defined:
            # ('HY000', u"[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")
            #
            # Oracle11g driver (Oracle database) also appears not support timeout and throws an error:
            # ('HYC00', u'[HYC00] [Oracle][ODBC]Optional feature not implemented ....(0) (SQLSetConnectAttr)')))
            #
            # Try to catch a pyodbc.Error, log it as warning and pass.
            try:
                db_connection.timeout = sql_query_timeout
            except pyodbc.Error as e:
                LOG.warning(f"ODBC driver does not implement the connection timeout attribute. Error code: {e.args[0]} - {e.args[1]}")

        except Exception as e:
            raise RuntimeError(f"Could not setup the ODBC connection, Exception {e}")

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
                self.db_connection.setencoding(encoding='utf-8')

            # Pyodbc Wiki page states recent MS SQL Server drivers match the specification,
            # no additional Unicode configuration is necessary. Using the pyodbc defaults is recommended.

    def set_db_cursor(self, db_cursor):
        self.db_cursor = db_cursor

    def create_cursor(self):
        """Create cursor"""
        try:
            db_cursor = self.db_connection.cursor()
            self.set_db_cursor(db_cursor)

        except Exception as e:
            raise RuntimeError(f"Could not execute SQL statement, Exception {e}")

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
            rows = self.db_cursor.fetchmany(sql_number_of_records_returned) if sql_number_of_records_returned else self.db_cursor.fetchall()
        except Exception as e:
            raise RuntimeError(f"Could not execute SQL statement {sql_query}, Exception {e}")

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
            raise RuntimeError(f"Could not execute SQL statement {sql_query}, Exception {e}")

        return self.db_cursor.rowcount

    def close_connections(self):
        """  Tear down. Close connections if they're defined."""
        if self.db_cursor:
            self.db_cursor.close()

        if self.db_connection:
            self.db_connection.close()
