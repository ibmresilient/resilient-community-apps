# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.2.575

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-axonius
    resilient-circuits selftest --print-env -l fn-axonius

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
from resilient_lib import IntegrationError, RequestsCommon
from fn_axonius.lib.axonius_client import PACKAGE_NAME, AxoniusClient, IntegrationError

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        rc = RequestsCommon(opts, app_configs)

        # Call get device_count endpoint that does not have any parameters.
        axonius_client = AxoniusClient(rc, PACKAGE_NAME, app_configs)
        query = "((\"internal_axon_id\" == ({\"$exists\":true,\"$ne\":\"\"})))"
        result, err_msg = axonius_client.get_device_count(query=query, saved_query_name=None)
        reason = err_msg
        state = "success" if not err_msg else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }
