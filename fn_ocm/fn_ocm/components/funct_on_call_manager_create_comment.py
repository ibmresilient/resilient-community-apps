# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_ocm.util.helper import ocm_client, PACKAGE_NAME

FN_NAME = "on_call_manager_create_comment"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'on_call_manager_create_comment'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Validate required app.config settings
        validate_fields(["ocm_url", "ocm_api_key_name", "ocm_api_key_pass"], self.options)
        # Create client connection
        self.client = ocm_client(self.options.get("ocm_url", None), self.options.get("ocm_api_key_name", None), self.options.get("ocm_api_key_pass", None), self.rc)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Creates a comment for the incident
        Inputs:
            -   fn_inputs.ocm_incident_comment
            -   fn_inputs.ocm_incident_id
            -   fn_inputs.ocm_comment_author
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        try:
            # Validate required fields
            validate_fields(["ocm_incident_comment", "ocm_incident_id", "ocm_comment_author"], fn_inputs)
            # Make API call to create comment on an incident.
            results = self.client.create_comment(fn_inputs.ocm_incident_id, fn_inputs.ocm_incident_comment, fn_inputs.ocm_comment_author)
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            if isinstance(results, dict) and (results.get("level", None) == 'error' or results.get("error", None)):
                yield FunctionResult({}, success=False, reason=str(results))
            else:
                yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err.value)
