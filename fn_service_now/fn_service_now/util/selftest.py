# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import logging
import json
from fn_service_now.util.resilient_helper import ResilientHelper

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    This test uses configs in the app.config file to call the custom '/test_connection' endpoint
    To try and get a status_code=200, else its a failure
    """
    options = opts.get("fn_service_now", {})

    res_helper = ResilientHelper(options)

    try:

        LOG.info("Trying to connect to %s", res_helper.SN_HOST)

        res = res_helper.sn_api_request("GET", "/test_connection")

        status_code = res.status_code

        LOG.info("Status Code: %s", status_code)

        if status_code == 200:
            LOG.info("Test was successful!")
            return {"state": "success"}

        else:

            if res is not None and res.content is not None:
                response_result = json.loads(res.content)
                err_msg = response_result["error"]["message"]
                err_detail = response_result["error"]["detail"]

            else:
                err_msg = "Could not connect to ServiceNow"
                err_detail = "Unknown"

            err_reason_msg = """Could not connect to ServiceNow.
            status_code: {0}
            reason: {1}
            detail: {2}
            ---------
            Current Configs in app.config file::
            ---------
            sn_host: {3}
            sn_username: {4}
            sn_table_name: {5}
            sn_api_uri: {6}\n""".format(status_code, err_msg, err_detail, res_helper.SN_HOST, res_helper.SN_USERNAME, res_helper.SN_TABLE_NAME, res_helper.SN_API_URI)

            LOG.error(err_reason_msg)

            return {
                "state": "failure",
                "reason": err_reason_msg
            }

    except Exception as err:
        err_reason_msg = """Could not connect to ServiceNow.
            error: {0}
            ---------
            Current Configs in app.config file::
            ---------
            sn_host: {1}
            sn_username: {2}
            sn_table_name: {3}
            sn_api_uri: {4}\n""".format(err, res_helper.SN_HOST, res_helper.SN_USERNAME, res_helper.SN_TABLE_NAME, res_helper.SN_API_URI)

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
