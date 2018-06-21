#
# Unit tests for fn_odbc_query/util/odbc_utils.py
#
#
#
try:
    from unittest.mock import patch
except:
    from mock import patch
from fn_odbc_query.util import odbc_utils
import pyodbc

class TestOdbcUtils:
    #
    # Test data
    fake_sql_connection_string = "Driver={PostgreSQL};Server=IP Address;Port=5432;Database=myDataBase;Uid=myUserName;Pwd=myPassword;"

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_odbc_connection_setup_timeout_pyodbc_error_pass(self, mocked_pyodbc_connect):
        print("Test setup odbc connection set timeout pyodbc.Error pass")

        class PostgresODBCConnection(object):

            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        mocked_pyodbc_connect.return_value = PostgresODBCConnection()

        try:
            odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
            assert True
        except Exception:
            assert False

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_odbc_connection_setup_timeout_unknown_error(self, mocked_pyodbc_connect):
        print("Test setup odbc connection set timeout pyodbc.Error pass")

        class PostgresODBCConnection(object):

            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Driver doesn't support this")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        try:
            odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
            assert False
        except Exception:
            assert True

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_configure_unicode_settings(self, mocked_pyodbc_connect):
        print("Test configure unicode settings")

        class PostgresODBCConnection:
            def setencoding(self, *args, **kwargs):
                return None
            
            def setdecoding(self, *args, **kwargs):
                return None

            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        OdbcConnection.configure_unicode_settings("mariadb") # doesn't matter what arg is as long as it's mariadb, postgresql, or mysql same result

        assert True

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_set_db_cursor(self, mocked_pyodbc_connect):
        print("Test set db cursor")

        class PostgresODBCConnection:
            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        OdbcConnection.set_db_cursor(None)

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_create_cursor(self, mocked_pyodbc_connect):
        print("Test create cursor")

        class PostgresODBCConnection:
            def cursor(self):
                return None

            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        OdbcConnection.create_cursor()

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_execute_select_statement(self, mocked_pyodbc_connect):
        print("Test execute select statement")

        class PostgresODBCConnection:
            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        class FakeDBCursor:
            def execute(self, sql_query, sql_params):
                return None

            def fetchmany(self, sql_number_of_records_returned):
                return None

            def fetchall(self):
                return None

        db_cursor = FakeDBCursor()
        OdbcConnection.set_db_cursor(db_cursor)
        OdbcConnection.execute_select_statement("", "", 1)
        OdbcConnection.execute_select_statement("", "", None)

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_get_cursor_description(self, mocked_pyodbc_connect):
        print("Test get cursor description")

        class PostgresODBCConnection:
            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        class FakeDBCursor:
            @property
            def description(self):
                return ""
            

        db_cursor = FakeDBCursor()
        OdbcConnection.set_db_cursor(db_cursor)
        OdbcConnection.get_cursor_description()

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_execute_odbc_query(self, mocked_pyodbc_connect):
        print("Test execute odbc query")

        class PostgresODBCConnection:
            autocommit = None
            
            def commit():
                return None

            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        class FakeDBCursor:
            def execute(self, sql_query, sql_params):
                return None

            @property
            def rowcount(self):
                return 0
            

        db_cursor = FakeDBCursor()
        OdbcConnection.set_db_cursor(db_cursor)
        OdbcConnection.execute_odbc_query("", "")

    @patch("fn_odbc_query.util.odbc_utils.pyodbc.connect")
    def test_close_connections(self, mocked_pyodbc_connect):
        print("Test close connections")

        class PostgresODBCConnection:
            def close(self):
                return None

            @property
            def timeout(self):
                return 1

            @timeout.setter
            def timeout(self, value):
                raise pyodbc.Error('HY000',
                                   "[HY000] Couldn't set unsupported connect attribute 113 (216) (SQLSetConnectAttr)")

        db_connection = PostgresODBCConnection()
        mocked_pyodbc_connect.return_value = db_connection

        OdbcConnection = None
        try:
            OdbcConnection = odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
        except Exception:
            assert False

        class FakeDBCursor:
            def close(self):
                return None

        db_cursor = FakeDBCursor()
        OdbcConnection.set_db_cursor(db_cursor)
        OdbcConnection.close_connections()




