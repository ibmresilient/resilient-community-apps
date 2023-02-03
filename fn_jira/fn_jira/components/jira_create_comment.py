# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Add a comment to a Jira Issue"""

from re import subn, compile
from fn_jira.util import helper
from io import BytesIO
from resilient.co3base import BasicHTTPException
from resilient_circuits import AppFunctionComponent, FunctionError, FunctionResult, app_function
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "jira_create_comment"
src_pattern = compile(r'<img[^>]+src="([^">]+)')
alt_pattern = compile(r'<img[^>]+alt="([^">]+)')

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'jira_create_comment"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, helper.PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a jira comment.
        Inputs:
            -   fn_inputs.jira_label
            -   fn_inputs.task_id
            -   fn_inputs.jira_issue_id
            -   fn_inputs.jira_comment
            -   fn_inputs.incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get configuration for Jira server specified
        options = helper.get_server_settings(self.opts, getattr(fn_inputs, "jira_label", None))

        # Connect to Jira
        yield self.status_message("Connecting to JIRA")
        jira_client = helper.get_jira_client(self.opts, options)

        # Validate required parameters
        self.LOG.info("Validating function inputs")
        validate_fields(["jira_comment", "incident_id"], fn_inputs)

        self.LOG.info(f"Validated function inputs: {fn_inputs._asdict()}")

        # Get inputs
        task_id = getattr(fn_inputs, "task_id", None)
        jira_issue_id = getattr(fn_inputs, "jira_issue_id", None)
        incident_id = fn_inputs.incident_id
        url = options.get("url")

        # If this note is coming from a task
        if task_id:
            # Check if the task is synced to Jira already using datatable row with associated task_id.
            # If so, the jira id and jira url will be updated.

            # Using datatable in SOAR, grab the jira id and jira url from the correct row in the table.
            # If the table row associated with this task id doesn't exist, returns (None, None).
            jira_issue_id, jira_link = helper.get_jira_issue_id(self.rest_client(),
                                                                options.get("jira_dt_name", helper.DEFAULT_JIRA_DT_NAME),
                                                                incident_id,
                                                                task_id)

            if not jira_issue_id:
                # Gracefully exit if task_id wasn't found in datatable -- i.e. task isn't linked to Jira yet
                self.LOG.debug(f"Skipped function {FN_NAME} for task note, because task was not synced to Jira.")
                yield FunctionResult({}, success=False)
            else:
                # Success
                url = jira_link
                self.LOG.info(f"Found Jira ID {jira_issue_id} for task {url} in datatable")

        # First extract any image info and get the (src, alt) images tuple.
        # Also replaces the images with the appropriate Jira style markdown for including them.
        jira_comment = fn_inputs.jira_comment
        # Extract src values and alt values from SOAR's image tags
        # ex: <img src='https://ibm.com/some_pic.jpg' alt='some_pic.jpg' />
        srcs = src_pattern.findall(jira_comment)
        alts = alt_pattern.findall(jira_comment)

        # Sub in Jira image syntax for each image tag
        for alt in alts:
            jira_comment = subn(r'<img.*?>', f" !{alt}! ", jira_comment, count=1)[0]

        # Zip together the src and alts
        imgs = tuple(zip(srcs, alts))

        jira_comment = helper.to_markdown(jira_comment)

        if not jira_comment or not jira_comment.strip():
            raise FunctionError("Note is empty after rich text is removed")

        # Loop through any linked images in the note and add them as attachments on Jira
        for src, alt in imgs:
            try:
                # Read a url image to a filestream
                if src.lower().startswith("http"):
                    # External resource
                    img_data = self.rc.execute("GET", src, headers={"User-agent": "SOAR Apphost"}).content
                else:
                    # Resource from the platform
                    img_data = self.rest_client().get(src[src.index("/rest")+len("/rest"):], is_uri_absolute=True, get_response_object=True).content

                yield self.status_message(f"Adding attachment '{alt}' to {jira_issue_id} in JIRA")
                jira_client.add_attachment(jira_issue_id, attachment=BytesIO(img_data), filename=alt)
            except BasicHTTPException as e:
                yield self.status_message(f"Attachment '{alt}' could not be loaded. Details: {e}")
            except Exception as e:
                raise IntegrationError(f"Something went wrong when posting attachment to Jira. Details: {e}")

        yield self.status_message(f"Adding comment to {jira_issue_id} in JIRA")

        comment = jira_client.add_comment(jira_issue_id, jira_comment)

        results = comment.raw

        # For tasks we'll return the link here:
        if url:
            results["jira_url"] = url

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
