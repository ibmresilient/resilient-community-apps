# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cloud_foundry_instance_command"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cloud_foundry", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cloud_foundry", {})

    @function("fn_cloud_foundry_instance_command")
    def _fn_cloud_foundry_instance_command_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            fn_cloud_foundry_action = self.get_select_param(kwargs.get("fn_cloud_foundry_action"))  # select, values: "info", "start", "stop", "restage", "instances", "delete"
            fn_cloud_foundry_instances = kwargs.get("fn_cloud_foundry_instances")  # text
            fn_cloud_foundry_applications = kwargs.get("fn_cloud_foundry_applications")  # text

            log = logging.getLogger(__name__)
            log.info("fn_cloud_foundry_action: %s", fn_cloud_foundry_action)
            log.info("fn_cloud_foundry_instances: %s", fn_cloud_foundry_instances)
            log.info("fn_cloud_foundry_applications: %s", fn_cloud_foundry_applications)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()