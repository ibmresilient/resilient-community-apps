# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Util classes for qradar

from base64 import b64encode
from logging import getLogger
from six import binary_type
from typing import Union
from fn_qradar_integration.util.SearchWaitCommand import SearchWaitCommand, SearchFailure, SearchJobFailure
from fn_qradar_integration.util import function_utils
from resilient_lib import RequestsCommon, IntegrationError
import fn_qradar_integration.util.qradar_constants as qradar_constants
from fn_qradar_integration.lib.reference_data.ReferenceTableFacade import ReferenceTableFacade
from urllib.parse import quote as quote_func, urljoin, urlencode

LOG = getLogger(__name__)
FORWARD_SLASH = b'%2F'
ARIEL_SEARCHES_DELETE = "ariel/searches/{}"
OFFENSES_ENDPOINT = "siem/offenses/"
NOTE_MARKER = "\x03"

def quote(input_v, safe=None):
    """
    To make sure that integration on Python 2 works with unicode we will wrap quote
    to always pass bytes to it.
    """
    if not isinstance(input_v, binary_type):
        input_v = input_v.encode('utf-8')

    input_v = input_v.replace(b'/', FORWARD_SLASH)
    # No need to re-define the default for safe
    if safe:
        return quote_func(input_v, safe)
    return quote_func(input_v)

class QRadarServers():
    def __init__(self, opts, options):
        self.servers, self.server_name_list = self._load_servers(opts, options)

    def _load_servers(self, opts, options):
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_name = f"{server}"
            server_data = opts.get(server_name)
            if not server_data:
                raise KeyError(f"Unable to find QRadar server: {server_name}")

            servers[server] = server_data

        return servers, server_name_list

    @staticmethod
    def qradar_label_test(qradar_label, servers_list):
        """
        Check if the given qradar_label is in the app.config
        :param qradar_label: User selected server
        :param servers_list: list of qradar servers
        :return: dictionary of options for chosen server
        """
        # If label not given and using previous versions app.config [fn_qradar_integration]
        if not qradar_label and servers_list.get(qradar_constants.PACKAGE_NAME):
            return servers_list[qradar_constants.PACKAGE_NAME]
        if not qradar_label:
            raise IntegrationError("No label was given and is required if servers are labeled in the app.config")

        label = qradar_constants.PACKAGE_NAME+":"+qradar_label
        if qradar_label and label in servers_list:
            options = servers_list[label]
        elif (len(servers_list) == 1 and qradar_label == qradar_constants.PACKAGE_NAME) or len(servers_list) == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError(f"{qradar_label} did not match labels given in the app.config")

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of QRadar server names defined in the app.config in fn_qradar_integration.
        :param opts: list of options
        :return: list of servers
        """
        server_list = []
        for key in opts.keys():
            if key.startswith(f"{qradar_constants.PACKAGE_NAME}:"):
                server_list.append(key)
        return server_list

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list

class AuthInfo(object):
    # Singleton
    __instance = None

    def __init__(self):
        self.headers = {}
        self.qradar_auth = None
        self.qradar_token = None
        self.api_url = None
        self.cafile = True
        self.rc = None

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
            self.qradar_auth = b64encode(
                (username + ':' + password).encode('ascii'))
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

    def make_call(self, method, url, headers=None, data=None):
        my_headers = headers if headers else self.headers

        def make_call_callback(response):
            # 404 is not found, such as reference not found or item not found in reference set
            if response.status_code in (404,):
                return response

            response.raise_for_status()
            return response

        return self.rc.execute_call_v2(method, url, data=data, headers=my_headers, verify=self.cafile, callback=make_call_callback)

class ArielSearch(SearchWaitCommand):
    """
    Subclass of SearchWaitCommand.
    Overrides/implements get_search_id, check_status, get_search_result for QRadar
    """

    def __init__(self, timeout=600, poll=5):
        self.range_start = 0
        self.range_end = 50
        self.query_all = False
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
        url = auth_info.api_url + qradar_constants.ARIEL_SEARCHES
        utf8 = query.encode("utf-8")
        data = {"query_expression": utf8}

        search_id = ""
        try:
            response = auth_info.make_call("POST", url, data=data)

            json = response.json()
            if "search_id" in json:
                search_id = json["search_id"]
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
        url = auth_info.api_url + \
            qradar_constants.ARIEL_SEARCHES_RESULT.format(search_id)

        headers = auth_info.headers.copy()
        # if the # of returned items is big, this call will take a long time!
        # Need to use Range to limit the # if query_all is False.
        # If query_all is True, the Range will not be used and all the results will be returned from the query.
        if not self.query_all:
            headers[b"Range"] = f"items={str(self.range_start)}-{str(self.range_end)}"

        response = None
        try:
            response = auth_info.make_call("GET", url, headers=headers)
        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, None)

        ret = {}
        if int(response.status_code/100) == 2:
            events = response.json()["events"]
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
        url = f"{auth_info.api_url}{qradar_constants.ARIEL_SEARCHES}/{search_id}"
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

    def delete_search(self, search_id):
        """
        Deletes an AQL search in case of timeout or error
        """
        auth_info = AuthInfo.get_authInfo()

        url = urljoin(auth_info.api_url, ARIEL_SEARCHES_DELETE.format(search_id))
        headers = auth_info.headers.copy()

        response = None
        try:
            response = auth_info.make_call("DELETE", url, headers=headers)
        except Exception as e:
            LOG.error(str(e))
            raise SearchFailure(search_id, None)

        return response.status_code in [200, 202]

class QRadarClient(object):
    # QRadarClient has-a ReferenceTableFacade
    reference_tables = ReferenceTableFacade()
    auth_info = AuthInfo.get_authInfo()

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
        auth_info.create(host, username, password, token,
                         cafile, opts, function_opts)

    def check_openssl(self):
        """
        Do we need to verify openssl version?
        :return:
        """

    def get_versions(self):
        """
        Util function used to test connectivity to QRadar
        :return:
        """
        auth_info = AuthInfo.get_authInfo()

        url = auth_info.api_url + qradar_constants.HELP_VERSIONS
        response = auth_info.make_call("GET", url)

        return response

    def ariel_search(self, query, query_all, range_start=None, range_end=None, timeout=None):
        """
        Perform an Ariel search
        :param query_all: bool used to decide if Range header is included in query
        :param query: query string
        :param range_start:
        :param range_end:
        :param timeout: timeout for search
        :return: dict with events
        """
        ariel_search = ArielSearch()
        if range_start is not None:
            ariel_search.set_range_start(range_start)

        if range_end is not None:
            ariel_search.set_range_end(range_end)

        if timeout is not None:
            ariel_search.set_timeout(timeout)

        ariel_search.set_query_all(query_all)

        response = ariel_search.perform_search(query)
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
        if int(resp.status_code/100) == 2 and len(resp.json()) > 0:
            if "version" in resp.json()[0]:
                connected = True

        return connected

    @staticmethod
    def get_all_ref_set():
        """
        Get a list of all the reference sets.
        :return: list of reference set names
        """
        auth_info = AuthInfo.get_authInfo()
        url = f"{auth_info.api_url}{qradar_constants.REFERENCE_SET_URL}"
        ret = []
        try:
            response = auth_info.make_call("GET", url)
            ret = response.json()
        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [get_all_ref_set call failed with exception {str(e)}]")

        return ret

    @staticmethod
    def find_all_ref_set_contains(value):
        """
        Find all reference sets that contain user given value
        :param value: Value given by user
        :return: List of reference sets that contain the user given value
        """
        ref_sets = QRadarClient.get_all_ref_set()
        LOG.debug(f"All reference sets: {ref_sets}")

        ret = []
        for r_set in ref_sets:
            LOG.debug(f"Looking for {value} in reference set {r_set.get('name')}")
            element = QRadarClient.search_ref_set(r_set.get("name"), value)
            if element.get("found"):
                ret.append(element.get("content", {}))

        return ret

    @staticmethod
    def search_ref_set(ref_set, filter=None):
        """
        Search a reference set using the filter
        :param ref_set: Reference set name
        :param filter:
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        # Build base url for search
        url = f"{auth_info.api_url}{qradar_constants.REFERENCE_SET_URL}/{ref_set}"

        ret = None
        try:
            if filter:
                # Add filter to the search url
                url += f'?filter=value="{filter}"'
            # Make call to QRadar server to perform search on the reference set
            response = auth_info.make_call("GET", url)

            ret = {"status_code": response.status_code,
                    # If data is returned from the search and the status code is 2xx then found equals True, else False.
                    "found": len(response.json().get("data", [])) > 0 and int(response.status_code /100) == 2,
                    "content": response.json()}

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [search_ref_set call failed with exception {str(e)}]")

        return ret

    @staticmethod
    def add_ref_element(ref_set, value):
        """
        Add the value to the given ref_set
        :param ref_set: Name of reference set.
        :param value: Value given by user
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        ref_set_link = quote(ref_set, '')
        url = f"{auth_info.api_url}{qradar_constants.REFERENCE_SET_URL}/{ref_set_link}"

        ret = None
        try:
            data = {"value": value}
            response = auth_info.make_call("POST", url, data=data)

            ret = {"status_code": response.status_code,
                   "content": response.json()}

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError(f"Request to url [{url}] throws exception. Error [add_ref_element call failed with exception {str(e)}]")

        return ret

    @staticmethod
    def delete_ref_element(ref_set, value, reference_endpoint=qradar_constants.REFERENCE_SET_URL):
        """
        Delete value from the given ref_set
        :param ref_set: Name of existing reference set
        :param value:
        :return:
        """
        auth_info = AuthInfo.get_authInfo()
        ref_set_link = quote(ref_set, '').replace("%20", "%2520")
        value = quote(value, '').replace("%20", "%2520")
        url = f"{auth_info.api_url}{reference_endpoint}/{ref_set_link}/{value}"

        ret = {}
        try:
            response = auth_info.make_call("DELETE", url)

            ret = {"status_code": response.status_code,
                   "content": response.json()}

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError(f"Delete request to url [{url}] throws exception. Error [delete_ref_element failed with exception {str(e)}]")

        return ret

    @classmethod
    def get_ref_table_element(cls, ref_table, reference_endpoint=qradar_constants.REFERENCE_TABLE_URL):
        """
        Get value from the given ref_table
        :param ref_table: Name of reference table.
        :param value:
        :return:
        """
        return cls.reference_tables.get_one_reference_table(AuthInfo.get_authInfo(), ref_table)

    @classmethod
    def update_ref_table_element(cls, ref_table, inner_key, outer_key, value, reference_endpoint=qradar_constants.REFERENCE_TABLE_URL):
        """
        Delete value from the given ref_table
        :param ref_table: Name of reference table.
        :param value:
        :return:
        """
        return cls.reference_tables.update_ref_element(AuthInfo.get_authInfo(), ref_table, inner_key, outer_key, value)

    @classmethod
    def delete_ref_table_element(cls, ref_table, inner_key, outer_key, value, reference_endpoint=qradar_constants.REFERENCE_TABLE_URL):
        """
        Delete value from the given ref_table
        :param ref_table: Name of reference table.
        :param value:
        :return:
        """
        return cls.reference_tables.delete_ref_element(AuthInfo.get_authInfo(), ref_table, inner_key, outer_key, value)

    def get_all_ref_tables(self):
        """
        :return: All reference tables
        """
        return self.reference_tables.get_all_reference_tables(AuthInfo.get_authInfo())

    @classmethod
    def add_ref_table_element(cls, ref_table, inner_key, outer_key, value):
        """
        Add the value to the given ref_table
        :param ref_table: Name of reference table.
        :param value:
        :return:
        """
        return cls.reference_tables.add_ref_element(AuthInfo.get_authInfo(), ref_table, inner_key, outer_key, value)

    @classmethod
    def update_offense(cls, offense_id: int, update_payload: dict) -> Union[None, dict]:
        """
        Method to update a QRadar offense
        :param offense_id: id of the offense to be updated (required)
        :param update_payload: dictionary of payload to update the offense
        :return: updated offense
        """
        offense_url_base = urljoin(cls.auth_info.api_url, urljoin(OFFENSES_ENDPOINT, str(offense_id)))

        encoded_params = urlencode(update_payload)

        offense_url = f"{offense_url_base}?{encoded_params}"

        LOG.debug("Making POST request to [%s]", offense_url)

        updated_offense = cls.auth_info.make_call("POST", offense_url)

        if not updated_offense:
            LOG.error('Unable to update Offense.')
            return None

        return updated_offense.json()

    @classmethod
    def create_offense_note(cls, offense_id: int, note_text: str) -> Union[None, dict]:
        """
        Method to attach a new note to an offense
        :param offense_id: id of the offense to which the note will be attached
        :param note_text: Text content of the note
        :return Newly created offense note from the supplied params
        """
        note_url_base = urljoin(cls.auth_info.api_url, urljoin(OFFENSES_ENDPOINT, str(offense_id)))
        note_url = f"{note_url_base}/notes"

        # Put our "marker" on the end so we know it is a note we created.
        notes = {"note_text": note_text+NOTE_MARKER}

        offense_note = cls.auth_info.make_call("POST", note_url, data=notes)

        if not offense_note:
            LOG.error('Unable to create offense note.')
            return None

        return offense_note.json()
