# -*- coding: utf-8 -*-

import logging
import datetime
import pytest

from lib.test_sql_common import SQLCommon, blob_fields, BLOB_TABLE_NAME
from data_feeder_plugins.sqllib.sql_dialect import MySqlDialect 

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
                    "test_datetime": datetime.datetime(2019, 2, 13, 15, 55, 47),
                    "test_bool": 1
                 }

SETUP_STMT = "SET @@SQL_MODE = REPLACE(@@SQL_MODE, 'STRICT_TRANS_TABLES', '');"

@pytest.mark.livetest
@pytest.mark.order1
def test_get_parameters():
    common = SQLCommon(app_config)

    common.test_get_parameters()

@pytest.mark.livetest
def test_createtable():
    common = SQLCommon(app_config)

    common.test_createtable()

@pytest.mark.livetest
def test_insert_row():
    common = SQLCommon(app_config, setup_stmt=SETUP_STMT)

    common.test_insert_row(result_payload)

@pytest.mark.livetest
def test_update_row():
    common = SQLCommon(app_config, setup_stmt=SETUP_STMT)

    common.test_update_row(MAX_TEXT_SIZE, result_payload)

@pytest.mark.livetest
def test_delete_row():
    common = SQLCommon(app_config)

    common.test_delete_row()

@pytest.mark.livetest
def test_altertable():
    common = SQLCommon(app_config)

    common.test_altertable()

@pytest.mark.livetest
def test_droptable():
    common = SQLCommon(app_config)

    common.test_droptable()

@pytest.mark.livetest
def test_blob():
    common = SQLCommon(app_config, table_name=BLOB_TABLE_NAME, table_def=blob_fields)

    common.test_createtable()

    common.test_insert_blob(MySqlDialect.make_blob)
