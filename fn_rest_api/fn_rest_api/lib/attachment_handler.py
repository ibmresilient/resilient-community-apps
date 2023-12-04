
import json, copy, logging
from resilient_lib import (get_file_attachment, write_to_tmp_file)

LOG = logging.getLogger()

URL_FIND_ARTIFACT_DIRECT = "/incidents/{}/artifacts/{}"
URL_FIND_ATTACHMENT_DIRECT = "/incidents/{}/attachments/{}"

ID, NAME = "id", "name"
CONTENT_TYPE  = "content_type"
FILE_CONTENTS = "file_contents"
ARTIFACTS = "artifacts"
ATTACHMENTS = "attachments"
INCIDENT_ID = "incident_id"
ARTIFACT_ID = "artifact_id"
ATTACHMENT_ID = "attachment_id"
ATTACHMENT_FORM_FIELD = "attachment_form_field_name"


class AttachmentHandler:
    """
    This class acts as an abstraction layer for handling interactions with a REST API, specifically
    tailored to operations involving attachments and artifacts related to incident management.
    """
    def __init__(self, rest_client):
        self.rest_client = rest_client


    def find_artifact_by_id(self, artifact_id:int):
        """
        Find and retrieve information regarding an artifact of an incident. On finding the artifact, all
        artifact related information is removed and only the attachment information is returned.

        Example:
            .. code-block::
            {
                "type": "artifact",
                "id": 28,
                "uuid": "f9821dc2-05c4-4ce6-a2f6-6a3379b7d1e1",
                "name": "ibmLog.svg",
                "content_type": "image/svg+xml",
                "created": 1701693786896,
                "creator_id": 1,
                "size": 4121,
                "actions": [],
                "playbooks": [],
                "task_id": null,
                "task_name": null,
                "task_custom": null,
                "task_members": null,
                "task_at_id": null,
                "reconciliation_status": "matched",
                "vers": 3,
                "inc_id": 2096,
                "inc_name": "empty fries",
                "inc_owner": 1,
                "attachment_id": 475
            }

        :param artifact_id: id of the artifact that contains an attachment
        :type artifact_id: int
        :raises ValueError: if the retrieved artifact has no attachment
        :return: attachment information including id, name, content-type, size, etc..
        :rtype: dict
        """
        LOG.info("finding artifact by id")
        response = self.rest_client.get(URL_FIND_ARTIFACT_DIRECT.format(self.incident_id, artifact_id))
        _required_info = response.get("attachment")
        if _required_info:
            _required_info[ATTACHMENT_ID] = _required_info[ID]
            _required_info[ID] = response.get(ID)
            LOG.debug(f"artifacts found : {json.dumps(_required_info, indent=2)}")
            return _required_info
        raise ValueError("Artifact does not contain any attachment!")


    def find_attachments_by_id(self, attachment_id:int):
        """_summary_
        Find and retrieve information regarding an attachment of an incident.

        Example:
            .. code-block::
            {
                "type": "attachment",
                "id": 28,
                "uuid": "f9821dc2-05c4-4ce6-a2f6-6a3379b7d1e1",
                "name": "ibmLog.svg",
                "content_type": "image/svg+xml",
                "created": 1701693786896,
                "creator_id": 1,
                "size": 4121,
                "actions": [],
                "playbooks": [],
                "task_id": null,
                "task_name": null,
                "task_custom": null,
                "task_members": null,
                "task_at_id": null,
                "reconciliation_status": "matched",
                "vers": 3,
                "inc_id": 2096,
                "inc_name": "empty fries",
                "inc_owner": 1,
                "attachment_id": 475
            }

        :param artifact_id: id of the attachment to be sent with the request
        :type artifact_id: int
        :return: attachment information including id, name, content-type, size, etc..
        :rtype: dict
        """
        LOG.info("finding attachment by id")
        return self.rest_client.get(URL_FIND_ATTACHMENT_DIRECT.format(self.incident_id, attachment_id))


    def _format_files_for_request(self, form_field_name, file_metadata):
        """
        Prepares an attachment to be sent as a request. The client sends the attachment as
        ``Content-Type: multipart/form-data``, meaning that the body of the request is a series
        of parts, each of which contains files that are base64 encoded. The body of the request is
        divided into multiple parts, and each part is separated by a boundary defined that is
        auto-defined by the client. Each part typically contains a `Content-Disposition` header that
        describes the `name` and `type` of the data, along with the actual data itself. While the
        `type` is automatically assigned by the application, the `name` is supposed to be provided
        by the user using the form_field_name
        
        Format:
        .. code-block::

            (content-disposition_name, (file_name (with extension), file_content, content-type))
        
        Example:

        .. code-block::

            ('file', ('ibmLog.svg', b'<svg id="Laye......', 'image/svg+xml'))
            
        :param form_field_name: Each part in multipart/form-data is expected to contain a
            content-disposition header where the disposition type is automatically set by
            the application, and a disposition name. This disposition name changes with
            regard to the endpoint that is being used and is to be set by the user.
            Default value : "file"
        :type form_field_name: str
        :param file_metadata: attachment information and it's contents. Format matches
            the output of `find_attachments_by_id` with contents.
        :type file_metadata: dict
        :return: attachment information formatted as per request requirement
        :rtype: tuple
        """
        LOG.info("formatting attachment in the required format")
        return (
            form_field_name,
            (file_metadata.get(NAME), file_metadata.get(FILE_CONTENTS), file_metadata.get(CONTENT_TYPE)))


    def _get_file_contents(self, file_metadata:dict, object_type:str, write_to_phy_location:bool=False):
        """
        Download the contents of the attachment from soar. The function also has the ability to write the
        file to a physical location if required. This can then be later referenced if directly in the request
        later. The contents retrieved from soar is also stored within the metadata.

        :param file_metadata: attachment information. Format matches the output of
            `find_attachments_by_id`.
        :type file_metadata: dict
        :param object_type: used to identify the object type that is to be retrieved.
        :type object_type: str. Supported values : `artifacts` or `attachments`
        :param write_to_phy_location: Downloads the contents and recreates the file
            on the machine, defaults to False
        :type write_to_phy_location: bool, optional
        :return: _description_
        :rtype: _type_
        """
        _id = file_metadata.get(ID)
        if object_type == ARTIFACTS:
            _file_contents = get_file_attachment(
            LOG.info("Downloading artifact's attachment data")
                self.rest_client,
                incident_id=self.incident_id,
                artifact_id=_id)
        elif object_type == ATTACHMENTS:
            LOG.info("Downloading attachment data")
            _file_contents = get_file_attachment(
                self.rest_client,
                incident_id=self.incident_id,
                attachment_id=_id)

        if write_to_phy_location:
            LOG.info("Writing files to device")
            _file_path, _ = write_to_tmp_file(
                _file_contents,
                tmp_file_name=file_metadata.get(NAME))
            file_metadata["file_path_on_device"] = _file_path
        file_metadata[FILE_CONTENTS] = _file_contents
        return file_metadata


    def add_files(self, incident_id:int=None, artifact_id:int=None,
        attachment_id:int=None, attachment_form_field_name:str=None):

        if incident_id:
            self.incident_id, files = incident_id, []

            if artifact_id:
                _artifacts_metadata = self.find_artifact_by_id(artifact_id=artifact_id)
                _artifacts_metadata = self._get_file_contents(_artifacts_metadata, object_type=ARTIFACTS)
                files.append(self._format_files_for_request(attachment_form_field_name, _artifacts_metadata))

            if attachment_id:
                _attachments_metadata = self.find_attachments_by_id(attachment_id=attachment_id)
                _attachments_metadata = self._get_file_contents(_attachments_metadata, object_type=ATTACHMENTS)
                files.append(self._format_files_for_request(attachment_form_field_name, _attachments_metadata))

            return files
