# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_spamhaus_query
"""

import logging
from resilient_lib import RequestsCommon, validate_fields
from fn_spamhaus_query.util.spamhaus_helper import CONFIG_DATA_SECTION, make_api_call, format_dict

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
        valid_app_configs = validate_fields(["spamhaus_wqs_url", "spamhaus_dqs_key"], app_configs)

        # Execute api call
        res = make_api_call(
            base_url=valid_app_configs.get("spamhaus_wqs_url"),
            api_key=valid_app_configs.get("spamhaus_dqs_key"),
            search_resource="DBL",
            qry="test",
            rc=rc
        )

        if res.status_code == 200:
            log.info("%s", reason)
            return {"state": "success"}

    except Exception as err:
        print_error(err, app_configs)
        return {"state": "failure", "reason": err}
