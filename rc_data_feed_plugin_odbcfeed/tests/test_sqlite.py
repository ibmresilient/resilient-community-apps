# -*- coding: utf-8 -*-

import logging
import pytest
import sys

from lib.test_sql_common import SQLCommon, blob_fields, BLOB_TABLE_NAME
from data_feeder_plugins.sqlitefeed.sqlitefeed import SQLiteFeedDestination
from data_feeder_plugins.sqllib.sql_dialect import SqliteDialect

LOG = logging.getLogger(__name__)

# make sure this db already exists
TEST_DB = "test_db"

MAX_TEXT_SIZE = 32000

FIND_COLUMNS_STMT = """SELECT
       p.name as column_name,
       p.type as data_type
FROM sqlite_master m
left outer join pragma_table_info((m.name)) p
     on m.name <> p.name
where m.name = '{table_name}'
order by p.name;"""

app_config = {
    "class": "SQLiteFeed",
    "file_name": "/tmp/test.sqlite3" # nosec
}

result_payload = {  "id":  101,
                    "inc_id": 2301,
                    "test_text": u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ",
                    "test_int": 1000,
                    "test_bool": 1
                    }

if sys.version_info.major == 2:
    result_payload['test_date']     = "2019-02-13T15:55:47"
    result_payload['test_datetime'] = "2019-02-13T15:55:47+00:00"
else:
    result_payload['test_date']     = "2019-02-13T15:55:47.448000"
    result_payload['test_datetime'] = "2019-02-13T15:55:47.448000+00:00"

@pytest.mark.livetest
@pytest.mark.order1
def test_get_parameters():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_get_parameters()

@pytest.mark.livetest
def test_createtable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_createtable()

@pytest.mark.livetest
def test_insert_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_insert_row(result_payload)

@pytest.mark.livetest
def test_update_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_update_row(MAX_TEXT_SIZE, result_payload)

@pytest.mark.livetest
def test_delete_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_delete_row()

@pytest.mark.livetest
def test_altertable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_altertable()

@pytest.mark.livetest
def test_droptable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SQLiteFeedDestination)

    common.test_droptable()

@pytest.mark.livetest
def test_blob():
    common = SQLCommon(app_config, table_name=BLOB_TABLE_NAME,
                       inspect_cols_query=FIND_COLUMNS_STMT,
                       table_def=blob_fields, baseClass=SQLiteFeedDestination)

    common.test_createtable()

    common.test_insert_blob(SqliteDialect.make_blob)
