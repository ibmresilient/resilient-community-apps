# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import boto3
import logging
from resilient_circuits import FunctionError


class AwsSns:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, topic_name):
        """Initializes boto3 client"""
        client = None
        # Multithread-fix
        while not client:
            try:
                client = boto3.client("sns",
                                      aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region_name
                                      )
            except Exception:
                client = None

        self.aws_client = client
        self.topic_name = topic_name

    def create_sms_topic(self):
        """Create the topic if it doesn't exist, return resource name"""
        topic_exists = False

        topic = self.aws_client.create_topic(Name=self.topic_name)
        topic_arn = topic.get('TopicArn')  # get its Amazon Resource Name
        if topic_arn is None:
            raise FunctionError("Resource name of topic is null.")

        return topic_arn

    def message_members(self, message, cell_numbers):
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
