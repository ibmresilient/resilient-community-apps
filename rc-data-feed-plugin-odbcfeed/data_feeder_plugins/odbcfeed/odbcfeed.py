# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""This module contains the definition of the ODBCFeedDestination class."""
import logging
import pyodbc

from data_feeder_plugins.sqllib.sql_feed_base import SqlFeedDestinationBase

LOG = logging.getLogger(__name__)

class ODBCFeedDestination(SqlFeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed for writing Resilient data to an ODBC destination."""
    def __init__(self, rest_client_helper, options):
        """Initializes a new ODBCFeed.

        :param rest_client_helper: A Resilient SimpleClient object wrapper to use for interacting with
            the REST API.  This is expected to be used for loading type information (e.g.
            loading all of the types so we can create the tables, loading field type
            information, etc.).
        :param options: A dict containing the configuration options needed.
        """
        super(ODBCFeedDestination, self).__init__(rest_client_helper, options)

        self.connect_str = options.get("odbc_connect")

        self.pwd = options.get("pwd")
        self.uid = options.get("uid")

        self.connection = self._reinit(self.connect_str, self.uid, self.pwd)

        self._init_tables()

    def _reinit(self, connect_str, uid, pwd):
        # pylint: disable=c-extension-no-member
        connection = pyodbc.connect(connect_str, uid=uid, pwd=pwd)

        self.dialect.configure_connection(connection)

        return connection

    def _start_transaction(self):
        """Creates a new cursor and returns it to the caller.

        :returns A new DB cursor."""
        return self.connection.cursor()

    def _commit_transaction(self, context):
        """Commits the currently open transaction."""
        self.connection.commit()

    def _rollback_transaction(self, context):
        """Rolls back the currently open transaction."""
        self.connection.rollback()

    def _execute_sql(self, cursor, sql, data=None):
        """Executes the specified SQL.

        :param cursor: The cursor returned by a previous _start_transaction call.
        :param sql: The SQL to execute.
        :param data: The bind parameters in whatever format was returned by
            self.dialect.get_parameters.  In our case, we assume that it's
            an array (since that's what the pyodbc API wants."""
        if data is None:
            data = []

        try:
            return cursor.execute(sql, data)
        except Exception as err:
            raise err

    def _close_connection(self):
        """Close the connection to the database"""
        self.connection.close()
