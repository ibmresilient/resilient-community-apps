# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from base64 import b64decode
from logging import getLogger
from json import dumps
from mimetypes import guess_type
from io import BytesIO
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import write_file_attachment

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'base64_to_attachment'"""

    @function("soar_utils_base64_to_attachment")
    def _base64_to_attachment_function(self, event, *args, **kwargs):
        """Function: """
        try:
            log = getLogger(__name__)

            # Get the function parameters:
            # artifact_file_type:
            # "Email Attachment", "Malware Sample", "Log File", "X509 Certificate File", "Other File", etc.
            base64content = kwargs.get("soar_utils_base64content")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            file_name = kwargs.get("soar_utils_file_name")  # text
            content_type = kwargs.get("soar_utils_content_type")  # text

            content_type = content_type \
                           or guess_type(file_name or "")[0] \
                           or "application/octet-stream"

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("file_name: %s", file_name)
            log.info("content_type: %s", content_type)

            yield StatusMessage("Writing attachment...")

            datastream = BytesIO(b64decode(base64content.encode("utf-8")))

            client = self.rest_client()
            new_attachment  = write_file_attachment(client, file_name, datastream, incident_id, task_id, content_type)

            log.info(dumps(new_attachment))
            yield FunctionResult(new_attachment)
        except Exception:
            yield FunctionError()
