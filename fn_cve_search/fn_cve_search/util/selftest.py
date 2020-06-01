# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_cve_search
"""

import logging
from fn_cve_search.util.cve import make_rest_api_get_call

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    # Reading configuration variables from app.config file
    options = opts.get("fn_cve_search", {})

    try:
        url = "/".join((options.get('cve_base_url'), 'last'))
        _response = make_rest_api_get_call(url, opts, options)

        return {"state": "Success"}
    except Exception as e:
        log.info("Failed Connection to CVE Database Error - {}".format(e))
        return {
            "state": "Failed",
            "reason": str(e)
        }
