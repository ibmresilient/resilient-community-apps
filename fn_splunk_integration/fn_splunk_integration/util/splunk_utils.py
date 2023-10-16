# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
#   Util classes for Splunk

import requests
from json import dumps
from time import sleep
from logging import getLogger
import urllib.parse as urlparse
from resilient_lib import IntegrationError

PACKAGE_NAME = "fn_splunk_integration"
LOG = getLogger(__name__)
class SplunkUtils(object):
    """ Use python requests to call Splunk REST API"""

    # Member variables
    header = ""
    session_key = ""
    SUPPORTED_THREAT_TYPE = ["ip_intel", "file_intel", "user_intel", "http_intel",
                             "email_intel", "service_intel", "process_intel",
                             "registry_intel", "certificate_intel"]

    def __init__(self, host, port, username, password, token, verify, proxies):
        self.base_url = f"https://{host}:{port}"
        self.proxies = proxies
        self.verify = verify
        if username and password:
            self.get_session_key(username, password, verify)
        elif token:
            self.header = {"Authorization": f"Bearer {token}"}

    def get_session_key(self, username, password, verify):
        """
        Get session_key from Splunk server
        :param username: Username for splunk login
        :param password: Password for splunk login
        :param verify: Verify HTTPS cert or not
        :return: None
        """

        url = f"{self.base_url}/services/auth/login"
        try:
            resp = requests.post(url,
                                 headers={"Accept": "application/html"},
                                 data=urlparse.urlencode({"username": username,
                                                          "password": password}),
                                 verify=verify,
                                 proxies=self.proxies)
            # This one we only allows 200. Otherwise login failed
            if resp.status_code == 200:
                # docs.splunk.com/Documentation/Splunk/7.0.2/RESTTUT/RESTsearches
                session_key = str(resp.content)
                self.session_key = session_key[session_key.index("<sessionKey>")+12:session_key.index("</sessionKey>")]
                self.header = {"Authorization": f"Splunk {self.session_key}"}
            else:
                error_msg = f"Splunk login failed with status {resp.status_code}"
                raise IntegrationError(f"Request to url [{url}] throws exception. Error [{error_msg}]")
        except Exception as e:
            raise e

    def send_post(self, url, args):
        """
        Send POST request to splunk server
        :param url: The url api call
        :param args: args for the api call
        :return: Request response in json
        """
        try:
            resp = requests.post(url, headers=self.header, data=args, verify=self.verify, proxies=self.proxies)
            # We shall just return the response in json and let the post process
            # to make decision.
            return {"status_code": resp.status_code,
                    "content": resp.json()}

        except requests.ConnectionError as e:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [Connection error. {str(e)}]")
        except requests.HTTPError as e:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [An HTTP error. {str(e)}]")
        except requests.URLRequired:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [A valid URL is required]")
        except requests.TooManyRedirects:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [Too many redirects]")
        except requests.RequestException as e:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [Ambiguous exception when handling request. {str(e)}]")

    def update_notable(self, event_id, comment, status):
        """
        Update notable event
        :param event_id: event_id for notable event to be updated
        :param comment: Comment to add to the notable event
        :param status: Status of the notable event to change to
        :return: Response in json
        """

        return self.send_post(f"{self.base_url}/services/notable_update",
                              {"comment": comment,
                               "status": status,
                               "ruleUIDs": [event_id]})

    def delete_threat_intel_item(self, threat_type, item_key):
        """
        Delete an item from the threat_intel collections.
        :param threat_type: ip_intel, file_intel, user_intel, http_intel, email_intel, service_intel
                            process_intel, registry_intel, or certificate_intel
        :param item_key: The _key for ite to delete
        :return: Response in json
        """

        url = f"{self.base_url}/services/data/threat_intel/item/{threat_type}/{item_key}"

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [{threat_type} is not supported]")

        try:
            resp = requests.delete(url, headers=self.header, verify=self.verify, proxies=self.proxies)
            # We shall just return the response in json and let the post process
            # to make decision.
            return {"status_code": resp.status_code,
                    "content": resp.json()}

        except Exception as e:
            raise IntegrationError(f"Delete request to url [{url}] throws exception. Error [Failed to delete: {str(e)}]")

    def add_threat_intel_item(self, threat_type, threat_dict):
        """
        Add a new threat intel item to the ThreatIntelligence collections
        :param threat_type: ip_intel, file_intel, user_intel, http_intel, email_intel, service_intel
                         process_intel, registry_intel, or certificate_intel
        :param threat_dict:
        :return: Response in json
        """

        url = f"{self.base_url}/services/data/threat_intel/item/{threat_type}"

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [{threat_type} is not supported]")

        return self.send_post(url, {"item": dumps(threat_dict)})

    def get_search_results(self, search_id, max_return):
        """
        Get the results from a Jira search
        """
        resp = requests.get(f"{self.base_url}/services/search/v2/jobs/{search_id}/results", data={"output_mode": "json", "count": max_return}, headers=self.header, verify=self.verify, proxies=self.proxies)
        if not resp.content: # If content is empty then the search has not finished running yet
            return
        return resp.json()

    def search(self, query, max_return, time_to_wait):
        """
        Perform a search on splunk
        """
        header = self.header
        header["Accept"] = "application/json"
        # Create splunk search
        search_job = requests.post(f"{self.base_url}/services/search/v2/jobs", data={"search": query, "output_mode": "json"}, headers=header, verify=self.verify, proxies=self.proxies).json()
        search_id = search_job.get("sid")

        while True:
            sleep(time_to_wait)
            search_results = self.get_search_results(search_id, max_return)
            if search_results.get("results"):
                break

        return search_results.get("results")

class SplunkServers():
    def __init__(self, opts):
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_name = f"{server}"
            server_data = opts.get(server_name)
            if not server_data:
                raise KeyError("Unable to find Splunk server: {}".format(server_name))

            servers[server] = server_data

        return servers, server_name_list

    @staticmethod
    def splunk_label_test(splunk_label, servers_list):
        """
        Check if the given splunk_label is in the app.config
        :param splunk_label: User selected server
        :param servers_list: List of Splunk servers
        :return: Dictionary of options for chosen server
        """
        # If label not given and using previous versions app.config [fn_splunk_integration]
        if not splunk_label and servers_list.get(PACKAGE_NAME):
            return servers_list[PACKAGE_NAME]
        elif not splunk_label:
            raise IntegrationError("No label was given and is required if servers are labeled in the app.config")

        label = PACKAGE_NAME+":"+splunk_label
        if splunk_label and label in servers_list:
            options = servers_list[label]
        elif len(servers_list) == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError("{} did not match labels given in the app.config".format(splunk_label))

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of Splunk server names defined in the app.config in fn_splunk_integration.
        :param opts: List of options
        :return: List of servers
        """
        server_list = []
        for key in opts.keys():
            if key.startswith("{}:".format(PACKAGE_NAME)):
                server_list.append(key)
        return server_list

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list
