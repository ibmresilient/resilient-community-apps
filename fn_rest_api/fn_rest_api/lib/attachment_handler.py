
import json, copy, logging
from resilient_lib import (get_file_attachment, write_to_tmp_file)

LOG = logging.getLogger()

URL_ARTIFACTS = "/incidents/{}/artifacts/"
URL_ARTIFACT_INFORMATION = "/incidents/{}/artifacts/query_paged"
URL_ATTACHMENT_INFORMATION = "/incidents/{}/attachments/query?exclude_mismatch=true&include_tasks=true"

URL_FIND_ARTIFACT_DIRECT = "/incidents/{}/artifacts/{}"
URL_FIND_ATTACHMENT_DIRECT = "/incidents/{}/attachments/{}"

BOTH = "both"
TEMP_FILE_DIR = "/data"
ARTIFACTS = "artifacts"
ATTACHMENTS = "attachments"
INCIDENT_ID = "incident_id"
ARTIFACT_ID = "artifact_id"
ATTACHMENT_ID = "attachment_id"
ATTACHMENT_FORM_FIELD = "attachment_form_field_name"


QUERY_SEARCH_PARAM_TEMPLATE = {
    "attachments" : {
        "method"     : "equals",
        "field_name" : "name",
        "value"      : None },

    "artifacts" : {
        "method"     : "contains",
        "field_name" : "value",
        "value"      : None }}

QUERY_CONDITION_TEMPLATE =  {
    "attachments" : {
        "conditions"  : [],
        "logic_type"  : "any"},

    "artifacts" : {
        "conditions"  : []}}

ARTIFACT_PAYLOAD_TEMPLATE = {
    "filters" : []}


class AttachmentHandler:
    """
    This class acts as an abstraction layer for handling interactions with a REST API, specifically
    tailored to operations involving attachments and artifacts related to incident management.
    """
    def __init__(self, rest_client):
        self.rest_client = rest_client


    def find_artifact_by_id(self, artifact_id:int):
        LOG.info("finding artifact by id")
        response = self.rest_client.get(URL_FIND_ARTIFACT_DIRECT.format(self.incident_id, artifact_id))
        _required_info = response.get("attachment")
        if _required_info:
            _required_info["attachment_id"] = _required_info["id"]
            _required_info["id"] = response.get("id")
            LOG.debug(f"artifacts found : {json.dumps(_required_info, indent=2)}")
            return _required_info
        raise ValueError("Artifact does not contain any attachment!")


    def find_attachments_by_id(self, attachment_id:int):
        LOG.info("finding attachment by id")
        return self.rest_client.get(URL_FIND_ATTACHMENT_DIRECT.format(self.incident_id, attachment_id))


    def _format_files_for_request(self, form_field_name, file_metadata):
        LOG.info("formatting attachment in the required format")
        return (form_field_name , (file_metadata.get("name"), file_metadata.get("file_contents"), file_metadata.get("content_type")))


    def _get_file_contents(self, file_metadata:dict, object_type:str, write_to_phy_location:bool=False):

        _id = file_metadata.get("id")
        if object_type == ARTIFACTS:
            _file_contents = get_file_attachment(
                self.rest_client,
                incident_id=self.incident_id,
                artifact_id=_id)

        elif object_type == ATTACHMENTS:
            _file_contents = get_file_attachment(
                self.rest_client,
                incident_id=self.incident_id,
                attachment_id=_id)

        if write_to_phy_location:
            _file_path, _ = write_to_tmp_file(
                _file_contents,
                tmp_file_name=file_metadata.get("name"))
            file_metadata["file_path_on_device"] = _file_path

        file_metadata["file_contents"] = _file_contents

        return file_metadata


    def add_files(self,
        incident_id:int=None,
        artifact_id:int=None,
        attachment_id:int=None,
        attachment_form_field_name:str=None):

            if incident_id:
                self.incident_id, files = incident_id, []

                if artifact_id:
                    _artifacts_metadata = self.find_artifact_by_id(artifact_id=artifact_id)
                    _artifacts_metadata = self._get_file_contents(_artifacts_metadata, object_type=ARTIFACTS, write_to_phy_location=True)
                    files.append(self._format_files_for_request(attachment_form_field_name, _artifacts_metadata))

                if attachment_id:
                    _attachments_metadata = self.find_attachments_by_id(attachment_id=attachment_id)
                    _attachments_metadata = self._get_file_contents(_attachments_metadata, object_type=ATTACHMENTS, write_to_phy_location=True)
                    files.append(self._format_files_for_request(attachment_form_field_name, _attachments_metadata))

                return files
