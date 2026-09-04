# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from logging import getLogger
from tempfile import NamedTemporaryFile
from os import unlink
from json import dumps
from base64 import b64encode
from mimetypes import guess_type
from fn_soar_utils.util.soar_utils_common import s_to_b
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'base64_to_artifact' """

    @function("soar_utils_base64_to_artifact")
    def _base64_to_artifact_function(self, event, *args, **kwargs):
        """Function: """
        try:
            log = getLogger(__name__)

            # Get the function parameters:
            # artifact_file_type:
            # "Email Attachment", "Malware Sample", "Log File", "X509 Certificate File", "Other File", etc.
            base64content = kwargs.get("soar_utils_base64content")  # text
            incident_id = kwargs.get("incident_id")  # number
            artifact_file_type = self.get_select_param(kwargs.get("soar_utils_artifact_file_type")) or "Malware Sample"
            file_name = kwargs.get("soar_utils_file_name")  # text
            content_type = kwargs.get("soar_utils_content_type")  # text
            description = self.get_textarea_param(kwargs.get("soar_utils_description"))  # textarea

            content_type = content_type \
                           or guess_type(file_name or "")[0] \
                           or "application/octet-stream"

            log.info("incident_id: %s", incident_id)
            log.info("artifact_file_type: %s", artifact_file_type)
            log.info("file_name: %s", file_name)
            log.info("content_type: %s", content_type)
            log.info("description: %s", description)

            # To post a file artifact, we need to specify the type by id
            # So, look up the id of the type name
            client = self.rest_client()
            artifact_type_id = 16  # Other File (as default)
            for value in client.cached_get("/types/artifact/fields/type")["values"]:
                if artifact_file_type == value["label"]:
                    artifact_type_id = value["value"]
                    break

            yield StatusMessage("Writing artifact...")
            with NamedTemporaryFile(delete=False) as temp_file:
                try:
                    temp_file.write(b64encode(s_to_b(base64content)))
                    temp_file.close()
                    # Create a new artifact
                    client = self.rest_client()
                    artifact_uri = f"/incidents/{incident_id}/artifacts/files"
                    new_artifact = client.post_artifact_file(artifact_uri,
                                                             artifact_type_id,
                                                             temp_file.name,
                                                             description=description,
                                                             value=file_name,
                                                             mimetype=content_type)
                finally:
                    unlink(temp_file.name)

            # Produce a FunctionResult with the return value
            if isinstance(new_artifact, list):
                new_artifact = new_artifact[0]
            log.info(dumps(new_artifact))
            yield FunctionResult(new_artifact)
        except Exception:
            yield FunctionError()
