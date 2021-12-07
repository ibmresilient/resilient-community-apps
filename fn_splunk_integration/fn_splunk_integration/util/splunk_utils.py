# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
#   Util classes for Splunk
#

import splunklib.client as splunk_client
import splunklib.results as splunk_results
import time
import requests
from xml.dom import minidom
import json
import sys
import fn_splunk_integration.util.splunk_constants as splunk_constants
from resilient_lib import IntegrationError
import urllib.parse as urlparse
import logging

LOG = logging.getLogger(__name__)

class SplunkClient(object):
    """ Wrapper of splunklib.client"""

    # member variables
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
        :param host: hostname for splunk
        :param port: port for splunk
        :param username: user name to login
        :param password: password to login
        :param verify: True to validate the SSL cert
        :return:
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

        job = None
        try:
            job = self.splunk_service.jobs.create(query, **query_args)
            if job_ttl:
                job.set_ttl(job_ttl)
        except Exception as e:
            LOG.exception("Search job creation failed")
            #
            # If we failed to create a search job, it does not make sense to go further
            #
            raise IntegrationError("Failed to create search job for query [{}] ".format(query))

        return job

    def execute_query(self, query):
        """
        Execute splunk query
        :param query: query string
        :return:
        """
        result = dict()

        LOG.debug(u"Query: {}" .format(query))

        splunk_job = self.start_search(query)

        # Poll Splunk for result
        start_time = time.time()
        done = False

        while not done:
            if not splunk_job.is_ready():
                pass
            else:
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
                if self.time_out!= 0:
                    if time.time() - start_time > self.time_out:
                        #
                        # old sdk
                        #splunk_client.cancel_search(splunk_job)
                        #
                        splunk_job.cancel()
                        raise IntegrationError("Query [{}] timed out. Final Status was [{}]".format(splunk_job.name, splunk_job["dispatchState"]))
                LOG.debug("Sleeping for %s", self.polling_interval)
                time.sleep(self.polling_interval)

        if splunk_job["dispatchState"] != "DONE" or splunk_job["isFailed"] == True:
            if sys.version_info.major < 3:
                raise IntegrationError("Query [{}] failed with status [{}], {}".format(splunk_job.name, splunk_job["dispatchState"], unicode(splunk_job["messages"])))
            else:
                # strings in python3 are unicode
                raise IntegrationError("Query [{}] failed with status [{}], {}".format(splunk_job.name, splunk_job["dispatchState"], str(splunk_job["messages"])))

        reader = splunk_results.ResultsReader(splunk_job.results())
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
        :param username: user name for splunk login
        :param password: password for splunk login
        :param verify: verify HTTPS cert or not
        :return:
        """

        headers = dict()
        headers["Accept"] = "application/html"
        url = self.base_url + "/services/auth/login"
        try:
            resp = requests.post(url,
                                 headers=headers,
                                 data=urlparse.urlencode({"username": username,
                                                          "password": password}),
                                 verify=verify)
            #
            # This one we only allows 200. Otherwise login failed
            #
            if resp.status_code == 200:
                # docs.splunk.com/Documentation/Splunk/7.0.2/RESTTUT/RESTsearches
                self.session_key = minidom.parseString(resp.content).getElementsByTagName("sessionKey")[0].childNodes[
                    0].nodeValue
            else:
                error_msg = "Splunk login failed for user {} with status {}".format(username, resp.status_code)
                raise IntegrationError("Request to url [{}] throws exception. Error [{}]".format(url, error_msg))
        except Exception as e:
            raise e

        return

    def update_notable(self, event_id, comment, status, cafile):
        """
        Update notable event
        :param event_id: event_id for notable event to be updated
        :param comment: comment to add to the notable event
        :param status: status of the notable event to change to
        :param cafile: Verify HTTPS cert or not
        :return:
        """

        headers = dict()
        headers["Authorization"] = "Splunk {}".format(self.session_key)

        args = dict()
        args["comment"] = comment
        args["status"] = status
        args["ruleUIDs"] = [event_id]

        ret = None
        url = self.base_url + "/services/notable_update"

        try:
            resp = requests.post(url, headers=headers, data=args, verify=cafile)
            #
            # We shall just return the response in json and let the post process
            # to make decision.
            #
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
        :param item_key:    the _key for ite to delete
        :param cafile:      CA cert or False to skip cert verification
        :return:
        """

        headers = dict()
        headers["Authorization"] = "Splunk {}".format(self.session_key)
        url = "{0}/services/data/threat_intel/item/{1}/{2}".format(self.base_url, threat_type, item_key)

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError("Request to url [{}] throws exception. Error [{}]".format(url, "{} is not supported"))

        ret = {}
        try:
            resp = requests.delete(url, headers=headers, verify=cafile)
            #
            # We shall just return the response in json and let the post process
            # to make decision.
            #
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
        :param cafile:
        :return:
        """
        headers = {"Authorization": "Splunk {}".format(self.session_key)}

        url = self.base_url + "/services/data/threat_intel/item/" + threat_type

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise IntegrationError("Request to url [{}] throws exception. Error [{}]".format(url, "{} is not supported"))

        item = {"item": json.dumps(threat_dict)}

        try:
            resp = requests.post(url, headers=headers, data=item, verify=cafile)
            #
            # We shall just return the response in json and let the post process
            # to make decision.
            #
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

    def splunk_label_test(splunk_label, servers_list):
        """
        Check if the given splunk_label is in the app.config
        """
        label = splunk_constants.PACKAGE_NAME+":"+splunk_label
        if splunk_label and label in servers_list:
            options = servers_list[label]
        elif (len(servers_list) == 1 and splunk_label == splunk_constants.PACKAGE_NAME) or servers_list == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError("{} did not match labels given in the app.config".format(splunk_label))

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of Splunk server names defined in the app.config in fn_splunk_integration. 
        """
        server_list = []
        for key in opts.keys():
            if key.startswith("{}:".format(splunk_constants.PACKAGE_NAME)):
                server_list.append(key)
        return server_list

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list
