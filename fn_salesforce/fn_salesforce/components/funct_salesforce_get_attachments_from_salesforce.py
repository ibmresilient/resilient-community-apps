# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from io import BytesIO
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, write_file_attachment
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "salesforce_get_attachments_from_salesforce"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_get_attachments_from_salesforce'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get attachments associated with a Salesforce case and add the attachments in the corresponding SOAR case.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.task_id
            -   fn_inputs.salesforce_case_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "salesforce_case_id"], fn_inputs)

        app_common = AppCommon(self.PACKAGE_NAME, self.options)

        attachment_name_list = []
        content_versions = app_common.get_content_version_ids(fn_inputs.salesforce_case_id)
        for content_version in content_versions:
            response = app_common.get_content_version(content_version)
            version_data_uri = response.get("VersionData", None)
            datastream = BytesIO(app_common.get_content_version_data(version_data_uri))
            if datastream:

                #datastream = BytesIO(response.content)
                attachment_name = app_common.build_attachment_name(response)

                # Get the rest client so we can add the attachment to the incident.
                rest_client = self.rest_client()

                # Write the file as attachment: failures will raise an exception
                write_file_attachment(rest_client, attachment_name, datastream,
                                      fn_inputs.incident_id, None)
                attachment_name_list.append(attachment_name)
        results = {"salesforce_attachments": attachment_name_list}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

