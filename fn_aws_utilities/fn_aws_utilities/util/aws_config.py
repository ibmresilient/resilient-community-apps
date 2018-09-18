# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.


class AWSConfig:
    def __init__(self, opts):
        self.my_aws_secret_access_key = opts.get("aws_secret_access_key")
        self.my_aws_access_key_id = opts.get("aws_access_key_id")
        self.aws_region_name = opts.get("aws_region_name")
        self.aws_sms_topic_name = opts.get("aws_sms_topic_name")

        if self.aws_region_name is None:
            raise Exception("aws_region_name undefined in app.config")

        if self.my_aws_access_key_id is None:
            raise Exception("aws_access_key_id undefined in app.config")

        if self.my_aws_secret_access_key is None:
            raise Exception("aws_secret_access_key undefined in app.config")

        if self.aws_sms_topic_name is None:
            raise Exception("aws_sms_topic_name undefined in app.config")