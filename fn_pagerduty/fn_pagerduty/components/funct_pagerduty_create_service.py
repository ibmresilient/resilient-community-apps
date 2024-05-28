# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_pagerduty.lib.pd_common import PDClient, PACKAGE_NAME

FN_NAME = "pagerduty_create_service"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'pagerduty_create_service"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create a Service on PagerDuty"""
        try:
            # validate required fields
            validate_fields(['pd_title', 'pd_escalation_policy'], fn_inputs)

            payloadDict = self.options.copy()
            payloadDict['title'] = getattr(fn_inputs, "pd_title", None)
            payloadDict['description'] = getattr(fn_inputs, "pd_description", None)
            payloadDict['escalation_policy'] = getattr(fn_inputs, "pd_escalation_policy", None)

            yield self.status_message("Starting PagerDuty Create Service...")
            resp = PDClient(payloadDict).create_service()
            yield self.status_message("PagerDuty Service Created")

            # Produce a FunctionResult with the results
            yield FunctionResult({"pd": resp})
        except Exception as err:
            yield FunctionError(str(err))
