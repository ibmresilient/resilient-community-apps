# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_odbc_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_odbc_query]
#For testing purposes I'm connecting to MariaDB that lives on my Docker
sql_connection_string='DRIVER={MariaDB ODBC 3.0 Driver};SERVER=127.0.0.1;PORT=3306;UID=root;PWD=password;'
# The timeout value, in seconds, for an individual SQL query. Use zero to disable.
sql_connection_timeout = 60
# Return a list of specific number of rows in the query. Leave blank to fetch all.
sql_number_of_records_returned = 10
sql_allowed_statements=[select]
    """
    return config_data

