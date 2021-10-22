# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, INCIDENTS_URL, PACKAGE_NAME

FN_NAME = "defender_get_incident"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'defender_get_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get a Defender 365 Incident
        Inputs:
            -   fn_inputs.defender_incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        incident_id = fn_inputs.defender_incident_id

        defender_api = DefenderAPI(self._app_configs_as_dict['tenant_id'],
                                   self._app_configs_as_dict['client_id'],
                                   self._app_configs_as_dict['app_secret'],
                                   self.opts,
                                   self._app_configs_as_dict)

        url = '/'.join([INCIDENTS_URL, str(incident_id)])
        incident_payload, status, reason = defender_api.call(url)
        self.LOG.debug(incident_payload)
        results = incident_payload

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.options)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

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

        ##############################################

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
