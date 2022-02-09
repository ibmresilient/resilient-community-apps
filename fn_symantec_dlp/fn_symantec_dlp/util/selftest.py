# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2022
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_symantec_dlp
"""

import logging
import traceback
import datetime

from fn_symantec_dlp.lib.dlp_rest_client import DLPRestClient


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_symantec_dlp", {})
    try:
        # Ensure the shared class_vars_loaded var is False so the init of DLPRestClient isin't skipped
        DLPRestClient.class_vars_loaded = False
        # Init the DLPRestClient, this will try to validate the WSDL
        dlp_rest_client = DLPRestClient(app_configs=options)

        # Assert the DLPSoapClient is connected
        assert dlp_rest_client.is_connected
        # Make the a call to incident_list in the DLPRestClient.
        # This will validate that the saved report id is provided as well as the authentication pieces.
        dlp_rest_client.incident_list(saved_report_id=options.get("sdlp_savedreportid"), incident_creation_date_later_than=datetime.datetime.now() - datetime.timedelta(
            days=int(options.get("sdlp_incident_creation_date_later_than", 14))))

        return {"state": "success"}
    # For the selftest, we want to catch ANY issue found when setting up the soap_client, then print out the issue.
    except Exception as self_test_ex:
        # Put the traceback into DEBUG
        log.debug(traceback.format_exc())
        # Log the Connection error to the user
        log.error(u"Problem: %s", repr(self_test_ex))
        log.error(u"[Symantec DLP] Encountered an exception when running the selftest")

        return {"state": "failure"}
