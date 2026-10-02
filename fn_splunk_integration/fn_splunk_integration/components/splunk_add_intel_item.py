# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util.function_utils import get_servers_list,\
    make_item_dict, function_basics, PACKAGE_NAME, QUERY_PARAM
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "splunk_add_intel_item"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'splunk_add_intel_item'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = get_servers_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Add a new splunk es threat intelligence item to the collections
        splunk_thread_intel_type: ip_intel, user_intel, ...., or registry_intel
        splunk_query_param1: field1 name of the dict used to create the item;
        splunk_query_param2: field1 value;
        splunk_query_param3: field2 name;
        splunk_query_param4: field2 value;
        ....."""

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["splunk_threat_intel_type"], fn_inputs)

        # Build list of parameters
        params_list = [value for input, value in fn_inputs._asdict().items() if QUERY_PARAM in input]

        # Build the dict used to add threat intel item
        item_dict = make_item_dict(params_list)
        # Log it for debug
        self.LOG.debug(f"item dict: {str(item_dict)}")

        splunk = function_basics(fn_inputs, self.servers_list, self.opts)

        splunk_result = splunk.add_threat_intel_item(threat_type=fn_inputs.splunk_threat_intel_type,
                                                     threat_dict=item_dict)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(splunk_result.get('content', {}))
