# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_icdx.util.helper import ICDXHelper
from fn_icdx.util.amqp_facade import AmqpFacade

GET_EVENT_API_CODE = 0


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'icdx_get_event"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_icdx", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_icdx", {})

    @function("icdx_get_event")
    def _icdx_get_event_function(self, event, *args, **kwargs):
        """Function: Takes in an input of a UUID for an event and attempts to get the details of this event from the ICDx platform."""

        try:
            # Get the function parameters:
            icdx_uuid = kwargs.get("icdx_uuid")  # text

            log = logging.getLogger(__name__)
            log.info("icdx_uuid: %s", icdx_uuid)

            if icdx_uuid is None:
                raise FunctionError("Encountered error: icdx_uuid may not be None")

            helper = ICDXHelper(self.options)
            yield StatusMessage("Attempting to gather config and setup the AMQP Client")
            try:
                # Initialise the AmqpFacade, pass in config values
                amqp_client = AmqpFacade(host=helper.get_config_option("icdx_amqp_host"),
                                         port=helper.get_config_option("icdx_amqp_port", True),
                                         virtual_host=helper.get_config_option("icdx_amqp_vhost"),
                                         username=helper.get_config_option("icdx_amqp_username"),
                                         amqp_password=helper.get_config_option("icdx_amqp_password")
                                         )
                yield StatusMessage("Config options gathered and AMQP client setup.")
            except Exception:
                raise FunctionError("Encountered error while initialising the AMQP Client")

            yield StatusMessage("Sending request to ICDx with a UUID of {0}".format(icdx_uuid))
            # Prepare request payload
            request = {
                "id": GET_EVENT_API_CODE,
                "uuid": icdx_uuid,
            }

            # Make the call to ICDx and get a handle on any results
            search_result_payload, status = amqp_client.call(json.dumps(request))

            yield StatusMessage("ICDx call complete with status: {}".format(status))

            # Define variables related to artifact search to avoid reference before assignment
            artifact_dictionary = None
            artifact_keys_as_list = None
            artifact_values_as_list = None

            if 'connection'.encode('utf-8') in search_result_payload:
                yield StatusMessage("Network Connection attribute found on Event. Parsing for artifact data")

            if 'file'.encode('utf-8') in search_result_payload:
                yield StatusMessage("File attribute found on Event. Parsing for artifact data")

            if 'email'.encode('utf-8') in search_result_payload:
                yield StatusMessage("Email attribute found on Event. Parsing for artifact data")

            if status == 200:
                # Parse the search result for any artifacts
                artifact_dictionary = helper.search_for_artifact_data(json.loads(search_result_payload))
                """Lastly get the keys and the values as separate lists
                This is needed in v30 or lower.
                Post-processing script shows how to use the data in both v30 and v31
                """
                artifact_keys_as_list = artifact_dictionary.keys()
                artifact_values_as_list = artifact_dictionary.values()
            elif status == 400:
                yield StatusMessage("Received a 400 (Bad Request). Check the formatting of your ICDx Query")
            elif status == 401:
                yield StatusMessage("Received a 401 (Auth). Check the credentials in app.config")

            # Return the results
            results = {
                "inputs": {
                    "icdx_uuid": icdx_uuid
                },
                "success": (False if status != 200 else True),
                # 200 is the only status code where we expect a returning event, in all other cases, set to None
                "event": None if status != 200 else json.loads(search_result_payload.decode('utf-8')),
                "artifacts": artifact_dictionary,
                "artifact_keys_as_list": None if isinstance(artifact_keys_as_list, type(None)) else list(
                    artifact_keys_as_list),
                "artifact_values_as_list": None if isinstance(artifact_values_as_list, type(None)) else list(
                    artifact_values_as_list),
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
