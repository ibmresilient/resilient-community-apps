# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v49.0.4423

import logging
from urllib.parse import urljoin

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, readable_datetime, str_to_bool

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

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

# E N D P O I N T S
# define the endpiont api calls your app will make to the endpoint solution. Below are examples
#ALERT_URI = "alert/{}/"
#POLICY_URI = "policy/"

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
        self.api_key = app_configs.get("api_key", "<- ::CHANGE_ME:: change to default for API Key or remove default ->")
        self.api_secret = app_configs.get("api_secret","<- ::CHANGE_ME:: change to default for API secret or remove default ->")
        self.endpoint_url = app_configs.get("endpoint_url", "<- ::CHANGE_ME:: change to default for endpoint url or remove default ->")
        self.rc = rc
        self.verify = _get_verify_ssl(app_configs)

        # Specify any additional parameters needed to communicate with your endpoint solution

    def _get_uri(self, cmd):
        """
        Build API url
        <- ::CHANGE_ME:: change this to reflect the correct way to build an API call ->

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        raise IntegrationError("UNIMPLEMENTED")
        return urljoin(self.endpoint_url, cmd)

    def _make_headers(self, token):
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        raise IntegrationError("UNIMPLEMENTED")
        header = HEADER.copy()
        # modify to represent how to build the header

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

    def query_entities_since_ts(self, timestamp, *args, **kwargs):
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """
        # <- ::CHANGE_ME:: -> for the specific API calls
        # and make sure to properly handle pagination!
        raise IntegrationError("UNIMPLEMENTED")
        query = {
            "query_field_name": readable_datetime(timestamp) # utc datetime format
        }

        LOG.debug("Querying endpoint with %s", query)
        response, err_msg = self._api_call("GET", 'alerts', query, refresh_authentication=True)
        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None

        return response.json()

    def make_linkback_url(self, entity_id, linkback_url):
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: string to in which one can format the entity ID to join to the base url
        :type linkback_url: str
        :return: completed url for linkback
        :rtype: str
        """
        raise IntegrationError("UNIMPLEMENTED")
        return urljoin(self.endpoint_url, linkback_url.format(entity_id))


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

def _get_verify_ssl(app_configs):
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