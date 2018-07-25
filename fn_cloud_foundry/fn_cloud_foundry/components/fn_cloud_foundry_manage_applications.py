# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ..util.cloud_foundry_api import IBMCloudFoundryAPI
from ..util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cloud_foundry_manage_applications"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cloud_foundry", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cloud_foundry", {})

    @function("fn_cloud_foundry_manage_applications")
    def _fn_cloud_foundry_manage_applications_function(self, event, *args, **kwargs):
        """Function: Performs a specified action on the chosen Cloud Foundry applications."""
        try:
            # Get the function parameters:
            action_name = self.get_select_param(kwargs.get("fn_cloud_foundry_action"))  # select, values: "Start", "Stop", "Metadata"
            application_names = kwargs.get("fn_cloud_foundry_applications")  # text

            log = logging.getLogger(__name__)
            log.info("fn_cloud_foundry_action: %s", action_name)
            log.info("fn_cloud_foundry_applications: %s", application_names)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            yield StatusMessage("starting...")

            api_key2 = self.options["api_key"]
            bx_apps_url2 = self.options["bx_apps_url"]
            bx_api_url2 = self.options["bx_api_url"]
            bx_app_details_url2 = self.options["bx_app_details_url"]
            authenticator = IBMCloudFoundryAuthenticator(bx_api_url2, api_key2)
            bx_service = IBMCloudFoundryAPI(api_key2, bx_api_url2, bx_apps_url2, bx_app_details_url2, authenticator)
            results = bx_service.run(application_names, action_name)

            log.info("result: %s", results)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()