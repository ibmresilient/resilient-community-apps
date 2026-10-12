# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from json import dumps
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_sep.lib.symantec_sep_client import Symantec_SEP, PACKAGE_NAME

FN_NAME = "sep_cancel_a_command"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sep_cancel_a_command'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Cancels an existing command by creating a new cancel command for clients for which the command is still pending.
        Inputs:
            -   fn_inputs.sep_command_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        try:
            # Validate required inputs
            validate_fields(['sep_command_id'], fn_inputs)
            # Create connection to Symantec server
            sep_client = Symantec_SEP(self.options, self.rc)

            response, err = sep_client.make_api_call("POST",
                                                     f"/command-queue/{fn_inputs.sep_command_id}/cancel",
                                                     use_callback=True)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            if err:
                raise ValueError(err)

            yield FunctionResult(response)

        except Exception as err_message:
            yield self.status_message(f"Error in Symantec SEP integration: {err_message}.")
            yield FunctionResult({}, success=False, reason=dumps(err_message, default=str))
