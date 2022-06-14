# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
from retry import retry
from urllib.parse import urljoin
from resilient import SimpleHTTPException
from resilient_lib import IntegrationError
from cachetools import cached, LRUCache

LOG = logging.getLogger(__name__)

APPS_URI = "/apps/"
FUNCTIONS_URI = "/functions/"
TYPES_URI = "/types/"
IMPORTS_URI = "/configurations/imports"
PLAYBOOKS_URI = "/playbooks/"

class SOARCommon():
    """ common methods for accessing IBM SOAR apps and functions, etc. """
    def __init__(self, rest_client):
        self.rest_client = rest_client

    def import_res(self, export_res):
        result = self.rest_client.post(IMPORTS_URI, export_res)
        import_id = result["id"]  # if this isn't here and the response code is 200 OK, something went really wrong

        if result["status"] == "PENDING":
            result["status"] = "ACCEPTED"      # Have to confirm changes
            uri =  "/".join([IMPORTS_URI, str(import_id)])
            self.rest_client.put(uri, result)
            return True
        else:
            return False

    @retry(SimpleHTTPException, tries=3, delay=2, backoff=20)
    def get_playbook_by_api_name(self, playbook_api_name):
        url = urljoin(PLAYBOOKS_URI, playbook_api_name)
        return self.rest_client.get(url)

    def get_function_info_by_app(self, app_name):
        app = self._get_app(app_name)
        funct_api_names = []
        if app:
            # get the function display names with their uuids
            funct_display_name = {item['display_name']: item['uuid'] \
                                    for item in app['current_installation'].get("items", []) if item['customization_type'] == "function"}
            # get the function api names with their uuids
            funct_api_names = [
                    {
                        "function_name": custom['name'],
                        "function_uuid": funct_display_name.get(custom['display_name'])
                    } for custom in app['current_installation'].get('customizations', []) if custom['type'] == "function"
                ]

            # match up the function inputs fields with each function
            for funct in funct_api_names:
                funct["fields"] = self._get_function_fields(funct['function_name'])

        LOG.debug(funct_api_names)
        return funct_api_names

    def _get_app(self, app_name):
        url = urljoin(APPS_URI, app_name)
        try:
            return self.rest_client.get(url)
        except SimpleHTTPException as err:
            LOG.warning(str(err))
            return None

    def get_function_info(self, function_name):
        function_info = self._get_function(function_name)

        result = None
        if function_info:
            # get all the fields for this function. This list does not contain api_names
            field_uuids = [field['content'] for field in function_info['view_items'] if field['field_type'] == '__function']
            # get all fields for all functions, by uuid
            function_input_fields = self._get_type_info_indexed("__function", "uuid")
            result = {
                        "function_name": function_name,
                        "function_display_name": function_info['display_name'],
                        "function_uuid": function_info['uuid'],
                        "fields": [field_info \
                            for field_uuid, field_info in function_input_fields.items() \
                                if field_uuid in field_uuids]
                     }

        return result

    def _get_function(self, function_name):
        url = urljoin(FUNCTIONS_URI, function_name)
        try:
            return self.rest_client.get(url)
        except SimpleHTTPException as err:
            LOG.warning(str(err))
            return None

    def _get_function_fields(self, function_name):
        function_info = self._get_function(function_name)

        # the function should be found, but need to check
        function_fields = []
        if function_info:
            # get all the fields for this function. This list does not contain api_names
            field_uuids = [field['content'] for field in function_info['view_items'] if field['field_type'] == '__function']
            # now get the api name from these uuids
            function_input_fields = self._get_type_info_indexed("__function", "uuid")
            function_fields = [field_info \
                                for field_uuid, field_info in function_input_fields.items() \
                                    if field_uuid in field_uuids]

        return function_fields

    def _get_type_info_indexed(self, object_type, index_field):
        """ get a specified SOAR field set of values, based on their ID (ex. status, incident_type_ids) """
        type_info = self._get_types(object_type)

        # create a lookup table based on the index_field
        return {field_info[index_field]: field_info for field, field_info in type_info['fields'].items()}

    @cached(cache=LRUCache(maxsize=100))
    def _get_types(self, res_type):
        """ cached API call to get types information for a given type: case, artifact, etc. """
        uri = urljoin(TYPES_URI, res_type)
        return self.rest_client.get(uri)

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
    """ string to bytes """
    try:
        return bytes(value, 'utf-8')
    except Exception:
        return value

def b_to_s(value):
    """ bytes to string """
    try:
        return value.decode()
    except Exception:
        return value
