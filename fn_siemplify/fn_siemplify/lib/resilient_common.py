# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import base64
import logging
import re
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError
from resilient_lib import get_file_attachment, get_file_attachment_name
from cachetools import cached, LRUCache

LOG = logging.getLogger(__name__)

SIEMPLIFY_SEARCH_QUERY = "Siemplify Task Id"
SIEMPLIFY_SEARCH_REGEX = re.compile(r"{}: (\d+)".format(SIEMPLIFY_SEARCH_QUERY))

TYPES_URI = "/types"

class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, siemplify_case_id):
        """Find a Resilient incident which contains a custom field associated with a Sentinel
             incident

        Args:
            siemplify_case_id ([str]): [sentinel incident id]

        Returns:
            [dict]: [API results of the first incident found]
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{0}'.format(None),
                        'method': 'equals',
                        'value': "{}".format(siemplify_case_id)
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
            sentinel_incident ([dict]): [Sentinel incident data]
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

    def create_incident_comment(self, incident_id, sentinel_comment_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            comment = "<b>{} ({}):</b><br>{}".format(None, sentinel_comment_id, note)

            note_json = {
                'format': 'html',
                'content': comment
            }
            payload = {'text': note_json}

            return self.rest_client.post(uri=uri, payload=payload)

        except Exception as err:
            raise IntegrationError(err)

    def get_incident(self, incident_id):
        return self._get_incident_info(incident_id, None)

    def get_incident_attachment(self, incident_id, artifact_id=None, task_id=None, attachment_id=None, return_base64=True):
        file_content = get_file_attachment(self.rest_client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        if return_base64:
            file_content = b_to_s(base64.b64encode(file_content))

        file_name = get_file_attachment_name(self.rest_client, incident_id, artifact_id=artifact_id, task_id=task_id, attachment_id=attachment_id)
        return file_name, file_content

    def get_incident_artifacts(self, incident_id):
        return self._get_incident_info(incident_id, "artifacts")

    def get_incident_comments(self, incident_id):
        return self._get_incident_info(incident_id, "comments")

    def get_incident_attachments(self, incident_id):
        attachments =  self._get_incident_info(incident_id, "attachments")
        for attachment in attachments:
            _, attachment['content'] = self.get_incident_attachment(incident_id, attachment_id=attachment['id'])

        return attachments

    def get_incident_task(self, task_id):
        uri = "/tasks/{}".format(task_id)
        task_info = self.rest_client.get(uri=uri)

        # get the comments and search for the siemlify task id
        siemplify_task_id = self.get_siemplify_task_id(task_id)

        return task_info, siemplify_task_id

    def get_siemplify_task_id(self, task_id):
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

        # {"root_comments":[{"type":"task","id":253,"parent_id":null,"user_id":3,"user_fname":"Resilient","user_lname":"Sysadmin","text":{"format":"html","content":"<div class=\"rte\"><div>Siemplify Task Id: 15</div></div>"},"create_date":1639517174903,"modify_date":1639517174903,"children":[],"mentioned_users":[],"is_deleted":false,"modify_user":{"id":3,"first_name":"Resilient","last_name":"Sysadmin"},"actions":[{"id":155,"name":"Siemplify Sync Comment","enabled":true}],"inc_id":2298,"inc_name":"sync27","task_id":1552,"task_name":"my task","task_custom":true,"task_members":null,"task_at_id":null,"inc_owner":3,"user_name":"Resilient Sysadmin","modify_principal":{"id":3,"type":"user","name":"a@example.com","display_name":"Resilient Sysadmin"},"comment_perms":{"update":true,"delete":true}},{"type":"task","id":254,"parent_id":null,"user_id":3,"user_fname":"Resilient","user_lname":"Sysadmin","text":{"format":"html","content":"<div class=\"rte\"><div>Siemplify Task Id: 15</div></div>"},"create_date":1639517207320,"modify_date":1639517207320,"children":[],"mentioned_users":[],"is_deleted":false,"modify_user":{"id":3,"first_name":"Resilient","last_name":"Sysadmin"},"actions":[{"id":155,"name":"Siemplify Sync Comment","enabled":true}],"inc_id":2298,"inc_name":"sync27","task_id":1552,"task_name":"my task","task_custom":true,"task_members":null,"task_at_id":null,"inc_owner":3,"user_name":"Resilient Sysadmin","modify_principal":{"id":3,"type":"user","name":"a@example.com","display_name":"Resilient Sysadmin"},"comment_perms":{"update":true,"delete":true}}],"incident_comment_match_ids":[],"task_comment_match_ids":[253,254],"max_results_exceeded":false}"
        # get the siemplify_task_id if it exists
        search_results = self.rest_client.post(uri=uri, payload=query)
        LOG.debug(search_results)

        siemplify_task_id = None
        if search_results.get("root_comments"):
            m = SIEMPLIFY_SEARCH_REGEX.search(search_results["root_comments"][0]["text"])
            if m:
                siemplify_task_id = m.group(1)

        return siemplify_task_id

    def lookup_artifact_type(self, artifact_type):
        types = self.get_artifact_types()
        if artifact_type in types:
            return types[artifact_type]
        return None

    def get_artifact_types(self):
        type_info = self._get_types("artifact")

        # create a lookup table based on artifact id
        return { type['value']: type['label'] for type in type_info['fields']['type']['values'] }

    @cached(cache=LRUCache(maxsize=100))
    def _get_types(self, res_type):
        uri = "/".join([TYPES_URI, res_type])
        return self.rest_client.get(uri)

    def _get_incident_info(self, incident_id, child_uri):
        try:
            uri = u'/incidents/{0}'.format(incident_id)
            if child_uri:
                uri = "/".join([uri, child_uri])

            response = self.rest_client.get(uri=uri)
            return response

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
        new_comments = [comment for comment in sentinel_comments if not None in comment['properties']['message']]

        # filter out the comments already sync'd
        if soar_comment_list:
            new_comments = [comment for comment in new_comments \
                if not any([comment['name'] in already_syncd for already_syncd in soar_comment_list])]

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
    try:
        return bytes(value, 'utf-8')
    except:
        return value

def b_to_s(value):
    """[binary to string]"""
    try:
        return value.decode()
    except:
        return value
