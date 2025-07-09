# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from resilient_lib import validate_fields, clean_html
from fn_pagerduty.lib.pd_common import PACKAGE_NAME, PDClient

FN_NAME = "pagerduty_create_note"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'pagerduty_create_note"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create a note on a PagerDuty incident"""
        try:
            # validate the function parameters:
            validate_fields(['pd_incident_id', 'pd_description'], fn_inputs)

            incident_id = getattr(fn_inputs, 'pd_incident_id', None)  # text
            description = clean_html(getattr(fn_inputs, 'pd_description', None))  # text

            yield self.status_message("Starting PagerDuty Create Note for Incidents...")
            resp = PDClient(self.options).create_note(incident_id, description)
            yield self.status_message("Pagerduty Note created")

            # Produce a FunctionResult with the results - if not error, the response is not used
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(str(err))
