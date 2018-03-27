# -*- coding: utf-8 -*-
#
# Copyright IBM Corp. - Confidential Information
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import splunk_utils


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'splunk_delete_threat_intel_item"""

    #
    # Member variables
    #
    splunk_password = None
    app_config = None

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_splunk_integration", {})
        self.app_config = opts.get(splunk_utils.SPLUNK_SECTION, {})

        #
        # Somehow keyrings only works for the resilient section
        #
        args = dict(opts)
        self.splunk_password = args["resilient"]["splunkpassword"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_splunk_integration", {})

    @function("splunk_delete_threat_intel_item")
    def _splunk_delete_threat_intel_item_function(self, event, *args, **kwargs):
        """Function: Delete a threat intel item:
        splunk_threat_intel_type: ip_intel, email_intel....., registry_intel
        splunk_threat_intel_key: _key returned from Splunk ES for this item
        splunk_verify_cert: False to skipping the validation of https cert."""
        try:
            # Get the function parameters:
            splunk_threat_intel_type = kwargs.get("splunk_threat_intel_type")  # text
            splunk_threat_intel_key = kwargs.get("splunk_threat_intel_key")  # text
            splunk_verify_cert = kwargs.get("splunk_verify_cert")  # boolean
            if not splunk_verify_cert:
                splunk_verify_cert = False

            # Log all the info
            log = logging.getLogger(__name__)
            log.info("splunk_threat_intel_type: %s", splunk_threat_intel_type)
            log.info("splunk_threat_intel_key: %s", splunk_threat_intel_key)
            log.info("splunk_verify_cert: " + str(splunk_verify_cert))

            # Log the splunk server we are using
            log.info("Splunk host: %s, port: %s, username: %s",
                     self.app_config["host"], self.app_config["port"], self.app_config["username"])

            yield StatusMessage("starting...")

            splnk_utils = splunk_utils.SplunkUtils(host=self.app_config["host"],
                                                   port=self.app_config["port"],
                                                   username=self.app_config["username"],
                                                   password=self.splunk_password,
                                                   verify=splunk_verify_cert)

            result = splnk_utils.delete_threat_intel_item(threat_type=splunk_threat_intel_type,
                                                          item_key=splunk_threat_intel_key,
                                                          cafile=splunk_verify_cert)

            yield StatusMessage("done...")
            yield FunctionResult(result)
        except Exception as e:
            log.error("Function execution throws exception {}".format(str(e)))
            yield FunctionError(str(e))