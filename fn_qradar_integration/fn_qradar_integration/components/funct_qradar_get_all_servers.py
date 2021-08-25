# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_qradar_integration.util.function_utils as function_utils

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_get_all_servers''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts, "init")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts, "reload")

    @function("qradar_get_all_servers")
    def _qradar_get_all_servers_function(self, event, *args, **kwargs):
        """Function: Return all of the servers in the app.config"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_get_all_servers' running in workflow '{0}'".format(wf_instance_id))

            LOG.info("Servers found in app.config:")
            for server in self.server_list:
                LOG.info(server[server.index(":")+1:])

            yield StatusMessage("Finished 'qradar_get_all_servers' that was running in workflow '{0}'".format(wf_instance_id))

            results = {"content" : self.servers_list}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
