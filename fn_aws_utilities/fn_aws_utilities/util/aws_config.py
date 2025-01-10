# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

class AWSConfig:
    def __init__(self, opts):
        self.my_aws_secret_access_key = opts.get("aws_secret_access_key")
        self.my_aws_access_key_id = opts.get("aws_access_key_id")
        self.aws_region_name = opts.get("aws_region_name")
        self.aws_sms_topic_name = opts.get("aws_sms_topic_name")

        if not self.aws_region_name:
            raise ValueError("aws_region_name undefined in app.config")

        if not self.my_aws_access_key_id:
            raise ValueError("aws_access_key_id undefined in app.config")

        if not self.my_aws_secret_access_key:
            raise ValueError("aws_secret_access_key undefined in app.config")

        if not self.aws_sms_topic_name:
            raise ValueError("aws_sms_topic_name undefined in app.config")
