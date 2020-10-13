# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_vmray_analyzer
"""

import logging
from resilient_lib import validate_fields, RequestsCommon, IntegrationError
from fn_vmray_analyzer.util.vmrapi import VMRayAPI

CONFIG_DATA_SECTION = "fn_vmray_analyzer"
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    # Get app.config parameters.
    options = opts.get(CONFIG_DATA_SECTION, {})

    validate_fields(['vmray_api_key', 'vmray_analyzer_url', 'vmray_analyzer_report_request_timeout'], options)
    vmray_api_key = options.get("vmray_api_key")
    vmray_analyzer_url = options.get("vmray_analyzer_url")

    try:
        log.info(u"vmray_api_key: {0}\nvmray_analyzer_url: {1}".format(vmray_api_key, vmray_analyzer_url))
        state, reason = "", ""
        vmray = VMRayAPI(vmray_api_key, url=vmray_analyzer_url, proxies=RequestsCommon(opts, options).get_proxies())

        if vmray.is_available():
            state = "success"
        else:
            state = "failure"
            reason = "authorization failure"
    except IntegrationError as err:
        state = "failure"
        reason = err.value

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result