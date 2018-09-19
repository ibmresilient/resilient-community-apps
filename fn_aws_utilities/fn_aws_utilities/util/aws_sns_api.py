# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
from resilient_circuits import FunctionError
from fn_aws_utilities.util.aws_common import AWSCommon


class AwsSns(AWSCommon):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, topic_name):
        """Initializes boto3 client"""
        AWSCommon.__init__(self, "sns", aws_access_key_id, aws_secret_access_key, region_name)
        self.topic_name = topic_name

    def send_text_via_sns(self, message, cell_numbers):
        log = logging.getLogger(__name__)
        results = {}
        for cell_number in cell_numbers:
            try:
                results[cell_number] = self.aws_client.publish(PhoneNumber=cell_number, Message=message)
            except Exception as e:
                log.error(e)
                log.info('Phone number %s is invalid' % cell_number)

        return results