# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""
This module contains the KafkaFeedDestination for writing Resilient data
to a Kafka Topic.
"""
import json
import logging
from confluent_kafka import Producer
from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo

LOG = logging.getLogger(__name__)

class KafkaFeedDestination(FeedDestinationBase):
    """Feed destination for writing Resilient data to a Kafka Topic."""
    def __init__(self, rest_client_helper, options):
        super(KafkaFeedDestination, self).__init__()

        ## Get all options, needed as we just blind pass kwargs to support all kafka options
        self.all_options = options.copy()
        LOG.debug(self.all_options)

        ## Get the mapping of topics
        topic_map = self.all_options['topic_map']
        self.topic_dict = dict(item.strip(" ").split("=") for item in topic_map.strip(" ").split(";"))
        LOG.debug("Topic Map is: %s", self.topic_dict)

        ## Tidy up to remove our options vs kafkas options
        self.all_options.pop('class')
        self.all_options.pop('topic_map')

        # create the producer - this will be a long persistence object
        self.p = Producer(**self.all_options)


    def send_data(self, context, payload):
        """
        send the object to the kafka topic based on the mapping in app.config file: 'topic_map'
        :param context:
        :param payload:
        :return: None
        """

        name = context.type_info.get_pretty_type_name()

        kafka_message = context.type_info.flatten(payload, TypeInfo.translate_value)

        # find the topic to use, either an explicit one or the default
        kafka_topic = None
        if self.topic_dict.get(name):
            kafka_topic = self.topic_dict[name].strip(" ")
        elif self.topic_dict.get("default"):
            kafka_topic = self.topic_dict.get("default")
        else:
            LOG.error("Object type: %s not specified in app.config 'topic_map'", name)

        if kafka_topic:

            def status(err, msg):
                """
                check the result of sending the message to kafka as this is an async event
                :
                """
                if err:
                    raise Exception(err)

                LOG.debug('Message delivered to %s partition [%d] @ %d',
                          msg.topic(), msg.partition(), msg.offset())

            try:
                # communicate the action
                action = "delete" if context.is_deleted else "upsert"

                headers = [
                    ( "action", action ),
                    ( "type", name )
                ]

                LOG.info("Action: %s %s(%d) on Kafka topic: %s", action, name, payload['id'], kafka_topic)

                self.p.produce(kafka_topic, json.dumps(kafka_message).encode(), headers=headers, on_delivery=status)

                self.p.flush()
            except BufferError:
                LOG.error(('Local producer queue is full (%d messages awaiting delivery)', len(self.p)))
