# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import tempfile
import os
import json
import base64
import mimetypes
from io import BytesIO
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import write_file_attachment

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'base64_to_attachment'"""

    @function("utilities_base64_to_attachment")
    def _base64_to_attachment_function(self, event, *args, **kwargs):
        """Function: """
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            # artifact_file_type:
            # "Email Attachment", "Malware Sample", "Log File", "X509 Certificate File", "Other File", etc.
            base64content = kwargs.get("base64content")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            file_name = kwargs.get("file_name")  # text
            content_type = kwargs.get("content_type")  # text

            content_type = content_type \
                           or mimetypes.guess_type(file_name or "")[0] \
                           or "application/octet-stream"

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("file_name: %s", file_name)
            log.info("content_type: %s", content_type)


            yield StatusMessage("Writing attachment...")

            datastream = BytesIO(base64.b64decode(base64content))
            client = self.rest_client()
            new_attachment  = write_file_attachment(client, file_name, datastream, incident_id, task_id, content_type)


            log.info(json.dumps(new_attachment))
            yield FunctionResult(new_attachment)
        except Exception:
            yield FunctionError()
