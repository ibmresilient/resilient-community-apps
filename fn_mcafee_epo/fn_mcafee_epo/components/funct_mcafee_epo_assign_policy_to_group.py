# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_assign_policy_to_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_assign_policy_to_group'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Assigns policy to the specified group no ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_group_id
            -   fn_inputs.mcafee_epo_reset_inheritance
            -   fn_inputs.mcafee_epo_product_id
            -   fn_inputs.mcafee_epo_object_id
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Validate parameters
        validate_fields(["mcafee_epo_group_id", "mcafee_epo_product_id", "mcafee_epo_object_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "policy.assignToGroup",
            {"groupId": int(fn_inputs.mcafee_epo_group_id),
            "productId": fn_inputs.mcafee_epo_product_id,
            "objectId": int(fn_inputs.mcafee_epo_object_id),
            "resetInheritance": bool(fn_inputs.mcafee_epo_reset_inheritance) if hasattr(fn_inputs, "mcafee_epo_reset_inheritance") else False}
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
