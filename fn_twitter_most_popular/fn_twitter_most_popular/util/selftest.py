# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_query_tor_network
"""

import logging
from fn_twitter_most_popular.components.twitter_most_popular_tweets import get_twitter_handler

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_twitter_most_popular", {})
    try:
        # creating the object, performs the authenization
        get_twitter_handler(options)

        return {"state": "Success"}

    except Exception as e:
        msg = "Failed Connection to Twitter Error - {}".format(e)
        LOG.info(msg)
        return {
            "state": "Failed",
            "reason": msg
        }
