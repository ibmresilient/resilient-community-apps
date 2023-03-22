# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-trusteer-ppd
    resilient-circuits selftest --print-env -l fn-trusteer-ppd

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
from resilient_lib import RequestsCommon, IntegrationError
from fn_trusteer_ppd.lib.trusteer_ppd_client import TrusteerPPDClient, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Trusteer currently does not have a REST API endpoint to call to test connectivity,
    so this function is just testing that the app.config parameters are set.
    """
    app_configs = opts.get("fn_trusteer_ppd", {})

    rc = RequestsCommon(opts, app_configs)

    try:
        
        trusteer_ppd_client = TrusteerPPDClient(rc, PACKAGE_NAME, app_configs=app_configs)
        return {
            "state": "success",
            "reason": "Successful connection to Trusteer."
        }
    except IntegrationError as error:
        return {
            "state": "failure",
            "reason": f"Failed to connect to Trusteer: {str(error)}"
        }
