# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from fn_aws_utilities.util.aws_lambda_api import AWSLambda


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_invoke_lambda"""

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
            my_aws_secret_access_key = self.options.get("aws_secret_access_key")
            my_aws_access_key_id = self.options.get("aws_access_key_id")
            aws_region_name = self.options.get("aws_region_name")
            aws_sms_topic_name = self.options.get("aws_sms_topic_name")

            if aws_region_name is None:
                yield FunctionError("aws_region_name undefined in app.config")

            if my_aws_access_key_id is None:
                yield FunctionError("aws_access_key_id undefined in app.config")

            if my_aws_secret_access_key is None:
                yield FunctionError("aws_secret_access_key undefined in app.config")

            if aws_sms_topic_name is None:
                yield FunctionError("aws_sms_topic_name undefined in app.config")

            # Get the function parameters:
            lambda_function_name = kwargs.get("lambda_function_name")  # text
            lambda_payload = kwargs.get("lambda_payload")  # text

            log = logging.getLogger(__name__)
            log.info("lambda_function_name: %s", lambda_function_name)
            log.info("lambda_payload: %s", lambda_payload)

            if lambda_function_name is None or lambda_function_name == "":
                yield FunctionError("Invalid function name provided")

            if lambda_payload is None:
                lambda_payload = ""

            lambda_api = AWSLambda(my_aws_access_key_id, my_aws_secret_access_key, aws_region_name)
            response = lambda_api.invoke_lambda(lambda_function_name, lambda_payload)

            if response == {}:
                yield FunctionError("Function not found")

            payload = response.get("Payload")
            if payload is None:
                yield FunctionResult({"response_payload": None})

            payload_string = str(payload.read())
            payload_string = payload_string.replace('"', '')  # boto3 appends quote chars to payload

            yield FunctionResult({"response_payload": payload_string})
        except Exception:
            yield FunctionError()
