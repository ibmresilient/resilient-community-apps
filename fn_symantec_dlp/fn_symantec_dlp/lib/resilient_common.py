# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
from fn_symantec_dlp.lib.constants import SYMANTEC_DLP_INCIDENT_ID, FROM_SYMANTEC_DLP_COMMENT_HDR, FROM_SOAR_COMMENT_HDR
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError

LOG = logging.getLogger(__name__)

TYPES_URI = "/types"

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client
        self.default_artifact_type_id = 16 # When uploading DLP Binaries as attachments, they will be uploaded at 'Other File'
        
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
            comment = "<b>{} ({}):</b><br>{}".format(FROM_SYMANTEC_DLP_COMMENT_HDR, sdlp_comment_id, note)

            note_json = {
                'format': 'html',
                'content': comment
            }
            payload = {'text': note_json}

            return self.rest_client.post(uri=uri, payload=payload)

        except Exception as err:
            raise IntegrationError(err)

    def get_incident_comments(self, incident_id):
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)

            comment_response = self.rest_client.get(uri=uri)
            return comment_response

        except Exception as err:
            raise IntegrationError(err)

    def filter_resilient_comments(self, soar_case_id, sdlp_comments):
        """
            need to avoid creating same comments over and over
              this logic will read all comments from an incident
              and remove those comments which have already sync

        Args:
            soar_case_id ([str]): [ SOAR case id]
            sdlp_comments ([list]): [description]
        Returns:
            new_comments ([list])
        """
        soar_comments = self.get_incident_comments(soar_case_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # filter comments with our SOAR header
        new_comments = [comment for comment in sdlp_comments if not FROM_SOAR_COMMENT_HDR in comment['text']]

        # filter out the comments already sync'd
        if soar_comment_list:
            new_comments = [comment for comment in new_comments \
                if not any([comment['id'] in already_syncd for already_syncd in soar_comment_list])]

        return new_comments

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError(u"status code failure: {0}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError(u"status code failure: {0}".format(resp.status_code))

            return resp.json()

        return {}
