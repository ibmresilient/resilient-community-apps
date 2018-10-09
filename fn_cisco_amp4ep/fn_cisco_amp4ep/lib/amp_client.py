# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Class for Resilient circuits Functions supporting REST API client for Cisco AMP for endpoints  """
import logging
import requests
from requests.auth import HTTPBasicAuth
import urlparse
import json

LOG = logging.getLogger(__name__)

class Ampclient(object):
    """
    Client class used to expose Cisco AMP for endpoints Rest API for queries
    """
    def __init__(self, options):
        """
        Class constructor
        """
        self.base_url = options.get("base_url")
        self.client_id = options.get("client_id")
        self.api_token = options.get("api_token")
        self.api_version = options.get("api_version")
        # Rest request endpoints
        self._endpoints = {
            # Computers
            "computers":                    "/"+self.api_version+"/computers/",
            "computer":                     "/"+self.api_version+"/computers/{}",
            "computer_trajectory":          "/"+self.api_version+"/computers/{}/trajectory/",
            "activity":                     "/"+self.api_version+"/computers/activity",
            "computer_move":                 "/"+self.api_version+"/computers/{}",
            # File lists
            "file_lists":                   "/"+self.api_version+"/file_lists/simple_custom_detections",
            "file_lists_files":             "/"+self.api_version+"/file_lists/{}/files",
            "file_lists_files_by_sha256":   "/"+self.api_version+"/file_lists/{}/files/{}",
            # Events
            "events":                       "/" + self.api_version + "/events/",
            "event_types":                  "/" + self.api_version + "/event_types/",
            # Groups
            "groups":                       "/" + self.api_version + "/groups/",
            "group_by_guid":                "/" + self.api_version + "/groups/{}"
        }
        self._headers = {"content-type": "application/json", "Accept": "application/json",
                        "Accept-Encoding": "application/gzip", "Authorization": "Basic FILTERED"}
        self._auth = HTTPBasicAuth(self.client_id, self.api_token)
        self._s = requests.Session()



    def _req(self, uri, method='GET', params=None, data=None, ):
        """Test if a parameter is None value or string 'None'.

        :param uri: Used to form url
        :param method: Request method, defaults to "GET"
        :param params: Parameters used by session request to form finished request
        :param data: Data body used in post requests
        :return: Response in json format

        """
        url = urlparse.urljoin(self.base_url, uri)

        if data is None:
            data = {}

        if params is None:
            params = {}

        if method == "GET":
            r = self._s.get(url, params=params, headers=self._headers, auth=self._auth)
        elif method == "POST":
            r = self._s.post(url, params=params, data=data, headers=self._headers, auth=self._auth)
        elif method == "PATCH":
            r = self._s.patch(url, params=params, data=data, headers=self._headers, auth=self._auth)
        elif method == "DELETE":
            r = self._s.delete(url, params=params, headers=self._headers, auth=self._auth)
        else:
            raise ValueError("Unsupported request method '{}'.".format(method))

        r.raise_for_status()  # If the request fails throw an error.
        return r.json()

    def get_computers(self, group_guid=None, limit=None, hostname=None, internal_ip=None, external_ip=None):
        """Get a list of computers with agents deployed on them. Use parameters to narrow the search by IP address
        ,hostname or guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param group_guid: Filter by group guid
        :param limit: Limit number of results
        :param hostname: Filter by hostname
        :param internal_ip: Filter by internal ip
        :param external_ip: Filter by external ip
        :return: Response in json format
        """
        uri = self._endpoints["computers"]
        params = {"group_guid": group_guid, "limit": limit, "hostname": hostname,
                  "internal_ip": internal_ip, "external_ip": external_ip }
        r_json = self._req(uri, params=params)
        return r_json

    def get_computer(self, connector_guid):
        """Get information about a specific computer by guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: connector_guid. Computer selection criteria
        :return Result in json format.

        """

        uri = self._endpoints["computer"].format(connector_guid)
        r_json = self._req(uri)
        return r_json

    def get_computer_trajectory(self, connector_guid, limit=None):
        """Get a list of all activities associated with a particular computer, search by guid

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: connector_guid. Computer selection criteria
        :return Result in json format.

        """

        uri = self._endpoints["computer_trajectory"].format(connector_guid)
        r_json = self._req(uri)
        return r_json

    def get_activity(self, q, limit=None, offset=None):
        """Search all computers for any events or activities associated with a file or network operation

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: group_guid.
        :return Result in json format.

        """
        uri = self._endpoints["activity"]
        params = {"q": q, "limit": limit, "offset": offset}
        r_json = self._req(uri, params=params)
        return r_json

    def get_file_lists(self, name, limit=None, offset=None):
        """
        :param name: group_guid.
        :return Result in json format.

        """
        uri = self._endpoints["file_lists"]
        params = {"name": name, "limit": limit, "offset": offset}
        r_json = self._req(uri, params=params)
        return r_json

    def get_file_list_files(self, file_list_guid, sha256, limit=None, offset=None):
        """
        :param: file_list_guid.
        :return Result in json format.

        """
        if sha256 is None:
            uri = self._endpoints["file_lists_files"].format(file_list_guid)
        else:
            uri = self._endpoints["file_lists_files_by_sha256"].format(file_list_guid, sha256)
        params = {"limit": limit, "offset": offset}
        r_json = self._req(uri, params=params)
        return r_json

    def set_file_list_files(self, file_list_guid, sha256, description):
        """

        :param: group_guid.
        :return Result in json format.

        """
        uri = self._endpoints["file_lists_files_by_sha256"].format(file_list_guid, sha256)
        data = json.dumps({"description": description})
        r_json = self._req(uri, method="POST", data=data)
        return r_json

    def delete_file_list_files(self, file_list_guid, sha256):
        """

        :param: group_guid.
        :return Result in json format.

        """
        uri = self._endpoints["file_lists_files_by_sha256"].format(file_list_guid, sha256)
        r_json = self._req(uri, method="DELETE")
        return r_json

    def get_events(self, detection_sha256=None, application_sha256=None, connector_guid=None,
                   group_guid=None, start_date=None, event_type=None, limit=None, offset=None):
        """Get a list of events. Filter by criteria set by parameter values. The criteria types
        are logically ORed.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param detection_sha256: Filter by detection sha256
        :param application_sha256: Filter by application sha256
        :param connector_guid: Filter by connector guid
        :param group_guid: Filter by group guid
        :param start_date: Filter by start date
        :param event_type: Filter by event types
        :param limit: Limit number of results
        :param offset: Results from offset
        :return: Response in json format
        """
        uri = self._endpoints["events"]
        params = {"detection_sha256": detection_sha256, "application_sha256": application_sha256,
                  "connector_guid[]": connector_guid, "group_guid[]": group_guid, "start_date": start_date,
                  "event_type[]": event_type, "limit": limit, "offset": offset }
        r_json = self._req(uri, params=params)
        return r_json

    def get_event_types(self):
        """Get list of human readable names, and short descriptions of each event by ID.

        For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :return Result in json format.

        """
        uri = self._endpoints["event_types"]
        r_json = self._req(uri)
        return r_json

    def get_groups(self, group_guid, name, limit=None):
        """Get information on groups or individual group by group_guid.

         For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: group_guid: Lookup by group_guid
        :param: name: Filter by group name
        :param limit: Limit number of results
        :return Result in json format.

        """
        if group_guid is None:
            uri = self._endpoints["groups"]
        else:
            uri = self._endpoints["group_by_guid"].format(group_guid)
        params = {"name": name , "limit": limit}
        r_json = self._req(uri, params=params)
        return r_json

    def move_computer(self, connector_guid, group_guid):
        """Get information on groups or individual group by group_guid.

         For more detail v1, see https://api-docs.amp.cisco.com/api_resources?api_host=api.amp.cisco.com&api_version=v1

        :param: connector_guid: Connector guid of computer to move.
        :param: group_guid: Group guid to move computer to.

        :return Result in json format.

        """
        uri = self._endpoints["computer_move"].format(connector_guid)
        data = json.dumps({"group_guid": group_guid})
        r_json = self._req(uri, method="PATCH", data=data)
        return r_json