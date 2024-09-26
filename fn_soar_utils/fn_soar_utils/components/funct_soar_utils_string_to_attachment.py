# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from io import BytesIO
from os import path
from resilient_circuits import (
    ResilientComponent,
    function,
    handler,
    StatusMessage,
    FunctionResult,
    FunctionError
)
from resilient_lib import write_file_attachment, validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'soar_utils_string_to_attachment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_soar_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_soar_utils", {})

    @function("soar_utils_string_to_attachment")
    def _soar_utils_string_to_attachment_function(self, event, *args, **kwargs):
        """Function: Create a new attachment from an inputted string"""

        try:
            validate_fields(["soar_utils_string_to_convert_to_attachment", "attachment_name", "incident_id"], kwargs)
            # Check required inputs are defined
            string_to_convert_to_attachment = kwargs.get(
                "soar_utils_string_to_convert_to_attachment"
            )  # text (required)

            attachment_name = kwargs.get("attachment_name")  # text (required)

            ext = path.splitext(attachment_name)[1]
            if not ext or ext == ".":
                # Attachment has no extension specified or ends with '.'.
                a_ext = "txt" if attachment_name.endswith(".") else ".txt"
                attachment_name = f"{attachment_name}{a_ext}"

            incident_id = kwargs.get("incident_id")  # number (required)

            # Optional Inputs
            task_id = kwargs.get("task_id")  # number (optional)

            # Define local variables
            content_type = "text/plain"
            new_attachment = None

            # Initialize logging
            log = getLogger(__name__)
            log.info(
                "string_to_convert_to_attachment: %s", string_to_convert_to_attachment
            )
            log.info("attachment_name: %s", attachment_name)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)

            yield StatusMessage("Writing attachment...")
            datastream = BytesIO(string_to_convert_to_attachment.encode("utf-8"))

            #  Access SOAR API
            client = self.rest_client()

            # POST the new attachment
            new_attachment = write_file_attachment(
                client,
                attachment_name,
                datastream,
                incident_id,
                task_id=task_id,
                content_type=content_type,
            )

            # If the attachment succeeded in POSTing, print message, return result
            if new_attachment:
                yield StatusMessage(f"Attachment {new_attachment['id']} was created")
                yield FunctionResult({"attachment_id": new_attachment["id"]})

            # Else, raise an error
            else:
                yield StatusMessage("Failed creating attachment")
                raise FunctionError("Failed creating attachment")

        except Exception:
            yield FunctionError()
