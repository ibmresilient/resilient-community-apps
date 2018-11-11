# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cloud_foundry.util.cloud_foundry_api import IBMCloudFoundryAPI
from fn_cloud_foundry.util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

CONFIG_DATA_SECTION = 'fn_cloud_foundry'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cloud_foundry_instance_command"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        if self.options == {}:
            raise ValueError("{} section is not set in the config file".format(CONFIG_DATA_SECTION))

        self.base_url = self.options.get("cf_api_base")

        if not self.base_url:
            raise ValueError("cf_api_base is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))

        self.base_url = str(self.base_url).rstrip('/')

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
            log.info("fn_cloud_foundry_action: %s", action_name) # text
            log.info("fn_cloud_foundry_applications: %s", application_name) # text
            log.info("fn_cloud_foundry_instances: %s", instances) # text

            yield StatusMessage("Starting.")

            instances = [x.strip() for x in instances.split(",")]

            authenticator = IBMCloudFoundryAuthenticator(self.base_url, self.options)
            yield StatusMessage("Authenticated into Cloud Foundry")
            cf_service = IBMCloudFoundryAPI(self.base_url, authenticator)
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
