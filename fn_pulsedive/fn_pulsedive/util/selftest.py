# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_pulsedive
"""

import logging
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

CONFIG_SECTION = "fn_pulsedive"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_pulsedive", {})
    log.info("key: %s, url: %s", options["pulsedive_api_key"], options["pulsedive_api_url"])

    # form the url request
    api_url = "{}/search.php?".format(options["pulsedive_api_url"])
    # set generic params for indicator
    pulsedive_data = {
        "type": all,
        "risk": all
    }
    rc = RequestsCommon(opts, options)  # initialize

    state, reason = "", ""

    try:
        resp = rc.execute_call_v2("get",
                                  url=api_url,
                                  params=pulsedive_data
                                  )
        # Check the results
        if resp.status_code == 200:
            state = "success"
        else:
            state = "failure"
            reason = resp.error
    except Exception as err:
        state = "failure"
        reason = str(err)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result