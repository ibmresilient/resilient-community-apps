# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
# Copyright IBM Corp. 2010, 2023 - Confidential Information

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_microsoft_defender.lib.defender_common import DefenderAPI, ALERTS_URL, EXPAND_PARAMS_URL, PACKAGE_NAME

FN_NAME = "defender_get_related_alert_information"
ALERT_TYPES = {
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

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        alert_id = fn_inputs.defender_alert_id
        alert_info = fn_inputs.defender_alert_info

        defender_api = DefenderAPI(self._app_configs_as_dict['tenant_id'],
                                   self._app_configs_as_dict['client_id'],
                                   self._app_configs_as_dict['app_secret'],
                                   self.opts,
                                   self._app_configs_as_dict)

        if 'All' in alert_info:
            alert_info = ALERT_TYPES.keys()

        result = {}
        url = '/'.join([ALERTS_URL, alert_id])
        url = f"{url}?{EXPAND_PARAMS_URL}"
        alert_payload, _status, _reason = defender_api.call(url)
        self.LOG.debug(alert_payload)
        result['General'] = alert_payload.get('value') if alert_payload.get('value') else alert_payload

        for alert_type in alert_info:
            url = '/'.join([ALERTS_URL, alert_id, ALERT_TYPES.get(alert_type)])
            alert_payload, _status, _reason = defender_api.call(url)
            self.LOG.debug(alert_payload)
            result[alert_type] = alert_payload.get('value') if alert_payload.get('value') else alert_payload

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(result)
