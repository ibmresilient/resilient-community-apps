# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-yeti
    resilient-circuits selftest --print-env -l fn-yeti

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging
import pyeti

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):

    app_configs = opts.get("fn_yeti", {})

    try:
        yeti_client = pyeti.YetiApi(app_configs["url"], (app_configs["username"],
                                        app_configs["password"]), app_configs["apikey"])
   
        return {"state": "success"}
    except Exception as e:
        return {
            "state": "failure",
            "reason": e
        }