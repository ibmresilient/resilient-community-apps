# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import boto3
import boto3.session


class AWSCommon:
    def __init__(self, service_name, aws_access_key_id, aws_secret_access_key, region_name):
        session = boto3.session.Session(aws_access_key_id=aws_access_key_id,
                                        aws_secret_access_key=aws_secret_access_key,
                                        region_name=region_name)
        self.aws_client = session.client(service_name)
