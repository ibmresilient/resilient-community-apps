# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util import function_utils
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkUtils
from fn_splunk_integration.util.splunk_constants import QUERY_PARAM, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "splunk_add_intel_item"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'splunk_add_intel_item'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = function_utils.get_servers_list(opts)
        function_utils.update_splunk_servers_select_list(self.servers_list, self.rest_client(), "splunk_servers")

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Add a new splunk es threat intelligence item to the collections
        splunk_thread_intel_type: ip_intel, user_intel, ...., or registry_intel
        splunk_query_param1: field1 name of the dict used to create the item;
        splunk_query_param2: field1 value;
        splunk_query_param3: field2 name;
        splunk_query_param4: field2 value;
        ....."""
        try:
            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["splunk_threat_intel_type"], fn_inputs)

            params_list = []
            for input in fn_inputs._asdict():
                if QUERY_PARAM in input:
                    params_list.append(fn_inputs._asdict().get(input))

            options = SplunkServers.splunk_label_test(fn_inputs.splunk_label, self.servers_list)

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            # Log all the info
            self.LOG.info(str(fn_inputs))

            # Build the dict used to add threat intel item
            item_dict = function_utils.make_item_dict(params_list)
            # Log it for debug
            self.LOG.debug("item dict: {}".format(str(item_dict)))

            splnk_utils = SplunkUtils(host=options.get("host"),
                                      port=options.get("port"),
                                      username=options.get("username"),
                                      password=options.get("splunkpassword"),
                                      verify=splunk_verify_cert)

            splunk_result = splnk_utils.add_threat_intel_item(threat_type=fn_inputs.splunk_threat_intel_type,
                                                              threat_dict=item_dict,
                                                              cafile=splunk_verify_cert)

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult(splunk_result.get('content', {}))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
