# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

import logging
from fn_bitsight_cyber_insurance.util.helper import bitsight_client
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        app_configs = opts.get("fn_bitsight_cyber_insurance", {})
        bitsight_client(RequestsCommon(opts, app_configs), app_configs).selftest()

        return {
            "state": "Success",
            "reason": "Successfully made API call to BitSight."
        }
    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
