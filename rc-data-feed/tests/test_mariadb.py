# -*- coding: utf-8 -*-

import logging
import datetime
import pytest
import sys

from .lib.test_sql_common import SQLCommon

LOG = logging.getLogger(__name__)

# make sure this db already exists
TEST_DB = "test_db"

MAX_TEXT_SIZE = 32000

FIND_COLUMNS_STMT = "SELECT column_name, data_type FROM information_schema.columns WHERE  table_name='{table_name}'"

app_config = {
    "class": "ODBCFeed",
    "odbc_connect": "Driver={{MariaDB ODBC 3.0 Driver}};Server=127.0.0.1;DATABASE={db};Port=3306;connectTimeout=0".format(db=TEST_DB),
    "sql_dialect": "MariaDBDialect",
    "uid": "res_test",
    "pwd": "res_test"
}


result_payload = {  "id":  101,
                    "inc_id": 2301,
                    "test_text": u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ",
                    "test_int": 1000,
                    "test_date": datetime.date(2019, 2, 13),
                    "test_bool": "1"
                    }

if sys.version_info.major == 2:
    result_payload['test_datetime'] = datetime.datetime(2019, 2, 13, 15, 55, 47)
else:
    result_payload['test_datetime'] = datetime.datetime(2019, 2, 13, 15, 55, 47, 448000)

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