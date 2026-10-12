# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-google-maps-directions
    resilient-circuits selftest --print-env -l fn-google-maps-directions

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""
import requests
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    url = "https://www.google.com/maps/dir/?api=1"

    state = ""
    reason = None
    
    try:
        response = requests.get(url, timeout=5)
        # Check the results
    
        if response.status_code == 200:
            state = "success"
    
        else:
            state = "failure"
            reason = response.error
    
    except Exception as ex:
        state = "failure"
        reason = str(ex)
    
    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result
