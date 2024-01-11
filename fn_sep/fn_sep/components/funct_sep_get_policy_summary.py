# -*- coding: utf-8 -*-

"""AppFunction implementation"""
import json
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_sep.lib.symantec_sep_client import Symantec_SEP

PACKAGE_NAME = "fn_sep"
FN_NAME = "sep_get_policy_summary"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sep_get_policy_summary'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the policy summary for specified policy type. Also gets the list of groups to which the policies are assigned.
        Inputs:
            -   fn_inputs.sep_domainid
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        try:
            sep_client = Symantec_SEP(self.options, self.rc)

            query_params = fn_inputs._asdict()

            if 'sep_domainid' in query_params :
                query_params['domainId'] = query_params.pop('sep_domainid')
            if not query_params :
                query_params = None

            url = "/policies/summary"
            method = "GET"

            response = sep_client.make_api_call(method, url, query_params=query_params)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(response)

        except Exception as err_message:
            response = {}
            yield self.status_message("Error in Symantec SEP integration: {err}.".format(err=err_message))
            err_message = json.dumps(err_message, default=str)
            yield FunctionResult(response, success=False, reason=err_message)