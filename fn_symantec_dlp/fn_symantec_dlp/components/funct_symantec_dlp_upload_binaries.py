# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from resilient import get_client
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
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
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sdlp_incident_id = fn_inputs.sdlp_incident_id
        soar_case_id = fn_inputs.incident_id

        rest_client = get_client(self.opts)
        res_common = ResilientCommon(rest_client)
        sdlp_client = SymantecDLPCommon(self.rc, self.options)

        artifact_name_list = sdlp_client.upload_sdlp_binaries(res_common, sdlp_incident_id, soar_case_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {
                   "success": True,
                   "artifact_name_list": artifact_name_list
                }
        yield FunctionResult(results)