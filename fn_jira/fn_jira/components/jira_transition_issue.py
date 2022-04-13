# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Transition a Jira issue from IBM SOAR"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_jira.util.helper import CONFIG_DATA_SECTION, validate_app_configs, get_jira_client, to_markdown

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'jira_transition_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("jira_transition_issue")
    def _jira_transition_issue_function(self, event, *args, **kwargs):
        """Function: Transition a jira issue."""
        try:
            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get + validate the app.config parameters:
            log.info("Validating app configs")
            app_configs = validate_app_configs(self.options)

            # Get + validate the function parameters:
            log.info("Validating function inputs")
            fn_inputs = validate_fields(["jira_issue_id", "jira_transition_id"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            jira_fields = json.loads(fn_inputs.get("jira_fields"))
            jira_comment = to_markdown(fn_inputs.get("jira_comment"))

            yield StatusMessage("Connecting to JIRA")

            jira_client = get_jira_client(app_configs, rc)

            yield StatusMessage(u"Transition issue {0} to '{1}'".format(fn_inputs.get("jira_issue_id"), fn_inputs.get("jira_transition_id")))

            jira_client.transition_issue(
                issue=fn_inputs.get("jira_issue_id"),
                transition=fn_inputs.get("jira_transition_id"),
                comment=jira_comment,
                fields=jira_fields)

            results = rp.done(success=True, content="Done")

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)
