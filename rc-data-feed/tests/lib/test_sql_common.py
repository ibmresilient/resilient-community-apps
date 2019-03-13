import logging
from collections import OrderedDict
from rc_data_feed.lib.odbc_feed import ODBCFeedDestination
from rc_data_feed.lib.type_info import TypeInfo, ActionMessageTypeInfo

LOG = logging.getLogger(__name__)


TABLE_NAME = "all_types"

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


flat_payload = OrderedDict({ "id":  10,
                             "inc_id": 2301,
                             "test_text": u"this is a text field",
                             "test_int": 1000,
                             "test_date": 1550073347448,
                             "test_datetime": 1550073347448,
                             "test_bool": True
                             })


class SQLCommon():
    def __init__(self, app_config, table_name=TABLE_NAME, table_def=all_fields, inspect_cols_query=FIND_COLUMNS_QUERY, baseClass=ODBCFeedDestination):
        self.app_config = app_config
        self.table_name = table_name
        self.table_def = table_def
        self.inspect_cols_query = inspect_cols_query.format(table_name=self.table_name)
        self.baseClass = baseClass


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
                for ndx in range(len(flat_payload)):
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

            for field in all_fields:
                field_name = field['name']
                field_type = field['input_type']
                col_type = connection.dialect.get_column_type(field_type)
                exected_col_types[field_name.lower()] = col_type.lower()

            connection._create_or_update_table(self.table_name, all_fields)

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
                    print(col, table_cols.get(col, ''), exected_col_types[col])
                    assert table_cols.get(col, '').startswith(exected_col_types[col])
            finally:
                cursor.close()
        finally:
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_insert_row(self, result_payload):
        global flat_payload

        connection = self.baseClass(None, self.app_config)
        try:
            payload = flat_payload.copy()
            # convert data for the fields
            for field in all_fields:
                item_name = field['name']
                item_type = field['input_type']
                item_value = flat_payload[item_name]
                converted_value = TypeInfo.translate_value(None, field, item_value)
                payload[item_name] = converted_value

            # add data to table
            cursor = connection._start_transaction()

            insert_result = connection._execute_sql(
                cursor,
                connection.dialect.get_upsert(TABLE_NAME, self.all_field_names, self.all_field_types),
                connection.dialect.get_parameters(self.all_field_names, payload))

            connection._commit_transaction(cursor)

            assert insert_result.rowcount == 1

            # get the row and confirm the values
            select_stmt = "select * from {} where id = {}".format(TABLE_NAME, payload["id"])
            select_result = connection._execute_sql(
                cursor,
                select_stmt)

            rows = cursor.fetchall()
            for row in rows:
                for ndx in range(len(select_result.description)):
                    col_name = select_result.description[ndx][0]
                    print (row[ndx])
                    assert row[ndx] == result_payload[col_name]

        finally:
            cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_update_row(self, MAX_TEXT_SIZE, result_payload):
        global flat_payload

        connection = self.baseClass(None, self.app_config)
        try:
            payload = flat_payload.copy()
            # convert data for the fields
            for field in all_fields:
                item_name = field['name']
                item_type = field['input_type']
                item_value = flat_payload[item_name]
                converted_value = TypeInfo.translate_value(None, field, item_value)
                payload[item_name] = converted_value

            payload['test_text'] = u"a" * MAX_TEXT_SIZE

            payload_result = result_payload.copy()
            payload_result['test_text'] = payload['test_text']

            # add data to table
            cursor = connection._start_transaction()

            update_result = connection._execute_sql(
                cursor,
                connection.dialect.get_upsert(TABLE_NAME, self.all_field_names, self.all_field_types),
                connection.dialect.get_parameters(self.all_field_names, payload))

            connection._commit_transaction(cursor)

            #assert update_result.rowcount == 1

            # get the row and confirm the values
            select_stmt = "select * from {} where id = {}".format(TABLE_NAME, payload["id"])
            select_result = connection._execute_sql(
                cursor,
                select_stmt)

            rows = cursor.fetchall()
            for row in rows:
                for ndx in range(len(select_result.description)):
                    col_name = select_result.description[ndx][0]
                    assert row[ndx] == payload_result[col_name]

        finally:
            cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()

    def test_delete_row(self):
        global flat_payload
        connection = self.baseClass(None, self.app_config)
        cursor = connection._start_transaction()

        try:
            # delete the row
            delete_result = connection._execute_sql(
                cursor,
                connection.dialect.get_delete(TABLE_NAME),
                [flat_payload['id']])

            connection._commit_transaction(cursor)

            assert delete_result.rowcount == 1
        finally:
            cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_altertable(self):
        global flat_payload

        ALTER_COL = "alter_col"
        connection = self.baseClass(None, self.app_config)
        cursor = connection._start_transaction()
        try:
            print (connection.dialect.get_add_column_to_table(TABLE_NAME, ALTER_COL, "text"))
            alter_result = connection._execute_sql(
                cursor,
                connection.dialect.get_add_column_to_table(TABLE_NAME, ALTER_COL, "text"))

            connection._commit_transaction(cursor)

            get_cols_result = connection._execute_sql(
                cursor,
                self.inspect_cols_query)

            rows = cursor.fetchall()
            assert len(rows) == 8    # number of columns

        finally:
            cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()


    def test_droptable(self):
        connection = self.baseClass(None, self.app_config)
        cursor = connection._start_transaction()
        try:
            alter_result = connection._execute_sql(
                cursor,
                "Drop table {}".format(TABLE_NAME))

            connection._commit_transaction(cursor)

        finally:
            cursor.close()
            if hasattr(connection, "_close_connection"):
                connection._close_connection()
