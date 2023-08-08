# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-salesforce
    resilient-circuits selftest --print-env -l fn-salesforce

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
from resilient_lib import RequestsCommon, IntegrationError
from fn_salesforce.lib.app_common import PACKAGE_NAME, AppCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Call Salesforce  to make sure we can get access token. 

    """

    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        rc = RequestsCommon(opts, app_configs)

        # If we can create an AppCommon object we are able to get an access token.
        app_common = AppCommon(rc, PACKAGE_NAME, app_configs)
        reason = None
        state = "success"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }