import logging
import datetime
import pytest

from lib.test_sql_common import SQLCommon

LOG = logging.getLogger(__name__)

# make sure this db already exists
TEST_DB = "test_db"

MAX_TEXT_SIZE = 65535

FIND_COLUMNS_STMT = "SELECT column_name, data_type FROM information_schema.columns WHERE  table_name='{table_name}'"

app_config = {
    "class": "ODBCFeed",
    "odbc_connect": "DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=127.0.0.1;PORT=1443;DATABASE={db}".format(db=TEST_DB),
    "sql_dialect": "SQLServerDialect",
    "uid": "sa",
    "pwd": "Passw0rd"
}


result_payload = {  "id":  10,
                    "inc_id": 2301,
                    "test_text": "this is a text field",
                    "test_int": 1000,
                    "test_date": datetime.date(2019, 2, 13),
                    "test_datetime": datetime.datetime(2019, 2, 13, 15, 55, 47, 448000),
                    "test_bool": True
                    }

@pytest.mark.order1
def test_get_parameters():
    common = SQLCommon(app_config)

    common.test_get_parameters()

def test_createtable():
    common = SQLCommon(app_config)

    common.test_createtable()

def test_insert_row():
    common = SQLCommon(app_config)

    common.test_insert_row(result_payload)

def test_update_row():
    common = SQLCommon(app_config)

    common.test_update_row(MAX_TEXT_SIZE, result_payload)

def test_delete_row():
    common = SQLCommon(app_config)

    common.test_delete_row()

def test_altertable():
    common = SQLCommon(app_config)

    common.test_altertable()

def test_droptable():
    common = SQLCommon(app_config)

    common.test_droptable()