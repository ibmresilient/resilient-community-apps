# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_test_app_one
"""

import logging
import json

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    This test uses configs in the app.config file to call the custom '/test_connection' endpoint
    To try and get a status_code=200, else its a failure
    """

    return {
        "state": "failure",
        "reason": err_reason_msg
    }
