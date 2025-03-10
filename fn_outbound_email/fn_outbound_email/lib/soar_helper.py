# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=line-too-long

from logging import getLogger
from os import path
from tempfile import mkdtemp

LOG = getLogger(__name__)

UPDATE_FIELD = "/types/actioninvocation/fields/{}"
GET_FIELD = "/types/actioninvocation/fields/{}?include_principals=true"

class SoarHelper():
    def __init__(self, rest_client):
        self.rest_client = rest_client

    def temp_attach(self, inc_id, incident_attachment_list, requested_attachments):
        """[match attachments found in an incident with the list provided by the function call and
            prep for sending email]

        Args:
            inc_id ([int]):
            incident_attachment_list ([json]): [results of api call to get all incident attachments ]
            requested_attachments ([list]): [list of attachments to include, or '*' for all]

        Returns:
            [set]: [file paths of attachments to send]
        """
        remaining_attachment_list = requested_attachments[:]
        attachment_path = []
        tempdir = mkdtemp()

        for incident_attachment in incident_attachment_list:
            file_name = incident_attachment["name"]
            if file_name in requested_attachments:
                remaining_attachment_list.remove(file_name)

                if incident_attachment['type'] == 'incident':
                    file_contents = self.rest_client.get_content(f"/incidents/{inc_id}/attachments/{incident_attachment.get('id')}/contents")
                else:
                    file_contents = self.rest_client.get_content(f"/tasks/{incident_attachment.get('task_id')}/attachments/{incident_attachment.get('id')}/contents")
                file_path = path.join(tempdir, file_name)
                with open(file_path, "wb+") as temp_file:
                    temp_file.write(file_contents)
                attachment_path.append(file_path)

        # send warnings when attachments are not found
        if remaining_attachment_list:
            LOG.warning("Unable to find the following attachments: %s", ",".join(remaining_attachment_list))

        return set(attachment_path)

    def process_attachments(self, inc_id, attachments):
        """[return a list of filepaths to include as attachments ]

        Args:
            inc_id ([int]): [incident id]
            attachments ([str]): [comma separated attachment list or '*' for all]

        Returns:
            [set]: [file paths for attachments]
        """
        if not attachments:
            return None

        incident_attachment_result = self.rest_client.post(f"/incidents/{inc_id}/attachments/query?include_tasks=true", None)
        incident_attachment_list = incident_attachment_result['attachments']
        # convert the list of requested attachments
        if attachments and attachments == "*":
            # include all incident attachments
            attachment_list = [incident_attachment.get("name") for incident_attachment in incident_attachment_list]
        else:
            attachment_list = [attach.strip() for attach in split_string(attachments)] \
                                if attachments else []

        all_attach = self.temp_attach(inc_id, incident_attachment_list, attachment_list)
        all_attach and LOG.debug("Attachments to include: %s", ",".join(all_attach))

        return all_attach

    def get_incident_data(self, mail_incident_id):
        return self.rest_client.get(f"/incidents/{mail_incident_id}?handle_format=names")

    def get_artifact_data(self, mail_incident_id):
        return self.rest_client.post(f"/incidents/{mail_incident_id}/artifacts/query_paged?include_related_incident_count=true", payload={})

    def get_note_data(self, mail_incident_id):
        return self.rest_client.post(f"/incidents/{mail_incident_id}/comments/query?include_tasks=false", payload={})

def split_string(in_string):
    return in_string.split(',') if in_string else []
