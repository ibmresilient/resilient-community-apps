# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-ip-void
"""

import logging
from resilient_lib import RequestsCommon, validate_fields
from fn_ip_void.util.ipvoid_helper import CONFIG_DATA_SECTION, make_api_call, format_dict

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def print_error(reason, app_configs):
    err_str = "Test Failure!\nReason:\n\t{0}".format(reason)
    err_str += "\n\nApp Configs:"
    err_str += format_dict(app_configs)
    log.error(err_str)


def selftest_function(opts):
    app_configs = opts.get(CONFIG_DATA_SECTION, {})
    rc = RequestsCommon(opts, app_configs)
    reason = "Test was successful!"

    try:
        # Get and validate app configs
        valid_app_configs = validate_fields([{"name": "ipvoid_api_key", "placeholder": "<your-api-key>"}, "ipvoid_base_url"], app_configs)

        # Execute api call
        res = make_api_call(
            base_url=valid_app_configs.get("ipvoid_base_url"),
            sub_url=valid_app_configs.get("ipvoid_sub_url"),
            query_type="selftest",
            value=True,
            api_key=valid_app_configs.get("ipvoid_api_key"),
            rc=rc
        )

        res = res.json()

        if res.get("success"):
            log.info("%s\nCredits Remaining:\t%s\nEstimated Queries:\t%s", reason, res.get("credits_remained", "Unknown"), res.get("estimated_queries", "Unknown"))
            return {"state": "success"}

        elif res.get("error"):
            reason = res.get("error")
            print_error(reason, app_configs)
            return {"state": "failure", "reason": reason}

        reason = "Test was not successful. An unknown error occurred"
        print_error(reason, app_configs)
        return {"state": "failure", "reason": reason}

    except Exception as err:
        print_error(err, app_configs)
        return {"state": "failure", "reason": err}
