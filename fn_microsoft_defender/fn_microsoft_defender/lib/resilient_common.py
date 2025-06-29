# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

from logging import getLogger
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError

DEFENDER_INCIDENT_ID = "defender_incident_id"
LOG = getLogger(__name__)
IBM_SOAR_LABEL = "IBM SOAR"

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, defender_incident_id):
        """Find a SOAR incident which contains a custom field associated with a Defender alert
        Args:
            defender_incident_id ([str]): Defender incident id
        Returns:
            [dict]: API results of the first incident found
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': f'properties.{DEFENDER_INCIDENT_ID}',
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
        Create a new SOAR incident by rendering a jinja2 template
        :param defender_incident: defender_incident (json object)
        :return: SOAR incident
        """
        try:
            # Post incident to SOAR
            return self.rest_client.post("/incidents", incident_payload)
        except Exception as err:
            raise IntegrationError(f"Failed to create SOAR incident with reason: {str(err)}")

    def update_incident(self, incident_id, incident_payload):
        """
        Update a SOAR incident by rendering a jinja2 template
        :param incident_id: Incident to modify
        :param incident_payload: [dict] of patched fields
        :return: SOAR incident updated
        """
        try:
            return self._patch_incident(incident_id, incident_payload)
        except Exception as err:
            raise IntegrationError(f"Failed to update SOAR incident with reason: {str(err)}")

    def _patch_incident(self, incident_id, incident_payload):
        """ _patch_incident will update an incident with the specified json payload.
        :param incident_id: Incident ID of incident to be updated.
        ;param incident_payload: Incident fields to be updated.
        :return:
        """
        try:
            # Update incident
            incident_url = f"/incidents/{incident_id}"
            incident = self.rest_client.get(incident_url)
            patch = Patch(incident)

            # Iterate over payload dict.
            for name, _ in incident_payload.items():
                if name == 'properties':
                    for field_name, field_value in incident_payload.get('properties', {}).items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = incident_payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client.patch(incident_url, patch)
            result = self._chk_status(patch_result)
            # Add back the incident id
            result['id'] = incident_id
            return result

        except Exception as err:
            raise IntegrationError(f"Failed to patch SOAR incident with reason: {str(err)}")

    def create_incident_comment(self, incident_id, note):
        """
        Add a comment to the specified SOAR Incident by ID
        :param incident_id: SOAR Incident ID
        :param note: Content to be added as note
        :return: Response from SOAR for debug
        """
        try:
            return self.rest_client.post(
                uri=f'/incidents/{incident_id}/comments',
                payload={
                    'text': {
                        'format': 'text',
                        'content': note
                    }
                }
            )

        except Exception as err:
            raise IntegrationError(err)

    def get_incident_comments(self, incident_id):
        try:
            return self.rest_client.get(uri=f'/incidents/{incident_id}/comments')
        except Exception as err:
            raise IntegrationError(err)

    def _chk_status(self, resp, rc=200):
        """
        Check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError(f"status code failure: {resp.status_code}")
            elif resp.status_code != rc:
                raise IntegrationError(f"status code failure: {resp.status_code}")

            return resp.json()

        return {}
