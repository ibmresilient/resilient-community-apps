# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_cisco_enforcecment
"""

import logging
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

HEADERS = {'content-type': 'application/json'}
SECTION_NAME = "fn_cisco_enforcement"

def selftest_function(opts):
    """
    Simple test to confirm access to Cisco AMP for endpoint API connectivity.
    """
    options = opts.get(SECTION_NAME, {})
    try:

        url = '/'.join((options['url'], 'events?customerKey={}'))
        url = url.format(options['api_token'])

        test_data = {
            "alertTime": "2013-02-08T11:14:26.0Z",
            "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
            "deviceVersion": "13.7a",
            "dstDomain": "internetbadguys.com",
            "dstUrl": "http://internetbadguys.com/a-bad-url",
            "eventTime": "2013-02-08T09:30:26.0Z",
            "protocolVersion": options.get('protocol_version'),
            "providerName": options.get('provider_name')
        }

        rc = RequestsCommon(opts, options)
        response = rc.execute_call_v2("post", url, json=test_data, verify=False, headers=HEADERS)
        log.info(str(response))

        if response.status_code < 300:
            return {"state": "success", "reason": None }
        else:
            return {"state": "failure", "reason": response.status_code }

    except Exception as e:
        return {"state": "failure", "reason": e}
