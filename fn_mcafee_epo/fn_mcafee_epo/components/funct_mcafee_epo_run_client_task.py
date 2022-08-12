# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_run_client_task"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_run_client_task'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Run a client task on specified system(s)
        Inputs:
            -   fn_inputs.mcafee_epo_system_name_or_id
            -   fn_inputs.mcafee_epo_task_id
            -   fn_inputs.mcafee_epo_timeout_in_hours
            -   fn_inputs.mcafee_epo_use_all_agent_handlers
            -   fn_inputs.mcafee_epo_abort_after_minutes
            -   fn_inputs.mcafee_epo_retry_intervals_in_seconds
            -   fn_inputs.mcafee_epo_product_id
            -   fn_inputs.mcafee_epo_retry_attempts
            -   fn_inputs.mcafee_epo_random_minutes
            -   fn_inputs.mcafee_epo_stop_after_minutes
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

         # Get the function parameters:
        validate_fields(["mcafee_epo_system_name_or_id", "mcafee_epo_task_id", "mcafee_epo_product_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "clienttask.run",
            {"names": fn_inputs.mcafee_epo_system_name_or_id,
            "productId": fn_inputs.mcafee_epo_product_id,
            "taskId": fn_inputs.mcafee_epo_task_id,
            "retryAttempts": fn_inputs.mcafee_epo_retry_attempts if hasattr(fn_inputs, "mcafee_epo_retry_attempts") else None,
            "retryIntervalInSeconds": fn_inputs.mcafee_epo_retry_intervals_in_seconds if hasattr(fn_inputs, "mcafee_epo_retry_intervals_in_seconds") else None,
            "abortAfterMinutes": fn_inputs.mcafee_epo_abort_after_minutes if hasattr(fn_inputs, "mcafee_epo_abort_after_minutes") else None,
            "useAllAgentHandlers": fn_inputs.mcafee_epo_use_all_agent_handlers if hasattr(fn_inputs, "mcafee_epo_use_all_agent_handlers") else False,
            "stopAfterMinutes": fn_inputs.mcafee_epo_stop_after_minutes if hasattr(fn_inputs, "mcafee_epo_stop_after_minutes") else None,
            "randomMinutes": fn_inputs.mcafee_epo_random_minutes if hasattr(fn_inputs, "mcafee_epo_random_minutes") else None,
            "timeoutInHours": fn_inputs.mcafee_epo_timeout_in_hours if hasattr(fn_inputs, "mcafee_epo_timeout_in_hours") else None}
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
