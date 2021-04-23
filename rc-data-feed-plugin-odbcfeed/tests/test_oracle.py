# -*- coding: utf-8 -*-

import logging
import datetime
import pytest

from lib.test_sql_common import SQLCommon, blob_fields, BLOB_TABLE_NAME
from data_feeder_plugins.sqllib.sql_dialect import OracleDialect 

LOG = logging.getLogger(__name__)

# make sure this db already exists
TEST_DB = "test_db"

MAX_TEXT_SIZE = 2000

FIND_COLUMNS_STMT = "SELECT column_name, data_type FROM user_tab_cols WHERE table_name = '{table_name}'"

app_config = {
    "class": "ODBCFeed",
    "odbc_connect": "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.215)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=ORCLCDB.localdomain)))",
    "sql_dialect": "OracleDialect",
    "uid": "res",
    "pwd": "res"
}


result_payload = {  "id":  101,
                    "inc_id": 2301,
                    "test_text": u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ",
                    "test_int": 1000,
                    "test_date": datetime.datetime(2019, 2, 13, 15, 55, 47),
                    "test_datetime": datetime.datetime(2019, 2, 13, 15, 55, 47, 448000),
                    "test_bool": 1
                    }

@pytest.mark.livetest
@pytest.mark.order1
def test_get_parameters():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_get_parameters()

@pytest.mark.livetest
def test_createtable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_createtable()

@pytest.mark.livetest
def test_insert_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_insert_row(result_payload)

@pytest.mark.livetest
def test_update_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_update_row(MAX_TEXT_SIZE, result_payload)

@pytest.mark.livetest
def test_delete_row():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_delete_row()

@pytest.mark.livetest
def test_altertable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_altertable(col_type='NVARCHAR2(2000)')

@pytest.mark.livetest
def test_droptable():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT, table_name='ALL_TYPES')

    common.test_droptable()

@pytest.mark.livetest
def test_blob():
    common = SQLCommon(app_config, inspect_cols_query=FIND_COLUMNS_STMT,
                       table_name=BLOB_TABLE_NAME.upper(), table_def=blob_fields)

    common.test_createtable()

    common.test_insert_blob(None)
