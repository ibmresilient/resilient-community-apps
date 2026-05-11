# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-urlhaus
"""

import logging
from resilient_lib import RequestsCommon, validate_fields, IntegrationError
from fn_urlhaus.util.helper import CONFIG_DATA_SECTION, make_api_call, format_dict

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def print_error(reason, app_configs):
    err_str = "Test Failure!\nReason:\n\t{0}".format(reason)
    err_str += "\n\nApp Configs:"
    err_str += format_dict(app_configs)
    log.error(err_str)


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    app_configs = opts.get(CONFIG_DATA_SECTION, {})
    rc = RequestsCommon(opts, app_configs)

    try:
        # Get and validate app configs
        valid_app_configs = validate_fields(["url"], app_configs)

        # Execute api call
        res = make_api_call(
            call_type="lookup",
            base_url=valid_app_configs.get("url"),
            artifact_type="URL",
            artifact_value="www.ibm.com",
            rc=rc
        )

        if res.status_code == 200:
            log.info("Test was successful!")
            return {"state": "success"}

        else:
            raise IntegrationError("Response was not successful")

    except Exception as err:
        print_error(err, app_configs)
        return {"state": "failure", "reason": err}
