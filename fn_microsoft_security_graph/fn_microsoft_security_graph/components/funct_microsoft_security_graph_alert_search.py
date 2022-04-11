# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from time import time
from logging import getLogger
from fn_microsoft_security_graph.lib.ms_graph_helper import connect_MSGraph
from resilient_circuits import AppFunctionComponent, FunctionResult, StatusMessage, FunctionError, handler, function

PACKAGE_NAME = "fn_microsoft_security_graph"
LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'microsoft_security_graph_alert_search'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})
        # Connect to micosoft security graph
        self.ms_graph_helper = connect_MSGraph(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        # Connect to micosoft security graph
        self.ms_graph_helper = connect_MSGraph(opts, True)

    @function("microsoft_security_graph_alert_search")
    def _microsoft_security_graph_alert_search_function(self, event, *args, **kwargs):
        """Function: Query alerts from the Microsoft Security Graph API."""
        try:
            start_time = time()
            yield StatusMessage("Starting Microsoft security graph alert search function...")

            # Get the function parameters:
            alert_search_query = kwargs.get("microsoft_security_graph_alert_search_query", None)  # text

            LOG.info("microsoft_security_graph_alert_search_query: %s", alert_search_query)

            # If alert_search_query does not equal None then start_query equals "?$"
            start_query = "?$" if alert_search_query else ""

            response = self.ms_graph_helper.ms_graph_session.get(
                "{}/security/alerts/{}{}".format(self.options.get("microsoft_graph_url"), start_query, alert_search_query))

            if not response:
                raise FunctionError("Request failed, please check the LOG.")

            yield StatusMessage("Microsoft security graph alert search function complete...")

            results = {
                "inputs": {
                    "microsoft_security_graph_alert_search_query": alert_search_query
                },
                "run_time": time() - start_time,
                "content": response.json(),
                "success": True
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
