# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from fn_pagerduty.lib.pd_common import PDClient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "pagerduty_list_incidents"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'pagerduty_list_incidents"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: List PagerDuty incidents"""
        try:
            yield self.status_message("Starting List Incidents...")
            resp = PDClient(self.options).list_incidents(getattr(fn_inputs, "pb_search_date", ""))
            yield self.status_message("Pagerduty Incidents Listed")

            # Produce a FunctionResult with the results - if not error, the response is not used
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(str(err))
