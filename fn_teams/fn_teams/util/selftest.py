# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_teams
"""

import logging
import pymsteams
from datetime import datetime

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# channel reference for testing
SELF_TEST = "selftest"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_teams", {})

    # determine if self test is enabled
    if not options.get(SELF_TEST):
        return {
            "state": "unimplemented",
            "reason": "{} not found in app.config".format((SELF_TEST))
        }
    else:
        webhook = options.get(SELF_TEST)

        try:
            card = pymsteams.connectorcard(webhook, http_proxy=opts['proxy_http'] if opts.get('proxy_http') else None,
                                           https_proxy=opts['proxy_https'] if opts.get('proxy_https') else None,
                                           http_timeout=60)

            card.title("Resilient SelfTest")
            card.text(datetime.ctime(datetime.now()))
            card.send()

            return {
                "state": "success",
                "reason": None
            }
        except Exception as err:
            log.error(err.message)
            return {
                "state": "failure",
                "reason": err.message if err.message else None
            }
