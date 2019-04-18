# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2017. All Rights Reserved.

import logging
import pika
from pika.exceptions import AMQPConnectionError
import resilient
from resilient import SimpleClient
import json
import os
import time

from fn_icdx.util.helper import ICDXHelper

LOG_FORMAT = (u'%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              u'-35s %(lineno) -5d: %(message)s')
log = logging.getLogger(__name__)


class AMQPAsyncConsumer(object):
    """This is an asynchronous consumer that will handle unexpected interactions
    with RabbitMQ such as channel and connection closures.

    If RabbitMQ closes the connection, it will reopen it. You should
    look at the output, as there are limited reasons why the connection may
    be closed, which usually are tied to permission related issues or
    socket timeouts.

    If the channel is closed, it will indicate a problem with one of the
    commands that were issued and that should surface in the output as well.
    Alternatively, every so often you may see a duplicate command error which
    will cause the connection to close and reopen
    """
    EXCHANGE = 'resilient'
    EXCHANGE_TYPE = 'direct'
    QUEUE = 'resilient'
    ROUTING_KEY = ''
    DEFAULT_PORT = 5672

    def __init__(self, host, virtual_host, username, amqp_password, rest_client, helper, port):
        """Create a new instance of the consumer class, passing in the AMQP
        URL used to connect to RabbitMQ.

        :param username
        :param amqp_password
        :param host
        :param port
        :param virtual_host
        :param rest_client -- An instance of the Resilient Rest Client
        :param helper -- An instance of the ICDxHelper

        """

        self._connection = None
        self._channel = None
        self._closing = False
        self._consumer_tag = None
        self._url = "amqp://{}:{}@{}:{}/{}".format(username, amqp_password, host, port, virtual_host)

        self._host = host
        self._port = (port if isinstance(port, int) else self.DEFAULT_PORT)
        self._username = username
        self._amqp_password = amqp_password
        self._virtual_host = virtual_host
        # Validate rest_client is of type SimpleClient, python 2 doesnt have type annotations
        self._client = (rest_client if isinstance(rest_client, SimpleClient)else None)
        # An instance of ICDxHelper
        self._helper = (helper if isinstance(helper, ICDXHelper) else None)

    def connect(self):
        """This method connects to RabbitMQ, returning the connection handle.
        When the connection is established, the on_connection_open method
        will be invoked by pika.

        :rtype: pika.SelectConnection

        """
        try:
            log.info('Connecting to %s', self._url)
            return pika.SelectConnection(
                        pika.ConnectionParameters(
                            host=self._host,
                            port=self._port,
                            virtual_host=self._virtual_host,
                            credentials=pika.PlainCredentials(self._username, self._amqp_password),
                            heartbeat_interval=600,
                            blocked_connection_timeout=300),
                        self.on_connection_open,
                        stop_ioloop_on_close=False,
                        )
        except AMQPConnectionError:
            raise ValueError("Error connecting to the AMQP instance, double check credentials and any proxy settings")

    def on_connection_open(self, unused_connection):
        """This method is called by pika once the connection to RabbitMQ has
        been established. It passes the handle to the connection object in
        case we need it, but in this case, we'll just mark it unused.

        :type unused_connection: pika.SelectConnection

        """
        log.info('Connection opened')
        self.add_on_connection_close_callback()
        self.open_channel()

    def add_on_connection_close_callback(self):
        """This method adds an on close callback that will be invoked by pika
        when RabbitMQ closes the connection to the publisher unexpectedly.

        """
        log.info('Adding connection close callback')
        self._connection.add_on_close_callback(self.on_connection_closed)

    def on_connection_closed(self, connection, reply_code, reply_text):
        """This method is invoked by pika when the connection to RabbitMQ is
        closed unexpectedly. Since it is unexpected, we will reconnect to
        RabbitMQ if it disconnects.

        :param pika.connection.Connection connection: The closed connection obj
        :param int reply_code: The server provided reply_code if given
        :param str reply_text: The server provided reply_text if given

        """
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
        else:
            log.warning('Connection closed, reopening in 5 seconds: (%s) %s',
                        reply_code, reply_text)
            self._connection.add_timeout(5, self.reconnect)

    def reconnect(self):
        """Will be invoked by the IOLoop timer if the connection is
        closed. See the on_connection_closed method.

        """
        # This is the old connection IOLoop instance, stop its ioloop
        self._connection.ioloop.stop()

        if not self._closing:
            # Create a new connection
            self._connection = self.connect()

            # There is now a new connection, needs a new ioloop to run
            self._connection.ioloop.start()

    def open_channel(self):
        """Open a new channel with RabbitMQ by issuing the Channel.Open RPC
        command. When RabbitMQ responds that the channel is open, the
        on_channel_open callback will be invoked by pika.

        """
        log.info('Creating a new channel')
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        """This method is invoked by pika when the channel has been opened.
        The channel object is passed in so we can make use of it.

        Since the channel is now open, we'll declare the exchange to use.

        :param pika.channel.Channel channel: The channel object

        """
        log.info('Channel opened')
        self._channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange(self.EXCHANGE)

    def add_on_channel_close_callback(self):
        """This method tells pika to call the on_channel_closed method if
        RabbitMQ unexpectedly closes the channel.

        """
        log.info('Adding channel close callback')
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        """Invoked by pika when RabbitMQ unexpectedly closes the channel.
        Channels are usually closed if you attempt to do something that
        violates the protocol, such as re-declare an exchange or queue with
        different parameters. In this case, we'll close the connection
        to shutdown the object.

        :param pika.channel.Channel: The closed channel
        :param int reply_code: The numeric reason the channel was closed
        :param str reply_text: The text reason the channel was closed

        """
        log.warning('Channel %i was closed: (%s) %s',
                    channel, reply_code, reply_text)
        self._connection.close()

    def setup_exchange(self, exchange_name):
        """Setup the exchange on RabbitMQ by invoking the Exchange.Declare RPC
        command. When it is complete, the on_exchange_declareok method will
        be invoked by pika.

        :param str|unicode exchange_name: The name of the exchange to declare

        """
        log.info('Declaring exchange %s', exchange_name)
        self._channel.exchange_declare(self.on_exchange_declareok,
                                       exchange_name,
                                       self.EXCHANGE_TYPE, auto_delete='false')

    def on_exchange_declareok(self, unused_frame):
        """Invoked by pika when RabbitMQ has finished the Exchange.Declare RPC
        command.

        :param pika.Frame.Method unused_frame: Exchange.DeclareOk response frame

        """
        log.info('Exchange declared')
        self.setup_queue(self.QUEUE)

    def setup_queue(self, queue_name):
        """Setup the queue on RabbitMQ by invoking the Queue.Declare RPC
        command. When it is complete, the on_queue_declareok method will
        be invoked by pika.

        :param str|unicode queue_name: The name of the queue to declare.

        """
        log.info('Declaring queue %s', queue_name)
        self._channel.queue_declare(self.on_queue_declareok, queue_name)

    def on_queue_declareok(self, method_frame):
        """Method invoked by pika when the Queue.Declare RPC call made in
        setup_queue has completed. In this method we will bind the queue
        and exchange together with the routing key by issuing the Queue.Bind
        RPC command. When this command is complete, the on_bindok method will
        be invoked by pika.

        :param pika.frame.Method method_frame: The Queue.DeclareOk frame

        """
        log.info('Binding %s to %s with %s',
                 self.EXCHANGE, self.QUEUE, self.ROUTING_KEY)
        self._channel.queue_bind(self.on_bindok, self.QUEUE,
                                 self.EXCHANGE, self.ROUTING_KEY)

    def on_bindok(self, unused_frame):
        """Invoked by pika when the Queue.Bind method has completed. At this
        point we will start consuming messages by calling start_consuming
        which will invoke the needed RPC commands to start the process.

        :param pika.frame.Method unused_frame: The Queue.BindOk response frame

        """
        log.info('Queue bound')
        self.start_consuming()

    def start_consuming(self):
        """This method sets up the consumer by first calling
        add_on_cancel_callback so that the object is notified if RabbitMQ
        cancels the consumer. It then issues the Basic.Consume RPC command
        which returns the consumer tag that is used to uniquely identify the
        consumer with RabbitMQ. We keep the value to use it when we want to
        cancel consuming. The on_message method is passed in as a callback pika
        will invoke when a message is fully received.

        """
        log.info('Issuing consumer related RPC commands')
        self.add_on_cancel_callback()
        self._consumer_tag = self._channel.basic_consume(self.on_message,
                                                         self.QUEUE)

    def add_on_cancel_callback(self):
        """Add a callback that will be invoked if RabbitMQ cancels the consumer
        for some reason. If RabbitMQ does cancel the consumer,
        on_consumer_cancelled will be invoked by pika.

        """
        log.info('Adding consumer cancellation callback')
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame):
        """Invoked by pika when RabbitMQ sends a Basic.Cancel for a consumer
        receiving messages.

        :param pika.frame.Method method_frame: The Basic.Cancel frame

        """
        log.info('Consumer was cancelled remotely, shutting down: %r',
                 method_frame)
        if self._channel:
            self._channel.close()

    def on_message(self, unused_channel, basic_deliver, properties, body):
        """Invoked by pika when a message is delivered from RabbitMQ. The
        channel is passed for your convenience. The basic_deliver object that
        is passed in carries the exchange, routing key, delivery tag and
        a redelivered flag for the message. The properties passed in is an
        instance of BasicProperties with the message properties and the body
        is the message that was sent.

        :param pika.channel.Channel unused_channel: The channel object
        :param pika.Spec.Basic.Deliver: basic_deliver method
        :param pika.Spec.BasicProperties: properties
        :param str|unicode body: The message body

        """
        payload = json.loads(body)

        # If we have a batch of events rather than just 1
        if type(payload) is list:
            for message in payload:
                log.info('Received event with batch # %s with UUID %s and with severity %s',
                         basic_deliver.delivery_tag, message['uuid'], message['severity_id'])
                # If user provides an assignee, add it to payload.
                try:
                    message['log_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(message['log_time']/1000))
                    # Check if the incident owner config var is provided
                    if self._helper.get_config_option("icdx_forwarder_inc_owner", True):
                        log.info("Incident Assignee is provided. Asignee : {}".format(self._helper.get_config_option("icdx_forwarder_inc_owner", True)))
                        message['owner'] = self._helper.get_config_option("icdx_forwarder_inc_owner")

                    # Perform a mapping between the severity
                    message['severity_code'] = self.map_to_resilient_severity(source_range=range(1, (6+1)), severity=int(message["severity_id"]))
                except Exception as e:
                    log.error("Error while determining incident owner and severity. Error : {0}".format(str(e)))
                finally:
                    try:
                        self.create_resilient_incident(message)

                    except Exception as e:
                        log.error("Encountered error while creating incident " + str(e))

        else:
            log.debug('Payload is not a list ')
            log.info('Received single event with batch # %s with UUID %s and with severity %s',
                     basic_deliver.delivery_tag, payload['uuid'], payload['severity_id'])
            # If user provides an asignee, add it to payload.
            try:
                if self._helper.get_config_option("icdx_forwarder_inc_owner", True):
                    log.info("Incident Assignee is provided. Asignee : {}".format(
                        self._helper.get_config_option("icdx_forwarder_inc_owner", True)))
                    payload['owner'] = self._helper.get_config_option("icdx_forwarder_inc_owner")

            except Exception as e:
                log.error("Error gathering Incident Owner config value. Error : ".format(str(e)))
            finally:
                self.create_resilient_incident(payload)

        # Send ACK after dealing with the message
        self.acknowledge_message(basic_deliver.delivery_tag)

    def map_to_resilient_severity(self, source_range, severity):
        """
        A function which takes in :
        A source range (1,5) in list form
        A severity

        Contacts the REST API to get both the severity codes enabled for the org and the amount of them
        Then perform a transformation on the input, outputting its equivalent code in resilient
        :return:
        """
        try:
            uri = '/types/incident/fields/severity_code'

            # Create the incident
            incident = self._client.get(uri)

            """
            Apply an algorithm to transform our provided severity code into a resilient one
            
            The formula to determine this is detailed in our internal wiki
            This is a one-liner but is seperated into multiple lines for PEP8
            """
            res_severity = round(
                (severity-source_range[0])
                * ((len([value for value in incident["values"]
                        if value["enabled"] and not value["hidden"]])-1)
                    / (source_range[len(source_range)-1]
                        - source_range[0]))+1)
            # Above calculation-1 gets us the index of the ideal severity to use, take its value and wrap as str
            return str(incident["values"][res_severity-1]["value"])

        except Exception as e:
            log.error("Encountered exception when trying to determine the resilient severity code {0}".format(str(e)))

    def create_resilient_incident(self, message):
        # Get current path for this .py file, then join this to the 'data/templates' folder
        default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "data/templates")
        # Construct the basic incident DTO that will be posted
        new_incident = self._helper.map_values(
            # Add file name to our path to complete the path of template_file
            template_file=os.path.abspath(default_dir+'/_icdx_incident_from_event_template.jinja2'),
            message_dict=message)

        try:
            uri = '/incidents'




            # Create the incident
            incident = self._client.post(uri, json.loads(new_incident))

            inc_id = incident["id"]

            log.info("\n\nCreated a new incident with ID: {}".format(inc_id))

        except resilient.SimpleHTTPException as ecode:
            log.error("create failed : {}".format(ecode))

    def acknowledge_message(self, delivery_tag):
        """Acknowledge the message delivery from RabbitMQ by sending a
        Basic.Ack RPC method for the delivery tag.

        :param int delivery_tag: The delivery tag from the Basic.Deliver frame

        """
        log.info('Acknowledging message/batch %s', delivery_tag)
        self._channel.basic_ack(delivery_tag)

    def stop_consuming(self):
        """Tell RabbitMQ that you would like to stop consuming by sending the
        Basic.Cancel RPC command.

        """
        if self._channel:
            log.info('Sending a Basic.Cancel RPC command to RabbitMQ')
            self._channel.basic_cancel(self.on_cancelok, self._consumer_tag)

    def on_cancelok(self, unused_frame):
        """This method is invoked by pika when RabbitMQ acknowledges the
        cancellation of a consumer. At this point we will close the channel.
        This will invoke the on_channel_closed method once the channel has been
        closed, which will in-turn close the connection.

        :param pika.frame.Method unused_frame: The Basic.CancelOk frame

        """
        log.info('RabbitMQ acknowledged the cancellation of the consumer')
        self.close_channel()

    def close_channel(self):
        """Call to close the channel with RabbitMQ cleanly by issuing the
        Channel.Close RPC command.

        """
        log.info('Closing the channel')
        self._channel.close()

    def run(self):
        """Run the example consumer by connecting to RabbitMQ and then
        starting the IOLoop to block and allow the SelectConnection to operate.

        """
        try:
            log.error("Starting connection to AMQP Exchange")
            self._connection = self.connect()
            self._connection.ioloop.start()
        except Exception as e:
            log.error("Encountered Exception: {}. Attempting to stop consumer gracefully".format(str(e)))
            self.stop()

    def stop(self):
        """Cleanly shutdown the connection to RabbitMQ by stopping the consumer
        with RabbitMQ. When RabbitMQ confirms the cancellation, on_cancelok
        will be invoked by pika, which will then closing the channel and
        connection. The IOLoop is started again because this method is invoked
        when CTRL-C is pressed raising a KeyboardInterrupt exception. This
        exception stops the IOLoop which needs to be running for pika to
        communicate with RabbitMQ. All of the commands issued prior to starting
        the IOLoop will be buffered but not processed.

        """
        log.info('Stopping')
        self._closing = True
        self.stop_consuming()
        self._connection.ioloop.start()
        log.info('Stopped')

    def close_connection(self):
        """This method closes the connection to RabbitMQ."""
        log.info('Closing connection')
        self._connection.close()

