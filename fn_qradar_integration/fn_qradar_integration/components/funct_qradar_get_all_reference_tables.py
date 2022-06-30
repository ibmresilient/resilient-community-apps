# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
import fn_qradar_integration.util.function_utils as function_utils

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_get_all_reference_tables''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts)

    @function("qradar_get_all_reference_tables")
    def _qradar_get_all_reference_tables_function(self, event, *args, **kwargs):
        """Function: Get all reference tables from a QRadar instance"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'qradar_get_all_reference_table' that was running in workflow '{0}'".format(wf_instance_id))
            
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            qradar_label = kwargs.get("qradar_label")  # text

            LOG.info("qradar_label: %s", qradar_label)

            # Test to see if given label exists then return options for the server with that label
            options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
            qradar_verify_cert = False if options.get("verify_cert", "false").lower() == "false" else options.get("verify_cert")

            LOG.debug("Connecting to QRadar instance @ {}".format(options.get("host")))

            qradar_client = QRadarClient(host=options.get("host"),
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            result = qradar_client.get_all_ref_tables()

            status_code = isinstance(result, list)
            reason = None if status_code else result["content"]["http_response"].get("message")
            results = rp.done(success=status_code, 
                              content=result,
                              reason=reason)

            yield StatusMessage("Finished 'qradar_get_all_reference_table' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
