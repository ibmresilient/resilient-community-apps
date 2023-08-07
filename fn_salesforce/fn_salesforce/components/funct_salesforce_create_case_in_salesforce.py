# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""
import json
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, build_incident_url
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "salesforce_create_case_in_salesforce"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_create_case_in_salesforce'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "salesforce_case_payload"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        salesforce_case_payload = json.loads(fn_inputs.salesforce_case_payload)

        response = app_common.create_salesforce_case(salesforce_case_payload)
        response["entity_url"] = app_common.make_linkback_url(entity_type='Case', entity_id=response.get("id"))
        rest_client = self.rest_client()
        response["soar_case_url"] = build_incident_url(rest_client.base_url, fn_inputs.incident_id, rest_client.org_id)

        results = {"salesforce_case": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
