# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_lib import validate_fields, clean_html
from fn_pagerduty.lib.pd_common import PDClient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "pagerduty_transition_incident"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'pagerduty_transition_incident
        Transitioning an incident can be used to update specific fields (such as priority) or
        Change the status to acknowledged or resolved
    """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: transition an incident"""
        try:
            validate_fields(['pd_incident_id'], fn_inputs)

            # Get the function parameters:
            incident_id = getattr(fn_inputs, "pd_incident_id", None)  # text
            status = self.get_select_param(getattr(fn_inputs, "pd_status", None))  # select, values: "acknowledge", "resolve", "escalate"
            priority = getattr(fn_inputs, "pd_priority", None)  # text
            resolution = clean_html(getattr(fn_inputs, "pd_description", None))  # text
            severity = getattr(fn_inputs, "pd_severity", None)

            yield self.status_message("Starting Update Incident......")
            resp = PDClient(self.options).update_incident(incident_id, status, priority, resolution, severity)
            yield self.status_message("Pagerduty Incident Updated")

            # Produce a FunctionResult with the results
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(str(err))
