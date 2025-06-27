# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_microsoft_defender.lib.defender_common import DefenderAPI, INCIDENTS_URL, PACKAGE_NAME, \
            DEFAULT_DEFENDER_UPDATE_INCIDENT_TEMPLATE, DEFENDER_INCIDENT_SCOPE
from fn_microsoft_defender.lib.jinja_common import JinjaEnvironment

PACKAGE_NAME = "fn_microsoft_defender"
FN_NAME = "defender_update_incident"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'defender_update_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update a Defender Incident
        Inputs:
            -   fn_inputs.defender_determination
            -   fn_inputs.defender_incident_status
            -   fn_inputs.defender_comment
            -   fn_inputs.defender_classification
            -   fn_inputs.defender_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        incident_id = fn_inputs.defender_incident_id

        try:
            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                self.options.get('client_id', None),
                self.options.get('app_secret', None),
                self.opts, self.options,
                scope=DEFENDER_INCIDENT_SCOPE)

            self.LOG.debug(fn_inputs)
            defender_incident = fn_inputs._asdict()    # convert tuple data to dictionary

            self.jinja_env = JinjaEnvironment()
            if fn_inputs.defender_incident_status == "C":  # close action
                defender_incident['defender_incident_status'] = 'Resolved'

            update_payload = self.jinja_env.make_payload_from_template(
                                                            self.options.get("update_defender_alert_template"),
                                                            DEFAULT_DEFENDER_UPDATE_INCIDENT_TEMPLATE,
                                                            defender_incident)

            self.LOG.debug(update_payload)
            incident_payload, status, reason = defender_api.call(
                '/'.join([INCIDENTS_URL, str(incident_id)]), oper='PATCH', payload=update_payload)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(incident_payload, success=status, reason=reason)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
