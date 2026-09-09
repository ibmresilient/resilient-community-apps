# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""
Function implementation test.
Usage:
    resilient-circuits selftest -l fn-reaqta
    resilient-circuits selftest --print-env -l fn-reaqta

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
from resilient_lib import RequestsCommon
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        rc = RequestsCommon(opts, app_configs)

        # test each hive setting
        for hive in [hive_name.strip() for hive_name in app_configs.get('polling_hives', "").split(",")]:
            hive_settings = get_hive_options(hive, opts)
            if hive_settings:
                app_common = AppCommon(rc, hive_settings)
                err_msg = app_common.authenticate()
                if err_msg:
                    return {
                        "state": "failure",
                        "reason": "Authentication error for hive: {}. {}".format(hive, err_msg)
                    }
            else:
                return {
                    "state": "failure",
                    "reason": "Hive setting not found: {}".format(hive)
                }

        return {
            "state": "success",
            "reason": None
        }
    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
