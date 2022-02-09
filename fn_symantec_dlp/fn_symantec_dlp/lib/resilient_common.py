# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import base64
import logging
import re
import traceback
from ast import literal_eval
from fn_symantec_dlp.lib.dlp_common import SYMANTEC_DLP_HEADER, SOAR_HEADER
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError
from resilient_lib import get_file_attachment, get_file_attachment_name

LOG = logging.getLogger(__name__)

SYMANTEC_DLP_INCIDENT_ID = "sdlp_incident_id"

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def get_open_symantec_dlp_incidents(self):
        # find all open incidents which are associated with Symantec DLP incidents
        query = {
            "filters": [{
                "conditions": [
                    {
                        "field_name": "properties.{0}".format(SYMANTEC_DLP_INCIDENT_ID),
                        "method": "has_a_value"
                    },
                    {
                        "field_name": "plan_status",
                        "method": "equals",
                        "value": "A"
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }

        incidents = self._query_incidents(query)
        # return dictionary of incidents indexed by symantec DLP incident id.
        return { incident['properties'][SYMANTEC_DLP_INCIDENT_ID]: incident['id'] for incident in incidents }


    def find_incident(self, sdlp_incident_id):
        """Find a Resilient incident which contains a custom field associated with a siemplify
             incident
        Args:
            siemplify_case_id ([str]): [siemplify incident id]
        Returns:
            [dict]: [API results of the first incident found]
        """
        query = {
            "filters": [{
                "conditions": [
                    {
                        "field_name": "properties.{0}".format(SYMANTEC_DLP_INCIDENT_ID),
                        "method": "equals",
                        "value": sdlp_incident_id
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }
        r_incidents = self._query_incidents(query)

        return r_incidents[0] if r_incidents else None

    def _query_incidents(self, query):
        # run a query to find incident(s) which match the query string
        query_uri = "/incidents/query?return_level=normal"

        try:
            return self.rest_client.post(query_uri, query)
        except SimpleHTTPException as err:
            LOG.error(str(err))
            LOG.error(query)
            return None

    def create_incident(self, incident_payload):
        """
        Create a new Resilient incident by rendering a jinja2 template
        :param incident_payload: fields to use for creating a SOAR incident (json object)
        :return: Resilient incident
        """
        try:
            # Post incident to Resilient
            incident = self.rest_client.post("/incidents", incident_payload)
            return incident
        except Exception as err:
            raise IntegrationError(str(err))

    def close_incident(self, incident_id, incident_payload):
        """Close an incident, applying a template for the required and optional fields needed
              during the close process
        Args:
            incident_id ([int]): [SOAR incident id]
            incident_payload ([dict]): [incident data to update for close]
        Raises:
            IntegrationError: [catch any errors]
        Returns:
            [dict]: [returned Resilient data]
        """

        try:
            result = self._patch_incident(incident_id, incident_payload)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def update_incident(self, incident_id, incident_payload):
        """
        Update a Resilient incident by rendering a jinja2 template
        :param incident_payload: inciednt fields to update (json object)
        :return: Resilient incident
        """

        try:
            result = self._patch_incident(incident_id, incident_payload)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def _patch_incident(self, incident_id, incident_payload):
        """ _patch_incident will update an incident with the specified json payload.
        :param incident_id: incident ID of incident to be updated.
        ;param incident_payload: incident fields to be updated.
        :return:
        """
        try:
            # Update incident
            incident_url = "/incidents/{0}".format(incident_id)
            incident = self.rest_client.get(incident_url)
            patch = Patch(incident)

            # Iterate over payload dict.
            for name, _ in incident_payload.items():
                if name == 'properties':
                    for field_name, field_value in incident_payload['properties'].items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = incident_payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client.patch(incident_url, patch)
            result = self._chk_status(patch_result)
            # add back the incident id
            result['id'] = incident_id
            return result

        except Exception as err:
            raise IntegrationError(err)

    def create_incident_comment(self, incident_id, sdlp_comment_id, note):
        """
        Add a comment to the specified SOAR Incident by ID
        :param incident_id:  SOAR Incident ID
        :param sdlp_comment_id: Symantec DLP comment id (or None)
        :param note: Content to be added as note
        :return: Response from SOAR
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            comment = "<b>{} ({}):</b><br>{}".format(SYMANTEC_DLP_HEADER, sdlp_comment_id, note)

            note_json = {
                'format': 'html',
                'content': comment
            }
            payload = {'text': note_json}

            return self.rest_client.post(uri=uri, payload=payload)

        except Exception as err:
            raise IntegrationError(err)

    def get_incident(self, incident_id):
        # get an SOAR incident based on the incident id
        incident = self._get_incident_info(incident_id, None)
        incident['incident_types'] = self.convert_incident_types(incident['incident_type_ids'])
        return incident

    def get_incident_types(self):
        # get all incident_type_id labels
        return self.get_types("incident", "incident_type_ids")

    def convert_incident_types(self, incident_type_ids):
        # Convert a SOAR incident type to a Symantec DLP type
        if not incident_type_ids:
            return incident_type_ids

        incident_type_lookup = self.get_incident_types()

        return [incident_type_lookup[incident_type] for incident_type in incident_type_ids \
            if incident_type in incident_type_lookup]

    def get_incident_attachment(self, incident_id, artifact_id=None, task_id=None, attachment_id=None, return_base64=True):
        # get contents of a file attachment
        file_content = get_file_attachment(self.rest_client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        if return_base64:
            file_content = b_to_s(base64.b64encode(file_content))

        file_name = get_file_attachment_name(self.rest_client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        return file_name, file_content

    def get_incident_artifacts(self, incident_id):
        # get all incident artifacts
        return self._get_incident_info(incident_id, "artifacts")

    def get_incident_comments(self, incident_id):
        # get all incident comments
        return self._get_incident_info(incident_id, "comments")

    def get_incident_attachments(self, incident_id):
        # get all incident attachments
        attachments =  self._get_incident_info(incident_id, "attachments")
        for attachment in attachments:
            _, attachment['content'] = self.get_incident_attachment(incident_id, attachment_id=attachment['id'])

        return attachments

    def _get_incident_info(self, incident_id, child_uri):
        # API call for a given incident and it's child objects: tasks, notes, attachments, etc.
        try:
            uri = u'/incidents/{0}'.format(incident_id)
            if child_uri:
                uri = "/".join([uri, child_uri])

            response = self.rest_client.get(uri=uri)
            return response

        except Exception as err:
            raise IntegrationError(err)