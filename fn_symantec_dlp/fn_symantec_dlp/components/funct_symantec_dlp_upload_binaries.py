# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon

PACKAGE_NAME = "fn_symantec_dlp"
FN_NAME = "symantec_dlp_upload_binaries"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_upload_binaries'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Upload the Symantec DLP Component binary files and add as artifact files.
        Inputs:
            -   fn_inputs.sdlp_incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sdlp_incident_id = fn_inputs.sdlp_incident_id
        sdlp_client = SymantecDLPCommon(self.rc, self.app_configs)

        update_results = sdlp_client.upload_sdlp_binaries(sdlp_incident_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {
                   "success_status": update_results
                }
        yield FunctionResult(results)