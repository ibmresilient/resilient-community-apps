# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from grr_api_client import api
from google.protobuf import json_format
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_grr", {})

    @function("grr_search")
    def _grr_search_function(self, event, *args, **kwargs):
        """Function: A function to search for GRR Agent"""
        try:
            # Get the function parameters:
            grr_search_type = self.get_select_param(kwargs.get("grr_search_type"))  # select, values: "ip", "user", "host"
            grr_search_value = kwargs.get("grr_search_value")  # text

            log = logging.getLogger(__name__)
            log.info("grr_search_type: %s", grr_search_type)
            log.info("grr_search_value: %s", grr_search_value)

            # Set the connection parameters
            grr_server=self.options["grr_server"]
            grr_user=self.options["grr_user"]
            grr_pwd=self.options["grr_pwd"]
            verify_cert=self.options["verify_cert"]

            # Setup the connection
            grrapi = api.InitHttp(api_endpoint=grr_server,
                                auth=(grr_user, grr_pwd),verify=verify_cert)

            # Inform the user
            yield StatusMessage("Searching GRR Agents for {}".format(grr_search_value))

            # Search the clients
            # Search Format: "ip:127.0.0.1"
            search_result = grrapi.SearchClients("{}:{}".format(grr_search_type,grr_search_value))

            agents = []
            success = True

            # Set success to False if no agents found
            if search_result == None:
                success = False
          
          # Loop the results and append some them in dict format to agents
            else:
                for agent in search_result:
                    # Get the agent in JSON and convert to Python dictionary
                    entry = json.loads(json_format.MessageToJson(agent.data))
                    agents.append(entry)

            # Create the results dictionary
            results = {
                "success": success,
                "grr_search_value": grr_search_value,
                "grr_search_type": grr_search_type,
                "agents": agents
            }

            # Some logging
            log.info("Sending results to Resilient Appliance")
            log.info(results)
            log.info("Complete")

            # Send the results to the appliance
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()