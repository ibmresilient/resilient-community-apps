# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import tempfile
import os
import json
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'attachment_move_to_artifact"""

    @function("attachment_move_to_artifact")
    def _attachment_move_to_artifact_function(self, event, *args, **kwargs):
        """Function: """
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            # artifact_file_type:
            # "Email Attachment", "Malware Sample", "Log File", "X509 Certificate File", "Other File", etc.
            incident_id = kwargs.get("incident_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_file_type = self.get_select_param(kwargs.get("artifact_file_type")) or "Malware Sample"
            description = self.get_textarea_param(kwargs.get("description"))  # textarea

            log.info("incident_id: %s", incident_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("artifact_file_type: %s", artifact_file_type)
            log.info("description: %s", description)

            if not incident_id:
                raise FunctionError("Error: Incident ID must be specified.")
            if not attachment_id:
                raise FunctionError("Error: Attachment ID must be specified.")

            # To post a file artifact, we need to specify the type by id
            # So, look up the if of the type name
            client = self.rest_client()
            artifact_type_id = 16  # Other File (as default)
            for value in client.cached_get("/types/artifact/fields/type")["values"]:
                if artifact_file_type == value["label"]:
                    artifact_type_id = value["value"]
                    break

            yield StatusMessage("Reading attachment...")
            metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
            data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)

            metadata = client.get(metadata_uri)
            data = client.get_content(data_uri)

            yield StatusMessage("Writing artifact...")
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                try:
                    temp_file.write(data)
                    temp_file.close()
                    # Create a new artifact
                    client = self.rest_client()
                    artifact_uri = "/incidents/{}/artifacts/files".format(incident_id)
                    new_artifact = client.post_artifact_file(artifact_uri,
                                                             artifact_type_id,
                                                             temp_file.name,
                                                             description=description,
                                                             value=metadata["name"],
                                                             mimetype=metadata["content_type"])
                finally:
                    os.unlink(temp_file.name)

            # Delete the file attachment
            client.delete(metadata_uri)

            # Produce a FunctionResult with the return value
            if isinstance(new_artifact, list):
                new_artifact = new_artifact[0]
            log.info(json.dumps(new_artifact))
            yield FunctionResult(new_artifact)
        except Exception:
            yield FunctionError()
