# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields, readable_datetime

FN_NAME = "mcafee_epo_update_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_update_issue'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update an issue on the ePO server. McAfee user requires permission to edit the issue for this function.
        Inputs:
            -   fn_inputs.mcafee_epo_issue_id
            -   fn_inputs.mcafee_epo_issue_properties
            -   fn_inputs.mcafee_epo_issue_priority
            -   fn_inputs.mcafee_epo_ticket_server_name
            -   fn_inputs.mcafee_epo_issue_resolution
            -   fn_inputs.mcafee_epo_issue_due
            -   fn_inputs.mcafee_epo_ticket_id
            -   fn_inputs.mcafee_epo_issue_severity
            -   fn_inputs.mcafee_epo_issue_state
            -   fn_inputs.mcafee_epo_issue_name
            -   fn_inputs.mcafee_epo_issue_assignee
            -   fn_inputs.mcafee_epo_issue_description
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate function parameters:
        validate_fields(["mcafee_epo_issue_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "issue.updateIssue",
            {"id": fn_inputs.mcafee_epo_issue_id,
            "name": getattr(fn_inputs, "mcafee_epo_issue_name", None),
            "desc": getattr(fn_inputs, "mcafee_epo_issue_description", None),
            "type": fn_inputs.mcafee_epo_issue_type.upper() if hasattr(fn_inputs, "mcafee_epo_issue_type") and fn_inputs.mcafee_epo_issue_type else None,
            "state": fn_inputs.mcafee_epo_issue_state.upper() if hasattr(fn_inputs, "mcafee_epo_issue_state") and fn_inputs.mcafee_epo_issue_state else None,
            "priority": fn_inputs.mcafee_epo_issue_priority.upper() if hasattr(fn_inputs, "mcafee_epo_issue_priority") and fn_inputs.mcafee_epo_issue_priority else None,
            "severity": fn_inputs.mcafee_epo_issue_severity.upper() if hasattr(fn_inputs, "mcafee_epo_issue_severity") and fn_inputs.mcafee_epo_issue_severity else None,
            "resolution": fn_inputs.mcafee_epo_issue_resolution.upper().replace(" ","") if hasattr(fn_inputs, "mcafee_epo_issue_resolution") and fn_inputs.mcafee_epo_issue_resolution else None,
            "due": readable_datetime(fn_inputs.mcafee_epo_issue_due, rtn_format='%Y-%m-%d %H:%M:%S') if hasattr(fn_inputs, "mcafee_epo_issue_due") and fn_inputs.mcafee_epo_issue_due else None,
            "assigneeName": getattr(fn_inputs, "mcafee_epo_issue_assignee", None),
            "ticketServerName": getattr(fn_inputs, "mcafee_epo_ticket_server_name", None),
            "ticketId": getattr(fn_inputs, "mcafee_epo_ticket_id", None),
            "properties": getattr(fn_inputs, "mcafee_epo_issue_properties", None)}
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
