# -*- coding: utf-8 -*-

import logging
import datetime
import pytest
import sys

from lib.test_sql_common import SQLCommon, blob_fields, BLOB_TABLE_NAME
from data_feeder_plugins.sqllib.sql_dialect import SqlServerDialect

LOG = logging.getLogger(__name__)

# make sure this db already exists
TEST_DB = "res_test"

MAX_TEXT_SIZE = 65000

FIND_COLUMNS_STMT = "SELECT column_name, data_type FROM information_schema.columns WHERE  table_name='{table_name}'"

app_config = {
    "class": "ODBCFeed",
    "odbc_connect": "DRIVER={{FreeTDS}};SERVER=192.168.1.215;PORT=1433;DATABASE={db}".format(db=TEST_DB),
    "sql_dialect": "SQLServerDialect",
    "uid": "res_test",
    "pwd": "R#s_test"
}

SETUP_STMT = "set timezone='UTC'"


result_payload = {  "id":  101,
                    "inc_id": 2301,
                    "test_text": u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ",
                    "test_int": 1000,
                    "test_date": datetime.date(2019, 2, 13),
                    "test_bool": True
                    }

if sys.version_info.major == 2:
    result_payload['test_datetime'] = datetime.datetime(2019, 2, 13, 15, 55, 47)
else:
    result_payload['test_datetime'] = datetime.datetime(2019, 2, 13, 15, 55, 47, 448000)

def test_default_passing_test():
    # needed to allow travis tox to pass with one successful test
    pass

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
    common = SQLCommon(app_config)

    common.test_insert_row(result_payload)

@pytest.mark.livetest
def test_update_row():
    common = SQLCommon(app_config)

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

    common.test_insert_blob(None)
