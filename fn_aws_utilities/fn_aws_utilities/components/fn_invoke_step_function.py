# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from fn_aws_utilities.util.aws_step_function_api import AwsStepFunction
import datetime
from fn_aws_utilities.util.aws_config import AWSConfig


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_invoke_step_function"""

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
            state_machine_name = kwargs.get("state_machine_name")  # text
            state_machine_payload = kwargs.get("state_machine_payload")  # text
            state_machine_async = kwargs.get("state_machine_async")  # boolean

            if state_machine_name is None or state_machine_name == "":
                yield FunctionError("state_machine_name is a required argument.")

            if state_machine_async is None:
                state_machine_async = False

            if state_machine_payload is None or state_machine_payload == "":
                state_machine_payload = "{}"

            step_function_api = AwsStepFunction(config.my_aws_access_key_id,
                                                config.my_aws_secret_access_key,
                                                config.aws_region_name)

            result = step_function_api.invoke_step_function(state_machine_name, state_machine_async,
                                                            state_machine_payload)
            if result.get("startDate") is not None and type(result["startDate"]) == datetime.datetime:
                result["startDate"] = result["startDate"].strftime("%Y-%m-%d %H:%M:%S")  # datetime is not serializable

            if result.get("stopDate") is not None and type(result["stopDate"]) == datetime.datetime:
                result["stopDate"] = result["stopDate"].strftime("%Y-%m-%d %H:%M:%S")  # datetime is not serializable

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as e:
            yield FunctionError(e)
