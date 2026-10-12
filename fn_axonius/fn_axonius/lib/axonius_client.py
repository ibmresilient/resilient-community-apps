# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
import logging
from urllib.parse import urljoin
from requests.exceptions import JSONDecodeError

from resilient_lib import (IntegrationError, RequestsCommon, validate_fields)

#----------------------------------------------------------------------------------------
# This module is an open template for you to develop the methods necessary to interact
# with your endpoint solution. The only required method is:
#  query_entities_since_ts: get your entities (alerts, events, etc.) based on a timestamp
#       since the last time the poller ran
# Helper functions:
#  authenticate: authenticate to your endpoint solution, yielding a token for ongoing API calls
#  _make_header: create the necessary API header for your endpoint communication
#  make_linkback_url: create a url for your alert, event, etc. to navigate back to your endpoint console
#  _get_uri: assemble the parts of your URL (base address, version information, command and arguments)
#  _api_call: perform the API call, passing parameters and check the returned status code before
#      returning the response object

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_axonius"

# URL prefix to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "{organization_name}/targets/{target_id}"

HEADER = { "accept": "application/json",
           "content-type": "application/json" }

# E N D P O I N T S
GET_DEVICE_BY_ID_URI = "/api/{api_version}/assets/devices/{id}"
GET_DEVICES_URI = "/api/{api_version}/assets/devices"
GET_DEVICES_COUNT_URI = "/api/{api_version}/assets/devices/count"
GET_ENFORCEMENTS_URI = "/api/{api_version}/enforcements"
GET_USERS_URI = "/api/{api_version}/assets/users"
POST_ENFORCEMENTS_URI = "/api/{api_version}/enforcements/run"

DEFAULT_LIMIT = 1000
DEFAULT_AXONIUS_FIELDS = ["specific_data.data.network_interfaces.ips_preferred",
                          "specific_data.data.name",
                          "specific_data.data.hostname_preferred",
                          "specific_data.data.owner",
                          "specific_data.data.last_used_users_mail_association",
                          "specific_data.data.os.type_distribution",
                          "specific_data.data.last_used_users",
                          "specific_data.data.last_used_users_departments_association",
                          "specific_data.data.hard_drives.encryption_status",
                          "specific_data.data.device_disabled",
                          "specific_data.data.network_interfaces.security_level_preferred",
                          "specific_data.data.network_interfaces.region_preferred",
                          "specific_data.data.network_interfaces.country_preferred",
                          "labels"]
class AxoniusClient():
    def __init__(self, rc: RequestsCommon, package_name: str, app_configs: dict) -> None:
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """
        self.rc = rc
        self.package_name = package_name

        validate_fields(["endpoint_url", "api_key", "api_secret", "api_version"], app_configs)

        # required configs
        self.endpoint_url = app_configs.get("endpoint_url")
        self.api_key = app_configs.get("api_key")
        self.api_secret = app_configs.get("api_secret")
        self.api_version = app_configs.get("api_version")

        self.headers = self._make_headers(self.api_key, self.api_secret)



    def _make_headers(self, api_key: str, api_secret: str) -> dict:
        """ Build API header using API key and secret

        Args:
            api_key (str): API key
            api_secret (str): API secret 

        Returns:
            dict: header to make Axonius REST API calls.
        """

        header = HEADER.copy()
        # modify to represent how to build the header
        header["api-key"] = f"{api_key}"
        header["api-secret"] = f"{api_secret}"

        return header
    
    def get_endpoint_url(self):
        """Return the base URL.  This method is used in functions to pass the base URL in
        function results so that links back to the Axonius device can be created in a post script.

        Returns:
            str: base URL for links to devices in Axonius
        """
        return self.endpoint_url

    def get_device_count(self, query: str=None, saved_query_name: str=None):
        """Return the number of devices in the Axonius platform.  
           This function is used by self test as no parameters are required.

        Returns:
            dict: JSON results from Axonius REST API call to get device count
            str: Error message if API calls fails.
        """
        if not query and not saved_query_name:
            raise IntegrationError("Get Device Count requires a query string OR an save query name as a parameter.")
        
        url = urljoin(self.endpoint_url, GET_DEVICES_COUNT_URI.format(api_version=self.api_version))

        payload = {            
            "saved_query_name": saved_query_name,
            "query": query
        }
        response, error_msg = self.rc.execute("POST", url, headers=self.headers, json=payload, callback=callback)
        
        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return None, error_msg
        
        response_json = response.json()
        return response_json, None

    def get_device_by_id(self, id: str):
        """Returns an device asset (JSON format) in its entirety using the internal_axon_id.

        Args:
            id (str): Internal Axon ID

        Returns:
            dict: JSON results from Axonius REST API call to get device
            str: Error message if API calls fails.
        """
        url = urljoin(self.endpoint_url, GET_DEVICE_BY_ID_URI.format(api_version=self.api_version, id=id))
        params = {
            "return_empty_details": False, 
            "return_complex_fields": False
        }
        response, error_msg = self.rc.execute("GET", url, headers=self.headers, params=params, callback=callback)

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return None, error_msg

        response_json = response.json()
        return response_json, None
    
    def get_device_by_query(self, query: str=None, saved_query_name: str=None, fields: list=DEFAULT_AXONIUS_FIELDS, limit: int=DEFAULT_LIMIT):
        """ Get Axonius devices which match the specified query (AQL) string.

        Args:
            query (str, optional): Axonius query string used to search for devices. Defaults to None.
            saved_query_name (str, optional): Axonius saved query name used to search for devices. Defaults to None.
            fields (list, optional): Axonius device fields to be returned by the query. Defaults to [].

        Returns:
            list: list of device assets matching the query results
            str: Error message if API calls fails.
        """
        if not query and not saved_query_name:
            raise IntegrationError("Get Device by Query requires a query string OR an save query name as a parameter.")
        
        url = urljoin(self.endpoint_url, GET_DEVICES_URI.format(api_version=self.api_version))

        payload = {
            "include_metadata": True,
            "page": { "limit": DEFAULT_LIMIT if limit > DEFAULT_LIMIT else limit },
            "use_cache_entry": True,
            "return_plain_data": True,
            "fields": fields,
            "saved_query_name": saved_query_name,
            "query": query
        }

        response, error_msg = self.rc.execute("POST", url, headers=self.headers, json=payload, callback=callback)

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return None, error_msg

        response_json = response.json()


        meta = response_json.get("meta", None)
        if not meta:
            # No assets mostly likely if we get here
            return response_json.get("assets"), error_msg

        page = meta.get("page")
        size = page.get("size")
        if size >= limit:
            return response_json.get("assets"), error_msg

        # Drop through here if pagination is needed. 
        # In most cases we don't get here.
        assets, error_msg = self.paginate_results(response_json, url, payload, limit)
        return assets, error_msg
    
    def paginate_results(self, response_json: dict, url: str, payload: dict, limit: int):
        """ Paginate

        Args:
            response_json (dict): JSON response from the call to the first call to the endpoint
            url (str): REST API endpoint URL
            payload (dict): payload 
            limit (int): maximum number of results to return

        Returns:
            list: List of assets matching the query 
            str: Error message if an error occurs during REST API call 
        """
        assets = []
        error_msg = None
        if not response_json.get("assets"):
            # Return the assets list, error message tuple
            return assets, error_msg
        
        # Add first page of assets into the list
        assets.extend(response_json.get("assets"))
        # Collect the next page
        meta = response_json.get("meta")
        page = meta.get("page")
        total_pages = page.get("totalPages")
        offset = page.get("size")
        page_number = 2
        while offset < limit and page_number <= total_pages:
            # Set the payload to collect starting at the offset and set the limit so we get correct total
            payload["page"] = {"limit": DEFAULT_LIMIT if (limit - offset) > DEFAULT_LIMIT else (limit - offset), 
                               "offset": offset}
            response, error_msg = self.rc.execute("POST", url, headers=self.headers, json=payload, callback=callback)

            if error_msg:
                LOG.error("%s API call failed: %s", self.package_name, error_msg)
                return None, error_msg
            response_json = response.json()

            if response_json.get("assets"):
                # Add next batch of devices to the list 
                assets.extend(response_json.get("assets"))

            # Advance to the next page of results.
            meta = response_json.get("meta")
            page = meta.get("page")
            offset = offset + page.get("size")
            page_number = page_number + 1

        # Return the assets list, error message tuple
        return assets, error_msg

    def get_enforcement_by_name(self, enforcement_name: str=None, limit: int=DEFAULT_LIMIT):
        """ Get Axonius enforcement which match the enforcement name.

        Args:
            query (str, optional): Axonius query string used to search for enforcement. Defaults to None.
            saved_query_name (str, optional): Axonius saved query name used to search for devices. Defaults to None.
            fields (list, optional): Axonius device fields to be returned by the query. Defaults to [].

        Returns:
            dict: JSON results from Axonius REST API call to get device information
            str: Error message if API calls fails.
        """
        if not enforcement_name:
            raise IntegrationError("Get Enforcement by Name requires an enforcement name.")
        
        url = urljoin(self.endpoint_url, GET_ENFORCEMENTS_URI.format(api_version=self.api_version))

        params = {
            "include_metadata": True,
            "limit": limit,
            "name": enforcement_name
        }

        response, error_msg = self.rc.execute("GET", url, headers=self.headers, params=params, callback=callback)

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return None, error_msg

        response_json = response.json()
        return response_json, None

    def run_enforcement(self, id):
        """ Run the enforcement set 

        Args:
            id (str): ID of the Axonius Enforcement Set to run.

        Returns:
            dict: JSON result value that includes the id and name of the enforcement set run
            str: error message returned from Axonius REST API 
        """

        url = urljoin(self.endpoint_url, POST_ENFORCEMENTS_URI.format(api_version=self.api_version))
        payload = { "value": { "ids": [id] } }

        response, error_msg = self.rc.execute("POST", url, headers=self.headers, json=payload, callback=callback)

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return None, error_msg

        response_json = response.json()
        return response_json, None
    
def callback(response):
    """
    Callback needed for certain REST API calls to return a formatted error message

    :param response: the requests response object
    :type response: ``requests.Response``
    :return: response, error_msg
    :rtype: tuple(``requests.Reponse``, str)
    """
    error_msg = None
    if response.status_code >= 300 and response.status_code <= 500:
        try:
            response_json = response.json()
            msg = response_json.get("error_id", None)
            errors = response_json.get("errors", None)
            if errors:
                error = errors[0].get("error", None)
                description = errors[0].get("description", None)
            else:
                error = None
                description = None
            details = f"{error} : {description}"
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = u"Error: \n    status code: {0}\n    message: {1}\n    reason: {2}".format(
                response.status_code,
                msg,
                details)

    return response, error_msg