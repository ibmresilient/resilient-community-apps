# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Function implementation
   test with: resilient-circuits selftest -l fn_sep
"""

import logging
from fn_sep.lib.sep_client import Sepclient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to confirm access to Cisco AMP for endpoint API connectivity.
    """
    options = opts.get("fn_sep", {})
    try:
        sep = Sepclient(options, None)

        r = sep.get_computers(pagesize=5)

        if r:
            return {"state": "success"}
        else:
            return {"state": "failure"}

    except Exception as e:
        return {"state": "failure", "status_code": e}
