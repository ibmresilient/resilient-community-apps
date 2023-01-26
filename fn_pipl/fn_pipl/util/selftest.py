# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_pipl
"""

import logging
from piplapis.search import SearchAPIRequest

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_pipl", {})
    # Read configuration settings:
    if "pipl_api_key" in options:
        pipl_api_key = options["pipl_api_key"]
    else:
        log.error(u"Mandatory config setting 'pipl_api_key' not set.")
        raise ValueError("Mandatory config setting 'pipl_api_key' not set.")

    state, reason = "", ""
    try:
        request = SearchAPIRequest(email=u'clark.kent@example.com', first_name=u'Clark', last_name=u'Kent',
                                   api_key=pipl_api_key)
        response = request.send()
        if response and response.http_status_code == 200:
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
