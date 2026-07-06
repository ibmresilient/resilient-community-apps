# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_algosec.util.helper import PACKAGE_NAME, algosec_client, fireflow

FN_NAME = "algosec_traffic_change_request_details"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'algosec_traffic_change_request_details'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Returns full details about a specified change request, including custom fields configured for the template.
        Inputs:
            -   fn_inputs.algosec_change_request_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Validate required fields
        validate_fields(["algosec_change_request_id"], fn_inputs)

        # Create connection to AlgoSec server and get SessionID, faSessionID, and phpSessionID
        sessionID, faSessionID, phpSessionID = algosec_client(self.options, self.rc).fire_flow_auth()
        # Send request to get details of specified Traffic Change Request
        results = fireflow(self.rc, sessionID, faSessionID, phpSessionID).traffic_change_request_details(fn_inputs.algosec_change_request_id)

        if results.get("status") == "Success":
            yield FunctionResult(results)
        else:
            yield FunctionResult(results, success=False, reason=str(results.get("messages", None)))
