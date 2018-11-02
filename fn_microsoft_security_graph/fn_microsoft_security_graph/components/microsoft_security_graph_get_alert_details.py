# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_microsoft_security_graph.util.helper import MicrosoftGraphHelper


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'microsoft_security_graph_get_alert_details"""

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

    @function("microsoft_security_graph_get_alert_details")
    def _microsoft_security_graph_get_alert_details_function(self, event, *args, **kwargs):
        """Function: Get the details of an alert from the Microsoft Security Graph API."""
        options = self.options
        ms_graph_helper = options.get("Microsoft_security_graph_helper")
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            # Get the function parameters:
            microsoft_security_graph_alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text

            if microsoft_security_graph_alert_id is not None:
                log.info("microsoft_security_graph_alert_id: %s", microsoft_security_graph_alert_id)
            else:
                raise ValueError("microsoft_security_graph_alert_id is required to run this function.")

            r = None
            for i in list(range(2)):
                headers = {
                    "Content-type": "application/json",
                    "Authorization": "Bearer " + ms_graph_helper.get_access_token()
                }
                r = requests.get("{}security/alerts/{}".format(options.get("microsoft_graph_url"),
                                                               microsoft_security_graph_alert_id), headers=headers)
                # Need to refresh token and run again
                if ms_graph_helper.check_status_code(r):
                    break
                elif i == 2:
                    raise FunctionError("Problem with the access_token")

            yield StatusMessage("done...")
            end_time = time.time()
            results = {
                "Inputs": {
                    "microsoft_security_graph_alert_id": microsoft_security_graph_alert_id
                },
                "Run Time": str(end_time - start_time),
                "Details": r.json()
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
