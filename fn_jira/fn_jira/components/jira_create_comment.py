# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Add a comment to a Jira Issue"""

import logging

from fn_jira.util import helper
from resilient_circuits import (FunctionError, FunctionResult,
                                ResilientComponent, StatusMessage, function,
                                handler)
from resilient_lib import (MarkdownParser, RequestsCommon, ResultPayload,
                           validate_fields)

PACKAGE_NAME = helper.CONFIG_DATA_SECTION
FUNCT_NAME = "jira_create_comment"


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

    @function(FUNCT_NAME)
    def _jira_create_comment_function(self, event, *args, **kwargs):
        """Function: Create a jira comment."""
        try:
            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get + validate the app.config parameters:
            log.info("Validating app configs")
            app_configs = helper.validate_app_configs(self.options)

            # Get + validate the function parameters:
            log.info("Validating function inputs")
            fn_inputs = validate_fields([helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME, 
                helper.JIRA_COMMENT_FUNCT_INPUT_NAME, helper.INCIDENT_ID_FUNCT_INPUT_NAME], kwargs)

            # if this note is coming from a task
            if kwargs.get(helper.TASK_ID_FUNCT_INPUT_NAME):

                # check if the task is synced to Jira already using datatable row with associated task_id
                # if so, fn_inputs will be updated with the jira id and jira url
                if not helper.validate_task_id_for_jira_issue_id(self.rest_client(), app_configs,
                        kwargs.get(helper.INCIDENT_ID_FUNCT_INPUT_NAME), kwargs.get(helper.TASK_ID_FUNCT_INPUT_NAME), fn_inputs):
                    # gracefully exit if task_id wasn't found in datatable -- i.e. task isn't liked to Jira yet
                    log.debug("Skipped function %s for task note because task was not synced to Jira.", FUNCT_NAME)

                    yield FunctionResult({}, success=False)
                    return
                else:
                    log.info("Found Jira ID %s for task %s in datatable", fn_inputs[helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME], fn_inputs[helper.JIRA_ISSUE_LINK])

            log.info("Validated function inputs: %s", fn_inputs)

            # first extract any image info and get the (src, alt) images tuple
            # also replaces the images with the appropriate Jira style markdown for including them
            imgs, jira_comment = helper.extract_images(fn_inputs.get("jira_comment"))

            jira_comment = helper.to_markdown(jira_comment)

            if jira_comment is None or not jira_comment.strip():
                raise FunctionError("Note is empty after rich text is removed")

            yield StatusMessage("Connecting to JIRA")

            jira_client = helper.get_jira_client(app_configs, rc)

            # loop through any linked images in the note and add them as attachments on Jira
            for src, alt in imgs:
                img_data = helper.read_img(src)
                if img_data:
                    yield StatusMessage("Adding attachment '{0}' to {1} in JIRA".format(alt, fn_inputs.get(helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME)))
                    jira_client.add_attachment(fn_inputs.get(helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME), attachment=img_data, filename=alt)
                else:
                    yield StatusMessage("Attachment '{0}' could not be loaded".format(alt))

            yield StatusMessage("Adding comment to {0} in JIRA".format(fn_inputs.get(helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME)))

            comment = jira_client.add_comment(fn_inputs.get(helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME), jira_comment)

            results = comment.raw

            # for tasks we'll return the link here:
            if fn_inputs.get(helper.JIRA_ISSUE_LINK):
                results[helper.JIRA_ISSUE_LINK] = fn_inputs[helper.JIRA_ISSUE_LINK]

            results = rp.done(success=True, content=results)

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            yield FunctionError(err)
