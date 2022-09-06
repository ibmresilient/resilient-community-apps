# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from data_feeder_plugins.elasticfeed.elasticfeed import ElasticFeedDestination
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    reason = None
    try:
        options = opts.get("elastic_feed", {})
        elastic = ElasticFeedDestination(None, options)

        info = elastic.es.info()

        state = "success"
    except Exception as err:
        state = "failure"
        reason = str(err)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result
