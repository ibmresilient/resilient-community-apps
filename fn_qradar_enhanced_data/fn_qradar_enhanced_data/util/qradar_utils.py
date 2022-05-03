# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
#   Util classes for qradar

from json import dumps
from six import binary_type
from base64 import b64encode
from logging import getLogger
from requests import get, post
from urllib.parse import quote as quote_func
from resilient_lib import RequestsCommon, IntegrationError
from fn_qradar_enhanced_data.util.function_utils import fix_dict_value
import fn_qradar_enhanced_data.util.qradar_constants as qradar_constants
from fn_qradar_enhanced_data.util.qradar_graphql_queries import GRAPHQL_SYSTEMDATE
from fn_qradar_enhanced_data.util.SearchWaitCommand import SearchWaitCommand, SearchFailure, SearchJobFailure

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
            self.qradar_auth = b64encode((username + ':' + password).encode('ascii'))
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

    def delete_search(self, search_id):
        """
        Deletes an AQL search in case of timeout or error
        """
        auth_info = AuthInfo.get_authInfo()

        url = auth_info.api_url + qradar_constants.ARIEL_SEARCHES_DELETE.format(search_id)

        headers = auth_info.headers.copy()

        response = None

        try:
            response = auth_info.make_call("DELETE", url, headers=headers)
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

        url = auth_info.api_url + "ariel/searches/{}/results".format(search_id)

        headers = auth_info.headers.copy()
        # If the # of returned items is big, this call will take a long time!
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
            events = fix_dict_value(events)
            ret = {"events": events}

        return ret

    def check_status(self, search_id):
        """
        Check the search status associated with search_id
        :param search_id: ID
        :return: Search status
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
                    or json_dict["status"] == "SORTING" \
                        or json_dict["status"] == "EXECUTE":
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
        :return: 
        """
        auth_info = AuthInfo.get_authInfo()

        url = auth_info.api_url + "help/versions"
        response = auth_info.make_call("GET", url)

        return response

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
        if range_start is not None:
            ariel_search.set_range_start(range_start)

        if range_end is not None:
            ariel_search.set_range_end(range_end)

        if timeout is not None:
            ariel_search.set_timeout(timeout)

        ariel_search.set_query_all(query_all)

        response = ariel_search.perform_search(temp_query,False) # Execute the query on a temp table
        response = ariel_search.perform_search(search_query, True) # Get the actual query results from temp table

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
        """
        Verify if a connection to graphql on the given QRadar server can be made
        :return: (boolean) True if response.status_code equals 200 and False if it does not
        """
        auth_info = AuthInfo.get_authInfo()
        url = u"{}{}".format(auth_info.api_url.replace("api/", ""), qradar_constants.GRAPHQL_URL)
        headers = auth_info.headers.copy()
        headers["Cookie"] = QRadarClient.get_qr_sessionid(auth_info.api_url.replace("api/", ""))
        headers["Content-Type"] = "application/json"
        data = {"operationName":"getSystemDate","variables":{},"query":GRAPHQL_SYSTEMDATE}

        try:
            response = auth_info.make_call("POST", url, data=dumps(data), headers=headers)
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
        operationName = query_name[query_name.index(" ")+1:query_name.index("(")]
        query_call = query_name[query_name.index("\n")+1:query_name.index("(", query_name.index("\n")+2)]

        url = u"{}{}".format(auth_info.api_url.replace("api/",""), qradar_constants.GRAPHQL_URL)
        data = {"operationName":operationName,"variables":variables,"query":query_name}
        ret = {}

        try:
            response = auth_info.make_call("POST", url, data=dumps(data), headers=headers)

            ret["status_code"] = response.status_code

            if add_content_source:
                ret["content"] = response.json()["data"][query_call.strip()][add_content_source]
            else:
                ret["content"] = response.json()["data"][query_call.strip()]

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError("Request to url [{}] throws exception. Error [{} call failed with exception {}]".format(url, query_call.strip(), str(e)))

        return ret

    @staticmethod
    def get_qr_sessionid(host):
        """
        Get QRadar Session Id
        :param host: QRadar address (IP/URL)
        :return: QRadar session ID
        """
        cookies = {}

        try:
            auth_info = AuthInfo.get_authInfo()

            if not auth_info.username and not auth_info.password:
                cookies = {"SEC":auth_info.qradar_token}
            else:
                res = get("{0}console/logon.jsp".format(host), verify=auth_info.cafile)
                cookies = res.cookies.get_dict()

                res = post("{0}{1}".format(host, qradar_constants.GRAPHQL_BASICAUTH), data={"j_username":auth_info.username,"j_password":auth_info.password,"LoginCSRF":post("{0}{1}".format(host, qradar_constants.GRAPHQL_BASICAUTH), data={"get_csrf": ""}, headers={"Cookie": "JSESSIONID="+cookies["JSESSIONID"]}, verify=auth_info.cafile).text}, headers={"Cookie": "JSESSIONID="+cookies["JSESSIONID"]}, verify=auth_info.cafile)
                cookies = res.cookies.get_dict()
        except Exception as e:
            LOG.error(str(e))

        return "; ".join([x+"="+cookies[x] for x in cookies.keys()])

class QRadarServers():
    def __init__(self, opts, options):
        self.servers, self.server_name_list = self._load_servers(opts, options)

    def _load_servers(self, opts, options):
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_name = u"{}".format(server)
            server_data = opts.get(server_name)
            if not server_data:
                raise KeyError(u"Unable to find QRadar server: {}".format(server_name))
            
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

        label = qradar_constants.PACKAGE_NAME+":"+qradar_label
        if qradar_label and label in servers_list:
            options = servers_list[label]
        elif len(servers_list) == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError("{} did not match labels given in the app.config".format(qradar_label))

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of QRadar server names defined in the app.config in fn_qradar_integration.
        :param opts: List of options
        :return: List of servers
        """
        server_list = []
        for key in opts.keys():
            if key.startswith("{}:".format(qradar_constants.PACKAGE_NAME)):
                server_list.append(key)
        return server_list

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list
