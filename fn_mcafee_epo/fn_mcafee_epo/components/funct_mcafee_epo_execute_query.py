# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
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
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        # Get function parameters:
        if fn_inputs.mcafee_epo_queryid and fn_inputs.mcafee_epo_target:
            raise ValueError("Define either mcafee_epo_queryid or mcafee_epo_target, but not both.")
        elif fn_inputs.mcafee_epo_queryid:
            response = client.request(
                "core.executeQuery",
                {"queryId": fn_inputs.mcafee_epo_queryid}
            )
        elif fn_inputs.mcafee_epo_target:
            response = client.request(
                "core.executeQuery",
                {"target": fn_inputs.mcafee_epo_target}
            )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
