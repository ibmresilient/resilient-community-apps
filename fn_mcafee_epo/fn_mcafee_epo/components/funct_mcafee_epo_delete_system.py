# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_delete_system"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_delete_system'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Delete a system from the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_system_name_or_id
            -   fn_inputs.mcafee_epo_uninstall_software
            -   fn_inputs.mcafee_epo_uninstall
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Validate parameter
        validate_fields(["mcafee_epo_system_name_or_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "system.delete",
            {"names": fn_inputs.mcafee_epo_system_name_or_id,
            "uninstall": fn_inputs.mcafee_epo_uninstall if hasattr(fn_inputs, "mcafee_epo_uninstall") else False,
            "uninstallSoftware": fn_inputs.mcafee_epo_uninstall_software if hasattr(fn_inputs, "mcafee_epo_uninstall_software") else False}
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
