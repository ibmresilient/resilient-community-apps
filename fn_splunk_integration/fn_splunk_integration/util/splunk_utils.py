# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
#   Util classes for Splunk
#
import requests
from json import dumps
from time import time, sleep
from logging import getLogger
import urllib.parse as urlparse
import splunklib.client as splunk_client
import splunklib.results as splunk_results
from resilient_lib import IntegrationError
from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME

LOG = getLogger(__name__)

class SplunkClient(object):
    """ Wrapper of splunklib.client"""

    # Member variables
    splunk_service = None
    time_out = 600
    polling_interval = 5
    max_return = 0

    def __init__(self, host, port, username, password, verify=True):
        """Init splunk_service"""
        self.splunk_service = self.connect(host, port, username, password, verify)

    @staticmethod
    def connect(host, port, username, password, verify):
        """
        Connect to Splunk
        :param host: Hostname for splunk
        :param port: Port for splunk
        :param username: Username to login
        :param password: Password to login
        :param verify: True to validate the SSL cert
        :return: Connection to splunk
        """
        LOG.info("Splunk SDK verify flag is {}".format(verify))
        return splunk_client.connect(host=host,
                                     port=port,
                                     username=username,
                                     password=password,
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
        except Exception as e:
            LOG.exception("Search job creation failed")
            # If we failed to create a search job, it does not make sense to go further
            raise IntegrationError("Failed to create search job for query [{}] ".format(query))

        return job

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
            if splunk_job.is_ready():
                splunk_job.refresh()
                done = splunk_job["dispatchState"] in ("FAILED", "DONE")

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
                    if time() - start_time > self.time_out:
                        splunk_job.cancel()
                        raise IntegrationError("Query [{}] timed out. Final Status was [{}]".format(splunk_job.name, splunk_job["dispatchState"]))
                LOG.debug("Sleeping for %s", self.polling_interval)
                sleep(self.polling_interval)

        if splunk_job["dispatchState"] != "DONE" or splunk_job["isFailed"] == True:
            raise IntegrationError("Query [{}] failed with status [{}], {}".format(splunk_job.name, splunk_job["dispatchState"], str(splunk_job["messages"])))

        results_args = {}
        if self.max_return:
            results_args["count"] = self.max_return

        reader = splunk_results.ResultsReader(splunk_job.results(**results_args))
        result = {"events": list([dict(row) for row in reader])}

        return result

class SplunkUtils(object):
    """ Use python requests to call Splunk REST API"""

    # Member variables
    session_key = ""
    base_url = ""
    SUPPORTED_THREAT_TYPE = ["ip_intel", "file_intel", "user_intel", "http_intel",
                             "email_intel", "service_intel", "process_intel",
                             "registry_intel", "certificate_intel"]

    def __init__(self, host, port, username, password, verify):
        self.base_url = "https://{}:{}".format(host, port)
        self.get_session_key(username, password, verify)

    def get_session_key(self, username, password, verify):
        """
        Get session_key from Splunk server
        :param username: Username for splunk login
        :param password: Password for splunk login
        :param verify: Verify HTTPS cert or not
        :return: None
        """

        headers = {"Accept": "application/html"}
        url = self.base_url + "/services/auth/login"
        try:
            resp = requests.post(url,
                                 headers=headers,
                                 data=urlparse.urlencode({"username": username,
                                                          "password": password}),
                                 verify=verify)
            # This one we only allows 200. Otherwise login failed
            if resp.status_code == 200:
                # docs.splunk.com/Documentation/Splunk/7.0.2/RESTTUT/RESTsearches
                session_key = str(resp.content)
                self.session_key = session_key[session_key.index("<sessionKey>")+12:session_key.index("</sessionKey>")]
            else:
                error_msg = "Splunk login failed for user {} with status {}".format(username, resp.status_code)
                raise IntegrationError("Request to url [{}] throws exception. Error [{}]".format(url, error_msg))
        except Exception as e:
            raise e

    def update_notable(self, event_id, comment, status, cafile):
        """
        Update notable event
        :param event_id: event_id for notable event to be updated
        :param comment: Comment to add to the notable event
        :param status: Status of the notable event to change to
        :param cafile: Verify HTTPS cert or not
        :return: Response in json
        """

        headers = {"Authorization": "Splunk {}".format(self.session_key)}

        args = {"comment": comment,
                "status": status,
                "ruleUIDs": [event_id]}

        url = self.base_url + "/services/notable_update"

        try:
            resp = requests.post(url, headers=headers, data=args, verify=cafile)
            # We shall just return the response in json and let the post process
            # to make decision.
            ret = {"status_code": resp.status_code,
                   "content": resp.json()}

        except requests.ConnectionError as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [Connection error. {}]".format(url, str(e)))
        except requests.HTTPError as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [An HTTP error. {}]".format(url, str(e)))
        except requests.URLRequired as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [A valid URL is required]".format(url))
        except requests.TooManyRedirects as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [Too many redirects]".format(url))
        except requests.RequestException as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [Ambiguous exception when handling request. {}]".format(url, str(e)))

        return ret

    def delete_threat_intel_item(self, threat_type, item_key, cafile):
        """
        Delete an item from the threat_intel collections.
        :param threat_type: ip_intel, file_intel, user_intel, http_intel, email_intel, service_intel
                            process_intel, registry_intel, or certificate_intel
        :param item_key: The _key for ite to delete
        :param cafile: CA cert or False to skip cert verification
        :return: Response in json
        """

        headers = {"Authorization": "Splunk {}".format(self.session_key)}
        url = "{0}/services/data/threat_intel/item/{1}/{2}".format(self.base_url, threat_type, item_key)

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError("Request to url [{}] throws exception. Error [{}]".format(url, "{} is not supported"))

        try:
            resp = requests.delete(url, headers=headers, verify=cafile)
            # We shall just return the response in json and let the post process
            # to make decision.
            ret = {"status_code": resp.status_code,
                   "content": resp.json()}

        except Exception as e:
            raise IntegrationError("Delete request to url [{}] throws exception. Error [Failed to delete: {}]".format(url, u"Failed to delete: " + str(e)))

        return ret

    def add_threat_intel_item(self, threat_type, threat_dict, cafile):
        """
        Add a new threat intel item to the ThreatIntelligence collections
        :param threat_type: ip_intel, file_intel, user_intel, http_intel, email_intel, service_intel
                         process_intel, registry_intel, or certificate_intel
        :param threat_dict:
        :param cafile: CA cert or False to skip cert verification
        :return: Response in json
        """
        headers = {"Authorization": "Splunk {}".format(self.session_key)}

        url = self.base_url + "/services/data/threat_intel/item/" + threat_type

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError("Request to url [{}] throws exception. Error [{}]".format(url, "{} is not supported"))

        item = {"item": dumps(threat_dict)}

        try:
            resp = requests.post(url, headers=headers, data=item, verify=cafile)
            # We shall just return the response in json and let the post process
            # to make decision.
            ret = {"status_code": resp.status_code,
                   "content": resp.json()}

        except requests.ConnectionError as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [Connection error. {}]".format(url, str(e)))
        except requests.HTTPError as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [An HTTP error. {}]".format(url, str(e)))
        except requests.URLRequired as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [A valid URL is required]".format(url))
        except requests.TooManyRedirects as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [Too many redirects]".format(url))
        except requests.RequestException as e:
            raise IntegrationError("Request to url [{}] throws exception. Error [Ambiguous exception when handling request. {}]".format(url, str(e)))

        return ret

class SplunkServers():
    def __init__(self, opts, options):
        self.servers, self.server_name_list = self._load_servers(opts, options)

    def _load_servers(self, opts, options):
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
        :return: Dictionary of options for choosen server
        """
        label = PACKAGE_NAME
        if splunk_label:
            label = "{}:{}".format(label, splunk_label)

        if label in servers_list:
            options = servers_list[label]
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
