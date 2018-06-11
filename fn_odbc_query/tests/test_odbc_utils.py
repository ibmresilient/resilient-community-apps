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

    @patch("pyodbc.connect")
    def test_odbc_connection_setup_timeout_pyodbc_error_pass(self, mocked_pyodbc_connect):
        print("Test setup odbc connection set timeout pyodbc.Error pass")

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

        try:
            odbc_utils.OdbcConnection(self.fake_sql_connection_string, True, 10, 'HY000')
            assert True
        except Exception:
            assert False

    @patch("pyodbc.connect")
    def test_odbc_connection_setup_timeout_unknown_error(self, mocked_pyodbc_connect):
        print("Test setup odbc connection set timeout pyodbc.Error pass")

        class PostgresODBCConnection:

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
