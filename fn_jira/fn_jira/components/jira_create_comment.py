# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Add a comment to a Jira Issue"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, MarkdownParser, ResultPayload, RequestsCommon
from fn_jira.util.helper import CONFIG_DATA_SECTION, validate_app_configs, get_jira_client, to_markdown

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'jira_create_comment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("jira_create_comment")
    def _jira_create_comment_function(self, event, *args, **kwargs):
        """Function: Create a jira comment."""
        try:
            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get + validate the app.config parameters:
            log.info("Validating app configs")
            app_configs = validate_app_configs(self.options)

            # Get + validate the function parameters:
            log.info("Validating function inputs")
            fn_inputs = validate_fields(["jira_issue_id", "jira_comment"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            jira_comment = to_markdown(fn_inputs.get("jira_comment"))

            if jira_comment is None or not jira_comment.strip():
                raise FunctionError("Note is empty after rich text is removed")

            yield StatusMessage("Connecting to JIRA")

            jira_client = get_jira_client(app_configs, rc)

            yield StatusMessage("Adding comment to {0} in JIRA".format(fn_inputs.get("jira_issue_id")))

            comment = jira_client.add_comment(fn_inputs.get("jira_issue_id"), jira_comment)

            results = rp.done(success=True, content=comment.raw)

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            yield FunctionError(err)
