# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_ocm.util.helper import ocm_client, PACKAGE_NAME

FN_NAME = "on_call_manager_list_incidents"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'on_call_manager_list_incidents'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: List incidents in a team, owner, or default queue. Specify only owner to get a personal queue. Specify only team for a team queue. Omit owner and team to fetch incidents that are on the default queue.
        Inputs:
            -   fn_inputs.ocm_incident_owner
            -   fn_inputs.ocm_limit
            -   fn_inputs.ocm_start
            -   fn_inputs.ocm_incident_team
            -   fn_inputs.ocm_stream
            -   fn_inputs.ocm_eventsummary
            -   fn_inputs.ocm_includecounts
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        try:
            # Create client connection
            client = ocm_client(self.options.get("ocm_url", None), self.options.get("ocm_api_key_name", None), self.options.get("ocm_api_key_pass", None), self.rc)
            # Make API call to list incidents with the given parameters
            results = client.list_incidents(
                owner=fn_inputs.ocm_incident_owner if getattr(fn_inputs, "ocm_incident_owner", None) else None,
                team=fn_inputs.ocm_incident_team if getattr(fn_inputs, "ocm_incident_team", None) else None,
                limit=fn_inputs.ocm_limit if getattr(fn_inputs, "ocm_limit", None) else 9999,
                start=fn_inputs.ocm_start if getattr(fn_inputs, "ocm_start", None) else 1,
                eventsummary=fn_inputs.ocm_eventsummary if getattr(fn_inputs, "ocm_eventsummary", None) else False,
                includecounts=fn_inputs.ocm_includecounts if getattr(fn_inputs, "ocm_includecounts", None) else False,
                stream=fn_inputs.ocm_stream if getattr(fn_inputs, "ocm_stream", None) else False
            )

            if isinstance(results, dict) and (results.get("level", None) == 'error' or results.get("error", None)):
                yield FunctionResult({}, success=False, reason=str(results))
            else:
                yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err.value)
