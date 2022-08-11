# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME, clear
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

FN_NAME = "mcafee_epo_execute_query"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_execute_query'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Execute a query on the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_target
            -   fn_inputs.mcafee_epo_queryid
            -   fn_inputs.datatable_name
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        # Create dictionary of inputs
        inputs_dict = fn_inputs._asdict()

        # Log parameters
        self.LOG.info(str(inputs_dict))

        # Get function parameters:
        datatable = fn_inputs.datatable_name if hasattr(fn_inputs, "datatable_name") else None
        incident_id = fn_inputs.incident_id if hasattr(fn_inputs, "incident_id") else None
        if inputs_dict.get('mcafee_epo_queryid') and inputs_dict.get('mcafee_epo_target'):
            raise ValueError("Define either mcafee_epo_queryid or mcafee_epo_target, but not both.")
        elif inputs_dict.get('mcafee_epo_queryid'):
            response = client.request(
                "core.executeQuery",
                {"queryId": fn_inputs.mcafee_epo_queryid}
            )
        elif inputs_dict.get('mcafee_epo_target'):
            response = client.request(
                "core.executeQuery",
                {"target": fn_inputs.mcafee_epo_target}
            )
        else:
            raise ValueError("Either mcafee_epo_queryid or mcafee_epo_target have to be defined.")

        # Clear datatable if requires params are given
        if datatable and incident_id:
            clear(self.rest_client(), datatable, incident_id)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
