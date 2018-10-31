# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cloud_foundry.util.cloud_foundry_api import IBMCloudFoundryAPI
from fn_cloud_foundry.util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cloud_foundry_instance_command"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cloud_foundry", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cloud_foundry", {})

    @function("fn_cloud_foundry_instance_command")
    def _fn_cloud_foundry_instance_command_function(self, event, *args, **kwargs):
        """Function: Performs a specified action on the chosen Cloud Foundry applications."""
        try:
            # Get the function parameters:
            action_name = self.get_select_param(kwargs.get("fn_cloud_foundry_instance_action"))
            application_name = kwargs.get("fn_cloud_foundry_applications", None)  # text
            instances = kwargs.get("fn_cloud_foundry_instances", None)  # text
            additional_parameters = kwargs.get("fn_cloud_foundry_additional_parameters_json", None)  # text

            if action_name is None or application_name is None or instances is None:
                raise ValueError("fn_cloud_foundry_action, fn_cloud_foundry_applications, and "
                                 "fn_cloud_foundry_instances all have to be defined.")

            if additional_parameters is None:
                additional_parameters = {}
            else:
                import json
                additional_parameters = json.loads(additional_parameters)

            log = logging.getLogger(__name__)
            log.info("fn_cloud_foundry_action: %s", action_name)
            log.info("fn_cloud_foundry_applications: %s", application_name)
            log.info("fn_cloud_foundry_instances: %s", instances)

            yield StatusMessage("Starting.")

            base_url = self.options["cf_api_base"]
            instances = [x.strip() for x in instances.split(",")]

            authenticator = IBMCloudFoundryAuthenticator(base_url, self.options)
            yield StatusMessage("Authenticated into Cloud Foundry")
            cf_service = IBMCloudFoundryAPI(base_url, authenticator)
            results = cf_service.run_application_instance_command(application_name, instances, action_name,
                                                                  **additional_parameters)
            log.info("Result: %s", results)
            yield StatusMessage("Done.")
            self._add_keys(results)
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(str(e))

    @staticmethod
    def _add_keys(result):
        keys = list(result.keys())
        for item in result:
            if isinstance(result[item], dict):
                FunctionComponent._add_keys(result[item])
        result["_keys"] = keys
