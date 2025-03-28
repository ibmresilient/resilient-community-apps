# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME, clear
from resilient_circuits import FunctionResult, AppFunctionComponent, app_function

FN_NAME = "mcafee_epo_list_tags"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'mcafee_epo_list_tags''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Find all tags specified in ePO. McAfee user requires Tag use permission for this function."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request("system.findTag", {})

        # Clear datatable if required params are given
        if hasattr(fn_inputs, "datatable_name") and hasattr(fn_inputs, "incident_id"):
            clear(self.rest_client(), fn_inputs.datatable_name, fn_inputs.incident_id)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
