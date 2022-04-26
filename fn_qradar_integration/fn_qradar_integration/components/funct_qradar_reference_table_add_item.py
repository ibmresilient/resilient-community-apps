# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2022. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
import fn_qradar_integration.util.function_utils as function_utils

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_reference_table_add_item''"""

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

    @function("qradar_reference_table_add_item")
    def _qradar_reference_table_add_item_function(self, event, *args, **kwargs):
        """Function: Add an item to a given QRadar reference table"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'qradar_reference_table_add_item' running in workflow '{0}'".format(wf_instance_id))

            validate_fields(["qradar_reference_table_name", "qradar_reference_table_item_value"], kwargs)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            # Get the function parameters:
            qradar_reference_table_name = kwargs.get("qradar_reference_table_name")  # text
            qradar_reference_table_item_value = kwargs.get("qradar_reference_table_item_value")  # text
            qradar_reference_table_item_inner_key = kwargs.get("qradar_reference_table_item_inner_key")  # text
            qradar_reference_table_item_outer_key = kwargs.get("qradar_reference_table_item_outer_key")  # text
            qradar_label = kwargs.get("qradar_label")  # text

            LOG.info("qradar_reference_table_name: %s", qradar_reference_table_name)
            LOG.info("qradar_reference_table_item_value: %s", qradar_reference_table_item_value)
            LOG.info("qradar_reference_table_item_inner_key: %s", qradar_reference_table_item_inner_key)
            LOG.info("qradar_reference_table_item_outer_key: %s", qradar_reference_table_item_outer_key)
            LOG.info("qradar_label: %s", qradar_label)

            options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
            qradar_verify_cert = False if options.get("verify_cert", "false").lower() == "false" else options.get("verify_cert")

            LOG.debug("Connecting to QRadar instance @ {}".format(options.get("host")))

            qradar_client = QRadarClient(host=options.get("host"),
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            result = qradar_client.add_ref_table_element(qradar_reference_table_name, 
                                                         qradar_reference_table_item_inner_key,
                                                         qradar_reference_table_item_outer_key,
                                                         qradar_reference_table_item_value)
            
            # Tests if there is a status code
            status_code = bool(result.get('status_code', False) < 300)
            reason = None if status_code else result['content'].get('message', None)
            results = rp.done(success=status_code,
                              content=result,
                              reason=reason)

            yield StatusMessage("Call made to QRadar and response code returned: {}".format(result.get('status_code', 'no response code found')))
            yield StatusMessage("Finished 'qradar_reference_table_add_item' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
