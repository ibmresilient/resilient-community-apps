# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-abuseipdb
    resilient-circuits selftest --print-env -l fn-abuseipdb

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

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get('fn_abuseipdb', {})

    try:
        headers = {
            'content-type': 'application/json',
            'X-Auth-Token': app_configs['abuseipdb_key']
        }
        url = app_configs["abuseipdb_url"]

        params = {
                'ipAddress': '',
                'isWhitelisted': app_configs['ignore_white_listed'],
                'verbose': True
            }

        rc = RequestsCommon(opts, app_configs)
        rc.execute('get', url, params=params, headers=headers)
        return {"state": "success"}
    except Exception as e:
        return {
            "state": "failure",
            "reason": e
        }
