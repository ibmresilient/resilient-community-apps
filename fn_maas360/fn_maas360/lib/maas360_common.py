# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
from resilient_lib.components.integration_errors import IntegrationError

LOG = logging.getLogger(__name__)


class MaaS360Utils(object):
    """
    Helper object MaaS360Utils.
    """
    def __init__(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey, auth_url, requests_common):
        """
        Constructor for MaaS360Utils
        Note: Object will not be created if auth token is not generated successfully

        :param host: web-services host
        :param billingId: billingId of the customer
        :param userName: user name of the portal admin
        :param password: password of the portal admin
        :param appID:
        :param appVersion:
        :param platformID:
        :param appAccessKey:
        :param auth_url:
        :param requests_common:
        """
        self.host = host
        self.billingId = billingId
        self.rc = requests_common
        # generating auth token and setting it in the object, to be used in further api calls
        self.authToken = self.generate_auth_token(host, billingId, userName, password, appID, appVersion, platformID,
                                                  appAccessKey, auth_url)

    def generate_auth_token(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey, auth_url):
        """
        Generates auth token with given user credentials
        :param host:
        :param billingId:
        :param userName:
        :param password:
        :param appID:
        :param appVersion:
        :param platformID:
        :param appAccessKey:
        :return: String, auth token, if auth token is generated for portal admin or an error
        """
        complete_auth_url = host + auth_url + billingId
        auth_request_body = {
            "authRequest": {
                "maaS360AdminAuth": {
                    "billingID": billingId,
                    "password": password,
                    "userName": userName,
                    "appID": appID,
                    "appVersion": appVersion,
                    "platformID": platformID,
                    "appAccessKey": appAccessKey
                }
            }
        }
        auth_headers = {'Accept': 'application/json'}
        try:
            auth_response_json = self.rc.execute_call("post", complete_auth_url, auth_request_body, headers=auth_headers)
        except IntegrationError as err:
            raise err

        if auth_response_json:
            if auth_response_json.get("authResponse") and auth_response_json.get("authResponse").get("errorCode") == 0:
                return auth_response_json.get("authResponse").get("authToken")
        else:
            raise IntegrationError(auth_response_json)

    def get_devices(self, basic_search_url, query_string):
        """
        Search for devices by Device Name, Username, Phone Number, Platform, Device Status and other Device Identifiers.
        Support for partial match for Device Name, Username, Phone Number.
        :param basic_search_url:
        :param query_string:
        :return: count, device or list of devices or None if there aren't any found
        """

        url_endpoint = self.host + basic_search_url + self.billingId

        auth_headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'MaaS token="' + self.authToken + '"'}
        try:
            results_basic_search = self.rc.execute_call("get", url_endpoint, query_string, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise err

        devices = results_basic_search.get("devices")
        if not devices:
            return None, None

        count = devices.get("count")
        if not count:
            return None, None

        return count, devices
