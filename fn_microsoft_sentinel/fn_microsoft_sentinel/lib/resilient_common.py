# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import calendar
import json
import logging
import os
import resilient
import time
from fn_microsoft_sentinel.lib.sentinel_common import get_sentinel_incident_id
from resilient import SimpleHTTPException
from resilient_circuits.template_functions import render_json, environment
from resilient_lib import IntegrationError
from cachetools import cached, LRUCache

SENTINEL_INC_ID_FIELD = "sentinel_incident_id"

DEFAULT_INCIDENT_CREATION_TEMPLATE = "data/incident_creation_template.jinja"
DEFAULT_INCIDENT_UPDATE_TEMPLATE = "data/incident_update_template.jinja"
DEFAULT_INCIDENT_CLOSE_TEMPLATE = "data/incident_close_template.jinja"

COMMENT_ID_DATATABLE = "sentinel_comment_ids"
COMMENT_FIELD_SENTINEL_ID = "comment_id"
COMMENT_FIELD_RESILIENT_ID = "resilient_comment_id"


LOG = logging.getLogger(__name__)

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_substitute": jinja_resilient_substitute
            })
        env.filters.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_substitute": jinja_resilient_substitute
            })

    def find_incident(self, sentinel_incident_id):
        """Find a Resilient incident which contains a custom field associated with a sentinal
             incident 

        Args:
            sentinel_incident_id ([str]): [sentinel incident id]

        Returns:
            [dict]: [API results of the first incident found]
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{0}'.format(SENTINEL_INC_ID_FIELD),
                        'method': 'equals',
                        'value': "{}".format(sentinel_incident_id)
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

    def create_incident(self, sentinel_incident, incident_creation_template):
        """
        Create a new Resilient incident by rendering a jinja2 template
        :param sentinel_incident: sentinel_incident (json object)
        
        :return: Resilient incident
        """
        sentinel_incident_id = get_sentinel_incident_id(sentinel_incident)
        try:
            template_data = get_template(incident_creation_template,
                                        DEFAULT_INCIDENT_CREATION_TEMPLATE)

            # Render the template.
            new_incident_payload = render_json(template_data, sentinel_incident)
            LOG.debug(new_incident_payload)

            # Post incident to Resilient
            incident = self.rest_client.post("/incidents", new_incident_payload)

            return incident
        except Exception as err:
            raise IntegrationError(str(err))


    def close_incident(self, incident, sentinel_incident, incident_close_template):
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
            template_data = get_template(incident_close_template, DEFAULT_INCIDENT_CLOSE_TEMPLATE)

            incident_payload = render_json(template_data, sentinel_incident)
            LOG.debug(incident_payload)

            # Render the template.
            incident_id = incident.get('id')
            result = self._patch_incident(incident_id, incident_payload)

            return result

        except Exception as err:
            raise IntegrationError(err)

    def update_incident(self, incident, sentinel_incident, update_template):
        """
        Update a Resilient incident by rendering a jinja2 template
        :param sentinel_incident: Secureworks CTP sentinel_incident (json object)
        :return: Resilient incident
        """

        try:
            template_data = get_template(update_template, DEFAULT_INCIDENT_UPDATE_TEMPLATE)
            incident_payload = render_json(template_data, sentinel_incident)
            LOG.debug(incident_payload)

            # Render the template.
            incident_id = incident.get('id')
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
            return result if result else {}

        except Exception as err:
            raise IntegrationError(err)

    def _create_incident_comment(self, incident_id, note):
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

def get_template(specified_template, default_template):
    """return the contents of a jinja template, either from the default or a customer specified
          custom path

    Args:
        specified_template ([str]): [customer specified template path]
        default_template ([str]): [default template location]

    Returns:
        [str]: [contents of template]
    """
    template_file_path = specified_template
    if template_file_path:
        if not (os.path.exists(template_file_path) and os.path.isfile(template_file_path)):
            LOG.error(u"Template file: %s doesn't exist, using default template",
                      template_file_path)
            template_file_path = None

    if not template_file_path:
        # using default template
        template_file_path = os.path.join(
                                os.path.dirname(os.path.realpath(__file__)),
                                default_template
                             )

    LOG.info(u"Incident creation template file: %s", template_file_path)
    with open(template_file_path, "r") as definition:
        return definition.read()

def jinja_resilient_datetimeformat(value, date_format="%Y-%m-%dT%H:%M:%S"):
    """custom jinja filter to convert UTC dates to epoch format

    Args:
        value ([str]): [jinja provided field value]
        date_format (str, optional): [conversion format]. Defaults to "%Y-%m-%dT%H:%M:%S".

    Returns:
        [int]: [epoch value of datetime, in milliseconds]
    """
    if not value:
        return value

    utc_time = time.strptime(value[:value.rfind('.')], date_format)
    return calendar.timegm(utc_time)*1000

def jinja_resilient_substitute(value, json_str):
    """jinja custom filter to replace values based on a lookup dictionary

    Args:
        value ([str]): [original value]
        json_str ([str]): [string encoded json lookup values]

    Returns:
        [str]: [replacement value or original value if no replacement found]
    """
    replace_dict = json.loads(json_str)
    if value in replace_dict:
        return replace_dict[value]

    return value
