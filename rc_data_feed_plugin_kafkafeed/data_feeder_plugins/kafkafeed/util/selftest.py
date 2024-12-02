# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging

from confluent_kafka import Producer

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    reason = None
    try:
        all_options = opts.get("kafka_feed")
        all_options.pop("class")
        all_options.pop("topic_map")
        selftest_timeout = all_options.pop("selftest_timeout", 10)
        topics = Producer(**all_options).list_topics(timeout=selftest_timeout)

        if not topics:
            state = "failure"
            reason = "No topics"
        else:
            state = "success"
    except Exception as err:
        state = "failure"
        reason = str(err)

    result = {
        "state": state,
        "reason": reason
    }

    LOG.info(result)
    return result
