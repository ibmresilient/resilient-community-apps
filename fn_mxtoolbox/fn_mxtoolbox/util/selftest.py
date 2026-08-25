# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_mxtoolbox
"""


import logging
from resilient_lib import validate_fields, RequestsCommon

HEADERS = {'content-type': 'application/json'}

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_mxtoolbox", {})

    # Setup the URL request
    url = '/'.join((options['url'], 'mx', "?argument={}&Authorization={}"))
    url = url.format('abc.com', options['api_token'])

    # Make URL request
    rc = RequestsCommon(opts, options)

    state, reason = "", ""
    try:
        response = rc.execute_call_v2("get", url, headers=HEADERS)

        # Check the results
        if response.status_code == 200:
            state = "success"
        else:
            state = "failure"
            reason = response.error
    except Exception as ex:
        state = "failure"
        reason = str(ex)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result