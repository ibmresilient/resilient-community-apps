# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from fn_aws_utilities.util.aws_sns_api import AwsSns


class TestSendSmsViaSns:
    """ Tests for the send_sms_via_sns function"""

    def test_success(self):
        """ Test calling with sample values for the parameters """
        aws_access_key_id = ""  # Fill with access key id
        aws_secret_access_key = ""  # Fill with secret access key
        aws_region_name = "us-east-1"  # Fill with region name
        phone_number = ""  # Fill with number to send a test message to (include international code)

        sns = AwsSns(aws_access_key_id, aws_secret_access_key, aws_region_name)

        assert sns.message_members("best message", [phone_number]).get("MessageId") is not None
