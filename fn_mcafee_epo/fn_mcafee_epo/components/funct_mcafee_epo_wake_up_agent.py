# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_wake_up_agent"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_wake_up_agent'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Wake up an ePO agent
        Inputs:
            -   fn_inputs.mcafee_epo_systems
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Get the function parameters:
        validate_fields(["mcafee_epo_systems"], fn_inputs)

        self.LOG.info("mcafee_epo_systems: %s", fn_inputs.mcafee_epo_systems)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        # Make wakeupAgent call to given system
        response = client.request(
            "system.wakeupAgent",
            {"names": fn_inputs.mcafee_epo_systems.strip()})

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
