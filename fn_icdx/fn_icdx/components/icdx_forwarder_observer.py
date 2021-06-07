# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2017. All Rights Reserved.
"""Observer implementation for an ICDx Forwarder"""

import logging
import sys
from resilient_circuits import ResilientComponent
from fn_icdx.util.amqp_async_consumer import AMQPAsyncConsumer
from fn_icdx.util.helper import ICDXHelper, add_methods_to_global
import threading

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
log = logging.getLogger(__name__)


class ICDXComponentObserver(ResilientComponent):
    """Component that connects to a AMQP Message Queue created on the ICDX Platform using a AMQP Forwarder """

    def __init__(self, opts):
        super(ICDXComponentObserver, self).__init__(opts)
        self.options = opts.get("fn_icdx", {})
        add_methods_to_global()
        helper = ICDXHelper(self.options)
        if "pytest" in sys.modules:
            """
            Reaching here indicates that the component is invoked from within a testing session.
            In this case, don't start the forwarder
            """
            log.info("Running within a test environment. Not starting consumer")
        else:
            if helper.str_to_bool(self.options.get("icdx_forwarder_toggle", None)):
                self.setup_observer()

    def setup_observer(self):
        """
        Attempts to create an instance of the Consumer class and begin consuming forwarded messages.
        If the connection is closed unexpectedly, Consumer attempts to reopen it.

        AMQP sends hearbeats to keep a connection alive, if 2 consecutive heartbeats are missed
        the Consumer will completly stop.
        """

        helper = ICDXHelper(self.options)
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

        # Init the Consumer, passing in an instance of RestClient and ICDXHelper as injected deps
        observer = AMQPAsyncConsumer(host=helper.get_config_option("icdx_amqp_host"),
                                     port=helper.get_config_option("icdx_amqp_port", True),
                                     virtual_host=helper.get_config_option("icdx_amqp_vhost"),
                                     username=helper.get_config_option("icdx_amqp_username"),
                                     amqp_password=helper.get_config_option("icdx_amqp_password"),
                                     rest_client=self.rest_client(),
                                     helper=ICDXHelper(self.options))
        """
        Start our consumer, will attempt a connection to ICDX
        When a connection is attempted a chain of functions are called
        Each of these functions has a callback which in turn will trigger the next part of the setup       
        Interfacing with Pika asynchronously is done by passing in callback methods you would like to have invoked
        when a certain event completes.
        
        The on_message function is triggered to potentially create an incident every time a new forwarded event
        comes off the message queue
        
        The below pattern is similar to how threads work wherein all logic is encapsulated -- we only call run()
        All functions are event-based which requires that the output of one function be the input to another.
        """
        try:
            # Create a thread which targets the observers run function
            # N.B note the lack of parentheses on observer.run
            res_daemon_thread = threading.Thread(target=observer.run)
            # Make the thread a daemon (background)
            res_daemon_thread.daemon = True
            # Start daemon thread in bg so rest of resilient-circuits is not blocked
            res_daemon_thread.start()

        except Exception as e:
            log.error("Encountered an issue when starting the thread: {}".format(str(e)))
