# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Create an issue in Jira from IBM Resilient"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_jira.util.helper import CONFIG_DATA_SECTION, validate_app_configs, build_url_to_resilient, prepend_text, get_jira_client, to_markdown

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):

    """Component that implements Resilient function 'jirs_open_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.res_params = opts.get("resilient", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self.res_params = opts.get("resilient", {})

    @function("jira_open_issue")
    def _jira_open_issue_function(self, event, *args, **kwargs):
        """Function: Create a jira issue."""
        try:
            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get + validate the app.config parameters:
            log.info("Validating app configs")
            app_configs = validate_app_configs(self.options)

            # Get + validate the function parameters:
            log.info("Validating function inputs")
            fn_inputs = validate_fields(["incident_id", "jira_fields"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            # Get JIRA fields from input
            jira_fields = json.loads(fn_inputs.get("jira_fields"))

            yield StatusMessage("Connecting to JIRA")

            jira_client = get_jira_client(app_configs, rc)

            # Build the URL to Resilient
            resilient_url = build_url_to_resilient(self.res_params.get("host"), self.res_params.get("port"), fn_inputs.get("incident_id"), fn_inputs.get("task_id"))

            jira_fields["description"] = prepend_text("IBM Resilient Link: {0}".format(resilient_url), to_markdown(jira_fields.get("description", "")))

            yield StatusMessage("Creating JIRA issue")

            jira_issue = jira_client.create_issue(fields=jira_fields)

            results_contents = {
                "issue_url": jira_issue.permalink(),
                "issue_url_internal": jira_issue.self,
                "issue_key": jira_issue.key,
                "issue": jira_issue.raw
            }

            yield StatusMessage(u"JIRA issue {0} created".format(jira_issue.key))

            results = rp.done(success=True, content=results_contents)

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            yield FunctionError(err)
