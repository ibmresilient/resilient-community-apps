# -*- coding: utf-8 -*-
#
# Copyright IBM Corp. - Confidential Information
#
#   Util classes for Splunk
#

import splunklib.client as splunk_client
import splunklib.results as splunk_results
import time
import requests
import urllib
from xml.dom import minidom
import json

import logging
LOG = logging.getLogger(__name__)

# Constants
SPLUNK_SECTION="splunk_integration"


class SearchFailure(Exception):
    """ Search failed to execute """
    def __init__(self, search_id, search_status):
        fail_msg = "Query [{}] failed with status [{}]".format(search_id, search_status)
        super(SearchFailure, self).__init__(fail_msg)
        self.search_status = search_status


class SearchTimeout(Exception):
    """ Query failed to complete in time specified """
    def __init__(self, search_id, search_status):
        fail_msg = "Query [{}] timed out. Final Status was [{}]".format(search_id, search_status)
        super(SearchTimeout, self).__init__(fail_msg)
        self.search_status = search_status


class SearchJobFailure(Exception):
    """ Search job creation failure"""
    def __init__(self, query):
        fail_msg = "Failed to create search job for query [{}] ".format(query)
        super(SearchJobFailure, self).__init__(fail_msg)


class RequestError(Exception):
    """ Request error"""
    def __init__(self, url, message):
        fail_msg = "Request to url [{}] throws exception. Error [{}]".format(url, message)
        super(RequestError, self).__init__(fail_msg)


class DeleteError(Exception):
    """ Request error"""
    def __init__(self, url, message):
        fail_msg = "Delete request to url [{}] throws exception. Error [{}]".format(url, message)
        super(DeleteError, self).__init__(fail_msg)


class SplunkClient(object):
    """ Wrapper of splunklib.client"""

    # member variables
    splunk_service = None
    time_out = 600
    polling_interval = 5
    max_return = 0

    def __init__(self, host, port, username, password):
        """Init splunk_service"""
        self.splunk_service = self.connect(host, port, username, password)

    @staticmethod
    def connect(host, port, username, password):
        """
        Connect to Splunk
        :param host: hostname for splunk
        :param port: port for splunk
        :param username: user name to login
        :param password: password to login
        :return:
        """
        return splunk_client.connect(host=host,
                                     port=port,
                                     username=username,
                                     password=password)

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
            raise SearchJobFailure(query)

        return job

    def execute_query(self, query):
        """
        Execute splunk query
        :param query: query string
        :return:
        """
        result = dict()

        LOG.debug("Query: {}" .format(query))

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
                        raise SearchTimeout(splunk_job.name, splunk_job["dispatchState"])
                time.sleep(self.polling_interval)

        if splunk_job["dispatchState"] != "DONE" or splunk_job["isFailed"] == True:
            raise SearchFailure(splunk_job.name, splunk_job["dispatchState"] + u", " + unicode(splunk_job["messages"]))

        reader = splunk_results.ResultsReader(splunk_job.results())
        result = {"events": [row for row in reader]}

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
                                 data=urllib.urlencode({"username": username,
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
                raise RequestError(url, error_msg)
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
            resp = requests.post(url,
                                 headers=headers,
                                 data=args,
                                 verify=cafile)

            #
            # We shall just return the response in json and let the post process
            # to make decision.
            #
            ret = {"status_code": resp.status_code,
                   "content": resp.json()}

        except requests.ConnectionError as e:
            raise RequestError(url, "Connection error. " + str(e))
        except requests.HTTPError as e:
            raise RequestError(url, "An HTTP error. " + str(e))
        except requests.URLRequired as e:
            raise RequestError(url, "An valid URL is required.")
        except requests.TooManyRedirects as e:
            raise RequestError(url, "Too many redirects")
        except requests.RequestException as e:
            raise RequestError(url, "Ambiguous exception when handling request. " + str(e))
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
            raise RequestError(url, "{} is not supported")

        ret = {}
        try:
            resp = requests.delete(url,
                                   headers=headers,
                                   verify=cafile)
            #
            # We shall just return the response in json and let the post process
            # to make decision.
            #
            ret = {"status_code": resp.status_code,
                   "content": resp.json()}

        except Exception as e:
            raise DeleteError(url, "Failed to delete: {}".format(str(e)))

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
        headers = dict()
        headers["Authorization"] = "Splunk {}".format(self.session_key)

        url = self.base_url + "/services/data/threat_intel/item/" + threat_type

        if threat_type not in self.SUPPORTED_THREAT_TYPE:
            raise RequestError(url, "{} is not supported")

        item = {"item": json.dumps(threat_dict)}

        try:
            resp = requests.post(url,
                                 headers=headers,
                                 data=item,
                                 verify=cafile)

            #
            # We shall just return the response in json and let the post process
            # to make decision.
            #
            ret = {"status_code": resp.status_code,
                   "content": resp.json()}

        except requests.ConnectionError as e:
            raise RequestError(url, "Connection error. " + str(e))
        except requests.HTTPError as e:
            raise RequestError(url, "An HTTP error. " + str(e))
        except requests.URLRequired as e:
            raise RequestError(url, "An valid URL is required.")
        except requests.TooManyRedirects as e:
            raise RequestError(url, "Too many redirects")
        except requests.RequestException as e:
            raise RequestError(url, "Ambiguous exception when handling request. " + str(e))
        return ret
