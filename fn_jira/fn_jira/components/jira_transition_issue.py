# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Transition a Jira issue from IBM SOAR"""

from json import loads

from fn_jira.util.helper import (PACKAGE_NAME, get_jira_client,
                                 get_server_settings, to_markdown,
                                 validate_app_configs)
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import RequestsCommon, validate_fields

FN_NAME = "jira_transition_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_transition_issue"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Transition a jira issue."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get configuration for Jira server specified
        options = get_server_settings(self.opts, getattr(fn_inputs, "jira_label", None))

        # Get + validate the function parameters:
        self.LOG.info("Validating function app_configs")
        inputs = validate_fields(["jira_issue_id", "jira_transition_id"], fn_inputs)
        self.LOG.info(f"Validated function inputs: {inputs}")

        jira_fields = loads(inputs.get("jira_fields"))
        jira_comment = to_markdown(inputs.get("jira_comment"))

        yield self.status_message("Connecting to JIRA")

        jira_client = get_jira_client(validate_app_configs(options), RequestsCommon(self.opts, options))

        yield self.status_message(u"Transition issue {} to '{}'".format(inputs.get("jira_issue_id"), inputs.get("jira_transition_id")))

        jira_client.transition_issue(
            issue=inputs.get("jira_issue_id"),
            transition=inputs.get("jira_transition_id"))

        jira_client.issue(inputs.get("jira_issue_id")).update(comment=jira_comment, fields=jira_fields)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult("Done")
