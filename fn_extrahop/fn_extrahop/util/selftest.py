# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""
Selftest utility for Extrahop revealx
Usage:
    resilient-circuits selftest -l fn-extrahop
    resilient-circuits selftest --print-env -l fn-extrahop
"""
import logging
from fn_extrahop.lib.rx_client import RxClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_extrahop", {})

    """
    Simple test to verify Extrahop revealx connectivity.
    """
    app_configs = opts.get("fn_extrahop", {})
    try:
        rxcli = RxClient(opts, app_configs)
        result = rxcli.get_devices(limit=1)
        if isinstance(result.json(), list):
            return {
                "state": "success",
                "reason": "Successful connection to Extrahop revealx"
            }
        else:
            return {
                "state": "failure",
                "reason": "Failed to connect to Extrahop revealx"
            }

    except Exception as e:
        return {
            "state": "failure",
            "status_code": e
        }