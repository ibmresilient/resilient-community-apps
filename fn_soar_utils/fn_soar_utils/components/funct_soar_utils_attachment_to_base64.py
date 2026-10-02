# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from logging import getLogger
from base64 import b64encode
from json import dumps
from resilient_circuits import (
    ResilientComponent,
    function,
    StatusMessage,
    FunctionResult,
    FunctionError,
)
from fn_soar_utils.util.soar_utils_common import b_to_s
from resilient_lib import get_file_attachment, get_file_attachment_metadata, validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'attachment_base64"""

    @function("soar_utils_attachment_to_base64")
    def _attachment_to_base64_function(self, event, *args, **kwargs):
        """Function: Produce base64 content of a file attachment."""
        try:
            validate_fields(["incident_id"], kwargs)
            log = getLogger(__name__)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("artifact_id: %s", artifact_id)

            if not attachment_id and not artifact_id:
                raise FunctionError("Error: attachment_id or artifact_id must be specified.")
            else:
                yield StatusMessage("Function inputs OK")

            yield StatusMessage("Reading attachment...")

            client = self.rest_client()
            data = get_file_attachment(client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
            metadata = get_file_attachment_metadata(client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)

            results = {
                "filename": metadata["name"],
                "content_type": metadata["content_type"],
                "size": metadata["size"],
                "created": metadata["created"],
                "content": b_to_s(b64encode(data)),
            }
            yield StatusMessage("Complete...")
            # Produce a FunctionResult with the return value
            log.debug(dumps(results, indent=2))
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
