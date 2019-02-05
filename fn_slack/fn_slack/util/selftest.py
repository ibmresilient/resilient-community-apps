# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_slack
"""

import logging
from fn_slack.lib.resilient_common import validate_fields
from fn_slack.lib.slack_common import SlackUtils

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_slack", {})

    # validate input
    validate_fields(['api_token'], options)

    # configuration specific slack parameters
    api_token = options['api_token']

    state, reason = "", ""
    try:
        # Initialize SlackClient
        slack_utils = SlackUtils(api_token)
        api_test_results = slack_utils.api_test()
        if api_test_results.get("ok"):
            state = "success"
        else:
            state = "failure"
            reason = api_test_results.get("error", "")
    except Exception as ex:
        state = "failure"
        reason = str(ex)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result
