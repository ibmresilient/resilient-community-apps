# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from fn_aws_utilities.util.aws_step_function_api import AwsStepFunction
from fn_aws_utilities.util.aws_config import AWSConfig
import datetime


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_get_step_function_execution"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_utilities", {})

    @function("fn_get_step_function_execution")
    def _fn_get_step_function_execution_function(self, event, *args, **kwargs):
        """Function: Returns information about a step function execution"""
        try:
            # Get the function parameters:
            config = AWSConfig(self.options)

            execution_arn = kwargs.get("execution_arn")  # text
            if execution_arn is None or execution_arn == "":
                yield FunctionError("execution_arn is a required argument.")

            step_function_api = AwsStepFunction(config.my_aws_access_key_id,
                                                config.my_aws_secret_access_key,
                                                config.aws_region_name)

            result = step_function_api.get_execution_result(execution_arn)

            if result.get("startDate") is not None and type(result["startDate"]) == datetime.datetime:
                result["startDate"] = result["startDate"].strftime("%Y-%m-%d %H:%M:%S")  # datetime is not serializable

            if result.get("stopDate") is not None and type(result["stopDate"]) == datetime.datetime:
                result["stopDate"] = result["stopDate"].strftime("%Y-%m-%d %H:%M:%S")  # datetime is not serializable

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()