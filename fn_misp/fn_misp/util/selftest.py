# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_misp
"""
import logging
from pymisp import PyMISP
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_misp", {})
    rc = RequestsCommon(opts, options)
    verify_cert = True if options.get("verify_cert", "true").lower() == "true" else False

    try:
        misp_client = PyMISP(options.get("misp_url"), options.get("misp_key"), verify_cert, 'json', proxies=rc.get_proxies())

        result = misp_client.servers()
        return {"state": "success"}
    except Exception as err:
        print (err)
        return {"state": "failed", "reason": str(err)}
