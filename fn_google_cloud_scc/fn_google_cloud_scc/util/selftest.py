# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-google-cloud-scc
    resilient-circuits selftest --print-env -l fn-google-cloud-scc

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

import logging

from google.auth.exceptions import DefaultCredentialsError
from fn_google_cloud_scc.util.scc_common import PACKAGE_NAME, GoogleSCCCommon
from resilient_lib import validate_fields

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get(PACKAGE_NAME, {})

    try:
        # app configs are verified in the constructor of the GoogleSCCCommon obj
        GoogleSCCCommon(app_configs)
        return {
            "state": "success",
            "reason": "Successfully connected to Google Cloud SCC"
        }
    except DefaultCredentialsError as e:
        return {
            "state": "failure",
            "reason": "Google Cloud credentials not found"
        }
    except Exception as e:
        return {
            "state": "failure",
            "reason": str(e)
        }



    
