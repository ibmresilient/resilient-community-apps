

from rc_data_feed.lib.sql_feed_base import SqlFeedDestinationBase
from rc_data_feed.lib.sql_dialect import SqliteDialect

import sqlite3
import logging


logger = logging.getLogger(__name__)


class SqliteFeedDestination(SqlFeedDestinationBase):
    def __init__(self, rest_client, options):
        super(SqliteFeedDestination, self).__init__(rest_client, options, dialect=SqliteDialect())

        file_name = options.get('file_name', 'objects.sqlite3')

        self.db = sqlite3.connect(file_name)

        self._init_tables()

    def _start_transaction(self):
        return self.db.cursor()

    def _commit_transaction(self, cursor):
        self.db.commit()

    def _rollback_transaction(self, cursor):
        self.db.rollback()

    def _execute_sql(self, cursor, sql, data=None):
        if data is None:
            data = {}

        return cursor.execute(sql, data)
