# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields, readable_datetime

FN_NAME = "mcafee_epo_create_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_create_issue'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create an issue on the ePO server. McAfee user requires permission to edit issues for this function.
        Inputs:
            -   fn_inputs.mcafee_epo_issue_properties
            -   fn_inputs.mcafee_epo_issue_priority
            -   fn_inputs.mcafee_epo_ticket_server_name
            -   fn_inputs.mcafee_epo_issue_resolution
            -   fn_inputs.mcafee_epo_issue_type
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
        validate_fields(["mcafee_epo_issue_name", "mcafee_epo_issue_description"], fn_inputs)

        due = getattr(fn_inputs, "mcafee_epo_issue_due", None)
        if due:
            due = readable_datetime(due, rtn_format='%Y-%m-%d %H:%M:%S')

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "issue.createIssue",
            {"name": fn_inputs.mcafee_epo_issue_name,
            "desc": fn_inputs.mcafee_epo_issue_description,
            "type": fn_inputs.mcafee_epo_issue_type.upper() if hasattr(fn_inputs, "mcafee_epo_issue_type") and fn_inputs.mcafee_epo_issue_type else "BASIC",
            "state": fn_inputs.mcafee_epo_issue_state.upper() if hasattr(fn_inputs, "mcafee_epo_issue_state") and fn_inputs.mcafee_epo_issue_state else "UNKNOWN",
            "priority": fn_inputs.mcafee_epo_issue_priority.upper() if hasattr(fn_inputs, "mcafee_epo_issue_priority") and fn_inputs.mcafee_epo_issue_priority else "UNKNOWN",
            "severity": fn_inputs.mcafee_epo_issue_severity.upper() if hasattr(fn_inputs, "mcafee_epo_issue_severity") and fn_inputs.mcafee_epo_issue_severity else "UNKNOWN",
            "resolution": fn_inputs.mcafee_epo_issue_resolution.upper().replace(" ","") if hasattr(fn_inputs, "mcafee_epo_issue_resolution") and fn_inputs.mcafee_epo_issue_resolution else "NONE",
            "due": due,
            "assigneeName": getattr(fn_inputs, "mcafee_epo_issue_assignee", None),
            "ticketServerName": getattr(fn_inputs, "mcafee_epo_ticket_server_name", None),
            "ticketId": getattr(fn_inputs, "mcafee_epo_ticket_id", None),
            "properties": getattr(fn_inputs, "mcafee_epo_issue_properties", None)}
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
