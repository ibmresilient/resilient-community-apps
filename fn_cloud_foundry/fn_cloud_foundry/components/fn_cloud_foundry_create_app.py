# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ..util.cloud_foundry_api import IBMCloudFoundryAPI
from ..util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cloud_foundry_create_app"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cloud_foundry", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cloud_foundry", {})

    @function("fn_cloud_foundry_create_app")
    def _fn_cloud_foundry_create_app_function(self, event, *args, **kwargs):
        """Function: Creates and deploys a cloud foundry applications from the specified parameters/docker files."""
        try:
            # Get the function parameters:
            application_name = kwargs.get("fn_cloud_foundry_applications", None)  # text
            space_guid = kwargs.get("fn_cloud_foundry_space_guid", None)  # text
            additional_parameters = kwargs.get("fn_cloud_foundry_additional_parameters_json", None)  # text

            if additional_parameters is None:
                additional_parameters = {}
            else:
                import json
                additional_parameters = json.loads(additional_parameters)

            log = logging.getLogger(__name__)
            log.info("fn_cloud_foundry_applications: %s", application_name)
            log.info("fn_cloud_foundry_space_guid: %s", space_guid)
            log.info("fn_cloud_foundry_additional_parameters_json: %s", additional_parameters)

            base_url = self.options["cf_api_base"]

            authenticator = IBMCloudFoundryAuthenticator(base_url, self.options)
            cf_service = IBMCloudFoundryAPI(base_url, authenticator)

            values = {
                "space_guid": space_guid,
                "name": application_name
            }

            values = additional_parameters.update(values)  # so values overwrite additional params, not the other way

            results = cf_service.create_app(values)
            log.info("Result: %s", results)
            yield StatusMessage("Done...")
            self._add_keys(results)
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(str(e))
