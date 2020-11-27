# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient

PACKAGE_NAME = "fn_qradar_integration"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_reference_table_delete_item''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("qradar_reference_table_delete_item")
    def _qradar_reference_table_delete_item_function(self, event, *args, **kwargs):
        """Function: Delete an item from a given QRadar reference table"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

            yield StatusMessage("Starting 'qradar_reference_table_delete_item' running in workflow '{0}'".format(wf_instance_id))

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            qradar_reference_table_name = kwargs.get("qradar_reference_table_name")  # text
            qradar_reference_table_item_value = kwargs.get("qradar_reference_table_item_value")  # text
            qradar_reference_table_item_inner_key = kwargs.get("qradar_reference_table_item_inner_key")  # text
            qradar_reference_table_item_outer_key = kwargs.get("qradar_reference_table_item_outer_key")  # text

            log = logging.getLogger(__name__)
            log.info("qradar_reference_table_name: %s", qradar_reference_table_name)
            log.info("qradar_reference_table_item_value: %s", qradar_reference_table_item_value)
            log.info("qradar_reference_table_item_inner_key: %s", qradar_reference_table_item_inner_key)
            log.info("qradar_reference_table_item_outer_key: %s", qradar_reference_table_item_outer_key)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            log.debug("Connecting to QRadar instance @ {}".format(self.options["host"]))

            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options.get("username", None),
                                         password=self.options.get("qradarpassword", None),
                                         token=self.options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=self.options)

            result = qradar_client.delete_ref_table_element(qradar_reference_table_name, qradar_reference_table_item_inner_key, qradar_reference_table_item_outer_key, qradar_reference_table_item_value)
            results = rp.done(success=True,
                              content=result)
            
            yield StatusMessage("Call made to QRadar and response code returned is {}".format(result['status_code']))
            yield StatusMessage("Finished 'qradar_reference_table_delete_item' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
