# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from time import time
from logging import getLogger
from resilient_lib import validate_fields
from fn_microsoft_security_graph.lib.ms_graph_helper import connect_MSGraph
from resilient_circuits import AppFunctionComponent, FunctionResult, StatusMessage, FunctionError, handler, function

PACKAGE_NAME = "fn_microsoft_security_graph"
LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'microsoft_security_graph_get_alert_details'"""

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

    @function("microsoft_security_graph_get_alert_details")
    def _microsoft_security_graph_get_alert_details_function(self, event, *args, **kwargs):
        """Function: Get the details of an alert from the Microsoft Security Graph API."""
        try:
            start_time = time()
            yield StatusMessage("Starting Microsoft security graph get alert details function...")
            # Validate requiered fields
            validate_fields(["microsoft_security_graph_alert_id"], kwargs)

            # Get the function parameters:
            microsoft_security_graph_alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text

            LOG.info("microsoft_security_graph_alert_id: %s", microsoft_security_graph_alert_id)

            response = get_alert_details(self.options.get("microsoft_graph_url"), self.ms_graph_helper,
                                  microsoft_security_graph_alert_id)
            if not response:
                raise FunctionError("Request failed, please check the LOG.")

            yield StatusMessage("Microsoft security graph get alert details function complete...")
            end_time = time()
            results = {
                "inputs": {
                    "microsoft_security_graph_alert_id": microsoft_security_graph_alert_id
                },
                "run_time": end_time - start_time,
                "content": response.json(),
                "success": True
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)

def get_alert_details(url, ms_helper, alert_id):

    return ms_helper.ms_graph_session.get("{}/security/alerts/{}".format(url, alert_id))