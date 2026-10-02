# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from fn_aws_utilities.util.aws_step_function_api import AwsStepFunction
from datetime import datetime
from fn_aws_utilities.util.aws_config import AWSConfig

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_invoke_step_function"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_utilities", {})

    @function("fn_invoke_step_function")
    def _fn_invoke_step_function_function(self, event, *args, **kwargs):
        """Function: Invokes a step function (state machine)"""
        try:
            config = AWSConfig(self.options)

            # Get the function parameters:
            state_machine_name = kwargs.get("state_machine_name", None)  # text
            state_machine_payload = kwargs.get("state_machine_payload", None)  # text
            state_machine_async = kwargs.get("state_machine_async", None)  # boolean

            if not state_machine_name:
                yield FunctionError("state_machine_name is a required argument.")

            if not state_machine_async:
                state_machine_async = False

            if not state_machine_payload:
                state_machine_payload = "{}"

            step_function_api = AwsStepFunction(config.my_aws_access_key_id,
                                                config.my_aws_secret_access_key,
                                                config.aws_region_name)

            result = step_function_api.invoke_step_function(state_machine_name, state_machine_async,
                                                            state_machine_payload)
            if result.get("startDate", None) and type(result.get("startDate", None)) == datetime:
                result["startDate"] = result.get("startDate", None).strftime("%Y-%m-%d %H:%M:%S")  # datetime is not serializable

            if result.get("stopDate", None) and type(result.get("stopDate", None)) == datetime:
                result["stopDate"] = result.get("stopDate", None).strftime("%Y-%m-%d %H:%M:%S")  # datetime is not serializable

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as e:
            yield FunctionError(e)
