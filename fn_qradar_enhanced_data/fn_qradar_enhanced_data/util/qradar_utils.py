# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# Util classes for qradar

from base64 import b64encode
from json import dumps
from logging import getLogger
from urllib.parse import quote as quote_func
from requests import get, post
from resilient_lib import IntegrationError, RequestsCommon
from six import binary_type
import fn_qradar_enhanced_data.util.qradar_constants as qradar_constants
from fn_qradar_enhanced_data.util.qradar_graphql_queries import GRAPHQL_SYSTEMDATE
from fn_qradar_enhanced_data.util.SearchWaitCommand import (SearchFailure, SearchJobFailure, SearchWaitCommand)

LOG = getLogger(__name__)

def quote(input_v, safe=None):
    """
    To make sure that integration on Python 2 works with unicode we will wrap quote
    to always pass bytes to it.
    """
    if not isinstance(input_v, binary_type):
        input_v = input_v.encode('utf-8')

    # No need to re-define the default for safe
    if safe:
        return quote_func(input_v, safe)
    return quote_func(input_v)

class AuthInfo(object):
    # Singleton
    __instance = None

    def __init__(self):
        self.headers = {}
        self.qradar_auth = None
        self.qradar_token = None
        self.username = None
        self.password = None
        self.api_url = None
        self.cafile = True
        self.rc = None

    @staticmethod
    def get_authInfo():
        if not AuthInfo.__instance:
            AuthInfo.__instance = AuthInfo()
        return AuthInfo.__instance

    def create(self, host, username=None, password=None, token=None, cafile=None,
               opts=None, function_opts=None):
        """
        Create headers used for REST Api calls
        :param host: QRadar host
        :param username: QRadar user login
        :param password: QRadar password
        :param token: Use token or username/password to auth
        :param cafile: Boolean or path to cafile
        :param opts: app.config options
        :param function_opts: Function parameters from app.config
        :return: None
        """
        self.headers = {'Accept': 'application/json'}
        if username and password:
            self.username = username
            self.password = password
            self.qradar_auth = b64encode((f'{username}:{password}').encode('ascii'))
            self.headers['Authorization'] = b"Basic " + self.qradar_auth
        elif token:
            self.qradar_token = token
            self.headers["SEC"] = self.qradar_token

        if host.startswith("http"):
            self.api_url = f"{host}/api/"
        else:
            self.api_url = f"https://{host}/api/"

        self.cafile = cafile
        self.rc = RequestsCommon(opts, function_opts)

    def make_call(self, method, url, headers=None, data=None, timeout=None):
        my_headers = headers if headers else self.headers

        def make_call_callback(response):
            # 404 is not found, such as reference not found or item not found in reference set
            if response.status_code in (404,):
                return response
            else:
                response.raise_for_status()
                return response

        return self.rc.execute(method, url, data=data, headers=my_headers, verify=self.cafile, callback=make_call_callback, timeout=timeout)

class ArielSearch(SearchWaitCommand):
    """
    Subclass of SearchWaitCommand.
    Overrides/implements get_search_id, check_status, get_search_result for QRadar
    """

    def __init__(self, timeout=600, poll=5, graphql=False):
        self.range_start = 0
        self.range_end = 50
        self.query_all = False
        self.graphql = graphql
        super(ArielSearch, self).__init__(timeout, poll)

    def set_range_start(self, start):
        """
        Set range start for ariel search
        :param start: int for range start
        :return: None
        """
        self.range_start = start

    def set_range_end(self, end):
        """
        Set range end for ariel search
        :param end: int for range end
        :return: None
        """
        self.range_end = end

    def set_timeout(self, timeout):
        """
        Set timeout
        :param timeout: Length to timeout in seconds
        :return: None
        """
        self.search_timeout = timeout

    def set_query_all(self, query_all):
        """
        Set bool to determine if range header is necessary
        :param query_all: (boolean)
        :return: None
        """
        self.query_all = query_all

    def get_search_id(self, query):
        """
        Get the search if associated with the search using query
        :param query: Input query string
        :return: search_id returned from QRadar
        """
        auth_info = AuthInfo.get_authInfo()
        try:
            response = auth_info.make_call("POST",
                                           f"{auth_info.api_url}{qradar_constants.ARIEL_SEARCHES}",
                                           data = {"query_expression": query.encode("utf-8")},
                                           headers = auth_info.headers.copy())
        except Exception as e:
            LOG.error(str(e))
            raise SearchJobFailure(query)

        res = response.json()
        search_id = ""
        if "search_id" in res:
            search_id = res["search_id"]
        elif "cursor_id" in res:
            search_id = res["cursor_id"]

        return search_id

    def delete_search(self, search_id):
        """Deletes an AQL search in case of timeout or error"""
        auth_info = AuthInfo.get_authInfo()
        response = None
        try:
            response = auth_info.make_call("DELETE",
                                           f"{auth_info.api_url}{qradar_constants.ARIEL_SEARCHES_DELETE.format(search_id)}",
                                           headers = auth_info.headers.copy())
        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, None)

        return response.status_code in [200, 202]

    def get_search_result(self, search_id):
        """
        Get search result associated with search_id
        :param search_id: ID
        :return: Dict with events
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        response = None

        # If the # of returned items is big, this call will take a long time!
        # Need to use Range to limit the # if query_all is False.
        # If query_all is True, the Range will not be used and all the results will be returned from the query.
        if not self.query_all:
            headers[b"Range"] = f"items={str(self.range_start)}-{str(self.range_end)}"

        if self.graphql:
            headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        try:
            response = auth_info.make_call("GET", f"{auth_info.api_url}ariel/searches/{search_id}/results", headers=headers)
        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, None)

        res = response.json()
        ret = {}
        if response.status_code in [200, 206]:
            events = res["events"] if "events" in res else res["flows"] if "flows" in res else res["other"]
            ret = {"events": [{key: f"{event[key]}" for key in event} for event in events if isinstance(event, dict)]}

        return ret

    def check_status(self, search_id):
        """
        Check the search status associated with search_id
        :param search_id: ID
        :return: Search status
        """
        auth_info = AuthInfo.get_authInfo()
        status = SearchWaitCommand.SEARCH_STATUS_ERROR_STOP
        try:
            response = auth_info.make_call("GET", f"{auth_info.api_url}{qradar_constants.ARIEL_SEARCHES}/{search_id}")
        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, status)

        res = response.json()
        if res.get("status"):
            if res["status"] == qradar_constants.SEARCH_STATUS_COMPLETED:
                status = SearchWaitCommand.SEARCH_STATUS_COMPLETED
            elif res["status"] in [qradar_constants.SEARCH_STATUS_WAIT, "SORTING", "EXECUTE"]:
                status = SearchWaitCommand.SEARCH_STATUS_WAITING

        return status

class QRadarClient(object):

    def __init__(self, host, username=None, password=None, token=None, cafile=None,
                 opts=None, function_opts=None):
        """
        Init
        :param host: QRadar host
        :param username: QRadar user name
        :param password: QRadar password
        :param token: QRadar token
        :param cafile: Verify cert or not
        :param opts: app.config options dictionary
        :param function_opts: Function parameters from app.config
        :return: None
        """
        auth_info = AuthInfo.get_authInfo()
        auth_info.create(host, username, password, token, cafile, opts, function_opts)

    def get_versions(self):
        """
        Util function used to test connectivity to QRadar
        :return: response
        """
        auth_info = AuthInfo.get_authInfo()
        return auth_info.make_call("GET", f"{auth_info.api_url}help/versions")

    def ariel_graphql_search(self, temp_query, search_query, query_all=False, range_start=None,
                             range_end=None, timeout=None):
        """
        Perform an Ariel search
        :param query_all: Bool used to decide if Range header is included in query
        :param query: Query string
        :param range_start: Range start for ariel search
        :param range_end: Range end for ariel search
        :param timeout: Timeout for search
        :return: Dict with events
        """
        ariel_search = ArielSearch(graphql=True)
        if range_start:
            ariel_search.set_range_start(range_start)

        if range_end:
            ariel_search.set_range_end(range_end)

        if timeout:
            ariel_search.set_timeout(timeout)

        ariel_search.set_query_all(query_all)

        response = ariel_search.perform_search(temp_query, False) # Execute the query on a temp table
        response = ariel_search.perform_search(search_query, True) # Get the actual query results from temp table

        return response

    def verify_connect(self):
        """
        QRadar does not support session key. Check version to verify
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

        return True if resp.status_code == 200 and len(resp.json()) > 0 and "version" in resp.json()[0] else False

    @staticmethod
    def verify_graphql_connect():
        """
        Verify if a connection to graphql on the given QRadar server can be made
        :return: (boolean) True if response.status_code equals 200 and False if it does not
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))
        headers["Content-Type"] = "application/json"

        try:
            response = auth_info.make_call("POST",
                                           f"{auth_info.api_url.replace('api/', '')}{qradar_constants.GRAPHQL_URL}",
                                           data=dumps({"operationName": "getSystemDate", "variables": {}, "query": GRAPHQL_SYSTEMDATE}),
                                           headers=headers)
        except Exception as e:
            pass

        return response.status_code == 200

    @staticmethod
    def graphql_query(variables, query_name, add_content_source=None):
        """
        Query graphql and return data
        :param variables: Dictionary of variables
        :param query_name: Name of the query from qradar_graphql_queries.py
        :param add_content_source: Additional location to content in ret variable
        :return: Data received from running graphql query
        """
        auth_info = AuthInfo.get_authInfo()
        headers = auth_info.headers.copy()
        headers["Content-Type"] = "application/json"
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))

        query_name = query_name.replace("  ", "")
        url = f"{auth_info.api_url.replace('api/', '')}{qradar_constants.GRAPHQL_URL}"
        operationName = query_name[query_name.index(" ")+1: query_name.index("(")]
        query_call = query_name[query_name.index("\n")+1: query_name.index("(", query_name.index("\n")+2)]

        try:
            response = auth_info.make_call("POST", url,
                                           data=dumps({"operationName": operationName, "variables": variables, "query": query_name}),
                                           headers=headers)
        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [{query_call.strip()} call failed with exception {str(e)}]")

        ret = {"status_code": response.status_code}

        if add_content_source:
            ret["content"] = response.json()["data"].get(query_call.strip()).get(add_content_source)
        else:
            ret["content"] = response.json()["data"].get(query_call.strip())

        return ret

    @staticmethod
    def get_qr_sessionid(host):
        """
        Get QRadar Session Id
        :param host: QRadar address (IP/URL)
        :return: QRadar session ID
        """
        auth_info = AuthInfo.get_authInfo()
        cookies = {}

        try:
            if not auth_info.username and not auth_info.password:
                cookies = {"SEC": auth_info.qradar_token}
            else:
                res = get(f"{host}console/logon.jsp", verify=auth_info.cafile)
                cookies = res.cookies.get_dict()

                res = post(f"{host}{qradar_constants.GRAPHQL_BASICAUTH}",
                            data = {"j_username": auth_info.username,
                                    "j_password": auth_info.password,
                                    "LoginCSRF": post(f"{host}{qradar_constants.GRAPHQL_BASICAUTH}",
                                                      data = {"get_csrf": ""},
                                                      headers = {"Cookie": f"JSESSIONID={cookies['JSESSIONID']}"},
                                                      verify = auth_info.cafile).text},
                            headers = {"Cookie": f"JSESSIONID={cookies['JSESSIONID']}"},
                            verify = auth_info.cafile)
                cookies = res.cookies.get_dict()
        except Exception as e:
            LOG.error(str(e))

        return "; ".join([f"{x}={cookies[x]}" for x in cookies.keys()])

class QRadarServers():
    def __init__(self, opts):
        """
        Initialize the odbcDBs class
        :param opts: Dict of options
        """
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        """
        Create list of label names and a dictionary of the databases and their configs
        :param opts: Dict of options
        :return dbs: Dictonary of all the ODBC databases from the app.config that contains each databases configurations
        :return db_name_list: List filled with all of the labels for the servers from the app.config
        """
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_name = f"{server}"
            server_data = opts.get(server_name)
            if not server_data:
                raise KeyError(f"Unable to find QRadar server: {server_name}")

            servers[server] = server_data

        return servers, server_name_list

    def qradar_label_test(qradar_label, servers_list):
        """
        Check if the given qradar_label is in the app.config
        :param qradar_label: User selected server
        :param servers_list: List of QRadar servers
        :return: Dictionary of options for choosen server
        """
        # If label not given and using previous versions app.config [fn_qradar_integration]
        if not qradar_label and servers_list.get(qradar_constants.PACKAGE_NAME):
            return servers_list[qradar_constants.PACKAGE_NAME]
        elif not qradar_label:
            raise IntegrationError("No label was given and is required if servers are labeled in the app.config")

        label = f"{qradar_constants.PACKAGE_NAME}:{qradar_label}"
        if qradar_label and label in servers_list:
            options = servers_list[label]
        elif len(servers_list) == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError(f"{qradar_label} did not match labels given in the app.config")

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of QRadar server names defined in the app.config in fn_qradar_integration.
        :param opts: List of options
        :return: List of servers
        """
        return [key for key in opts.keys() if key.startswith(f"{qradar_constants.PACKAGE_NAME}:")]

    def get_server_name_list(self):
        """Return list of all server names"""
        return self.server_name_list
