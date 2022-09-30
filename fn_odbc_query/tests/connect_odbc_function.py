# Helper class for testing multiple active connections.
#
# Open odbc connection and run it simultaneously with fn_odbc_query function invoked through Resilient.
#
# Multiple active connections are ODBC driver-specific and it is possible that some databases
# won't handle more than one active connection.
#
# We've tested opening two active connections to the same db and issuing the same select statement on both.
# PostgreSQL psqlodbc driver and MariaDB Connector/ODBC 3.0.2 driver can handle multiple active connections.
from fn_odbc_query.util import odbc_utils
from fn_odbc_query.util import function_utils


def connect_postgreslq():
    # Open odbc connection to test database PostgreSQL server, run locally in Docker.
    # Create cursor and stop at breakpoint.
    # Invoke function fn_odbc_query through Resilient (configured to connect to the same PostgreSQL db)
    # to test if multiprocessing works.
    # PostgreSQL psqlodbc driver can handle multiple active connections.
    sql_connection_string = "Driver={PostgreSQL};Server=localhost;Port=5432;Database=postgres_test_database;Uid=postgres;Pwd=password;Timeout=60;"
    odbc_connection = odbc_utils.OdbcConnection(sql_connection_string, True, 10, "HY000")
    odbc_connection.configure_unicode_settings("postgresql")
    odbc_connection.create_cursor()

    sql_query = "SELECT id AS sql_column_1, first_name AS sql_column_2, last_name AS sql_column_3 FROM mock_data WHERE id = ?"
    sql_params = [6]
    rows = odbc_connection.execute_select_statement(sql_query, sql_params, 10)
    results = function_utils.prepare_results(odbc_connection.get_cursor_description(), rows)

    print(results)


def connect_mariadb():
    # Open odbc connection to test database MariaDB server, run locally in Docker.
    # Create cursor and stop at breakpoint.
    # Invoke function fn_odbc_query through Resilient (configured to connect to the same MariaDB db)
    # to test if multiprocessing works.
    # MariaDB Connector/ODBC 3.0.2 driver can handle multiple active connections.
    sql_connection_string = "DRIVER={MariaDB ODBC 3.0 Driver};SERVER=127.0.0.1;PORT=3306;UID=root;PWD=password;Connection Timeout=60;"
    odbc_connection = odbc_utils.OdbcConnection(sql_connection_string, True, 10, "HY000")
    odbc_connection.configure_unicode_settings("mariadb")
    odbc_connection.create_cursor()

    sql_query = "SELECT incident_id AS sql_column_1, name AS sql_column_2, description AS sql_column_3 FROM test.incidents WHERE incident_id = ?"
    sql_params = [1]
    rows = odbc_connection.execute_select_statement(sql_query, sql_params, 10)
    results = function_utils.prepare_results(odbc_connection.get_cursor_description(), rows)

    print(results)


connect_postgreslq()
#connect_mariadb()
