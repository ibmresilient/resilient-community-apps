# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-parse-utilities
    resilient-circuits selftest --print-env -l fn-parse-utilities

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
from os.path import join, exists, isfile

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_parse_utilities", {})

    # Get the stylesheet
    stylesheet_dir = join(app_configs.get("xml_stylesheet_dir"))
    if not (exists(stylesheet_dir)):
        return{
            "state": "failure",
            "reason": "Stylesheet directory not found."
        }

    return {
        "state": "success",
        "reason": None
    }
