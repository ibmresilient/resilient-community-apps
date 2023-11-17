# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import json
import logging

from fn_service_now.util.resilient_helper import (CONFIG_DATA_SECTION,
                                                  ResilientHelper)
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    This test uses configs in the app.config file to call the custom '/test_connection' endpoint
    To try and get a status_code=200, else its a failure
    """
    app_configs = opts.get(CONFIG_DATA_SECTION, {})
    rc = RequestsCommon(opts, app_configs)

    res_helper = ResilientHelper(app_configs)

    try:

        LOG.info("Trying to connect to %s", res_helper.SN_HOST)

        res = res_helper.sn_api_request(rc, "GET", "/test_connection")

        status_code = res.status_code

        LOG.info("Status Code: %s", status_code)

        if status_code == 200:
            LOG.info("Test was successful!")
            return {"state": "success"}

        else:

            if res and res.content:
                response_result = json.loads(res.content)
                err_msg = response_result["error"]["message"]
                err_detail = response_result["error"]["detail"]

            else:
                err_msg = "Could not connect to ServiceNow"
                err_detail = "Unknown"

            err_reason_msg = f"""Could not connect to ServiceNow.
            status_code: {status_code}
            reason: {err_msg}
            detail: {err_detail}
            ---------
            Current Configs in app.config file::
            ---------
            sn_host: {res_helper.SN_HOST}
            sn_username: {res_helper.SN_USERNAME}
            sn_table_name: {res_helper.SN_TABLE_NAME}
            sn_api_uri: {res_helper.SN_API_URI}
            """

            LOG.error(err_reason_msg)

            return {
                "state": "failure",
                "reason": err_reason_msg
            }

    except Exception as err:
        err_reason_msg = f"""Could not connect to ServiceNow.
            error: {err}
            ---------
            Current Configs in app.config file::
            ---------
            sn_host: {res_helper.SN_HOST}
            sn_username: {res_helper.SN_USERNAME}
            sn_table_name: {res_helper.SN_TABLE_NAME}
            sn_api_uri: {res_helper.SN_API_URI}
            """

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
