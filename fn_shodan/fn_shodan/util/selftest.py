# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2020. All Rights Reserved.

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_shodan
"""

import logging
from resilient_lib import validate_fields, IntegrationError
from fn_shodan.util.helper import CONFIG_DATA_SECTION, make_api_call, format_dict


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

    try:
        # Get and validate app configs
        valid_app_configs = validate_fields([{"name": "shodan_apikey", "placeholder": "<your-api-key>"}], app_configs)

        # Execute api call
        res = make_api_call(
            call_type="info",
            api_key=valid_app_configs.get("shodan_apikey"),
            app_configs=valid_app_configs
        )

        if not res.get("query_credits") is None:
            log.info("Test was successful!\nResponse from Shodan:\n%s", res)
            return {"state": "success"}

        else:
            raise IntegrationError("Response from Shodan was not successful")

    except Exception as err:
        print_error(err, app_configs)
        return {"state": "failure", "reason": err}
