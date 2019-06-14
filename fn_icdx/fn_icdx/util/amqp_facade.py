# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import pika
import uuid
import json


class AmqpFacade:
    def __init__(self, host, virtual_host, username, amqp_password, port):
        self.DEFAULT_PORT = 5672

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=host,
                port=int(port) if not isinstance(port, type(None)) else self.DEFAULT_PORT,  # Use provided port no or default if provided port is falsey
                virtual_host=virtual_host,
                credentials=pika.PlainCredentials(username, amqp_password)
            ))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        """
            When a response comes in, check if the correlation_ids match
            If they do, the body will contain our search request
        """
        if self.corr_id == props.correlation_id:
            self.response = body
            self.status = props.headers.get('status')

    def call(self, request):
        """
            Call is used to submit a query to the ICDX AMQP API.
            It performs these steps:
            + Init a response and setup a correlation_id
            + Publish a request to the ICDX Platform with a reply_to queue for response
            + Wait for response and return

            :param request - a JSON payload containing an ID attribute and other fields

            The function is setup such that any API request can be done with this one method
            Changing the 'ID' attribute of the request object will change which API you hit
            0 - Get Events
            1 - Find Events
            12 - Get Archive List
        """
        # Check response is valid JSON
        try:
            json.loads(request)
        except Exception:
            # Invalid JSON, raise a descriptive error
            raise ValueError("AMQP Request failed. Received a non-json Payload")

        self.response = None
        self.corr_id = str(uuid.uuid4())

        # Declare the search exchange
        self.channel.exchange_declare(exchange='dx.archives.search',
                                      exchange_type='direct',
                                      durable=False,
                                      auto_delete=True)
        # Publish the request and provide reply_to queue for response
        self.channel.basic_publish(exchange='dx.archives.search',
                                   routing_key='',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                       content_type='application/json'
                                   ),
                                   body=request)
        # Wait for response by processing incoming events
        while self.response is None:
            self.connection.process_data_events()
        # Return response and a status code indicating success after closing the connection
        self.connection.close()
        return self.response, self.status

