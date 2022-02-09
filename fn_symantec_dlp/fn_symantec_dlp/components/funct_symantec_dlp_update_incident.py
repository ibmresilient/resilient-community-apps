# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon
from resilient_lib import IntegrationError
from resilient_lib.components.resilient_common import str_to_bool

PACKAGE_NAME = "fn_symantec_dlp"
FN_NAME = "fn_symantec_dlp_update_incident"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_update_threat_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the status of a threat in SentinelOne.
        Inputs:
            -   fn_inputs.sdlp_update_payload
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sdlp_update_payload = fn_inputs.sdlp_update_payload
        sdlp_client = SymantecDLPCommon(self.rc, self.app_configs)

        update_results = sdlp_client.update_dlp_incident(sdlp_update_payload)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {
                   "success_status": update_results,
                }
        yield FunctionResult(results)