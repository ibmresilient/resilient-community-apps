# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
#
#   Util classes for qradar
#

import base64
import json
import logging
import requests
import six
import fn_qradar_enhanced_data.util.qradar_constants as qradar_constants
import fn_qradar_enhanced_data.util.function_utils as function_utils
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from resilient_lib import RequestsCommon
from fn_qradar_enhanced_data.util.SearchWaitCommand import SearchWaitCommand, SearchFailure, SearchJobFailure


# handle python2 and 3
try:
    from urllib import quote as quote_func  # Python 2.X
except ImportError:
    from urllib.parse import quote as quote_func  # Python 3+

LOG = logging.getLogger(__name__)


def quote(input_v, safe=None):
    """
    To make sure that integration on Python 2 works with unicode we will wrap quote
    to always pass bytes to it.
    """
    if not isinstance(input_v, six.binary_type):
        input_v = input_v.encode('utf-8')

    # No need to re-define the default for safe
    if safe:
        return quote_func(input_v, safe)
    return quote_func(input_v)


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


class AuthInfo(object):
    # Singleton
    __instance = None

    def __init__(self):
        self.headers = {}
        self.qradar_auth = None
        self.qradar_token = None
        self.username=None
        self.password=None
        self.api_url = None
        self.cafile = True
        self.rc = None
        pass

    @staticmethod
    def get_authInfo():
        if AuthInfo.__instance is None:
            AuthInfo.__instance = AuthInfo()
        return AuthInfo.__instance

    def create(self, host, username=None, password=None, token=None, cafile=None,
               opts=None, function_opts=None):
        """
        Create headers used for REST Api calls
        :param host: qradar host
        :param username: qradar user login
        :param password: qradar password
        :param token: Use token or username/password to auth
        :param cafile:
        :param opts: app.config options
        :param function_opts: function parameters from app.config
        :return:
        """
        self.headers = {'Accept': 'application/json'}
        if username and password:
            self.username = username
            self.password = password
            self.qradar_auth = base64.b64encode((username + ':' + password).encode('ascii'))
            self.headers['Authorization'] = b"Basic " + self.qradar_auth
        elif token:
            self.qradar_token = token
            self.headers["SEC"] = self.qradar_token
        if host.startswith("http"):
            self.api_url = "{}/api/".format(host)
        else:
            self.api_url = "https://{}/api/".format(host)
        self.cafile = cafile

        self.rc = RequestsCommon(opts, function_opts)

    def make_call(self, method, url, headers=None, data=None):
        my_headers = headers if headers else self.headers

        def make_call_callback(response):
            # 404 is not found, such as reference not found or item not found in reference set
            if response.status_code in (404,):
                return response
            else:
                response.raise_for_status()
                return response

        return self.rc.execute_call_v2(method, url, data=data, headers=my_headers, verify=self.cafile, callback=make_call_callback)


class ArielSearch(SearchWaitCommand):
    """
    Subclass of SearchWaitCommand.
    Overrides/implements get_search_id, check_status, get_search_result for QRadar
    """

    def __init__(self, timeout=600, poll=5,graphql=False):
        self.range_start = 0
        self.range_end = 50
        self.query_all = False
        self.graphql=graphql
        super(ArielSearch, self).__init__(timeout, poll)

    def set_range_start(self, start):
        """
        Set range start for ariel search
        :param start: int for range start
        :return:
        """
        self.range_start = start

    def set_range_end(self, end):
        """
        Set range end for ariel search
        :param end: int for range end
        :return:
        """
        self.range_end = end
    def set_timeout(self, timeout):
        """
        Set timeout
        :param timeout:
        :return:
        """
        self.search_timeout = timeout
    def set_query_all(self, query_all):
        """
        Set bool to determine if range header is necessary
        :param query_all:
        :return:
        """
        self.query_all = query_all

    def get_search_id(self, query):
        """
        Get the search if associated with the search using query
        :param query: input query string
        :return: search_id returned from QRadar
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()

        url = auth_info.api_url + qradar_constants.ARIEL_SEARCHES
        utf8 = query.encode("utf-8")
        data = {"query_expression": utf8}

        search_id = ""
        try:
            response = auth_info.make_call("POST", url, data=data, headers=headers)

            json = response.json()

            if "search_id" in json:
                search_id = json["search_id"]

            elif "cursor_id" in json:
                    search_id = json["cursor_id"]
        except Exception as e:
            LOG.error(str(e))
            raise SearchJobFailure(query)

        return search_id

    def get_search_result(self, search_id):
        """
        Get search result associated with search_id
        :param search_id:
        :return: dict with events
        """
        auth_info = AuthInfo.get_authInfo()

        url = auth_info.api_url + qradar_constants.ARIEL_SEARCHES_RESULT.format(search_id)

        headers = auth_info.headers.copy()
        # if the # of returned items is big, this call will take a long time!
        # Need to use Range to limit the # if query_all is False.
        # If query_all is True, the Range will not be used and all the results will be returned from the query.
        if not self.query_all:
            headers[b"Range"] = "items={}-{}".format(str(self.range_start), str(self.range_end))

        if self.graphql:
            headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        response = None
        try:
            response = auth_info.make_call("GET", url, headers=headers)
        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, None)

        ret = {}
        if response.status_code == 200:
            res = response.json()
            events = res["events"] if "events" in res else res["flows"] if "flows" in res else res["other"]
            events = function_utils.fix_dict_value(events)
            ret = {"events": events}

        return ret

    def check_status(self, search_id):
        """
        Check the search status associated with search_id
        :param search_id:
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        url = "{}{}/{}".format(auth_info.api_url, qradar_constants.ARIEL_SEARCHES, search_id)
        status = SearchWaitCommand.SEARCH_STATUS_ERROR_STOP
        try:
            response = auth_info.make_call("GET", url)

            json_dict = response.json()
            if "status" in json_dict:
                if json_dict["status"] == qradar_constants.SEARCH_STATUS_COMPLETED:
                    status = SearchWaitCommand.SEARCH_STATUS_COMPLETED
                elif json_dict["status"] == qradar_constants.SEARCH_STATUS_WAIT \
                    or json_dict["status"] == qradar_constants.SEARCH_STATUS_SORTING \
                        or json_dict["status"] == qradar_constants.SEARCH_STATUS_EXECUTE:
                    status = SearchWaitCommand.SEARCH_STATUS_WAITING

        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, status)

        return status


class QRadarClient(object):

    def __init__(self, host, username=None, password=None, token=None, cafile=None,
                 opts=None, function_opts=None):
        """
        Init
        :param host:  QRadar host
        :param username: QRadar user name
        :param password: QRadar password
        :param token: QRadar token
        :param cafile: verify cert or not
        :param opts: app.config options dictionary
        :param function_opts: function parameters from app.config
        """
        auth_info = AuthInfo.get_authInfo()
        auth_info.create(host, username, password, token, cafile, opts, function_opts)

    def get_versions(self):
        """
        Util function used to test connectivity to QRadar
        :return:
        """
        auth_info = AuthInfo.get_authInfo()

        url = auth_info.api_url + qradar_constants.HELP_VERSIONS
        response = auth_info.make_call("GET", url)

        return response

    def ariel_graphql_search(self, temp_query, search_query, query_all=False, range_start=None,
                             range_end=None, timeout=None):

        """
        Perform an Ariel search
        :param query_all: bool used to decide if Range header is included in query
        :param query: query string
        :param range_start:
        :param range_end:
        :param timeout: timeout for search
        :return: dict with events
        """
        ariel_search = ArielSearch(graphql=True)
        if range_start is not None:
            ariel_search.set_range_start(range_start)

        if range_end is not None:
            ariel_search.set_range_end(range_end)

        if timeout is not None:
            ariel_search.set_timeout(timeout)

        ariel_search.set_query_all(query_all)

        response = ariel_search.perform_search(temp_query,False)  # Execute the query on a temp table
        response = ariel_search.perform_search(search_query, True)  # Get the actual query results from temp table

        return response

    def verify_connect(self):
        """
        QRadar does not support session key. check version to verify
        Sample data
        [{"id":1,"deprecated":false,"root_resource_ids":[],"removed":true,"version":"0.1"},
        {"id":2,"deprecated":false,"root_resource_ids":[],"removed":true,"version":"0.2"},
        {"id":3,"deprecated":false,"root_resource_ids":[],"removed":true,"version":"1.0"},
        {"id":4,"deprecated":false,"root_resource_ids":[],"removed":true,"version":"2.0"},
        {"id":5,"deprecated":false,"root_resource_ids":[],"removed":true,"version":"3.0"},
        {"id":6,"deprecated":false,"root_resource_ids":[],"removed":true,"version":"3.1"},
        {"id":7,"deprecated":true,"root_resource_ids":[1,7,14,16,18,28,44,51],"removed":false,"version":"4.0"},
        {"id":8,"deprecated":true,"root_resource_ids":[62,70,76,83,85,99,102,104,114,130,137,148],"removed":false,"version":"5.0"},
        {"id":9,"deprecated":true,"root_resource_ids":[157,165,171,178,180,194,199,201,211,227,234,245],"removed":false,"version":"5.1"},
        {"id":10,"deprecated":false,"root_resource_ids":[254,262,268,275,277,291,296,303,311,327,334,347],"removed":false,"version":"6.0"},
        {"id":11,"deprecated":false,"root_resource_ids":[356,390,408,417,419,471,480,491,496,503,514,526,572,579,602,607],"removed":false,"version":"7.0"}]
        """
        resp = self.get_versions()

        connected = False
        if resp.status_code == 200 and len(resp.json()) > 0:
            if "version" in resp.json()[0]:
                connected = True

        return connected

    @staticmethod
    def verify_graphql_connect():
        auth_info = AuthInfo.get_authInfo()
        url = u"{}{}".format(auth_info.api_url.replace("api/", ""), qradar_constants.GRAPHQL_URL)
        headers = auth_info.headers.copy()
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))
        headers["Content-Type"] = "application/json"
        data = {"operationName":"getSystemDate","variables":{},"query":qradar_graphql_queries.GRAPHQL_SYSTEMDATE}

        try:
            response = auth_info.make_call("POST", url, data=json.dumps(data), headers=headers)
        except Exception as e:
            pass

        return response.status_code == 200

    @staticmethod
    def get_offense_summary_data(offenseid):
        """
        Get Offense summary for the given Offense
        :param offenseid: Id of the QRadar Offense
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        url = u"{}{}".format(auth_info.api_url.replace("api/",""), qradar_constants.GRAPHQL_URL)
        data = {"operationName":"offenseQuery","variables":{"id":offenseid},"query":qradar_graphql_queries.GRAPHQL_OFFENSEQUERY}
        ret = {}
        try:
            response = auth_info.make_call("POST", url,data=json.dumps(data),headers=headers)

            ret = {"status_code": response.status_code,
                   "content": response.json()["data"]["getOffense"]}

        except Exception as e:
            LOG.error(str(e))
            raise RequestError(url, "get_offense_summary_data call failed with exception {}".format(str(e)))

        return ret


    @staticmethod
    def get_rules_data(offenseid):
        """
        Get the contributing rules for the Offense
        :param offenseid: Id of the QRadar Offense
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        url = u"{}{}".format(auth_info.api_url.replace("/api",""), qradar_constants.GRAPHQL_URL)
        data = {"operationName":"ruleQuery","variables":{"id":offenseid},"query":qradar_graphql_queries.GRAPHQL_RULESQUERY}
        ret = {}
        try:
            response = auth_info.make_call("POST", url,data=json.dumps(data),headers=headers)
            res = response.json()

            ret = {"status_code": response.status_code,
                   "content": res["data"]["getOffense"]}

        except Exception as e:
            LOG.error(str(e))
            raise RequestError(url, "get_rules_data call failed with exception {}".format(str(e)))

        return ret


    @staticmethod
    def get_sourceip_data(event):
        """
        Get Source IP for the Offense
        :param offenseid: Id of the QRadar Offense
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        url = u"{}{}".format(auth_info.api_url.replace("/api",""), qradar_constants.GRAPHQL_URL)
        data = {"operationName":"assetQuery","variables":{"domainId":event["domainid"],"ipAddress":event["sourceip"]},"query":qradar_graphql_queries.GRAPHQL_SOURCEIP}
        ret = {}
        try:
            response = auth_info.make_call("POST", url,data=json.dumps(data),headers=headers)
            res = response.json()

            ret = {"status_code": response.status_code,
                   "content": res["data"]["getAsset"]}

        except Exception as e:
            LOG.error(str(e))
            raise RequestError(url, "get_sourceip_data call failed with exception {}".format(str(e)))

        return ret

    @staticmethod
    def get_offense_source(offenseid):
        """
        Get source addresses the Offense
        :param offenseid: Id of the QRadar Offense
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        url = u"{}{}".format(auth_info.api_url.replace("/api",""), qradar_constants.GRAPHQL_URL)
        data = {"operationName":"offenseSourceQuery","variables":{"id":offenseid}, "query":qradar_graphql_queries.GRAPHQL_OFFENSESOURCE}
        ret = {}
        try:
            response = auth_info.make_call("POST", url,data=json.dumps(data),headers=headers)
            res = response.json()

            ret = {"status_code": response.status_code,
                   "content": res["data"]["getOffense"]["sourceAddresses"]}

        except Exception as e:
            LOG.error(str(e))
            raise RequestError(url, "get_offense_source call failed with exception {}".format(str(e)))

        return ret

    @staticmethod
    def get_offense_asset_data(asset):
        """
                Get assests data for the Offense
                :param asset: dict of sourceip and domainid
                :return:
                """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        url = u"{}{}".format(auth_info.api_url.replace("/api", ""), qradar_constants.GRAPHQL_URL)
        data = {"operationName": "assetQuery",
                "variables": {"domainId": asset["domainId"], "ipAddress":  asset["sourceIp"]},
                "query": qradar_graphql_queries.GRAPHQL_OFFENSEASSETS}
        ret = {}
        try:
            response = auth_info.make_call("POST", url, data=json.dumps(data), headers=headers)
            res = response.json()

            ret = {"status_code": response.status_code,
                   "content": res["data"]["getAsset"]}

        except Exception as e:
            LOG.error(str(e))
            raise RequestError(url, "get_offense_asset_data call failed with exception {}".format(str(e)))

        return ret

    @staticmethod
    def get_qr_sessionid(host):
        """
        Get QRadar Session Id
        :return:
        """
        cookies = {}

        try:
            auth_info = AuthInfo.get_authInfo()

            if not auth_info.username and not auth_info.password:
                cookies={"SEC":auth_info.qradar_token}
            else:
                res = requests.get("{0}console/logon.jsp".format(host), verify=auth_info.cafile)
                cookies = res.cookies.get_dict()

                res = requests.post("{0}{1}".format(host, qradar_constants.GRAPHQL_BASICAUTH), data={"j_username":auth_info.username,"j_password":auth_info.password,"LoginCSRF":requests.post("{0}{1}".format(host, qradar_constants.GRAPHQL_BASICAUTH), data={"get_csrf": ""}, headers={"Cookie": "JSESSIONID="+cookies["JSESSIONID"]}, verify=auth_info.cafile).text}, headers={"Cookie": "JSESSIONID="+cookies["JSESSIONID"]}, verify=auth_info.cafile)
                cookies = res.cookies.get_dict()
        except Exception as e:
            LOG.error(str(e))

        return "; ".join([x+"="+cookies[x] for x in cookies.keys()])
