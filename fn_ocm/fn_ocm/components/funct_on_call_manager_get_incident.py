# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_ocm.util.helper import ocm_client, PACKAGE_NAME

FN_NAME = "on_call_manager_get_incident"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'on_call_manager_get_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the details of an On Call Manager incident
        Inputs:
            -   fn_inputs.ocm_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Validate required fields
        validate_fields(["ocm_incident_id"], fn_inputs)
        try:
            # Create client connection
            client = ocm_client(self.options.get("ocm_url", None), self.options.get("ocm_api_key_name", None), self.options.get("ocm_api_key_pass", None), self.rc)
            # Make API call to get the details of an incident.
            results = client.get_incident(fn_inputs.ocm_incident_id.strip())
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            if isinstance(results, dict) and (results.get("level", None) == 'error' or results.get("error", None)):
                yield FunctionResult({}, success=False, reason=str(results))
            else:
                yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err.value)
