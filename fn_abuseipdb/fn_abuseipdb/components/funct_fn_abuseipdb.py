# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_abuseipdb"
FN_NAME = "fn_abuseipdb"

LOG = logging.getLogger(__name__)

HEADER_TEMPLATE = {
    "Key": None,
    "Accept": "application/json"
}

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_abuseipdb'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _lookup_net_ip(self, fn_inputs):
        """Lookup an artifact"""

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = fn_inputs.abuseipdb_artifact_type
        artifact_value = fn_inputs.abuseipdb_artifact_value

        # Example validating app_configs
        validate_fields([
            {"name": "abuseipdb_key"},
            {"name": "abuseipdb_url"}],
            self.app_configs)

        LOG.info("AbuseIPDB lookup started for Artifact Type %s - Artifact Value %s",
                 artifact_type, artifact_value)

        params = {
                'ipAddress': artifact_value,
                'isWhitelisted': self.app_configs.ignore_white_listed,
                'verbose': True
            }

        headers = HEADER_TEMPLATE.copy()
        headers['Key'] = self.app_configs.abuseipdb_key

        url = self.app_configs.abuseipdb_url

        response = self.rc.execute("get", url, params=params, headers=headers)

        results = response.json()

        yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Call API implemtation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()
        #
        # yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        #
        # yield FunctionResult(results)
        ##############################################
