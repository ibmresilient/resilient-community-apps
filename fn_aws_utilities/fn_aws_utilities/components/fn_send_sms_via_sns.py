# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
import json
from fn_aws_utilities.util.aws_sns_api import AwsSns
from fn_aws_utilities.util.aws_config import AWSConfig
import re


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_send_sms_via_sns"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_utilities", {})

    @function("fn_send_sms_via_sns")
    def _fn_send_sms_via_sns_function(self, event, *args, **kwargs):
        """Function: Sends an SMS message to a list of phone numbers"""
        try:
            config = AWSConfig(self.options)

            # Get the function parameters:
            phone_numbers_csv = kwargs.get("phone_numbers")  # text
            msg_body = kwargs.get("msg_body")  # text

            try:
                phone_numbers_unstripped = [s.strip() for s in
                                            phone_numbers_csv.split(',')]  # Split commas ignoring any whitespace
                phone_numbers = []
                for phone_number_unstripped in phone_numbers_unstripped:
                    phone_numbers.append(re.sub("[^0-9]", "", phone_number_unstripped))  # Strip all non-numeric chars
            except Exception:
                raise FunctionError("Invalid phone numbers provided, failed to decode.")

            sns = AwsSns(config.my_aws_access_key_id,
                         config.my_aws_secret_access_key,
                         config.aws_region_name,
                         config.aws_sms_topic_name)

            results = sns.send_text_via_sns(msg_body, phone_numbers)

            # Produce a FunctionResult with the results
            yield FunctionResult({"message_id": results.get("MessageId")})
        except Exception:
            yield FunctionError()
