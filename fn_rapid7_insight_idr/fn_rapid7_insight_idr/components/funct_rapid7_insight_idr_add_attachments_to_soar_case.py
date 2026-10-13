# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.0.430

"""AppFunction implementation"""
from io import BytesIO
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, write_file_attachment
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "rapid7_insight_idr_add_attachments_to_soar_case"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rapid7_insight_idr_add_attachments_to_soar_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Manual playbook to get the attachments from a Rapid7 InsightIDR investigation and add them to the associated SOAR case.
        Inputs:
            -   fn_inputs.rapid7_insight_idr_rrn
            -   fn_inputs.rapid7_insight_idr_incident_id
        """


        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["rapid7_insight_idr_rrn", "rapid7_insight_idr_incident_id"], fn_inputs)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        response, error_msg = app_common.list_attachments(fn_inputs.rapid7_insight_idr_rrn)
        attachment_name_list = []

        # Get the rest client so we can add the attachment to the incident.
        rest_client = self.rest_client()

        error_msg_attachments = ""
        for attachment in response:
            rrn = attachment.get("rrn")
            response_attachment, error_msg_get_attachment = app_common.get_attachment(rrn)

            if response_attachment and not error_msg_get_attachment:
                datastream = BytesIO(response_attachment)
                attachment_name = app_common.build_attachment_name(attachment)

                mime_type= attachment.get("mime_type", None)

                # Write the file as attachment: failures will raise an exception
                write_file_attachment(rest_client, attachment_name, datastream,
                                      fn_inputs.rapid7_insight_idr_incident_id, None, 
                                      content_type=mime_type)
                attachment_name_list.append(attachment_name)
            else:
                # Append error message together if more than one
                error_msg_attachments = f"{error_msg_attachments}<br>{error_msg_get_attachment}"
        results = {"rapid7_insight_idr_attachments": attachment_name_list}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg or error_msg_attachments else True, 
                             reason=error_msg_attachments if error_msg_attachments else error_msg)

