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
    app_configs = opts.get("fn_odbc_query", {})
    OdbcConnection(app_configs.get("sql_connection_string"))

    return {
        "state": "success",
        "reason": None
    }
