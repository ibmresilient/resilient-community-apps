# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from dxlclient.client import DxlClient
from dxlclient import Request, Event, Response
from dxlclient.client_config import DxlClientConfig

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_publish_to_dxl"""

    config_file = "dxlclient_config"

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        try:
            self.config = opts.get("fn_mcafee_opendxl").get(self.config_file)
            if self.config is None:
                log.error(self.config_file + " is not set. You must set this path to run this function")
                raise ValueError(self.config_file + " is not set. You must set this path to run this function")

            # Create configuration from file for DxlClient
            config = DxlClientConfig.create_dxl_config_from_file(self.config)
            # Create client
            self.client = DxlClient(config)
            self.client.connect()
        except AttributeError:
            log.error("There is no [fn_mcafee_opendxl] section in the config file,"
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[fn_mcafee_opendxl] section is not set in the config file")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.config = opts.get("fn_mcafee_opendxl").get(self.config_file)

    @function("mcafee_publish_to_dxl")
    def _mcafee_publish_to_dxl_function(self, event, *args, **kwargs):
        """Function: A function which takes 3 inputs:

        mcafee_topic_name: String of the topic name. ie: /mcafee/service/epo/remote/epo1.
        mcafee_dxl_payload: The text of the payload to publish to the topic.
        mcafee_return_request: Specify whether or not to wait for and return the response.


        The function will publish the provided payload to the provided topic.
        Indicate whether acknowledgment response should be returned."""
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            mcafee_topic_name = kwargs.get("mcafee_topic_name")  # text
            if not mcafee_topic_name:
                yield FunctionError("mcafee_topic_name is required")
            mcafee_dxl_payload = kwargs.get("mcafee_dxl_payload")  # text
            if not mcafee_dxl_payload:
                yield FunctionError("mcafee_dxl_payload is required")
            mcafee_publish_method = self.get_select_param(
                kwargs.get("mcafee_publish_method"))  # select, values: "Event", "Service"
            if not mcafee_publish_method:
                yield FunctionError("mcafee_publish_method is required")
            mcafee_wait_for_response = self.get_select_param(
                kwargs.get("mcafee_wait_for_response"))  # select, values: "Yes", "No"

            log.info("mcafee_topic_name: %s", mcafee_topic_name)
            log.info("mcafee_dxl_payload: %s", mcafee_dxl_payload)
            log.info("mcafee_publish_method: %s", mcafee_publish_method)
            log.info("mcafee_wait_for_response: %s", mcafee_wait_for_response)

            response = None

            # Publish Event
            if mcafee_publish_method == "Event":
                event = Event(mcafee_topic_name)
                event.payload = mcafee_dxl_payload
                yield StatusMessage("Publishing Event...")
                self.client.send_event(event)

            # Invoke Service
            else:
                req = Request(mcafee_topic_name)
                req.payload = mcafee_dxl_payload
                yield StatusMessage("Invoking Service...")

                if mcafee_wait_for_response == "No":
                    self.client.async_request(req)
                else:
                    response = Response(self.client.sync_request(req, timeout=300))

            yield StatusMessage("Done...")
            r = {
                "mcafee_topic_name": mcafee_topic_name,
                "mcafee_dxl_payload": mcafee_dxl_payload,
                "mcafee_publish_method": mcafee_publish_method,
                "mcafee_wait_for_response": mcafee_wait_for_response
            }

            # Return response from publishing to topic
            if response is not None:
                r["response"] = vars(response)
                yield FunctionResult(r)
            else:
                yield FunctionResult(r)
        except Exception as e:
            yield FunctionError(e)