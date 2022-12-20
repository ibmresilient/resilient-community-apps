# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""
Function implementation test.
Usage:
    resilient-circuits selftest -l fn-github
    resilient-circuits selftest --print-env -l fn-github

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
from fn_github.lib.client_helper import GitHubHelper

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_github", {})

    gh = GitHubHelper(None, None, app_configs)
    _results, err_msg = gh.get_repositories("owner")

    return {
        "state": "success" if not err_msg else "failure",
        "reason": err_msg
    }
