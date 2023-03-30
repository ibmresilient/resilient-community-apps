# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_log_capture
"""

import logging
import os
from fn_log_capture.components.funct_fn_log_capture import LOG_FILE

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    log_dir = opts.get("resilient", {}).get("logdir")
    log_file = os.path.join(log_dir, LOG_FILE)

    reason = None
    if not log_dir:
        reason = "Log directory not found"
    elif not os.path.isfile(log_file):
        reason = "Log file incorrect or missing: {}".format(log_file)

    return {
            "state": "success" if not reason else "failure",
            "reason": reason
           }
