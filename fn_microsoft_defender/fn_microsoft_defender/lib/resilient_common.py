# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import logging
import resilient
from resilient import SimpleHTTPException
from resilient_lib import IntegrationError
from cachetools import cached, LRUCache

DEFENDER_ALERT_ID_FIELD = "defender_alert_id"

COMMENT_ID_DATATABLE = "sentinel_comment_ids"
COMMENT_FIELD_SENTINEL_ID = "comment_id"
COMMENT_FIELD_RESILIENT_ID = "resilient_comment_id"

LOG = logging.getLogger(__name__)

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, defender_alert_id):
        """Find a Resilient incident which contains a custom field associated with a Defender
             alert
        Args:
            defender_alert_id ([str]): [defender alert id]
        Returns:
            [dict]: [API results of the first incident found]
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{0}'.format(DEFENDER_ALERT_ID_FIELD),
                        'method': 'equals',
                        'value': "{}".format(defender_alert_id)
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

    def create_incident_comment(self, incident_id, sentinel_comment_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            note_json = {
                'format': 'html',
                'content': note
            }
            payload = {'text': note_json}

            comment_response = self.rest_client.post(uri=uri, payload=payload)
            if comment_response:
                # create a datatable reference to this comment
                self._update_comment_datatable(incident_id, sentinel_comment_id)

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

    def filter_resilient_comments(self, incident_id, sentinel_comments):
        """
            need to avoid creating same comments over and over
              this logic will read a datatable of sentinel incident comment_ids
              and remove those comments which have already sync
            WARNING: This logic will not update an existing comment (which may have been updated)
        Args:
            incident_id ([str]): [resilient incident id]
            sentinel_comments ([list]): [description]
        Returns:
            new_comments ([list])
        """
        new_comments = []
        # get incident comments and filter out those already sync'd
        incident_comments = self.get_comment_datatable(incident_id)

        if incident_comments:
            for comment in sentinel_comments:
                if comment['name'] not in incident_comments:
                    new_comments.append(comment)
        else:
            new_comments = sentinel_comments

        LOG.info("Filtered new comments %s out of %s", len(new_comments), len(sentinel_comments))

        return new_comments


    def get_comment_datatable(self, incident_id, sort_by=COMMENT_FIELD_SENTINEL_ID):
        """read contents of datatable containing references of sentinel incident comments
             already sync'd
        Args:
            incident_id ([str]): [resilient incident id]
            sort_by ([str], optional): [field of datatable to build the dictionary of results].
                    Defaults to COMMENT_FIELD_SENTINEL_ID.
        Raises:
            IntegrationError: [description]
        Returns:
            [dict]: [dictionary of datatable results]
        """
        try:
            # get table information of sentinel to resilient comment ids
            uri = u'/incidents/{0}/table_data/{1}'.format(incident_id, COMMENT_ID_DATATABLE)
            comment_response = self.rest_client.get(uri=uri)
            # get type information of datatable
            table_lookup = self._get_comment_datatable_fields()
            LOG.debug(table_lookup)

            response = {}

            # convert datatable IDs to api names
            for row in comment_response['rows']:
                for cell, cell_data in row['cells'].items():
                    if cell in table_lookup:
                        if table_lookup[cell] == sort_by:
                            key = cell_data.get('value')
                        else:
                            value = cell_data.get('value')
                if 'key' in locals() and key:
                    response[key] = value

            return response
        except Exception as err:
            raise IntegrationError(err)

    def _update_comment_datatable(self, incident_id, sentinel_comment_id,\
                                  datatable_name=COMMENT_ID_DATATABLE,\
                                  field_name=COMMENT_FIELD_SENTINEL_ID):
        try:
            # get table information of sentinel to resilient comment ids
            uri = u'/incidents/{0}/table_data/{1}/row_data'.format(incident_id,
                                                          datatable_name)
            payload = {
                "cells": {
                    field_name: { "value": sentinel_comment_id }
                }
            }

            comment_response = self.rest_client.post(uri, payload)
        except Exception as err:
            raise IntegrationError(err)

    @cached(cache=LRUCache(maxsize=100))
    def _get_comment_datatable_fields(self):
        """get the datatable field information
        Raises:
            IntegrationError: [description]
        Returns:
            [dict]: [data definition of datatable]
        """
        try:
            uri = u'/types/{0}/fields'.format(COMMENT_ID_DATATABLE)

            comment_response = self.rest_client.get(uri=uri)
            table_lookup = { str(field['id']): field['name'] for field in comment_response }

            return table_lookup

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