# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Add a comment to a Jira Issue"""

from fn_jira.util import helper
from re import findall, subn
from requests import get
from resilient.co3base import BasicHTTPException
from resilient_circuits import (AppFunctionComponent, FunctionError,
                                FunctionResult, app_function)
from resilient_lib import IntegrationError, RequestsCommon, validate_fields

FN_NAME = "jira_create_comment"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_create_comment"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, helper.PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create a jira comment."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get configuration for Panorama server specified
        options = helper.get_server_settings(self.opts, getattr(fn_inputs, "jira_label", None))

        rc = RequestsCommon(self.opts, options)

        # Get + validate the app.config parameters:
        app_configs = helper.validate_app_configs(options)

        # if this note is coming from a task
        if getattr(fn_inputs, helper.TASK_ID_FUNCT_INPUT_NAME):

            # check if the task is synced to Jira already using datatable row with associated task_id
            # if so, fn_inputs will be updated with the jira id and jira url
            if not helper.validate_task_id_for_jira_issue_id(self.rest_client(), app_configs,
                    getattr(fn_inputs, helper.INCIDENT_ID_FUNCT_INPUT_NAME), getattr(fn_inputs, helper.TASK_ID_FUNCT_INPUT_NAME), fn_inputs):
                # gracefully exit if task_id wasn't found in datatable -- i.e. task isn't liked to Jira yet
                self.LOG.debug(f"Skipped function {FN_NAME} for task note because task was not synced to Jira.")

                yield FunctionResult({}, success=False)
                return
            else:
                self.LOG.info("Found Jira ID %s for task %s in datatable", getattr(fn_inputs, helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME, ""), getattr(fn_inputs, helper.JIRA_ISSUE_LINK, ""))

        # Get + validate the function parameters:
        self.LOG.info("Validating function inputs")
        inputs = validate_fields([helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME, 
            helper.JIRA_COMMENT_FUNCT_INPUT_NAME, helper.INCIDENT_ID_FUNCT_INPUT_NAME], fn_inputs)

        self.LOG.info(f"Validated function inputs: {inputs}")

        JIRA_ISSUE_ID_FUNCT_INPUT_NAME = inputs.get(helper.JIRA_ISSUE_ID_FUNCT_INPUT_NAME)

        # first extract any image info and get the (src, alt) images tuple
        # also replaces the images with the appropriate Jira style markdown for including them
        html = inputs.get("jira_comment")
        # extract src values and alt values from SOAR's image tags
        # ex: <img src='https://ibm.com/some_pic.jpg' alt='some_pic.jpg' />
        srcs = findall(r'<img[^>]+src="([^">]+)', html)
        alts = findall(r'<img[^>]+alt="([^">]+)', html)

        # sub in Jira image syntax for each image tag
        for alt in alts:
            html = subn(r'<img.*?>', f" !{alt}! ", html, count=1)[0]

        # zip together the src and alts
        imgs = tuple(zip(srcs, alts))

        jira_comment = helper.to_markdown(html)

        if not jira_comment or not jira_comment.strip():
            raise FunctionError("Note is empty after rich text is removed")

        yield self.status_message("Connecting to JIRA")

        jira_client = helper.get_jira_client(app_configs, rc)

        # loop through any linked images in the note and add them as attachments on Jira
        for src, alt in imgs:
            try:
                # Read a url image to a filestream
                if src.startswith("http"):
                    # external resource
                    img_data = get(src, headers={"User-agent": "SOAR Apphost"}).content
                else:
                    # resource from the platform
                    img_data = self.rest_client().get(src[src.index("/rest")+len("/rest"):], is_uri_absolute=True, get_response_object=True).content

                yield self.status_message(f"Adding attachment '{alt}' to {JIRA_ISSUE_ID_FUNCT_INPUT_NAME} in JIRA")
                jira_client.add_attachment(JIRA_ISSUE_ID_FUNCT_INPUT_NAME, attachment=img_data, filename=alt)
            except BasicHTTPException as e:
                yield self.status_message(f"Attachment '{alt}' could not be loaded. Details: {e}")
            except Exception as e:
                raise IntegrationError(f"Something went wrong when posting attachment to Jira. Details: {e}")

        yield self.status_message(f"Adding comment to {JIRA_ISSUE_ID_FUNCT_INPUT_NAME} in JIRA")

        comment = jira_client.add_comment(JIRA_ISSUE_ID_FUNCT_INPUT_NAME, jira_comment)

        results = comment.raw

        # for tasks we'll return the link here:
        if inputs.get(helper.JIRA_ISSUE_LINK):
            results[helper.JIRA_ISSUE_LINK] = inputs[helper.JIRA_ISSUE_LINK]

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
