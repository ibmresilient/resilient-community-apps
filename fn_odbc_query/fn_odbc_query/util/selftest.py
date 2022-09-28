# -*- coding: utf-8 -*-

import logging
from fn_odbc_query.util.odbc_utils import OdbcConnection
from resilient_lib import str_to_bool

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_odbc_query", {})
    sql_connection_string = options["sql_connection_string"]
    sql_autocommit = str_to_bool(options.get("sql_autocommit", 'False'))
    sql_query_timeout = options.get("sql_query_timeout", None)
    sql_query_timeout = int(sql_query_timeout) if sql_query_timeout else None

    reason = None
    odbc_connection = None
    try:
        odbc_connection = OdbcConnection(sql_connection_string, sql_autocommit, sql_query_timeout)
        status = True if odbc_connection else False
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
