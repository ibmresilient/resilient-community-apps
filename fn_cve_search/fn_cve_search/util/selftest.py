# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_cve_search
"""

import logging
import requests
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    test_url = "https://cve.circl.lu/api"
    try:
        _response = requests.get(url=test_url)
        if _response.status_code == 200:
            log.info("Successfully Established connection to CVE Database : {}".format(_response.status_code))
            return {"state": "Success"}
        else:
            raise requests.ConnectionError("The Status code {}".format(_response.status_code))
    except Exception as e:
        log.info("Failed Connection to CVE Database Error - {}".format(e))
        return {"state": "Failed"}
