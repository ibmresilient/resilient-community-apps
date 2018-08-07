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

    def create_sms_topic(self):
        """Create the topic if it doesn't exist, return resource name"""
        log = logging.getLogger(__name__)

        try:
            topic = self.aws_client.create_topic(Name=self.topic_name)
        except Exception as e:
            log.error(e)
            raise Exception("Failed to create topic")

        topic_arn = topic.get('TopicArn')  # get its Amazon Resource Name
        if topic_arn is None:
            raise FunctionError("Resource name of topic is null.")

        return topic_arn

    def send_text_via_sns(self, message, cell_numbers):
        """Sends a text message to cell_numbers using AWS SNS"""
        topic_arn = self.create_sms_topic()
        log = logging.getLogger(__name__)

        subscriptions = []
        for cell_number in cell_numbers:
            try:
                subscription = self.aws_client.subscribe(
                    TopicArn=topic_arn,
                    Endpoint=cell_number,
                    Protocol="sms",
                    ReturnSubscriptionArn=True
                )

                if subscription.get("SubscriptionArn"):
                    subscriptions.append(subscription.get("SubscriptionArn"))
            except Exception as e:
                # An example number would be 19998887777
                log.error(e)
                continue  # invalid number

        return_value = self.aws_client.publish(Message=message, TopicArn=topic_arn)

        # We need to unsubscribe everyone so that the next time someone texts to this topic, only cell_numbers gets msg
        for subscription in subscriptions:
            self.aws_client.unsubscribe(SubscriptionArn=subscription)

        return return_value
