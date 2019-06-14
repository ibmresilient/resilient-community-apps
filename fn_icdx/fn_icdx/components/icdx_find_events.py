# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_icdx.util.helper import ICDXHelper
from fn_icdx.util.amqp_facade import AmqpFacade


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'icdx_utilities_find_events"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_icdx", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_icdx", {})

    @function("icdx_find_events")
    def _icdx_find_events_function(self, event, *args, **kwargs):
        """Function: Takes a number of parameters in a search request and attempts to gather events from the ICDx Platform. Returns a response containing a list of events or a response with a 204 status code when no results are found."""
        try:
            # Get the function parameters:
            icdx_search_request = self.get_textarea_param(kwargs.get("icdx_search_request"))  # textarea

            log = logging.getLogger(__name__)
            log.info("icdx_search_request: %s", icdx_search_request)

            if icdx_search_request is None:
                raise FunctionError("Encountered error: icdx_search_request may not be None")

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
            except Exception as e:
                yield StatusMessage(
                    "Encountered error while initialising the AMQP Client; Reason (if any): {0}".format(str(e)))
                raise FunctionError()
            # Prepare request payload
            try:
                search_payload = json.loads(icdx_search_request)

                # Set the hard limit for displaying in the UI
                """
                if hard limit is not set, it defaults to 100
                if hard limit is set and exceeds 100 that is the new limit
                if hard limit is set and does not exceed 100, 100 is the limit
                Max limit appears to be 500
                """
                search_payload['hard_limit'] = max(
                    [helper.safe_cast(val=i, to_type=int) for i in
                     [helper.get_config_option("icdx_search_limit", True), 100] if i is not None])

                # Payload is now a dict -- read 'limit' and replace with app.config value if exceeds it
                if search_payload['limit'] > search_payload['hard_limit']:
                    search_payload['limit'] = search_payload['hard_limit']

                # All okay, request has valid JSON and an ID
                yield StatusMessage(
                    "Request payload validated. Sending request with a where attribute of {0} and a filter attribute of {1}".format(
                        search_payload.get('where', None) or '"No Where Condition"',
                        search_payload.get('filter', None) or '"No Filter Condition"'))

            except Exception:
                raise FunctionError("Problem parsing the JSON for search request")

            # Make the call to ICDx and get a handle on any results
            search_result, status = amqp_client.call(json.dumps(search_payload))

            yield StatusMessage("ICDX call complete with status: {}".format(status))
            result_set, num_of_results = None, 0

            if not search_result:
                log.info("Received an empty result set for search query.")

            else:
                log.info("Received response. Parsing for information")
                # Get results dict and number of results
                if status == 200:
                    res = json.loads(search_result)

                    result_set, num_of_results = res["result"], len(res["result"])
                elif status == 400:
                    yield StatusMessage("Received a 400 (Bad Request). Check the formatting of your ICDx Query")

            results = {
                "inputs": {
                    "icdx_search_request": search_payload
                },
                "success": (False if status != 200 else True),
                "result_set": result_set,
                "num_of_results": num_of_results,
                "execution_time": int(time.time() * 1000)
            }
            yield StatusMessage(
                "Finishing. Received results: {}. Number of results: {}".format(results["success"], num_of_results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
