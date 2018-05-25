# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_odbc_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_odbc_query]
# Define your connection string
#sql_connection_string=DRIVER={MariaDB ODBC 3.0 Driver};SERVER=127.0.0.1;PORT=3306;UID=root;PWD=password;Connection Timeout=60;
sql_connection_string=Driver={PostgreSQL};Server=localhost;Port=5432;Database=postgres_test_database;Uid=postgres;Pwd=password;Timeout=60;

# Optional setting
# Define a list of restricted SQL statements, separated by a comma.
# Example ["delete", "update", "insert"]. 
# Comment this line if there are no restrictions.
sql_restricted_sql_statements=["delete", "insert", "update"]

# Optional setting
# Define if you wish to execute commits automatically after every SQL statement.
# Comment this line to use false - the default.
sql_autocommit=true

# Optional setting
# Might not be supported for all database drivers.
# Define a query timeout in seconds. 
# Comment this line to use the default 0, which means "no timeout".
sql_query_timeout=10

# Optional setting
# Encoding and decoding settings needed for your SQL database.
# Define which one of supported SQL Server database settings you want to use. 
# At the moment MariaDB, PostgreSQL and MySQL are supported.
# Comment this line if you don't wish to configure decoding/encoding.
sql_database_type=MariaDB

# Optional setting
# Define number of rows to fetch. 
# Comment this line to fetch all.
sql_number_of_records_returned=10
    """
    return config_data

