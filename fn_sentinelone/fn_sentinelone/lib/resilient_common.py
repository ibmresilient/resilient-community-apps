# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
import resilient
from resilient import SimpleHTTPException
from resilient_lib import IntegrationError
from fn_sentinelone.lib.constants import FROM_SENTINELONE_COMMENT_HDR, FROM_SOAR_COMMENT_HDR, SENTINELONE_THREAT_ID

LOG = logging.getLogger(__name__)

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, sentinelone_threat_id):
        """Find a Resilient incident which contains a custom field associated with a SentinelOne
             threat

        Args:
            sentinelone_threat_id ([str]): [sentinelone threat id]

        Returns:
            [dict]: [API results of the first incident found]
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{0}'.format(SENTINELONE_THREAT_ID),
                        'method': 'equals',
                        'value': "{}".format(sentinelone_threat_id)
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
        :param sentinelone_incident: sentinelone_incident (json object)

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
            sentinelone_incident ([dict]): [SentinelOne incident data]
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
        :param sentinelone_incident: sentinelone_incident (json object)
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

    def create_incident_comment(self, incident_id, sentinelone_comment_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            comment = "<b>{} ({}):</b><br>{}".format(FROM_SENTINELONE_COMMENT_HDR, sentinelone_comment_id, note)

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

    def filter_resilient_comments(self, incident_id, sentinel_comments):
        """
            need to avoid creating same comments over and over
              this logic will read all comments from an incident
              and remove those comments which have already sync

        Args:
            incident_id ([str]): [resilient incident id]
            sentinel_comments ([list]): [description]
        Returns:
            new_comments ([list])
        """
        soar_comments = self.get_incident_comments(incident_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # filter comments with our SOAR header
        new_comments = [comment for comment in sentinel_comments if not FROM_SOAR_COMMENT_HDR in comment['text']]

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
