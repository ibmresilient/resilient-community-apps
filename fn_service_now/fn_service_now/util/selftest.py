# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import json
import logging

from fn_service_now.util.resilient_helper import (CONFIG_DATA_SECTION,
                                                  ResilientHelper)

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    This test uses configs in the app.config file to call the custom '/test_connection' endpoint
    To try and get a status_code=200, else its a failure
    """
    app_configs = opts.get(CONFIG_DATA_SECTION, {})

    res_helper = ResilientHelper(opts, app_configs)

    try:

        LOG.info("Trying to connect to %s", res_helper.host)

        res = res_helper.test_connection()

        status_code = res.status_code

        LOG.info("Status Code: %s", status_code)

        if status_code == 200:
            LOG.info("Test was successful!")
            return {
                "state": "success"
            }

        else:
            if res is not None and hasattr(res, "content"):
                response_result = json.loads(res.content)
                err_msg = response_result["error"]["message"]
                err_detail = response_result["error"]["detail"]
            else:
                err_msg = "Could not connect to ServiceNow"
                err_detail = "Unknown"

            err_reason_msg = f"""Could not connect to ServiceNow.
        Response Details:
        ---------
        status_code: {status_code}
        reason: {err_msg}
        detail: {err_detail}"""

    except Exception as err:
        err_reason_msg = f"""Could not connect to ServiceNow.
        Error:
        ---------
        error: {err}"""

    # NOTE: indentation on these matters because the whitespace in the multi-line string
    # is included with the logging
    err_reason_msg +=f"""
        ---------
        Current Configs in app.config file:
        ---------
        sn_host: {res_helper.host}
        sn_username: {res_helper.username}
        sn_table_name: {res_helper.table_name}
        sn_api_uri: {res_helper.api_uri}
        ---------"""


    LOG.error(err_reason_msg)
    return {
        "state": "failure",
        "reason": err_reason_msg
    }
