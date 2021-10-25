# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import logging
import resilient
from resilient import SimpleHTTPException
from resilient_lib import IntegrationError

DEFENDER_INCIDENT_ID = "defender_incident_id"

COMMENT_ID_DATATABLE = "sentinel_comment_ids"
COMMENT_FIELD_SENTINEL_ID = "comment_id"
COMMENT_FIELD_RESILIENT_ID = "resilient_comment_id"

LOG = logging.getLogger(__name__)

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, defender_incident_id):
        """Find a Resilient incident which contains a custom field associated with a Defender
             alert
        Args:
            defender_incident_id ([str]): [defender incident id]
        Returns:
            [dict]: [API results of the first incident found]
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{0}'.format(DEFENDER_INCIDENT_ID),
                        'method': 'equals',
                        'value': defender_incident_id
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }
        LOG.debug(query)

        try:
            r_incidents = self.rest_client.post(query_uri, query)
        except SimpleHTTPException as err:
            LOG.error(str(err))
            r_incidents = None

        return r_incidents[0] if r_incidents else None

    def create_incident(self, incident_payload):
        """
        Create a new Resilient incident by rendering a jinja2 template
        :param sentinel_incident: sentinel_incident (json object)
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
            incident ([dict]): [Resilient incident data]
            sentinel_incident ([dict]): [Senintel incident data]
            incident_close_template ([str]): [path to template to apply for close operation]
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
        :param sentinel_incident: Secureworks CTP sentinel_incident (json object)
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
            patch = resilient.Patch(incident)

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

    def create_incident_comment(self, incident_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            note_json = {
                'format': 'text',
                'content': note
            }
            payload = {'text': note_json}

            comment_response = self.rest_client.post(uri=uri, payload=payload)

            return comment_response

        except Exception as err:
            raise IntegrationError(err)

    def get_incident_comments(self, incident_id):
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)

            comment_response = self.rest_client.get(uri=uri)
            return comment_response

        except Exception as err:
            raise IntegrationError(err)

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
