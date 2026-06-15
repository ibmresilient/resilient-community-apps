# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

import logging
from fn_ocm.util.helper import ocm_client
from resilient_lib import RequestsCommon, validate_fields

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_ocm", {})
    # Validate required app.config settings
    validate_fields(["ocm_url", "ocm_api_key_name", "ocm_api_key_pass"], options)
    # Create client connection
    client = ocm_client(options.get("ocm_url", None), options.get("ocm_api_key_name", None), options.get("ocm_api_key_pass", None), RequestsCommon(opts, options))

    try:
        client.list_incidents(limit=1)
    except Exception as err:
        return {
            "state": "Failed",
            "reason": err
        }

    return {
        "state": "Success",
        "reason": None
    }
