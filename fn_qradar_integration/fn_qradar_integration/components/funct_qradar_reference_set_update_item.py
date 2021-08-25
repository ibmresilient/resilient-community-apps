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
    """Component that implements Resilient function 'qradar_reference_set_update_item''"""

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

    @function("qradar_reference_set_update_item")
    def _qradar_reference_set_update_item_function(self, event, *args, **kwargs):
        """Function: Update an item in a given QRadar reference set"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_reference_set_update_item' running in workflow '{0}'".format(wf_instance_id))

            rp = ResultPayload(qradar_constants.PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            qradar_reference_set_name = kwargs.get("qradar_reference_set_name")  # text
            qradar_label = kwargs.get("qradar_label")  # text
            qradar_reference_set_item_value = kwargs.get("qradar_reference_set_item_value")  # text

            LOG.info("qradar_reference_set_name: %s", qradar_reference_set_name)
            LOG.info("qradar_label: %s", qradar_label)
            LOG.info("qradar_reference_set_item_value: %s", qradar_reference_set_item_value)

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

            result = qradar_client.update_ref_set_elements(qradar_reference_set_name, qradar_reference_set_item_value)

            status_code = bool(result.get('status_code', False) < 300)
            reason = None if status_code else result['content'].get('mesasge', None)
            results = rp.done(success=status_code,
                              content=result,
                              reason=reason)

            yield StatusMessage("Call made to QRadar and response code returned: {}".format(result.get('status_code', 'no response code found')))
            yield StatusMessage("Finished 'qradar_reference_set_update_item' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
