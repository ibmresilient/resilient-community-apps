# -*- coding: utf-8 -*-

import logging
from fn_odbc_query.util.odbc_utils import OdbcConnection, odbcDBs
from fn_odbc_query.util.function_utils import PACKAGE_NAME
from resilient_lib import str_to_bool

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    db_list = [PACKAGE_NAME] if opts.get(PACKAGE_NAME, {}) else odbcDBs(opts).get_database_name_list()

    reason = None
    odbc_connection = None
    try:
        for db_name in db_list:
            database = opts.get(db_name, {})

            sql_connection_string = database["sql_connection_string"]
            sql_autocommit = str_to_bool(database.get("sql_autocommit", 'False'))
            sql_query_timeout = database.get("sql_query_timeout")
            sql_query_timeout = int(sql_query_timeout) if sql_query_timeout else None

            odbc_connection = OdbcConnection(sql_connection_string, sql_autocommit, sql_query_timeout)
            status = True if odbc_connection else False
            log.info(f"Test for {db_name} was successful")
    except Exception as err:
        status = False
        reason = str(err)
    finally:
        if odbc_connection:
            odbc_connection.close_connections()

    return {
        "state": "success" if status else "failure",
        "reason": reason
    }
