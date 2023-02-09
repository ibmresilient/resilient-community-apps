# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_threatminer
"""

import logging
from fn_threatminer.lib.threatminer_common import ThreatMiner, PACKAGE

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

TEST_URI = "/email.php?q=7bf5721bfa009479c33f3c3cf4ea5392200f030e"


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    threatminer = ThreatMiner(opts.get("resilient", {}), opts.get(PACKAGE, {}))

    data, msg = threatminer.get(TEST_URI)

    state = "success" if data else "failure"

    return {"state": state}
