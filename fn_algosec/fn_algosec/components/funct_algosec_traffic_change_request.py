# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_algosec.util.helper import PACKAGE_NAME, algosec_client, fireflow

FN_NAME = "algosec_traffic_change_request"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'algosec_traffic_change_request'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a traffic change request with AlgoSec's FireFlow
        Inputs:
            -   fn_inputs.algosec_application
            -   fn_inputs.algosec_traffic_change_action
            -   fn_inputs.algosec_service
            -   fn_inputs.algosec_traffic_change_template
            -   fn_inputs.algosec_user
            -   fn_inputs.algosec_destination
            -   fn_inputs.algosec_source
            -   fn_inputs.algosec_traffic_change_request_description
            -   fn_inputs.algosec_traffic_change_request_subject
            -   fn_inputs.algosec_traffic_change_request_devices
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Validate required fields
        validate_fields(["algosec_source", "algosec_destination", "algosec_service", "algosec_traffic_change_action", "algosec_traffic_change_template"], fn_inputs)

        # Create connection to AlgoSec server and get a SessionID
        sessionID, faSessionID, phpSessionID = algosec_client(self.options, self.rc).fire_flow_auth()
        # Create and send traffic change request
        results = fireflow(self.rc, sessionID, faSessionID, phpSessionID).traffic_change_request(
            source=fn_inputs.algosec_source,
            destination=fn_inputs.algosec_destination,
            service=fn_inputs.algosec_service,
            action=fn_inputs.algosec_traffic_change_action,
            user=getattr(fn_inputs, "algosec_user", ""),
            application=getattr(fn_inputs, "algosec_application", "any"),
            template=getattr(fn_inputs, "algosec_traffic_change_template", ""),
            description=getattr(fn_inputs, "algosec_traffic_change_request_description", ""),
            subject=getattr(fn_inputs, "algosec_traffic_change_request_subject", ""),
            devices=getattr(fn_inputs, "algosec_traffic_change_request_devices", ""))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        if results.get("status") == "Success":
            yield FunctionResult(results)
        else:
            yield FunctionResult(results, success=False, reason=str(results.get("messages", None)))
