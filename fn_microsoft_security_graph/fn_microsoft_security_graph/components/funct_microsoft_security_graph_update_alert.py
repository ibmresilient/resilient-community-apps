# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from ast import literal_eval
from time import time
from logging import getLogger
from resilient_lib import validate_fields
from fn_microsoft_security_graph.lib.ms_graph_helper import connect_MSGraph
from resilient_circuits import AppFunctionComponent, FunctionResult, StatusMessage, FunctionError, handler, function

PACKAGE_NAME = "fn_microsoft_security_graph"
LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'microsoft_security_graph_update_alert'"""

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

    @function("microsoft_security_graph_update_alert")
    def _microsoft_security_graph_update_alert_function(self, event, *args, **kwargs):
        """Function: Update an alert in the Microsoft Security Graph."""
        try:
            start_time = time()
            yield StatusMessage("Starting Microsoft security graph update alert function...")
            # Validate requiered fields
            validate_fields(["microsoft_security_graph_alert_id", "microsoft_security_graph_alert_data"], kwargs)

            # Get the function parameters:
            alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text
            alert_data = self.get_textarea_param(
                kwargs.get("microsoft_security_graph_alert_data"))  # textarea

            LOG.info("microsoft_security_graph_alert_id: %s", alert_id)
            LOG.info("microsoft_security_graph_alert_data: %s", alert_data)

            try:
                data = literal_eval(alert_data)
            except ValueError as e:
                raise FunctionError("microsoft_security_graph_alert_data needs to be in dict format; " + e)

            response = self.ms_graph_helper.ms_graph_session.patch(
                "{}/security/alerts/{}".format(self.options.get("microsoft_graph_url"), alert_id),
                headers={"Content-type": "application/json", "Prefer": "return=representation"},
                json=data)

            if not response:
                raise FunctionError("Request failed, please check the LOG.")

            yield StatusMessage("Microsoft security graph update alert function complete...")
            results = {
                "inputs": {
                    "microsoft_security_graph_alert_id": alert_id,
                    "microsoft_security_graph_alert_data": alert_data
                },
                "run_time": time() - start_time,
                "content": response.json(),
                "success": True
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
