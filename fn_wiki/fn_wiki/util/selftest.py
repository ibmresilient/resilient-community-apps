# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_wiki
"""

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_wiki", {})

    return {
        "state": "success",
        "reason": None
    }