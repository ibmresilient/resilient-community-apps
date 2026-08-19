# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""This module contains the class needed to implement a SQLite feed that writes
Resilient data to SQLite."""

import sqlite3
import logging

from data_feeder_plugins.sqllib.sql_feed_base import SqlFeedDestinationBase
from data_feeder_plugins.sqllib.sql_dialect import SqliteDialect

LOG = logging.getLogger(__name__)

class SQLiteFeedDestination(SqlFeedDestinationBase):  # pylint: disable=too-few-public-methods
    """SQLite feed destination that writes Resilient data to a SQLite DB."""
    def __init__(self, rest_client_helper, options):
        super(SQLiteFeedDestination, self).__init__(rest_client_helper, options, dialect=SqliteDialect())

        file_name = options.get('file_name', 'objects.sqlite3')

        self.sqlite_db = sqlite3.connect(file_name)

        self._init_tables()

    def _start_transaction(self):
        return self.sqlite_db.cursor()

    def _commit_transaction(self, context):
        self.sqlite_db.commit()

    def _rollback_transaction(self, context):
        self.sqlite_db.rollback()

    def _execute_sql(self, cursor, sql, data=None):
        if data is None:
            data = {}

        return cursor.execute(sql, data)
