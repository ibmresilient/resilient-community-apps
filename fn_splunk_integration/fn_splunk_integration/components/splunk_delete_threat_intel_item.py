# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_splunk_integration.util.function_utils import get_servers_list
from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkUtils

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'splunk_delete_threat_intel_item"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.servers_list = get_servers_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.servers_list = get_servers_list(opts)

    @function("splunk_delete_threat_intel_item")
    def _splunk_delete_threat_intel_item_function(self, event, *args, **kwargs):
        """Function: Delete a threat intel item:
        splunk_threat_intel_type: ip_intel, email_intel....., registry_intel
        splunk_threat_intel_key: _key returned from Splunk ES for this item
        """
        try:
            # Get the function parameters:
            splunk_threat_intel_type = kwargs.get("splunk_threat_intel_type")  # text
            splunk_threat_intel_key = kwargs.get("splunk_threat_intel_key")    # text
            splunk_verify_cert = kwargs.get("splunk_verify_cert")              # boolean
            splunk_label = kwargs.get("splunk_label")                          # text

            options = SplunkServers.splunk_label_test(splunk_label, self.servers_list)

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            # Log all the info
            log.info("splunk_threat_intel_type: %s", splunk_threat_intel_type)
            log.info("splunk_threat_intel_key: %s", splunk_threat_intel_key)
            log.info("splunk_verify_cert: " + str(splunk_verify_cert))
            log.info("splunk_label: %s", splunk_label)

            # Log the splunk server we are using
            log.info("Splunk host: %s, port: %s, username: %s",
                     options.get("host"), options.get("port"), options.get("username"))

            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'splunk_delete_threate_intel_item' that was running in workflow '{}'".format(wf_instance_id))

            result_payload = ResultPayload(PACKAGE_NAME, **kwargs)

            splnk_utils = SplunkUtils(host=options.get("host"),
                                      port=options.get("port"),
                                      username=options.get("username"),
                                      password=options.get("splunkpassword"),
                                      verify=splunk_verify_cert)

            splunk_result = splnk_utils.delete_threat_intel_item(threat_type=splunk_threat_intel_type,
                                                                 item_key=splunk_threat_intel_key,
                                                                 cafile=splunk_verify_cert)

            yield StatusMessage("Finished 'splunk_delete_threate_intel_item' that was running in workflow '{}'".format(wf_instance_id))
            yield FunctionResult(result_payload.done(True, splunk_result.get('content', {})))
        except Exception as e:
            log.error("Function execution throws exception {}".format(str(e)))
            yield FunctionError(str(e))
