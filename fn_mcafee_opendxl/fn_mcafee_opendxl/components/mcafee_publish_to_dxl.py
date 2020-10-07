# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from dxlclient.client import DxlClient
from dxlclient import Request, Event, Response
from dxlclient.client_config import DxlClientConfig

log = logging.getLogger(__name__)

PACKAGE_NAME = "fn_mcafee_opendxl"

def convert(data):
  if isinstance(data, bytes):      return data.decode()
  if isinstance(data, (str, int)): return str(data)
  if isinstance(data, dict):       return dict(map(convert, data.items()))
  if isinstance(data, tuple):      return tuple(map(convert, data))
  if isinstance(data, list):       return list(map(convert, data))
  if isinstance(data, set):        return set(map(convert, data))

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_publish_to_dxl"""

    config_file = "dxlclient_config"

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        try:
            self.opts = opts
            self.options = opts.get(PACKAGE_NAME, {})

            self.config = self.options.get(self.config_file)
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
        self.config = opts.get(PACKAGE_NAME).get(self.config_file)

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

            # Initialize the results payload
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Return response from publishing to topic
            if response is not None:
                # Convert response object to dict
                response_dict = vars(response)
                # Convert dict bytes fields to string for python 3
                response_dict_str = convert(response_dict)
                r["response"] = response_dict_str

            results = rp.done(True, r)
            # Include for backward compatibility
            results["mcafee_topic_name"] = mcafee_topic_name
            results["mcafee_dxl_payload"] = mcafee_dxl_payload
            results["mcafee_publish_method"] = mcafee_publish_method
            results["mcafee_wait_for_response"] = mcafee_wait_for_response
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)