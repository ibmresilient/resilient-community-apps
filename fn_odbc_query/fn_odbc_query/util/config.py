# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_odbc_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_odbc_query]
# Define your connection string
sql_connection_string=Driver={PostgreSQL};Server=IPAddress;Port=5432;Database=myDataBase;Uid=myUserName;Pwd=myPassword;

# Optional settings:

# Define restricted SQL statements as a list, separated by a comma, using square brackets.
# Example: ["delete", "update", "insert"].
# Comment out this line if there are no restrictions.
sql_restricted_sql_statements=["delete", "insert", "update"]

# Define number of rows to fetch.
# Comment out this line to fetch all.
sql_number_of_records_returned=10

# Executes commits automatically after every SQL statement.
# Comment out this line to use false - the default.
sql_autocommit=true

# Unicode encoding and decoding settings needed for your SQL database.
# MariaDB, PostgreSQL and MySQL encoding/decoding settings are supported out of the box.
# Recent SQLServer drivers match the specification, no additional Unicode configuration is necessary.
# Define which supported setting to use by using one of the keywords:
# MariaDB, PostgreSQL, MySQL, SQLServer
# If commented out, none of the supported encoding/decoding settings will be configured.
sql_database_type=PostgreSQL

# Define query timeout in seconds.
# If commented out, the default value 0 is used, which means "no timeout".
# Some ODBC drivers do not implement the connection timeout and will throw pyodbc.Error while trying to set it.
# The error will be logged as a warning and will not terminate the workflow.
#sql_query_timeout=10
    """
    return config_data

