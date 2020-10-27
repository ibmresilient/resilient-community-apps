# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_qradar_integration"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_reference_table_update_item''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("qradar_reference_table_update_item")
    def _qradar_reference_table_update_item_function(self, event, *args, **kwargs):
        """Function: Update an item in a given QRadar reference table"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_reference_table_update_item' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            qradar_reference_table_name = kwargs.get("qradar_reference_table_name")  # text
            qradar_reference_table_item_value = kwargs.get("qradar_reference_table_item_value")  # text
            qradar_reference_table_item_inner_key = kwargs.get("qradar_reference_table_item_inner_key")  # text
            qradar_reference_table_item_outer_key = kwargs.get("qradar_reference_table_item_outer_key")  # text

            log = logging.getLogger(__name__)
            log.info("qradar_reference_table_name: %s", qradar_reference_table_name)
            log.info("qradar_reference_table_item_value: %s", qradar_reference_table_item_value)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'qradar_reference_table_update_item' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
