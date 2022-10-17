# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json
import datetime
import pytz
from base64 import b64encode
import logging
from urllib.parse import urljoin

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, str_to_bool
from resilient_lib.components.templates_common import iso8601


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
#
# Review these functions which need modification. Currently they `raise IntegrationError("unimplemented")`
#   authenticate,
#   _make_header,
#   query_entities_since_ts,
#   make_linkback_url,
#   _get_uri

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_randori"

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

# URL prefix to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "{tenant_name}/targets/{target_id}"

# E N D P O I N T S
# define the endpiont api calls your app will make to the endpoint solution. Below are expamples
#ALERT_URI = "alert/{}/"
#POLICY_URI = "policy/"
GET_ALL_DETECTIONS_FOR_TARGET = "/recon/api/{api_version}/all-detections-for-target"
GET_VALIDATE = "/auth/api/{api_version}/validate"

TARGET_LIMIT = 2000

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
        self.api_token = app_configs.get("api_token")
        self.endpoint_url = app_configs.get("endpoint_url")
        self.api_version = app_configs.get("api_version")
        self.rc = rc
        self.verify = str_to_bool(app_configs.get("verify", "false"))
        self.tenant_name = app_configs.get("tenant_name")

        self.header = self._make_header(self.api_token)

    def _get_uri(self, cmd):
        """
        Build API url
        <- ::CHANGE_ME:: change this to reflect the correct way to build an API call ->

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.endpoint_url, cmd.format(api_version=self.api_version))

    def _make_header(self, token):
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """

        header = HEADER.copy()
        # modify to represent how to build the header
        header['Authorization'] = "Bearer {}".format(self.api_token)

        return header

    def _api_call(self, method, url, payload=None, refresh_authentication=False):
        """
        Make an API call to the endpoint solution and get back the response

        :param method: REST method to execute (GET, POST, PUT, ...)
        :type method: str
        :param url: URL to send request to
        :type url: str
        :param payload: JSON payload to send if a POST, defaults to None
        :type payload: dict|None
        :param refresh_authentication: boolean if a refresh is needed, defaults to False
        :type refresh_authentication: bool, optional
        :return: requests.Response object returned from the endpoint call
        :rtype: ``requests.Response``
        """    
        # <- ::CHANGE_ME:: there may be changes needed in here to
        # work with your endpoint solution ->


        if method in ["PUT", "POST"]:
            return self.rc.execute(method,
                                   self._get_uri(url),
                                   json=payload,
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)
        if payload:
            return self.rc.execute(method,
                                   self._get_uri(url),
                                   params=payload,
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)

        return self.rc.execute(method,
                               self._get_uri(url),
                               headers=self.header,
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
        :rtype: list of targets
        """
        iso_timestamp = iso8601(timestamp)

        query = {
            "condition": "OR",
            "rules": [
                {
                    "field": "table.target_first_seen",
                    "operator": "greater_or_equal",
                    "value": iso_timestamp
                },
                {
                    "field": "table.temptation_last_modified",
                    "operator": "greater_or_equal",
                    "value": iso_timestamp
                }
            ]
        }
        # Endpoint expects query to be base64 encoded.
        query = json.dumps(query)
        b64_query = b64encode(query.encode())


        params = {
            'q': b64_query, 
            'limit': TARGET_LIMIT
        }

        LOG.debug("Querying endpoint with %s", query)

        # Make at least one call to the get-all-detections-for-target endpoint to 
        # get the complete list of targets to be updated or created.  Keep looping
        # till we get the complete list.
        total_targets = -1
        offset = 0
        targets = []
        while offset > total_targets:
            params['offset'] = offset
            response = self.rc.execute("GET",
                                   self._get_uri(GET_ALL_DETECTIONS_FOR_TARGET),
                                   params=params,
                                   headers=self.header,
                                   verify=self.verify)
            response.raise_for_status()
            response_json = response.json()
            if response_json.get('count') == 0:
                break
            data = response_json.get('data')
            for target in data:
                targets.append(target)
            offset = offset + response_json.get('count')
            total_targets = response_json.get('total')
        return targets

    def make_linkback_url(self, entity_id, linkback_url=LINKBACK_URL):
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: _description_, defaults to LINKBACK_URL
        :type linkback_url: str|int, optional
        :return: completed url for linkback
        :rtype: str
        """
        return urljoin(self.endpoint_url, linkback_url.format(tenant_name=self.tenant_name, 
                                                              target_id=entity_id))

    def get_validate(self):
        response = self.rc.execute("GET",
                                   self._get_uri(GET_VALIDATE),
                                   headers=self.header,
                                   verify=self.verify)
        response.raise_for_status()
        return response.json()


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
