# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Transition a Jira issue from IBM SOAR"""

from json import loads
from fn_jira.util.helper import (PACKAGE_NAME,
                                 get_server_settings, to_markdown)
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields, IntegrationError
from fn_jira.lib.app_common import AppCommon

FN_NAME = "jira_transition_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_transition_issue"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Transition a jira issue.
        Inputs:
            -   fn_inputs.jira_issue_id
            -   fn_inputs.jira_transition_id
            -   fn_inputs.jira_fields
            -   fn_inputs.jira_comment
            -   fn_inputs.jira_label
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get configuration for Jira server specified
        options = get_server_settings(self.opts, getattr(fn_inputs, "jira_label", None))

        # Connect to Jira
        yield self.status_message("Connecting to JIRA")
        jira_client = AppCommon(self.opts, options).get_jira_client()

        # Get + validate the function parameters:
        self.LOG.info("Validating function inputs")
        validate_fields(["jira_issue_id", "jira_transition_id"], fn_inputs)
        self.LOG.info(f"Validated function inputs: {fn_inputs._asdict()}")

        jira_fields = loads(getattr(fn_inputs, "jira_fields", None))
        jira_comment = to_markdown(getattr(fn_inputs, "jira_comment", None))
        jira_issue_id = fn_inputs.jira_issue_id
        jira_transition_id = fn_inputs.jira_transition_id

        yield self.status_message(f"Transition issue {jira_issue_id} to '{jira_transition_id}'")

        try:
            # Transition Jira issue and update fields
            jira_client.transition_issue(issue=jira_issue_id, transition=jira_transition_id, fields=jira_fields)
            # Add comment to Jira issue
            jira_client.issue(jira_issue_id).update(comment=jira_comment)
        except Exception as err:
            if err.status_code == 400:
                # Update fields of the Jira issue
                jira_client.issue(jira_issue_id).update(comment=jira_comment, fields=jira_fields)
                # Transition Jira Issue
                jira_client.transition_issue(issue=jira_issue_id, transition=jira_transition_id)
            else:
                raise IntegrationError(str(err))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult("Done")
