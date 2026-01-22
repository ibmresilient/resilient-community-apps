# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2023, 2025. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_proofpoint_campaign
"""

import logging
import os
from requests.auth import HTTPBasicAuth
from resilient_lib import RequestsCommon, validate_fields

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get('fn_proofpoint_tap', {})

    validate_fields(['base_url', 'username', 'password'], options)

    base_url = options.get('base_url')
    username = options.get('username')
    password = options.get('password')
    cafile = options.get('cafile')
    bundle = os.path.expanduser(cafile) if cafile else False

    basic_auth = HTTPBasicAuth(username, password)
    url = f"{base_url}/siem/all?format=JSON&sinceSeconds={300}"  # /v2/siem/all Fetch events for all clicks and messages relating to known threats within the specified time period

    rc = RequestsCommon(opts=opts, function_opts=options)
    try:
        res = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies())

        if res.status_code == 200:
            return {'state': 'success'}

        return {
            'state': 'failure',
            'reason': f"status code {res.status_code}"
        }

    except Exception as ex:
        log.error(ex)
        return {
            'state': 'failure',
            'reason': ex
        }
