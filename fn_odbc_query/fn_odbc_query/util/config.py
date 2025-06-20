# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_odbc_query"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""
# V1.1.0+ have the option to have multiple servers configured.
# By default two examples of servers are given, example one is labeled `database_label1` and example two is labeled `database_label2`.
# The label for a server is placed after `[fn_odbc_query:` and then followed by `]`.
# To add additional servers copy the below example server configuration from `[fn_odbc_query:database_label1]` to `#sql_query_timeout=10`.
# Then paste it at the bottom of the app.config.
# Change the server label, `database_label1`, to a label helpful to define that server.
# Then change the setting to those of the server you wish to add.

[fn_odbc_query:database_label1]
# (Required) Define your connection string
sql_connection_string=Driver={PostgreSQL};Server=IPAddress;Port=5432;Database=myDataBase;Uid=myUserName;Pwd=myPassword;
# Define restricted SQL statements as a list, separated by a comma, using square brackets.
sql_restricted_sql_statements=["delete", "insert", "update"]
# Define number of rows to fetch.
sql_number_of_records_returned=10
# Executes commits automatically after every SQL statement.
sql_autocommit=true
# Define which supported setting to use by using one of the keywords:
# MariaDB, PostgreSQL, MySQL, SQLServer, Oracle
sql_database_type=PostgreSQL
# Define query timeout in seconds.
#sql_query_timeout=10

[fn_odbc_query:database_label2]
# Define your connection string
sql_connection_string=Driver={Oracle 12c ODBC driver};DBQ=<server>:1521/<db>;Uid=<user>;Pwd=<pwd>;
# Define restricted SQL statements as a list, separated by a comma, using square brackets.
sql_restricted_sql_statements=["delete", "insert", "update"]
# Define number of rows to fetch.
sql_number_of_records_returned=10
# Executes commits automatically after every SQL statement.
sql_autocommit=true
# Define which supported setting to use by using one of the keywords:
# MariaDB, PostgreSQL, MySQL, SQLServer, Oracle
sql_database_type=Oracle
# Define query timeout in seconds.
#sql_query_timeout=10
"""
