# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
import fn_qradar_integration.util.qradar_constants as qradar_constants
import fn_qradar_integration.util.function_utils as function_utils

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_get_reference_set_data''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts, "init")
        function_utils.update_qradar_servers_select_list(self.opts, self.servers_list)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts, "reload")

    @function("qradar_get_reference_set_data")
    def _qradar_get_reference_set_data_function(self, event, *args, **kwargs):
        """Function: Get the elements in a specified reference set"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            rp = ResultPayload(qradar_constants.PACKAGE_NAME, **kwargs)

            yield StatusMessage("Starting 'qradar_get_reference_set_data' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            qradar_label = kwargs.get("qradar_label")  # text
            qradar_reference_set_name = kwargs.get("qradar_reference_set_name")  # text

            LOG.info("qradar_label: %s", qradar_label)
            LOG.info("qradar_reference_set_name: %s", qradar_reference_set_name)

            options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)

            qradar_verify_cert = True
            if "verify_cert" in options and options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            LOG.debug("Connection to {} using {}".format(options["host"],
                                                         options.get("username") or "service token"))

            qradar_client = QRadarClient(host=options["host"],
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            result = qradar_client.get_ref_set_elements(qradar_reference_set_name)

            status_code = isinstance(result, list)
            reason = None if status_code else result.get('http_response', {}).get('message', 'unknown')
            results = rp.done(success=status_code, 
                              content=result,
                              reason=reason)

            yield StatusMessage("Finished 'qradar_get_reference_set_data' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
