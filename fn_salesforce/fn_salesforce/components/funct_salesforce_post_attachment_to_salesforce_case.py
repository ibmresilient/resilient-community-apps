# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""
import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, get_file_attachment, get_file_attachment_name
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "salesforce_post_attachment_to_salesforce_case"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_post_attachment_to_salesforce_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Post the SOAR attachment to the corresponding Case in Salesforce.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.task_id
            -   fn_inputs.salesforce_case_id
            -   fn_inputs.artifact_id
            -   fn_inputs.attachment_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "salesforce_case_id"], fn_inputs)

        incident_id = fn_inputs.incident_id  # number
        task_id = fn_inputs.task_id  # number
        attachment_id = fn_inputs.attachment_id  # number
        artifact_id = fn_inputs.artifact_id  # number
        salesforce_case_id = fn_inputs.salesforce_case_id

        log = logging.getLogger(__name__)
        log.info("incident_id: %s", incident_id)
        log.info("task_id: %s", task_id)
        log.info("attachment_id: %s", attachment_id)
        log.info("artifact_id: %s", artifact_id)
        log.info("salesforce_case_id: %s", salesforce_case_id)

        app_common = AppCommon(self.PACKAGE_NAME, self.options)
        rest_client = self.rest_client()

        # Get the file attachment name
        attachment_name = get_file_attachment_name(res_client=rest_client,
                                                   incident_id=incident_id, 
                                                   attachment_id=attachment_id,
                                                   artifact_id=artifact_id,
                                                   task_id=task_id)
        # Get the attachment data
        encoded_string = get_file_attachment(res_client=rest_client,
                                             incident_id=incident_id, 
                                             attachment_id=attachment_id,
                                             artifact_id=artifact_id,
                                             task_id=task_id)
        
        # Post the attachment to the Salesforce case
        response = app_common.post_attachment_to_salesforce_case(attachment_name, 
                                                                 encoded_string,
                                                                 salesforce_case_id)
        results = {"salesforce_attachment": attachment_name,
                   "content_document_link": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

