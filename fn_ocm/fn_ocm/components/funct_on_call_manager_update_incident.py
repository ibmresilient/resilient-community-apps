# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_ocm.util.helper import ocm_client, PACKAGE_NAME

FN_NAME = "on_call_manager_update_incident"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'on_call_manager_update_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Create client connection
        self.client = ocm_client(self.options.get("ocm_url", None), self.options.get("ocm_api_key_name", None), self.options.get("ocm_api_key_pass", None), self.rc)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Updates the header properties of an incident, like state, owner, and team. Set the owner to move the incident to a personal queue associated with the owner. Set the team, but not the owner, to put the incident on the team queue. Incidents with no team or owner set are on the default queue. Set the owner and/or team to a single dash(-) to clear the values and move the incident back to the default queue.
        Inputs:
            -   fn_inputs.ocm_incident_owner
            -   fn_inputs.ocm_incident_state
            -   fn_inputs.ocm_incident_resolutioncode
            -   fn_inputs.ocm_matchedpolicies
            -   fn_inputs.ocm_incident_id
            -   fn_inputs.ocm_incident_team
            -   fn_inputs.ocm_eventsummary
            -   fn_inputs.ocm_includecounts
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        try:
            # Validate required fields
            validate_fields(["ocm_incident_id"], fn_inputs)
            # Make API call to update the incident
            results = self.client.update_incident(
                incident_id=fn_inputs.ocm_incident_id,
                state=fn_inputs.ocm_incident_state if getattr(fn_inputs, "ocm_incident_state", None) else None,
                resolutionCode=fn_inputs.ocm_incident_resolutioncode if getattr(fn_inputs, "ocm_incident_resolutioncode", "") else "",
                owner=fn_inputs.ocm_incident_owner if getattr(fn_inputs, "ocm_incident_owner", None) else None,
                team=fn_inputs.ocm_incident_team if getattr(fn_inputs, "ocm_incident_team", None) else None,
                matchedPolicies=fn_inputs.ocm_matchedpolicies.replace(" ", "").split(",") if getattr(fn_inputs, "ocm_matchedpolicies", None) else None,
                eventsummary=fn_inputs.ocm_eventsummary if getattr(fn_inputs, "ocm_matchedsummary", False) else False,
                includecounts=fn_inputs.ocm_includecounts if getattr(fn_inputs, "ocm_includecounts", False) else False)
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            if isinstance(results, dict) and (results.get("level", None) == 'error' or results.get("error", None)):
                yield FunctionResult({}, success=False, reason=str(results))
            else:
                yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err.value)
