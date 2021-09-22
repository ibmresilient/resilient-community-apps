# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_microsoft_defender.lib.defender_common import DefenderAPI, ALERTS_URL, ALERTS_EXPAND_PARAMS, PACKAGE_NAME

FN_NAME = "defender_get_related_alert_information"
ALERT_TYPES = {
    'Files': 'files',
    'Devices': 'machine',
    'Domains': 'domains',
    'Files': 'files',
    'IPs': 'ips',
    'Users': 'user'
}

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'defender_get_related_alert_information'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get a Defender ATP machine alert details
        Inputs:
            -   fn_inputs.defender_alert_info
            -   fn_inputs.defender_alert_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        alert_id = fn_inputs.defender_alert_id
        alert_info = fn_inputs.defender_alert_info

        defender_api = DefenderAPI(self._app_configs_as_dict['tenant_id'],
                                   self._app_configs_as_dict['client_id'],
                                   self._app_configs_as_dict['app_secret'],
                                   self._app_configs_as_dict,
                                   self._app_configs_as_dict)

        if 'All' in alert_info:
            alert_info = ALERT_TYPES.keys()

        result = {}
        for type in alert_info:
            url = '/'.join([ALERTS_URL, alert_id, ALERT_TYPES.get(type)])
            alert_payload, status, reason = defender_api.call(url, payload=ALERTS_EXPAND_PARAMS)
            self.LOG.debug(alert_payload)
            result[type] = alert_payload.get('value') if alert_payload.get('value') else alert_payload


        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self._app_configs_as_dict)

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

        yield FunctionResult(result)
        # yield FunctionResult({}, success=False, reason="Bad call")
