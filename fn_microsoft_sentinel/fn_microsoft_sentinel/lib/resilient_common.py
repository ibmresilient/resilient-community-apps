# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from logging import getLogger
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError
from fn_microsoft_sentinel.lib.constants import FROM_SENTINEL_COMMENT_HDR, FROM_SOAR_COMMENT_HDR, SENTINEL_INCIDENT_NUMBER

LOG = getLogger(__name__)

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, sentinel_incident_id):
        """
        Find a SOAR incident which contains a custom field associated with a Sentinel incident
        :param sentinel_incident_id [str]: Sentinel incident id
        :return [dict]: API results of the first incident found
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': f'properties.{SENTINEL_INCIDENT_NUMBER}',
                        'method': 'equals',
                        'value': f"{sentinel_incident_id}"
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
        :param sentinel_incident: sentinel_incident (json object)
        :return: SOAR incident
        """
        try:
            # Post incident to SOAR
            return self.rest_client.post("/incidents", incident_payload)
        except Exception as err:
            raise IntegrationError(str(err))

    def close_incident(self, incident_id, incident_payload):
        """
        Close an incident, applying a template for the required and optional fields needed
        during the close process.
        :param incident [dict]: SOAR incident data
        :param sentinel_incident [dict]: Sentinel incident data
        :param incident_close_template [str]: path to template to apply for close operation
        :raises IntegrationError: catch any errors
        :return [dict]: returned SOAR data
        """
        try:
            return self._patch_incident(incident_id, incident_payload)
        except Exception as err:
            raise IntegrationError(err)

    def update_incident(self, incident_id, incident_payload):
        """
        Update a SOAR incident by rendering a jinja2 template
        :param sentinel_incident: Secureworks CTP sentinel_incident (json object)
        :return: SOAR incident
        """
        try:
            return self._patch_incident(incident_id, incident_payload)
        except Exception as err:
            raise IntegrationError(err)

    def _patch_incident(self, incident_id, incident_payload):
        """
        Update an incident with the specified json payload.
        :param incident_id: incident ID of incident to be updated.
        ;param incident_payload: incident fields to be updated.
        :return: Response from SOAR for debug
        """
        try:
            # Update incident
            incident_url = f"/incidents/{incident_id}"
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
            # Add back the incident id
            result['id'] = incident_id
            return result

        except Exception as err:
            raise IntegrationError(err)

    def create_incident_comment(self, incident_id, sentinel_comment_id, note):
        """
        Add a comment to the specified SOAR Incident by ID
        :param incident_id: SOAR Incident ID
        :param note: Content to be added as note
        :return: Response from SOAR for debug
        """
        try:
            uri = f'/incidents/{incident_id}/comments'
            comment = f"<b>{FROM_SENTINEL_COMMENT_HDR} ({sentinel_comment_id}):</b><br>{note}"

            note_json = {
                'format': 'html',
                'content': comment
            }
            payload = {'text': note_json}

            return self.rest_client.post(uri=uri, payload=payload)

        except Exception as err:
            raise IntegrationError(err)

    def get_incident_comments(self, incident_id):
        """
        Get the comments on a SOAR incident
        :param incident_id: SOAR Incident ID
        :return: SOAR incident comments
        """
        try:
            uri = f'/incidents/{incident_id}/comments'
            return self.rest_client.get(uri=uri)

        except Exception as err:
            raise IntegrationError(err)

    def filter_resilient_comments(self, incident_id, sentinel_comments):
        """
        Need to avoid creating same comments over and over this logic will read all comments
        from an incident and remove those comments which have already sync.
        :param incident_id [str]: SOAR incident id
        :param sentinel_comments ([list]): Comments from the sentinel incident
        :return: new_comments ([list])
        """
        soar_comments = self.get_incident_comments(incident_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # Filter comments with our SOAR header
        new_comments = [comment for comment in sentinel_comments if FROM_SOAR_COMMENT_HDR not in comment['properties']['message']]

        # Filter out the comments already sync'd
        if soar_comment_list:
            new_comments = [comment for comment in new_comments \
                if not any([comment['name'] in already_syncd for already_syncd in soar_comment_list])]

        return new_comments

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
