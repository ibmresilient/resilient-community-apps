# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util.function_utils import get_servers_list, function_basics, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "splunk_delete_threat_intel_item"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'splunk_delete_threat_intel_item"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = get_servers_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Delete a threat intel item:
        splunk_threat_intel_type: ip_intel, email_intel....., registry_intel
        splunk_threat_intel_key: _key returned from Splunk ES for this item"""

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["splunk_threat_intel_type", "splunk_threat_intel_key"], fn_inputs)

        splunk, splunk_verify_cert = function_basics(fn_inputs, self.servers_list, utils=True)

        splunk_result = splunk.delete_threat_intel_item(threat_type=fn_inputs.splunk_threat_intel_type,
                                                        item_key=fn_inputs.splunk_threat_intel_key,
                                                        cafile=splunk_verify_cert)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(splunk_result.get('content', {}))
