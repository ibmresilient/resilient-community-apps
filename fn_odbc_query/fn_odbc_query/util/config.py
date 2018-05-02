# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_odbc_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_odbc_query]
# Database server url
sql_server_url=127.0.0.1
# Database type [SQLite, MySQL, MariaDB]
sql_db_type = MariaDB
sql_port=3306
sql_uid=root
sql_pwd=password
    """
    return config_data

