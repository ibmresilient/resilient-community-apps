# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
#   Util classes for Splunk

import requests
from json import dumps
from time import time, sleep
from logging import getLogger
import urllib.parse as urlparse
import splunklib.client as splunk_client
import splunklib.results as splunk_results
from resilient_lib import IntegrationError

PACKAGE_NAME = "fn_splunk_integration"
LOG = getLogger(__name__)

class SplunkClient(object):
    """ Wrapper of splunklib.client"""

    # Member variables
    splunk_service = None
    time_out = 600
    polling_interval = 5
    max_return = 0

    def __init__(self, host, port, username=None, password=None, token=None, verify=True):
        """Init splunk_service"""
        self.splunk_service = self.connect(host, port, username, password, token, verify)

    @staticmethod
    def connect(host, port, username, password, token, verify):
        """
        Connect to Splunk
        :param host: Hostname for splunk
        :param port: Port for splunk
        :param username: Username to login
        :param password: Password to login
        :param token: Token string
        :param verify: True to validate the SSL cert
        :return: Connection to splunk
        """
        LOG.info(f"Splunk SDK verify flag is {verify}")
        return splunk_client.connect(host=host,
                                     port=port,
                                     username=username,
                                     password=password,
                                     token=token,
                                     verify=verify)

    def set_timeout(self, timeout):
        self.time_out = timeout

    def set_polling_interval(self, pollinginterval):
        self.polling_interval = pollinginterval

    def set_max_return(self, max):
        self.max_return = max

    def start_search(self, query, job_ttl=None):
        """Start a search for a query"""

        query_args = {"search_mode": "normal",
                      "enable_lookups": True}
        if self.max_return:
            query_args["max_count"] = self.max_return

        try:
            job = self.splunk_service.jobs.create(query, **query_args)
            if job_ttl:
                job.set_ttl(job_ttl)
            return job
        except Exception:
            LOG.exception("Search job creation failed")
            # If we failed to create a search job, it does not make sense to go further
            raise IntegrationError(f"Failed to create search job for query [{query}] ")

    def execute_query(self, query):
        """
        Execute splunk query
        :param query: Query string
        :return: Results of the query
        """

        LOG.debug(u"Query: {}" .format(query))

        splunk_job = self.start_search(query)

        # Poll Splunk for result
        start_time = time()
        done = False

        while not done:
            dispatch_state = splunk_job["dispatchState"]
            if splunk_job.is_ready():
                splunk_job.refresh()
                done = dispatch_state in ("FAILED", "DONE")

                stats = {"name": splunk_job.name,
                         "isDone": splunk_job.isDone,
                         "scanCount": int(splunk_job["scanCount"]),
                         "eventCount": int(splunk_job["eventCount"]),
                         "doneProgress": float(splunk_job["doneProgress"]) * 100,
                         "resultCount": int(splunk_job["resultCount"])}

                status = ("\r%(doneProgress)03.1f%%   %(scanCount)d scanned   "
                          "%(eventCount)d matched   %(resultCount)d results") % stats

                LOG.debug(status)

            if not done:
                if self.time_out != 0:
                    if ((time() - start_time) > self.time_out):
                        splunk_job.cancel()
                        raise IntegrationError(f"Query [{splunk_job.name}] timed out. Final Status was [{dispatch_state}]")
                LOG.debug(f"Sleeping for {self.polling_interval}")
                sleep(self.polling_interval)

        if dispatch_state != "DONE" or splunk_job["isFailed"] == True:
            raise IntegrationError(f"Query [{splunk_job.name}] failed with status [{dispatch_state}], {str(splunk_job['messages'])}")

        results_args = {}
        if self.max_return:
            results_args["count"] = self.max_return

        reader = splunk_results.ResultsReader(splunk_job.results(**results_args))
        return {"events": list([dict(row) for row in reader])}

class SplunkUtils(object):
    """ Use python requests to call Splunk REST API"""

    # Member variables
    header = ""
    session_key = ""
    base_url = ""
    SUPPORTED_THREAT_TYPE = ["ip_intel", "file_intel", "user_intel", "http_intel",
                             "email_intel", "service_intel", "process_intel",
                             "registry_intel", "certificate_intel"]

    def __init__(self, host, port, username, password, token, verify, proxies):
        self.base_url = f"https://{host}:{port}"
        self.proxies = proxies
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

    def send_post(self, url, args, cafile):
        """
        Send POST request to splunk server
        :param url: The url api call
        :param args: args for the api call
        :param cafile: Certificate file
        :return: Request response in json
        """
        try:
            resp = requests.post(url, headers=self.header, data=args, verify=cafile, proxies=self.proxies)
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

    def update_notable(self, event_id, comment, status, cafile):
        """
        Update notable event
        :param event_id: event_id for notable event to be updated
        :param comment: Comment to add to the notable event
        :param status: Status of the notable event to change to
        :param cafile: Verify HTTPS cert or not
        :return: Response in json
        """

        return self.send_post(f"{self.base_url}/services/notable_update",
                              {"comment": comment,
                               "status": status,
                               "ruleUIDs": [event_id]},
                              cafile)

    def delete_threat_intel_item(self, threat_type, item_key, cafile):
        """
        Delete an item from the threat_intel collections.
        :param threat_type: ip_intel, file_intel, user_intel, http_intel, email_intel, service_intel
                            process_intel, registry_intel, or certificate_intel
        :param item_key: The _key for ite to delete
        :param cafile: CA cert or False to skip cert verification
        :return: Response in json
        """

        url = f"{self.base_url}/services/data/threat_intel/item/{threat_type}/{item_key}"

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [{threat_type} is not supported]")

        try:
            resp = requests.delete(url, headers=self.header, verify=cafile, proxies=self.proxies)
            # We shall just return the response in json and let the post process
            # to make decision.
            return {"status_code": resp.status_code,
                    "content": resp.json()}

        except Exception as e:
            raise IntegrationError(f"Delete request to url [{url}] throws exception. Error [Failed to delete: {str(e)}]")

    def add_threat_intel_item(self, threat_type, threat_dict, cafile):
        """
        Add a new threat intel item to the ThreatIntelligence collections
        :param threat_type: ip_intel, file_intel, user_intel, http_intel, email_intel, service_intel
                         process_intel, registry_intel, or certificate_intel
        :param threat_dict:
        :param cafile: CA cert or False to skip cert verification
        :return: Response in json
        """

        url = f"{self.base_url}/services/data/threat_intel/item/{threat_type}"

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [{threat_type} is not supported]")

        return self.send_post(url, {"item": dumps(threat_dict)}, cafile)

    def search(self, query, cafile):
        """
        """
        url = f"{self.base_url}/services/search/jobs"
        return self.send_post(url,{"search": query}, cafile)

class SplunkServers():
    def __init__(self, opts):
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_name = u"{}".format(server)
            server_data = opts.get(server_name)
            if not server_data:
                raise KeyError(u"Unable to find Splunk server: {}".format(server_name))

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
