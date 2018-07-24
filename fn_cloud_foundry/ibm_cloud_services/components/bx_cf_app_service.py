# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ibm_cloud_services.components.bluemix import IBMBluemixConnectService


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bx_cf_app_service"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("ibm_cloud_services", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("ibm_cloud_services", {})

    @function("bx_cf_app_service")
    def _bx_cf_app_service_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            application_name = kwargs.get("application_name")  # text
            action_name = kwargs.get("action_name")  # text

            log = logging.getLogger(__name__)
            log.info("application_name: %s", application_name)
            log.info("action_name: %s", action_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            yield StatusMessage("starting...")

            api_key2 = self.options["api_key"]
            bx_apps_url2 = self.options["bx_apps_url"]
            bx_api_url2 = self.options["bx_api_url"]
            bx_app_details_url2 = self.options["bx_app_details_url"]
            bx_service = IBMBluemixConnectService(api_key2, bx_api_url2, bx_apps_url2, bx_app_details_url2)
            results = bx_service.run(application_name, action_name)

            log.info("result: %s", results)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
