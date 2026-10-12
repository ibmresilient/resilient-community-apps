# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""This module contains the definition of the ODBCFeedDestination class."""
import cx_Oracle
import logging
import pyodbc
import threading
import traceback
from retry import retry

from data_feeder_plugins.sqllib.sql_feed_base import SqlFeedDestinationBase
from data_feeder_plugins.sqllib.sql_dialect import OracleDialect

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

        # retain a connection pool per thread
        self.THREAD_CONNECTION = {}

        # see _start_transaction
        #self.connection = self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)

        self._init_tables()

    @retry(pyodbc.OperationalError, tries=10, delay=5, backoff=3, logger=LOG)
    def _reinit(self, connect_str, uid, pwd, dialect=None):
        LOG.info(f"Initializing database connection: {connect_str}")

        # is there a connection pool for this thread?
        thread_id = threading.current_thread().ident

        self._close_connection()

        # pylint: disable=c-extension-no-member
        if dialect and isinstance(dialect, OracleDialect):
            connection = cx_Oracle.connect(uid, pwd, connect_str, encoding="UTF-8")
        else:
            connection = pyodbc.connect(connect_str, uid=uid, pwd=pwd, autocommit=True)

        self.THREAD_CONNECTION[thread_id] = connection
        self.dialect.configure_connection(connection)

        return connection

    def _start_transaction(self):
        """Creates a new cursor and returns it to the caller.

        :returns A new DB cursor."""
        # is there a connection pool for this thread?
        thread_id = threading.current_thread().ident
        if thread_id not in self.THREAD_CONNECTION:
            self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)

        LOG.debug(f"thread: {thread_id} connection: {self.connect_str} {id(self.THREAD_CONNECTION[thread_id])}")
        try:
            return self.THREAD_CONNECTION[thread_id].cursor()
        except pyodbc.Error as err:
            LOG.error(str(err))
            LOG.error(traceback.format_exc())
            self._reinit(self.connect_str, self.uid, self.pwd, dialect=self.dialect)
            return self.THREAD_CONNECTION[thread_id].cursor()

    def _commit_transaction(self, context):
        """Commits the currently open transaction."""
        thread_id = threading.current_thread().ident
        self.THREAD_CONNECTION[thread_id].commit()

    def _rollback_transaction(self, context):
        """Rolls back the currently open transaction."""
        thread_id = threading.current_thread().ident
        self.THREAD_CONNECTION[thread_id].rollback()

    def _execute_sql(self, cursor, sql, data=None):
        """Executes the specified SQL.

        :param cursor: The cursor returned by a previous _start_transaction call.
        :param sql: The SQL to execute.
        :param data: The bind parameters in whatever format was returned by
            self.dialect.get_parameters.  In our case, we assume that it's
            an array (since that's what the pyodbc API wants."""
        if data is None:
            data = []

        if isinstance(cursor, cx_Oracle.Cursor):
            cursor.execute(sql, data)
            return cursor

        return cursor.execute(sql, data)

    def _close_connection(self):
        """Close the connection to the database"""
        thread_id = threading.current_thread().ident

        if self.THREAD_CONNECTION.get(thread_id):
            try:
                self.THREAD_CONNECTION[thread_id].close()
            except Exception:
                pass
            finally:
                del self.THREAD_CONNECTION[thread_id]
