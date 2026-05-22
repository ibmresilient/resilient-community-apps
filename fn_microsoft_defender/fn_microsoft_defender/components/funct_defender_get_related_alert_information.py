# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
# Copyright IBM Corp. 2010, 2025 - Confidential Information

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

        try:
            alert_id = getattr(fn_inputs, "defender_alert_id", None)
            alert_info = getattr(fn_inputs, "defender_alert_info", None)

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                        self.options.get('client_id', None),
                                        self.options.get('app_secret', None),
                                        self.opts, self.options)

            if 'All' in alert_info:
                alert_info = ALERT_TYPES.keys()

            result = {}
            alert_payload, _status, _reason = defender_api.call(
                f"{'/'.join([ALERTS_URL, alert_id])}?{EXPAND_PARAMS_URL}")
            self.LOG.debug(alert_payload)
            result['General'] = alert_payload.get('value', None) if alert_payload.get('value', None) else alert_payload

            for alert_type in alert_info:
                alert_payload, _status, _reason = defender_api.call(
                    '/'.join([ALERTS_URL, alert_id, ALERT_TYPES.get(alert_type)]))
                self.LOG.debug(alert_payload)
                result[alert_type] = alert_payload.get('value', None) if alert_payload.get('value', None) else alert_payload

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(result)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
