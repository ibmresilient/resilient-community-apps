# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import boto3
import logging


class AWSLambda:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        """Initializes boto3 client"""
        client = None
        # Multithread-fix
        while not client:
            try:
                client = boto3.client("lambda",
                                      aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region_name
                                      )
            except Exception:
                client = None

        self.aws_client = client

    def invoke_lambda(self, function_name, payload):
        """Invokes the lambda function synchronously and returns response"""
        log = logging.getLogger(__name__)

        try:
            resp = self.aws_client.invoke(
                FunctionName=function_name,
                InvocationType='RequestResponse',
                Payload=payload
            )
        except Exception:
            log.error("Function not found")
            resp = {}

        return resp
