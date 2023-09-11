# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, INCIDENTS_URL, PACKAGE_NAME, \
                                                      DEFENDER_INCIDENT_SCOPE, convert_date

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
                                   self._app_configs_as_dict,
                                   scope=DEFENDER_INCIDENT_SCOPE)

        url = '/'.join([INCIDENTS_URL, str(incident_id)])
        incident_payload, status, reason = defender_api.call(url)
        self.LOG.debug(incident_payload)

        # convert dates to timestamps for alert devices
        if status:
            for alert in incident_payload['alerts']:
                for device in alert['devices']:
                    device['firstSeen_ts'] = convert_date(device['firstSeen'])

        results = incident_payload

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
