# -*- coding: utf-8 -*-

import logging
from fn_odbc_query.util.odbc_utils import OdbcConnection

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_odbc_query", {})

    reason = None
    try:
        response = OdbcConnection(options.get("sql_connection_string"))
        status = True if response else False
    except Exception as err:
        status = False
        reason = str(err)

    return {
        "state": "success" if status else "failure",
        "reason": reason
    }
