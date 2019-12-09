# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_greynoise
"""

import logging
from fn_greynoise.lib.common import call_greynoise, SECTION_HEADER

TEST_IP = "8.8.8.8"
TEST_TYPE = "quick"

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    logging.basicConfig()
    options = opts.get(SECTION_HEADER, {})

    try:
        result = call_greynoise(opts, options, TEST_TYPE, TEST_IP)
        return {"state": True}
    except Exception as err:
        return {
            "state": False,
            "reason": str(err)
        }
