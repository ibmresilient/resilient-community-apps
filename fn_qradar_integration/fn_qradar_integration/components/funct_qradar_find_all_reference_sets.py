# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient
from fn_qradar_integration.lib.functions_common import QRadarServers

PACKAGE_NAME = "fn_qradar_integration"

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_find_all_reference_sets''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = {}

        options = opts.get(PACKAGE_NAME, {})

        if options:
            server_list = {PACKAGE_NAME}
        else:
            servers = QRadarServers(opts, options)
            server_list = servers.get_server_name_list()

        for server_name in server_list:
            self.servers_list[server_name] = opts.get(server_name, {})
            options = self.servers_list[server_name]

            required_fields = ["host", "verify_cert"]
            validate_fields(required_fields, options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = {}

        options = opts.get(PACKAGE_NAME, {})

        if options:
            server_list = {PACKAGE_NAME}
        else:
            servers = QRadarServers(opts, options)
            server_list = servers.get_server_name_list()

        for server_name in server_list:
            self.servers_list[server_name] = opts.get(server_name, {})

    @function("qradar_find_all_reference_sets")
    def _qradar_find_all_reference_sets_function(self, event, *args, **kwargs):
        """Function: Return all of the reference sets on a given QRadar server"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_find_all_reference_sets' running in workflow '{0}'".format(wf_instance_id))
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            qradar_label = kwargs.get("qradar_label")  # text

            LOG.info("qradar_label: %s", qradar_label)

            if qradar_label and PACKAGE_NAME+":"+qradar_label in self.servers_list:
                options = self.servers_list[PACKAGE_NAME+":"+qradar_label]
            elif len(self.servers_list) == 1 or qradar_label == PACKAGE_NAME:
                for server_name in self.servers_list:
                    options = self.servers_list[server_name]
            else:
                raise Exception("qradar_label did not match labels given in the app.config")

            qradar_verify_cert = True
            if "verify_cert" in options and options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            LOG.debug("Connection to {} using {}".format(options["host"],
                                                         options.get("username") or "service token"))

            yield StatusMessage("starting...")
            qradar_client = QRadarClient(host=options["host"],
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            result = qradar_client.get_all_ref_set()
            
            status_code = isinstance(result, list)
            reason = None if status_code else result.get('http_response', {}).get('message', 'unknown')
            results = rp.done(success=status_code, 
                              content=result,
                              reason=reason)

            yield StatusMessage("Finished 'qradar_find_all_reference_sets' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
