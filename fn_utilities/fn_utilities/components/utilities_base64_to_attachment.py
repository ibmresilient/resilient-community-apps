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
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


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
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                try:
                    temp_file.write(base64.b64decode(base64content))
                    temp_file.close()
                    # Create a new artifact
                    client = self.rest_client()
                    if task_id:
                        attachment_uri = "/tasks/{}/attachments".format(task_id)
                    else:
                        attachment_uri = "/incidents/{}/attachments".format(incident_id)
                    new_attachment = client.post_attachment(attachment_uri,
                                                            temp_file.name,
                                                            filename=file_name,
                                                            mimetype=content_type)
                finally:
                    os.unlink(temp_file.name)

            # Produce a FunctionResult with the return value
            if isinstance(new_attachment, list):
                new_attachment = new_attachment[0]
            log.info(json.dumps(new_attachment))
            yield FunctionResult(new_attachment)
        except Exception:
            yield FunctionError()
