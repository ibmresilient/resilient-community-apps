# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from kafka import KafkaProducer
from fn_kafka.lib.kafka_common import get_broker_section, s_to_b, pop_key, PACKAGE_NAME, create_producer
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, \
        FunctionError
from resilient_lib import validate_fields, ResultPayload

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.producers = {}

    @function("kafka_send")
    def kafka_send_function(self, event, *args, **kwargs):
        """Function: Sends arbitrary data to kafka topic"""
        try:
            # Get the function parameters:
            kafka_broker_label = kwargs.get("kafka_broker_label")  # text
            kafka_message = kwargs.get("kafka_message")  # text
            kafka_topic = kwargs.get("kafka_topic")  # text
            kafka_key = kwargs.get("kafka_key")  # optional
            validate_fields(["kafka_broker_label", "kafka_topic", "kafka_message"], kwargs)

            LOG.info("kafka_broker_label: %s", kafka_broker_label)
            LOG.info("kafka_topic: %s", kafka_topic)
            LOG.info("kafka_message: %s", kafka_message)
            LOG.info("kafka_key: %s", kafka_key)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            yield StatusMessage("Preparing to send message to Kafka")

            producer = self.get_producer(kafka_broker_label)

            # send the message
            if kafka_key:
                result = producer.send(kafka_topic, key=s_to_b(kafka_key), value=s_to_b(kafka_message))
            else:
                result = producer.send(kafka_topic, s_to_b(kafka_message))
            # clean out the bus to make sure all messages are pushed
            producer.flush()
            # send a return success to resilient
            yield StatusMessage(u"Sent Message to Kafka Topic: {}".format(kafka_topic))

            results = rp.done(True, None)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    def get_producer(self, broker_label):
        if broker_label not in self.producers:
            self.producers[broker_label] = create_producer(self.opts, broker_label)

        return self.producers[broker_label]
