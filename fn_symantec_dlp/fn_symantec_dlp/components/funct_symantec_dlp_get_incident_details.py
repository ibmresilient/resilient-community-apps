# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "symantec_dlp_get_incident_details"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_get_incident_details'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the information on the Symantec DLP incident by calling the DLP REST API incident endpoints and return the information in JSON format.
        Inputs:
            -   fn_inputs.sdlp_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["sdlp_incident_id"], fn_inputs)

        sdlp_client = SymantecDLPCommon(self.rc, self.options)
        results = sdlp_client.get_sdlp_incident_payload(getattr(fn_inputs, "sdlp_incident_id", None))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
        yield FunctionResult(results)
