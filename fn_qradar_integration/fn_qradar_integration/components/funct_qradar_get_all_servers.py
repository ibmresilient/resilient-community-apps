# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_qradar_integration.lib.functions_common import QRadarServers

PACKAGE_NAME = "fn_qradar_integration"

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_get_all_servers''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.servers_list = {}
        self.server_list = {}

        options = opts.get(PACKAGE_NAME, {})

        if options:
            self.server_list = {PACKAGE_NAME}
        else:
            servers = QRadarServers(opts, options)
            self.server_list = servers.get_server_name_list()

        for server_name in self.server_list:
            self.servers_list[server_name] = opts.get(server_name, {})
            options = self.servers_list[server_name]

            required_fields = ["host", "verify_cert"]
            validate_fields(required_fields, options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.servers_list = {}
        self.server_list = {}

        options = opts.get(PACKAGE_NAME, {})

        if options:
            self.server_list = {PACKAGE_NAME}
        else:
            servers = QRadarServers(opts, options)
            self.erver_list = servers.get_server_name_list()

        for server_name in self.server_list:
            self.servers_list[server_name] = opts.get(server_name, {})

    @function("qradar_get_all_servers")
    def _qradar_get_all_servers_function(self, event, *args, **kwargs):
        """Function: Return all of the servers in the app.config"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_get_all_servers' running in workflow '{0}'".format(wf_instance_id))

            LOG.info("Servers found in app.config:")
            for server in self.server_list:
                LOG.info(server)

            yield StatusMessage("Finished 'qradar_get_all_servers' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "Server_names" : self.server_list,
                "content" : self.servers_list
                }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
