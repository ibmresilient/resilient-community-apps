# -*- coding: utf-8 -*-

import cx_Oracle
import logging
import os
from collections import OrderedDict
from data_feeder_plugins.odbcfeed.odbcfeed import ODBCFeedDestination
from rc_data_feed.lib.type_info import TypeInfo, ActionMessageTypeInfo

LOG = logging.getLogger(__name__)

TABLE_NAME = "all_types"
BLOB_TABLE_NAME = "blob_test"

FIND_COLUMNS_QUERY = "SELECT column_name, data_type FROM information_schema.columns WHERE  table_name='{table_name}'"

all_fields = [
    {"name": "id", "input_type": "number"},
    {"name": "inc_id", "input_type": "number"},
    {"name": "test_text", "input_type": "text"},
    {"name": "test_int",  "input_type": "number"},
    {"name": "test_date", "input_type": "datepicker"},
    {"name": "test_datetime", "input_type": "datetimepicker"},
    {"name": "test_bool",  "input_type": "boolean"}
]

blob_fields = [
    {"name": "id", "input_type": "number"},
    {"name": "inc_id", "input_type": "number"},
    {"name": "content", "input_type": "blob"}
]

flat_payload = OrderedDict()
flat_payload["id"] =  101
flat_payload["inc_id"] = 2301
flat_payload["test_text"] = u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ"
flat_payload["test_int"] = 1000
flat_payload["test_date"] = 1550073347448
flat_payload["test_datetime"] = 1550073347448
flat_payload["test_bool"] = True


class SQLCommon():
    def __init__(self, app_config, table_name=TABLE_NAME, table_def=all_fields, inspect_cols_query=FIND_COLUMNS_QUERY,
                 baseClass=ODBCFeedDestination, setup_stmt=None, dialect=None):
        self.app_config = app_config
        self.table_name = table_name
        self.table_def = table_def
        self.inspect_cols_query = inspect_cols_query.format(table_name=self.table_name)
        self.baseClass = baseClass
        self.setup_stmt = setup_stmt
        self.dialect = dialect

        self.all_field_names = [field['name'] for field in table_def]
        self.all_field_types = dict()
        for field in table_def:
            self.all_field_types[field['name']] = field['input_type']

    def test_get_parameters(self, all_field_names=None, payload=flat_payload):
        connection = self.baseClass(None, self.app_config)

        if not all_field_names:
            all_field_names = self.all_field_names

        try:
            parameters = connection.dialect.get_parameters(all_field_names, payload)

            # sqlite returned the original dictionary
            if isinstance(parameters, list):
                payload_keys = [key for key in payload.values()]
                for ndx in range(len(payload)):
                    assert parameters[ndx] == payload_keys[ndx]
            else:
                for key in payload.keys():
                    assert parameters[key] == payload[key]

        finally:
            if hasattr(connection, "_close_connection"):
                connection._close_connection()

    def test_createtable(self):
        connection = self.baseClass(None, self.app_config)
        try:
            # find all the columns types by column name we expect
            exected_col_types = {}

            for field in self.table_def:
                field_name = field['name']
                field_type = field['input_type']
                col_type = connection.dialect.get_column_type(field_type)
                exected_col_types[field_name.lower()] = col_type.lower()

            connection._create_or_update_table(self.table_name, self.table_def)

            # confirm that the table was created
            cursor = connection._start_transaction()
            try:
                get_cols_result = connection._execute_sql(
                    cursor,
                    self.inspect_cols_query)

                table_cols = {}
                for row in get_cols_result:
                    col_name = row[0]
                    col_type = row[1]
                    table_cols[col_name.lower()] = col_type.lower()

                for col in exected_col_types.keys():
                    if col in ('id', 'inc_id'):
                        assert table_cols.get(col, '').startswith('int') or table_cols.get(col, '').startswith("number")
                    else:
                        db_col = table_cols.get(col, '')
                        col_type = db_col.split("(")[0]
                        col_type_simple = col_type.split(" ")[0]
                        assert exected_col_types[col].startswith(col_type_simple)
            finally:
                if 'cursor' in locals():
                    cursor.close()
        finally:
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_insert_row(self, result_payload, row_payload=flat_payload):
        connection = self.baseClass(None, self.app_config)
        translate_value_funct = getattr(connection.dialect,
                                        'mapped_translate_value',
                                        TypeInfo.translate_value)
        try:
            payload = row_payload.copy()
            # convert data for the fields
            for field in self.table_def:
                item_name = field['name']
                item_type = field['input_type']
                item_value = row_payload[item_name]
                converted_value = translate_value_funct(None, field, item_value)
                payload[item_name] = converted_value

            # add data to table
            cursor = connection._start_transaction()

            if self.setup_stmt:
                connection._execute_sql(
                    cursor,
                    self.setup_stmt)

            cmd = connection.dialect.get_upsert(self.table_name, self.all_field_names, self.all_field_types)
            params = connection.dialect.get_parameters(self.all_field_names, payload)

            insert_result = connection._execute_sql(
                cursor,
                cmd,
                params
            )

            connection._commit_transaction(cursor)

            if hasattr(insert_result, 'nextset'):
                while insert_result.nextset():
                    row_count = insert_result.rowcount
                    assert row_count == 1

            # get the row and confirm the values
            select_stmt = "select * from {} where id = {}".format(self.table_name, payload["id"]) # nosec
            select_result = connection._execute_sql(
                cursor,
                select_stmt)

            rows = cursor.fetchall()
            for row in rows:
                for ndx in range(len(select_result.description)):
                    col_name = select_result.description[ndx][0].lower()
                    if isinstance(row[ndx], cx_Oracle.LOB):
                        assert row[ndx].read() == result_payload[col_name]
                    elif isinstance(row[ndx], (bytes, bytearray)):
                        assert row[ndx][0:10] == result_payload[col_name][0:10]
                    else:
                        assert row[ndx] == result_payload[col_name]

        finally:
            if 'cursor' in locals():
                cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_update_row(self, MAX_TEXT_SIZE, result_payload):
        global flat_payload

        connection = self.baseClass(None, self.app_config)
        translate_value_funct = getattr(connection.dialect,
                                        'mapped_translate_value',
                                        TypeInfo.translate_value)

        try:
            payload = flat_payload.copy()
            # convert data for the fields
            for field in self.table_def:
                item_name = field['name']
                item_type = field['input_type']
                item_value = flat_payload[item_name]
                converted_value = translate_value_funct(None, field, item_value)
                payload[item_name] = converted_value

            payload['test_text'] = u"a" * MAX_TEXT_SIZE

            payload_result = result_payload.copy()
            payload_result['test_text'] = payload['test_text']

            # add data to table
            cursor = connection._start_transaction()

            if self.setup_stmt:
                connection._execute_sql(
                    cursor,
                    self.setup_stmt)

            update_result = connection._execute_sql(
                cursor,
                connection.dialect.get_upsert(self.table_name, self.all_field_names, self.all_field_types),
                connection.dialect.get_parameters(self.all_field_names, payload))

            connection._commit_transaction(cursor)

            #assert update_result.rowcount == 1

            # get the row and confirm the values
            select_stmt = "select * from {} where id = {}".format(self.table_name, payload["id"]) # nosec
            select_result = connection._execute_sql(
                cursor,
                select_stmt)

            rows = cursor.fetchall()
            for row in rows:
                for ndx in range(len(select_result.description)):
                    col_name = select_result.description[ndx][0].lower()
                    assert row[ndx] == payload_result[col_name]

        finally:
            if 'cursor' in locals():
                cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()

    def test_delete_row(self):
        global flat_payload
        connection = self.baseClass(None, self.app_config)
        cursor = connection._start_transaction()

        try:
            # delete the row
            delete_stmt = connection.dialect.get_delete(self.table_name)
            params = connection.dialect.get_parameters(['id'], {'id': flat_payload['id']})
            LOG.info(delete_stmt)

            delete_result = connection._execute_sql(
                cursor,
                delete_stmt,
                params
            )

            connection._commit_transaction(cursor)

            assert delete_result.rowcount == 1
        finally:
            if 'cursor' in locals():
                cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_altertable(self, col_type='text'):
        global flat_payload

        ALTER_COL = "alter_col"
        connection = self.baseClass(None, self.app_config)
        cursor = connection._start_transaction()
        try:
            alter_result = connection._execute_sql(
                cursor,
                connection.dialect.get_add_column_to_table(self.table_name, ALTER_COL, col_type))

            connection._commit_transaction(cursor)

            get_cols_result = connection._execute_sql(
                cursor,
                self.inspect_cols_query)

            rows = cursor.fetchall()
            assert len(rows) == 8    # number of columns

        finally:
            if 'cursor' in locals():
                cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()

    def test_droptable(self):
        connection = self.baseClass(None, self.app_config)
        cursor = connection._start_transaction()
        try:
            alter_result = connection._execute_sql(
                cursor,
                "Drop table {}".format(self.table_name))

            connection._commit_transaction(cursor)

        finally:
            if 'cursor' in locals():
                cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()

    def test_insert_blob(self, translate_blob):
        blob_data = self.get_blob_data()
        #LOG.info(blob_data)

        row_payload = OrderedDict()
        row_payload["id"] =  101
        row_payload["inc_id"] =  2301
        row_payload["content"] = blob_data

        result_blob = translate_blob(None, None, blob_data) if translate_blob else blob_data

        result_payload = OrderedDict()
        result_payload["id"] =  101
        result_payload["inc_id"] =  2301
        result_payload["content"] = result_blob if isinstance(result_blob, (bytes, bytearray, memoryview)) \
                                                else bytes(result_blob, 'utf-8')

        self.test_insert_row(result_payload, row_payload=row_payload)

    def get_blob_data(self, filename="app_logo.png"):
        with open(os.path.join(os.path.dirname(__file__), "data/{}".format(filename)), 'rb') as f:
            return f.read()
