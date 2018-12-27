# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cloud_foundry.util.cloud_foundry_api import IBMCloudFoundryAPI
from fn_cloud_foundry.util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

CONFIG_DATA_SECTION = 'fn_cloud_foundry'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cloud_foundry_create_app"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        if self.options == {}:
            raise ValueError("{} section is not set in the config file".format(CONFIG_DATA_SECTION))

        self.base_url = self.options.get("cf_api_base")
        self.cf_api_username = self.options.get("cf_api_username")
        self.cf_api_password = self.options.get("cf_api_password")

        if not self.base_url:
            raise ValueError("cf_api_base is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        else:
            self.base_url = str(self.base_url).rstrip('/')
        if not self.cf_api_username:
            raise ValueError("cf_api_username is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.cf_api_password:
            raise ValueError("cf_api_password is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))

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

            if space_guid is None or application_name is None:
                raise ValueError("Both fn_cloud_foundry_applications and fn_cloud_foundry_space_guid "
                                 "have to be defined.")

            if additional_parameters is None:
                additional_parameters = {}
            else:
                additional_parameters = json.loads(additional_parameters)

            log = logging.getLogger(__name__)
            log.info("fn_cloud_foundry_applications: %s", application_name)
            log.info("fn_cloud_foundry_space_guid: %s", space_guid)
            log.info("fn_cloud_foundry_additional_parameters_json: %s", additional_parameters)
            log.info("Params: {}".format(additional_parameters))

            authenticator = IBMCloudFoundryAuthenticator(self.base_url, self.options)
            yield StatusMessage("Authenticated into Cloud Foundry")
            cf_service = IBMCloudFoundryAPI(self.base_url, authenticator)

            values = {
                "space_guid": space_guid,
                "name": application_name,
                "username" : self.cf_api_username,
                "password" : self.cf_api_password
            }
            additional_parameters.update(values)  # so values overwrite additional params, not the other way
            values = additional_parameters

            results = cf_service.create_app(values)
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
