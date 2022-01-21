# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import base64
import logging
import re
import traceback
from ast import literal_eval
from fn_siemplify.lib.siemplify_common import SIEMPLIFY_HEADER, SOAR_HEADER
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError
from resilient_lib import get_file_attachment, get_file_attachment_name
from cachetools import cached, LRUCache

LOG = logging.getLogger(__name__)

SIEMPLIFY_SEARCH_QUERY = "Siemplify Task Id"
SIEMPLIFY_SEARCH_REGEX = re.compile(r"{}: (\d+)".format(SIEMPLIFY_SEARCH_QUERY))

SIEMPLIFY_CASE_ID = "siemplify_case_id"

TYPES_URI = "/types"

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def get_open_siemplify_incidents(self):
        # find all open incidents which are associated with Siemplify cases
        query = {
            "filters": [{
                "conditions": [
                    {
                        "field_name": "properties.{0}".format(SIEMPLIFY_CASE_ID),
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
        # return dictionary of incidents indexed by siemplify case id
        return { incident['properties'][SIEMPLIFY_CASE_ID]: incident['id'] for incident in incidents }


    def find_incident(self, siemplify_case_id):
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
                        "field_name": "properties.{0}".format(SIEMPLIFY_CASE_ID),
                        "method": "equals",
                        "value": "{}".format(siemplify_case_id)
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

    def create_incident_comment(self, incident_id, siemplify_comment_id, note):
        """
        Add a comment to the specified SOAR Incident by ID
        :param incident_id:  SOAR Incident ID
        :param siemplify_comment_id: siemplify comment id (or None)
        :param note: Content to be added as note
        :return: Response from SOAR
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            comment = "<b>{} ({}):</b><br>{}".format(SIEMPLIFY_HEADER, siemplify_comment_id, note)

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

    def convert_incident_types(self, incident_type_ids):
        # Convert a SOAR incident type to a Siemplify
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

    def get_incident_task(self, task_id):
        # get a given incident task
        uri = "/tasks/{}".format(task_id)
        task_info = self.rest_client.get(uri=uri)

        # get the comments and search for the siemlify task id
        siemplify_task_id = self.get_siemplify_task_id(task_id)

        return task_info, siemplify_task_id

    def get_siemplify_task_id(self, task_id):
        """[get the siemplify task id assiocated witha given SOAR task]

        Args:
            task_id ([int]): [SOAR task to search]

        Returns:
            [int]: [associated Siemplify task_id]
        """
        uri = "/tasks/{}/comments/query".format(task_id)
        query = {
            "conditions":
            [
                {
                    "field_name": "text",
                    "method": "contains",
                    "value": SIEMPLIFY_SEARCH_QUERY
                }
            ]
        }

        # get the siemplify_task_id if it exists
        search_results = self.rest_client.post(uri=uri, payload=query)

        siemplify_task_id = None
        if search_results.get("root_comments"):
            m = SIEMPLIFY_SEARCH_REGEX.search(search_results["root_comments"][0]["text"])
            if m:
                siemplify_task_id = m.group(1)

        return siemplify_task_id

    def lookup_artifact_type(self, artifact_type):
        # return an artifact type based on it's ID. If not found, return None
        types = self.get_artifact_types()
        if artifact_type in types:
            return types[artifact_type]
        return None

    def get_artifact_types(self):
        # get all artifact types labels
        return self.get_types("artifact", "type")

    def get_incident_types(self):
        # get all incident_type_id labels
        return self.get_types("incident", "incident_type_ids")

    def get_resolution_types(self):
        # get incident resolution_types labels
        return self.get_types("incident", "resolution_id")

    def get_types(self, obj_type, field):
        # get a specified SOAR field set of values, based on their ID (ex. status, incident_type)
        type_info = self._get_types(obj_type)

        # create a lookup table based on field name
        return { type['value']: type['label'] for type in type_info['fields'][field]['values'] }

    @cached(cache=LRUCache(maxsize=100))
    def _get_types(self, res_type):
        # cached API call to get types information for a given type: incident, artifact, etc.
        uri = "/".join([TYPES_URI, res_type])
        return self.rest_client.get(uri)

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

    def filter_resilient_comments(self, incident_id, siemplify_comments, soar_header=SOAR_HEADER, \
                                 sync_header=SIEMPLIFY_HEADER):
        """
            need to avoid creating same comments over and over
              this logic will read all comments from an incident
              and remove those comments which have already sync

        Args:
            incident_id ([str]): [resilient incident id]
            siemplify_comments ([list]): [description]
            soar_header ([str]): [title added to SOAR comment ]
            sync_header ([str]): [title of siemplify comment already sync'd]
        Returns:
            new_comments ([list])
        """
        soar_comments = self.get_incident_comments(incident_id)
        soar_comment_list = [comment['text'] for comment in soar_comments]

        # filter comments with our SOAR header
        new_comments = [comment for comment in siemplify_comments \
                            if soar_header not in comment['title']]

        # filter out the comments already sync'd
        if soar_comment_list:
            new_comments = [comment for comment in new_comments \
                if not any([comment['content'] in already_syncd for already_syncd in soar_comment_list])]

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


def s_to_b(value):
    # string to bytes
    try:
        return bytes(value, 'utf-8')
    except:
        return value

def b_to_s(value):
    # bytes to string
    """[binary to string]"""
    try:
        return value.decode()
    except:
        return value

@cached(cache=LRUCache(maxsize=100))
def eval_mapping(value, wrapper=None):
    """
    Args:
            value ([str]): [resilient incident id]
            wrapper ([str]): [values such as '[{}]' or '{{ {} }}']
        Returns:
            mapping ([list or dict]): converted data
    """
    if not value:
        return None

    try:
        if wrapper:
            value = wrapper.format(value)
        # Try converting input to a dict or array
        return literal_eval(value)

    except Exception as err:
        LOG.error(str(err))
        LOG.error(traceback.format_exc())
        LOG.error("""mapping value must be a string representation of a (partial) array or dictionary e.g. "['value1', 'value2']" or "{'key':'value'}" """)

    return None
