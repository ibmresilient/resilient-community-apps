# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Create an issue in Jira from IBM SOAR"""

import json
from fn_jira.util.helper import (PACKAGE_NAME, DEFAULT_JIRA_DT_NAME, get_jira_client, to_markdown,
                                 validate_app_configs, get_server_settings)
from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import RequestsCommon, validate_fields, build_incident_url, build_resilient_url

FN_NAME = "jira_open_issue"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_open_issue"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.res_params = opts.get("resilient", {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create a jira issue."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get configuration for Panorama server specified
        options = get_server_settings(self.opts, getattr(fn_inputs, "jira_label", None))

        rc = RequestsCommon(self.opts, options)

        # Get + validate the app.config parameters:
        self.LOG.info("Validating app configs")
        app_configs = validate_app_configs(options)

        # Get + validate the function parameters:
        self.LOG.info("Validating function app_configs")
        app_configs = validate_fields(["incident_id", "jira_fields"], fn_inputs)
        self.LOG.info(f"Validated function app_configs: {app_configs}")

        # Get JIRA fields from input
        jira_fields = json.loads(app_configs.get("jira_fields"))

        yield self.status_message("Connecting to JIRA")

        jira_client = get_jira_client(app_configs, rc)

        # Build the URL to SOAR
        resilient_url = build_incident_url(build_resilient_url(self.res_params.get("host"), self.res_params.get("port")), app_configs.get("incident_id"))
        task_id = app_configs.get("task_id")
        if task_id:
            resilient_url = f"{resilient_url}?task_id={task_id}"

        jira_fields["description"] = u"{0}\n\n{1}".format(f"IBM SOAR Link: {resilient_url}", to_markdown(jira_fields.get("description", ""))).strip()

        yield self.status_message("Creating JIRA issue")

        jira_issue = jira_client.create_issue(fields=jira_fields)

        results_contents = {
            "issue_url": jira_issue.permalink(),
            "issue_url_internal": jira_issue.self,
            "issue_key": jira_issue.key,
            "issue": jira_issue.raw,
            "jira_dt_name": app_configs.get("jira_dt_name", DEFAULT_JIRA_DT_NAME)
        }

        yield self.status_message(u"JIRA issue {0} created".format(jira_issue.key))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results_contents)
