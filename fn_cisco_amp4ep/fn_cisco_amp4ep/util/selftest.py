# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_cisco_amp4ep
"""

import logging
from fn_cisco_amp4ep.lib.amp_client import Ampclient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to confirm access to Cisco AMP for endpoint API connectivity.
    """
    options = opts.get("fn_cisco_amp4ep", {})
    try:

        amp = Ampclient(options, None)

        r = amp.test_connectivity()

        if r.status_code == 200:
            return {"state": "success", "status_code": r.status_code }
        else:
            return {"state": "failure", "status_code": r.status_code }

    except Exception as e:
        return {"state": "failure", "status_code": e}