# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from grr_api_client import api
from google.protobuf import json_format
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_grr_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_grr_search", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_grr_search", {})

    @function("fn_grr_search")
    def _fn_grr_search_function(self, event, *args, **kwargs):
        """Function: A function to search for GRR Agent"""
        
        def get_config_option(option_name, optional=False):
          """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
          option = self.options.get(option_name)

          if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in your app.config file. You must set this value to run this function".format(option_name)
            raise ValueError(err)
          else:
            return option

        try:
            # Get the function parameters:
            grr_search_type = self.get_select_param(kwargs.get("grr_search_type"))  # select, values: "ip", "user", "host"
            grr_search_value = kwargs.get("grr_search_value")  # text

            if grr_search_value is None:
                err = "'{0}' is a mandatory function input".format("grr_search_value")
                raise ValueError(err)

            log = logging.getLogger(__name__)
            log.info("grr_search_type: %s", grr_search_type)
            log.info("grr_search_value: %s", grr_search_value)

            # Set the connection parameters
            grr_server=get_config_option("grr_server")
            grr_user=get_config_option("grr_user")
            grr_pwd=get_config_option("grr_pwd")
            verify_cert=get_config_option("verify_cert")

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
          
            # Loop the results and append them in dict format to agents
            else:
                for agent in search_result:
                    # Get the agent in JSON and convert to Python dictionary
                    entry = json.loads(json_format.MessageToJson(agent.data))
                    agents.append(entry)

            # Check if any agents we added
            if len(agents) == 0:
                success = False

            # Create the results dictionary
            results = {
                "success": success,
                "grr_search_value": grr_search_value,
                "grr_search_type": grr_search_type,
                "agents": agents
            }

            # Some logging
            log.info("Sending results to Resilient Appliance")
            log.info("Complete")

            # Send the results to the appliance
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()