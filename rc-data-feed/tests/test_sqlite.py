import logging
import datetime
import pytest
import sys

from .lib.test_sql_common import SQLCommon
from rc_data_feed.lib.sqlite_feed import SqliteFeedDestination

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
    "file_name": "/tmp/test.sqlite3"
}

result_payload = {  "id":  101,
                    "inc_id": 2301,
                    "test_text": "this is a text field",
                    "test_int": 1000,
                    "test_bool": 1
                    }

if sys.version_info.major == 2:
    result_payload['test_date']     = "2019-02-13T15:55:47"
    result_payload['test_datetime'] = "2019-02-13T15:55:47"
else:
    result_payload['test_date']     = "2019-02-13T15:55:47"
    result_payload['test_datetime'] = "2019-02-13T15:55:47"


@pytest.mark.order1
def test_get_parameters():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_get_parameters()

def test_createtable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_createtable()

def test_insert_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_insert_row(result_payload)

def test_update_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_update_row(MAX_TEXT_SIZE, result_payload)

def test_delete_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_delete_row()

def test_altertable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_altertable()

def test_droptable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, baseClass=SqliteFeedDestination)

    common.test_droptable()