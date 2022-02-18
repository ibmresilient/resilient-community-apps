# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2022
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_symantec_dlp
"""

import logging
from resilient_lib import RequestsCommon, ResultPayload, IntegrationError, validate_fields
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_symantec_dlp", {})

    # Validate required fields in app.config are set
    validate_fields(["sdlp_host", "sdlp_username", "sdlp_password", "sdlp_savedreportid"], options)

    sdlp_client = SymantecDLPCommon(RequestsCommon(opts, options), options)

    reason = None

    try:
        state = "success" if sdlp_client.get_sdlp_incident_custom_attributes() else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }
