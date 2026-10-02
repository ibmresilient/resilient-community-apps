# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.1.0.695

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-wiz
    resilient-circuits selftest --print-env -l fn-wiz

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
from requests import HTTPError

from resilient_lib import RequestsCommon
from fn_wiz.lib.app_common import AppCommon, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Test connectivity to Wiz API by trying to generate an authorization bearer token with provided credentials
    If unable to successfully reach token endpoint, returns ``failure``
    """
    try:
        app_configs = opts.get(PACKAGE_NAME, {})

        rc = RequestsCommon(opts, app_configs)
        app_common = AppCommon(rc, PACKAGE_NAME, app_configs)

        token = app_common._generate_auth_token()
        
        if token:
            return {
                "state": "success",
                "reason": "Successfully connected to Wiz authentication endpoint"
            }
        
        reason = "Unable to reach Wiz authentication endpoint."

    except HTTPError as http_err:
        reason = str(http_err)

    return {
        "state": "failure",
        "reason": reason
    }
