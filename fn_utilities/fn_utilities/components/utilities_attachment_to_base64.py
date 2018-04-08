# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import base64
import json
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'attachment_base64"""

    @function("utilities_attachment_to_base64")
    def _attachment_to_base64_function(self, event, *args, **kwargs):
        """Function: Produce base64 content of a file attachment."""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            if incident_id is None and task_id is None:
                raise FunctionError("Error: incident_id or task_id must be specified.")
            if attachment_id is None:
                raise FunctionError("Error: attachment_id must be specified.")

            yield StatusMessage("Reading attachment...")
            if task_id:
                metadata_uri = "/tasks/{}/attachments/{}".format(task_id, attachment_id)
                data_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
            else:
                metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
                data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)

            client = self.rest_client()
            metadata = client.get(metadata_uri)
            data = client.get_content(data_uri)

            results = {
                "filename": metadata["name"],
                "content_type": metadata["content_type"],
                "size": metadata["size"],
                "created": metadata["created"],
                "content": base64.b64encode(data)
            }

            # Produce a FunctionResult with the return value
            log.debug(json.dumps(results, indent=2))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
