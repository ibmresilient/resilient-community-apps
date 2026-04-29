# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_lib import validate_fields, clean_html, build_incident_url, unescape
from fn_pagerduty.lib.pd_common import PACKAGE_NAME, PDClient
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "pagerduty_create_incident"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'pagerduty_create_incident"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME, ['api_token', 'from_email'])

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create an incident on PagerDuty"""
        try:
            # validate required fields
            validate_fields(['incidentID', 'pd_title', 'pd_service'], fn_inputs)
            
            incidentID = getattr(fn_inputs, "incidentID", None)
            res_client = self.rest_client()
            url = build_incident_url(res_client.base_url, incidentID, self.rest_client().org_name)

            payloadDict = self.options.copy()
            payloadDict['incidentID'] = incidentID
            payloadDict['title'] = unescape(getattr(fn_inputs, "pd_title", None))
            desc = self.get_textarea_param(getattr(fn_inputs, "pd_description", ""))
            desc = clean_html(desc)

            payloadDict['description'] = '\n'.join((url, desc))
            payloadDict['service'] = getattr(fn_inputs, "pd_service", None)
            payloadDict['escalation_policy'] = getattr(fn_inputs, "pd_escalation_policy", None)
            payloadDict['priority'] = getattr(fn_inputs, "pd_priority", None)
            payloadDict['incident_key'] = getattr(fn_inputs, "pd_incident_key", None)

            yield self.status_message("Starting PagerDuty Create Incident...")
            resp = PDClient(payloadDict).create_incident()
            yield self.status_message("Pagerduty Incident Created")

            # Produce a FunctionResult with the results
            yield FunctionResult({"pd": resp})
        except Exception as err:
            yield FunctionError(str(err))
