# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v49.0.4423
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import datetime
import logging
from urllib.parse import urljoin
from base64 import b64encode
from urllib.parse import quote_plus, urljoin

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, readable_datetime, str_to_bool
from resilient_lib.components.templates_common import iso8601

#----------------------------------------------------------------------------------------
# This module is an open template for you to develop the methods necessary to interact
# with your endpoint solution. The only required method is:
#  query_entities_since_ts: get your entities (alerts, events, etc.) based on a timestamp
#       since the last time the poller ran
# Helper functions:
#  _make_headers: create the necessary API header for your endpoint communication
#  make_linkback_url: create a url for your alert, event, etc. to navigate back to your endpoint console
#  _get_uri: assemble the parts of your URL (base address, version information, command and arguments)
#  _api_call: perform the API call, passing parameters and check the returned status code before
#      returning the response object
#
# Review these functions which need modification. Currently they `raise IntegrationError("UNIMPLEMENTED")`
#   _make_headers,
#   query_entities_since_ts,
#   make_linkback_url,
#   _get_uri
#   _api_call

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_salesforce"

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

# E N D P O I N T S
TOKEN_URL = "https://{my_domain_url}/services/oauth2/token"
BASE_URL = "https://{my_domain_url}"
QUERY_URI = "/services/data/{api_version}/query/?q=SELECT+FIELDS(ALL)+FROM+Case+LIMIT+200"
QUERY_URI_BY_DATE = "/services/data/{api_version}/query/?q=SELECT+FIELDS(ALL)+FROM+Case+WHERE+LastModifiedDate+>+{time}+LIMIT+200"
LINKBACK_URL = "https://{my_domain_name}.lightning.force.com/lightning/r/Case/{entity_id}/view"

class AppCommon():
    def __init__(self, rc, package_name, app_configs):
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """

        self.package_name = package_name
        self.my_domain_name = app_configs.get("my_domain_name")
        self.my_domain_url = app_configs.get("my_domain_url")
        self.api_version = app_configs.get("api_version")
        self.client_id = app_configs.get("consumer_key")
        self.client_secret = app_configs.get("consumer_secret")
        self.base_url = BASE_URL.format(my_domain_url=self.my_domain_url, api_version=self.api_version)
        self.token_url = TOKEN_URL.format(my_domain_url=self.my_domain_url)
        self.rc = rc
        self.verify = _get_verify_ssl(app_configs)
        self.access_token = self.get_token()

        # Setup access token in the header for making Salesforce REST API calls 
        if self.access_token:
            self.headers = self._make_headers(self.access_token)
        else:
            raise IntegrationError("Unable to get access token from Salesforce!")

        # Specify any additional parameters needed to communicate with your endpoint solution

    def get_token(self) -> str:
        """
        Get an API access token for Salesforce authentication.

        :return: API Access token (string)
        """
        uri = self.token_url

        auth_str = f"{self.client_id}:{self.client_secret}"
        auth_bytes = b64encode(auth_str.encode("utf-8"))
        encoded_auth = str(auth_bytes, "utf-8")

        headers = {
            "Authorization": "Basic {}".format(encoded_auth),
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = self.rc.execute("POST", uri, headers=headers, data="grant_type=client_credentials")

        response_json = response.json()

        return response_json.get("access_token", None)
    
    def _get_uri(self, cmd):
        """
        Build API url
        :param cmd: portion of API: 
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.base_url, cmd)

    def _make_headers(self, token: str) -> dict :
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        header = HEADER.copy()
        # modify to represent how to build the header
        header['Authorization'] = f"Bearer {token}"
        header['Content-Type'] = 'application/json'

        return header  

    def _api_call(self, method, url, payload=None):
        """
        Make an API call to the endpoint solution and get back the response

        :param method: REST method to execute (GET, POST, PUT, ...)
        :type method: str
        :param url: URL to send request to
        :type url: str
        :param payload: JSON payload to send if a POST, defaults to None
        :type payload: dict|None
        :return: requests.Response object returned from the endpoint call
        :rtype: ``requests.Response``
        """    
        # <- ::CHANGE_ME:: there may be changes needed in here to
        # work with your endpoint solution ->

        return self.rc.execute(method,
                               url,
                               params=params,
                               json=payload,
                               headers=self._make_headers(),
                               verify=self.verify,
                               callback=callback)

    def query_entities_since_ts(self, timestamp: datetime, *args, **kwargs) -> list:
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """
        # Get the first batch of query results based
        readable_time = readable_datetime(timestamp)
        query_url = self.base_url + QUERY_URI_BY_DATE.format(api_version=self.api_version, time=readable_time)
        LOG.debug("Querying endpoint with %s", query_url)

        response = self.rc.execute("GET", url=query_url, headers=self.headers)
        response_json = response.json()
        records = response_json.get("records", [])
        query_results = []
        query_results.extend(records)
            
        done = response_json.get("done", True)
        while not done:
            if response_json.get("nextRecordsUrl", None) == None:
                IntegrationError("No nextRecordsUrl key returned from Salesforce REST API case query!")

            # Get URL for next batch of results using the link sent back from Salesforce 
            query_url = self._get_uri(response_json.get("nextRecordsUrl"))
            LOG.debug("Querying endpoint with %s", query_url)

            # Get the next batch of cases 
            response = self.rc.execute("GET", url=query_url, headers=self.headers)
            response_json = response.json()
            records = response_json.get("records", [])

            query_results.extend(records)

            # Check if we are done
            done = response_json.get("done", True)
        return query_results

    def make_linkback_url(self, entity_id: str) -> str:
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: string to in which one can format the entity ID to join to the base url
        :type linkback_url: str
        :return: completed url for linkback
        :rtype: str
        """
        #https://ibmc4s-qradar-dev-dev-ed.develop.lightning.force.com/lightning/r/Case/500Hr00001Vhr73IAB/view

        return LINKBACK_URL.format(my_domain_name=self.my_domain_name, entity_id=entity_id)


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
            resp = response.json()
            msg = resp.get('messages') or resp.get('message')
            details = resp.get('details')
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = u"Error: \n    status code: {0}\n    message: {1}\n    details: {2}".format(
            response.status_code,
            msg,
            details)

    return response, error_msg

def _get_verify_ssl(app_configs: dict) -> bool:
    """
    Get ``verify`` parameter from app config.
    Value can be set in the [fn_my_app] section

    :param opts: All of the app.config file as a dict
    :type opts: dict
    :param app_options: App specific configs
    :type app_options: dict
    :return: Value to set ``requests.request.verify`` to. Either a path or a boolean. Defaults to ``True``
    :rtype: bool|str(path)
    """
    # start checking the app specific settings
    verify = app_configs.get("verify")

    # because verify can be either a boolean or a path,
    # we need to check if it is a string with a boolean 
    # value first then, and only then, we convert it to a bool
    # NOTE: that this will then only support "true" or "false"
    # (case-insensitive) rather than the normal "true", "yes", etc...
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    return verify