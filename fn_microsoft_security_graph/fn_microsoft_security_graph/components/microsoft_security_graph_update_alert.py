# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_microsoft_security_graph.util.helper import MicrosoftGraphHelper


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'microsoft_security_graph_update_alert"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_microsoft_security_graph", {})

        if self.Microsoft_security_graph_helper is None:
            self.Microsoft_security_graph_helper = MicrosoftGraphHelper(self.options.get("tenant_id"),
                                                                        self.options.get("client_id"),
                                                                        self.options.get("client_secret"))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_microsoft_security_graph", {})

    @function("microsoft_security_graph_update_alert")
    def _microsoft_security_graph_update_alert_function(self, event, *args, **kwargs):
        """Function: Update an alert in the Microsoft Security Graph."""
        try:

            yield StatusMessage("starting...")
            # Get the function parameters:
            microsoft_security_graph_alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text
            microsoft_security_graph_alert_data = kwargs.get("microsoft_security_graph_alert_data")  # text

            if microsoft_security_graph_alert_id is not None:
                log.info("microsoft_security_graph_alert_id: %s", microsoft_security_graph_alert_id)
            else:
                raise ValueError("microsoft_security_graph_alert_id is required to run this function.")
            if microsoft_security_graph_alert_data is not None:
                log.info("microsoft_security_graph_alert_data: %s", microsoft_security_graph_alert_data)
            else:
                raise ValueError("microsoft_security_graph_alert_data is required to run this function")

            headers = {
                "Content-type": "application/json",
                "Authorization": "Bearer " + self.Microsoft_security_graph_helper.get_access_token(),
                "Prefer": "return=representation"
            }
            try:
                data = json.loads(microsoft_security_graph_alert_data)
            except ValueError as e:
                raise FunctionError("microsoft_security_graph_alert_data needs to be in dict format; " + e.message)

            r = requests.get("https://graph.microsoft.com/v1.0/security/alerts", headers=headers, data=data)
            self.Microsoft_security_graph_helper.check_status_code(r)

            yield StatusMessage("done...")
            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
