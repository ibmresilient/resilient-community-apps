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

# Define number of rows to fetch. Leave blank to fetch all.
sql_number_of_records_returned = 10

# Define a list of restricted sql statements, separated by a comma. Leave blank if there are no restrictions.
sql_restricted_sql_statements=[delete, insert, update]

# Encoding and decoding settings needed for your database
# Define which SQL Server settings you want to use. 
# Leave sql_database_type blank if you don't wish to configure decoding/encoding.
# Supported database types are [MariaDB, PostgreSQL, MySQL]
sql_database_type=MariaDB
    """
    return config_data

