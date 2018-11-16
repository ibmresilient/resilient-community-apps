# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import json
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_microsoft_security_graph.util.helper import MicrosoftGraphHelper


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'microsoft_security_graph_update_alert"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_microsoft_security_graph", {})

        if "Microsoft_security_graph_helper" not in self.options:
            self.options["Microsoft_security_graph_helper"] = MicrosoftGraphHelper(self.options.get("tenant_id"),
                                                                                   self.options.get("client_id"),
                                                                                   self.options.get("client_secret"))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_microsoft_security_graph", {})

    @function("microsoft_security_graph_update_alert")
    def _microsoft_security_graph_update_alert_function(self, event, *args, **kwargs):
        """Function: Update an alert in the Microsoft Security Graph."""
        options = self.options
        ms_graph_helper = options.get("Microsoft_security_graph_helper")
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            # Get the function parameters:
            microsoft_security_graph_alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text
            microsoft_security_graph_alert_data = self.get_textarea_param(
                kwargs.get("microsoft_security_graph_alert_data"))  # textarea

            if microsoft_security_graph_alert_id is not None:
                log.info("microsoft_security_graph_alert_id: %s", microsoft_security_graph_alert_id)
            else:
                raise FunctionError("microsoft_security_graph_alert_id is required to run this function.")
            if microsoft_security_graph_alert_data is not None:
                log.info("microsoft_security_graph_alert_data: %s", microsoft_security_graph_alert_data)
            else:
                raise FunctionError("microsoft_security_graph_alert_data is required to run this function")

            r = None
            for i in list(range(2)):
                headers = {
                    "Content-type": "application/json",
                    "Authorization": "Bearer " + ms_graph_helper.get_access_token(),
                    "Prefer": "return=representation"
                }
                try:
                    data = json.loads(microsoft_security_graph_alert_data)
                except ValueError as e:
                    raise FunctionError("microsoft_security_graph_alert_data needs to be in dict format; " + e.message)

                r = requests.patch("{}/security/alerts/{}".format(options.get("microsoft_graph_url"),
                                                                  microsoft_security_graph_alert_id), headers=headers,
                                   json=data)
                # Check if need to refresh token and run again
                if ms_graph_helper.check_status_code(r):
                    break
                elif i == 1:
                    raise FunctionError("Problem with the access_token")

            yield StatusMessage("done...")
            end_time = time.time()
            results = {
                "Inputs": {
                    "microsoft_security_graph_alert_id": microsoft_security_graph_alert_id,
                    "microsoft_security_graph_alert_data": microsoft_security_graph_alert_data
                },
                "Run Time": str(end_time - start_time),
                "Value": r.json()
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
