# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME
from fn_splunk_integration.util.function_utils import get_servers_list
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkUtils
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
        splunk_threat_intel_key: _key returned from Splunk ES for this item
        """
        try:
            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["splunk_threat_intel_type", "splunk_threat_intel_key"], fn_inputs)

            options = SplunkServers.splunk_label_test(fn_inputs.splunk_label, self.servers_list)

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            # Log all the info
            self.LOG.info(str(fn_inputs))

            # Log the splunk server we are using
            self.LOG.info("Splunk host: %s, port: %s, username: %s",
                     options.get("host"), options.get("port"), options.get("username"))

            splnk_utils = SplunkUtils(host=options.get("host"),
                                      port=options.get("port"),
                                      username=options.get("username"),
                                      password=options.get("splunkpassword"),
                                      verify=splunk_verify_cert)

            splunk_result = splnk_utils.delete_threat_intel_item(threat_type=fn_inputs.splunk_threat_intel_type,
                                                                 item_key=fn_inputs.splunk_threat_intel_key,
                                                                 cafile=splunk_verify_cert)

            yield FunctionResult(splunk_result.get('content', {}))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
