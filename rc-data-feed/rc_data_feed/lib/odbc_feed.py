

from rc_data_feed.lib.sql_feed_base import SqlFeedDestinationBase

import pyodbc
import logging

logger = logging.getLogger(__name__)


class ODBCFeedDestination(SqlFeedDestinationBase):
    """Feed for writing data to an ODBC destination."""
    def __init__(self, rest_client, options):
        """Initializes a new ODBCFeed.

        :param rest_client: A Resilient SimpleClient object to use for interacting with the REST API.
            This is expected to be used for loading type information (e.g. loading all of the types so we
            can create the tables, loading field type information, etc.).
        :param options: A dict containing the configuration options needed.
        """
        super(ODBCFeedDestination, self).__init__(rest_client, options)

        connect_str = options.get("odbc_connect")

        pwd = options.get("pwd")
        uid = options.get("uid")

        self.db = pyodbc.connect(connect_str, uid=uid, pwd=pwd)

        self.dialect.configure_connection(self.db)

        self._init_tables()

    def _start_transaction(self):
        """Creates a new cursor and returns it to the caller.

        :returns A new DB cursor."""
        return self.db.cursor()

    def _commit_transaction(self, cursor):
        """Commits the currently open transaction."""
        self.db.commit()

    def _rollback_transaction(self, cursor):
        """Rolls back the currently open transaction."""
        self.db.rollback()

    def _execute_sql(self, cursor, sql, data=None):
        """Executes the specified SQL.

        :param cursor: The cursor returned by a previous _start_transaction call.
        :param sql: The SQL to execute.
        :param data: The bind parameters in whatever format was returned by
            self.dialect.get_parameters.  In our case, we assume that it's
            an array (since that's what the pyodbc API wants."""
        if data is None:
            data = []

        return cursor.execute(sql, data)
