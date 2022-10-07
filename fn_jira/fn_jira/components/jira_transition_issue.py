# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Transition a Jira issue from IBM SOAR"""

from json import loads
from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import validate_fields, RequestsCommon
from fn_jira.util.helper import PACKAGE_NAME, validate_app_configs, get_jira_client, to_markdown, get_server_settings

FN_NAME = "jira_transition_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_transition_issue"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Transition a jira issue."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get configuration for Panorama server specified
        options = get_server_settings(self.opts, getattr(fn_inputs, "jira_label", None))

        rc = RequestsCommon(self.opts, options)

        # Get + validate the app.config parameters:
        self.LOG.info("Validating app configs")
        app_configs = validate_app_configs(options)

        # Get + validate the function parameters:
        self.LOG.info("Validating function app_configs")
        app_configs = validate_fields(["jira_issue_id", "jira_transition_id"], fn_inputs)
        self.LOG.info(f"Validated function app_configs: {app_configs}")

        jira_fields = loads(app_configs.get("jira_fields"))
        jira_comment = to_markdown(app_configs.get("jira_comment"))

        yield self.status_message("Connecting to JIRA")

        jira_client = get_jira_client(app_configs, rc)

        yield self.status_message(u"Transition issue {0} to '{1}'".format(app_configs.get("jira_issue_id"), app_configs.get("jira_transition_id")))

        jira_client.transition_issue(
            issue=app_configs.get("jira_issue_id"),
            transition=app_configs.get("jira_transition_id"),
            comment=jira_comment,
            fields=jira_fields)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult("Done")
