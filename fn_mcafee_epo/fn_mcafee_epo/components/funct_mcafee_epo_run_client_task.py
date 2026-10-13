# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
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
        Function: Run a client task on specified system(s). McAfee user requires edit permission for at least one product for this function.
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

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
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
            "retryAttempts": getattr(fn_inputs, "mcafee_epo_retry_attempts", None),
            "retryIntervalInSeconds": getattr(fn_inputs, "mcafee_epo_retry_intervals_in_seconds", None),
            "abortAfterMinutes": getattr(fn_inputs, "mcafee_epo_abort_after_minutes", None),
            "useAllAgentHandlers": getattr(fn_inputs, "mcafee_epo_use_all_agent_handlers", False),
            "stopAfterMinutes": getattr(fn_inputs, "mcafee_epo_stop_after_minutes", None),
            "randomMinutes": getattr(fn_inputs, "mcafee_epo_random_minutes", None),
            "timeoutInHours": getattr(fn_inputs, "mcafee_epo_timeout_in_hours", None)}
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
