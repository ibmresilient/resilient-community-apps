# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_cisco_amp4ep
"""
import logging
import pyclamd

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Simple test to confirm tcp connectivity to ClamAV.
    """
    options = opts.get("fn_clamav", {})
    try:

        cd = pyclamd.ClamdNetworkSocket(host=str(options['host']),
                                        port=int(options['port']),
                                        timeout=int(options['timeout'])
                                        )
        if cd.ping():
            return {"state": "success", "status_code": "good" }

    except Exception as e:
        return {"state": "failure", "status_code": e}