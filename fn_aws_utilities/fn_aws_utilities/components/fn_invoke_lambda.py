# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from fn_aws_utilities.util.aws_lambda_api import AWSLambda
from fn_aws_utilities.util.aws_config import AWSConfig

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_invoke_lambda"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_utilities", {})

    @function("fn_invoke_lambda")
    def _fn_invoke_lambda_function(self, event, *args, **kwargs):
        """Function: Invokes an AWS Lambda function synchronously and returns the function output"""
        try:
            config = AWSConfig(self.options)

            # Get the function parameters:
            lambda_function_name = kwargs.get("lambda_function_name", None)  # text
            lambda_payload = kwargs.get("lambda_payload", None)  # text

            log = logging.getLogger(__name__)
            log.info("lambda_function_name: %s", lambda_function_name)
            log.info("lambda_payload: %s", lambda_payload)

            if not lambda_function_name:
                raise FunctionError("Invalid function name provided")

            if not lambda_payload:
                lambda_payload = ""

            lambda_api = AWSLambda(config.my_aws_access_key_id, config.my_aws_secret_access_key, config.aws_region_name)
            response = lambda_api.invoke_lambda(lambda_function_name, lambda_payload)

            payload = response.get("Payload")
            if not payload:
                yield FunctionResult({"response_payload": None})

            payload_string = str(payload.read().decode('utf-8'))

            yield FunctionResult({"response_payload": payload_string})
        except Exception:
            yield FunctionError()
