# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
import json
from fn_aws_utilities.util.aws_sns_api import AwsSns


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
            phone_numbers_json = kwargs.get("phone_numbers")  # text
            msg_body = kwargs.get("msg_body")  # text

            try:
                phone_numbers = json.loads(phone_numbers_json)
            except Exception:
                yield FunctionError("Invalid phone numbers provided, failed to decode.")

            sns = AwsSns(my_aws_access_key_id, my_aws_secret_access_key, aws_region_name, aws_sms_topic_name)

            results = sns.message_members(msg_body, phone_numbers)

            # Produce a FunctionResult with the results
            yield FunctionResult({"message_id": results.get("MessageId")})
        except Exception:
            yield FunctionError()
