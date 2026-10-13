# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-vmware-cbc
    resilient-circuits selftest --print-env -l fn-vmware-cbc

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
import time
import logging
from resilient_lib import IntegrationError, RequestsCommon
from fn_vmware_cbc.lib.app_common import PACKAGE_NAME, AppCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """ Selftest function used to test connectivity to the VMware Carbon Black Cloud endpoint

    Args:
        opts (dict): app.config options

    Returns:
        dict: dictionary containing state: success or failure; and reason if failure
    """
    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        # If we can create an AppCommon object we are able to get an access token.
        app_common = AppCommon(PACKAGE_NAME, app_configs)
        results, err_msg = app_common.query_entities_since_ts(int(time.time()))
        reason = err_msg
        state = "success" if not err_msg else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }