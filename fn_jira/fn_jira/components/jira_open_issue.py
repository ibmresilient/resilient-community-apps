# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Create an issue in Jira from IBM SOAR"""

from json import loads
from fn_jira.util.helper import (DEFAULT_JIRA_DT_NAME, PACKAGE_NAME,
                                 get_server_settings, to_markdown)
from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import build_incident_url, validate_fields
from fn_jira.lib.app_common import AppCommon

FN_NAME = "jira_open_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_open_issue"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a jira issue.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.task_id
            -   fn_inputs.jira_fields
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
        validate_fields(["incident_id", "jira_fields"], fn_inputs)

        # Get JIRA fields from inputs
        jira_fields = loads(fn_inputs.jira_fields)

        # Build the URL to SOAR
        resilient_url = build_incident_url(self.rest_client().base_url, fn_inputs.incident_id)
        task_id = getattr(fn_inputs, "task_id", None)
        if task_id:
            resilient_url = f"{resilient_url}?task_id={task_id}"

        jira_fields["description"] = u"{}\n\n{}".format(f"IBM SOAR Link: {resilient_url}", to_markdown(jira_fields.get("description", ""))).strip()

        yield self.status_message("Creating JIRA issue")

        jira_issue = jira_client.create_issue(fields=jira_fields)

        results_contents = {
            "issue_url": jira_issue.permalink(),
            "issue_url_internal": jira_issue.self,
            "issue_key": jira_issue.key,
            "issue": jira_issue.raw,
            "jira_dt_name": options.get("jira_dt_name", DEFAULT_JIRA_DT_NAME)
        }

        yield self.status_message(f"JIRA issue {jira_issue.key} created")
        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results_contents)
