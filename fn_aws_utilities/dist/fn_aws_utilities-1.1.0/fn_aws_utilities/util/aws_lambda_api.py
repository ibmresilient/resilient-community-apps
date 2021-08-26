# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
from fn_aws_utilities.util.aws_common import AWSCommon
from botocore.exceptions import ClientError

class AWSLambda(AWSCommon):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        """Initializes boto3 client"""
        AWSCommon.__init__(self, "lambda", aws_access_key_id, aws_secret_access_key, region_name)

    def invoke_lambda(self, function_name, payload):
        """Invokes the lambda function synchronously and returns response"""
        return self.aws_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=payload
        )
