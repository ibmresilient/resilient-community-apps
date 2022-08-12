# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_find_systems_in_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_find_systems_in_group'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Find systems in a specified group on ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_sub_group
            -   fn_inputs.mcafee_epo_group_id
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Validate fields
        validate_fields(["mcafee_epo_group_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "epogroup.findSystems",
            {"groupId": fn_inputs.mcafee_epo_group_id,
            "searchSubgroups": fn_inputs.mcafee_epo_sub_group if hasattr(fn_inputs, "mcafee_epo_sub_group") else None
            }
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
