# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

import logging
from fn_algosec.util.helper import PACKAGE_NAME, algosec_client
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get(PACKAGE_NAME, {})
    rc = RequestsCommon(opts, app_configs)
    # Create connection to AlgoSec server and get a SessionID
    sessionID = algosec_client(app_configs, rc).firewall_analyzer_auth()

    return {
        "state": "Success",
        "reason": None
    }
