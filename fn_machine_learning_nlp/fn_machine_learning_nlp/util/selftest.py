# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-machine-learning-nlp
"""

import logging
import os

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Test that model directory exists
    """
    model_path = opts.get("fn_machine_learning_nlp", {}).get("model_path", {})
    exist = os.path.exists(model_path)

    reason = None
    if not exist:
        reason = "Directory for models not found"

    return {
            "state": "success" if not reason else "failure: {}".format(reason)
            }
