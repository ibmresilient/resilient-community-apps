# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from json import dumps
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_sep.lib.symantec_sep_client import Symantec_SEP, PACKAGE_NAME

FN_NAME = "sep_get_critical_events_info"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sep_get_critical_events_info'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Gets information related to critical events. 'results_limit' is not currently used for this function.
        Inputs:
            -   fn_inputs.sep_results_limit
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        try:
            # Create connection to Symantec server
            sep_client = Symantec_SEP(self.options, self.rc)

            response, _err = sep_client.make_api_call("GET",
                                                     "/events/critical",
                                                     query_params={"pageSize": fn_inputs.sep_results_limit} if getattr(fn_inputs, "sep_results_limit", None) else None)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(response)

        except Exception as err_message:
            yield self.status_message(f"Error in Symantec SEP integration: {err_message}.")
            yield FunctionResult({}, success=False, reason=dumps(err_message, default=str))
