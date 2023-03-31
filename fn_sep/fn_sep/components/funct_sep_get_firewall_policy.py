# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import json
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_sep.lib.symantec_sep_client import Symantec_SEP

PACKAGE_NAME = "fn_sep"
FN_NAME = "sep_get_firewall_policy"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sep_get_firewall_policy'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the firewall policy for specified policy id.
        Inputs:
            -   fn_inputs.sep_firewall_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["sep_firewall_id"], fn_inputs)

        try:
            sep_client = Symantec_SEP(self.options, self.rc)

            input_data = fn_inputs._asdict()
            input_data = sep_client.transform_inputs(input_data)
            firewall_id = input_data['firewall_id']
            url = f"/policies/firewall/{firewall_id}"
            method = "GET"

            response, err = sep_client.make_api_call(method, url, use_callback=True)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            if err == None:
                yield FunctionResult(response)
            else:
                raise ValueError(err)

        except Exception as err_message:
            response = {}
            yield self.status_message("Error in Symantec SEP integration: {err}.".format(err=err_message))
            err_message = json.dumps(err_message, default=str)
            yield FunctionResult(response, success=False, reason=err_message) 