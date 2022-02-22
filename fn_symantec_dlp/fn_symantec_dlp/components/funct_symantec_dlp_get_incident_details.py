# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon

PACKAGE_NAME = "fn_symantec_dlp"
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

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sdlp_client = SymantecDLPCommon(self.rc, self.options)
        sdlp_inc_id = fn_inputs.sdlp_incident_id
        results = sdlp_client.get_sdlp_incident_payload(sdlp_inc_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
