# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-googlesafebrowsing
    resilient-circuits selftest --print-env -l fn-googlesafebrowsing

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
import json

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_googlesafebrowsing", {})
    SB_CLIENT_ID = "Resilient"
    SB_CLIENT_VER = "0.0.3"

    reqbody = {
            'client': {
                 'clientId': SB_CLIENT_ID,
                 'clientVersion': SB_CLIENT_VER
            },
            'threatInfo': {
                'threatTypes': ['THREAT_TYPE_UNSPECIFIED',
                             'MALWARE', 
                             'SOCIAL_ENGINEERING', 
                             'UNWANTED_SOFTWARE', 
                             'POTENTIALLY_HARMFUL_APPLICATION'],
                'platformTypes': ['ANY_PLATFORM'],
                'threatEntryTypes': ['URL'],
                'threatEntries': [{'url': 'https://ibm.com'}]
            }
        }
    try:
        rc = RequestsCommon(opts, app_configs)
        rc.execute('post', '{}{}'.format(app_configs['googlesafebrowsing_url'], app_configs['googlesafebrowsing_api_key']), headers={'Content-Type': 'applciation/json'}, data=json.dumps(reqbody))
        return {"state": "success"}

    except Exception as e:
        return {
            "state": "failure",
            "reason": e
        }
