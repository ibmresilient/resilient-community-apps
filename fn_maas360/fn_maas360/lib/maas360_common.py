# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
import json
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib.components.requests_common import RequestsCommon

LOG = logging.getLogger(__name__)
JSON_CONTENT_TYPE = "application/json"
URL_ENCODED_FORM = "application/x-www-form-urlencoded"


class MaaS360Utils(object):
    """
    Helper object MaaS360Utils.
    """
    def __init__(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey, auth_url,
                 opts=None, options=None):
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
        :param opts
        :param options
        """
        self.host = host
        self.billingId = billingId
        self.rc = RequestsCommon(opts, options)

        # generating auth token and setting it in the object, to be used in further api calls
        self.authToken = self.generate_auth_token(host, billingId, userName, password, appID, appVersion, platformID,
                                                  appAccessKey, auth_url)

    def get_auth_token(self):
        """
        Return instance variable authToken.
        :return: authToken
        """
        return self.authToken

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
            results = self.rc.execute_call("post", complete_auth_url, auth_request_body, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to create MaaS360APIsHelper instance, "
                                   "subsequent api calls will be cancelled: {}".format(err))

        auth_response = results.get("authResponse")
        if auth_response and auth_response.get("errorCode") == 0:  # 0 no error
            return auth_response.get("authToken")
        else:
            raise IntegrationError("Unable to create MaaS360APIsHelper instance, "
                                   "subsequent api calls will be cancelled: {}".format(json.dumps(auth_response)))

    def basic_search(self, basic_search_url, query_string):
        """
        Search for devices by Device Name, Username, Phone Number, Platform, Device Status and other Device Identifiers.
        Support for partial match for Device Name, Username, Phone Number.
        :param basic_search_url:
        :param query_string:
        :return: device or list of devices or None if there aren't any found
        """

        url_endpoint = self.host + basic_search_url + self.billingId
        auth_headers = self.get_auth_headers(JSON_CONTENT_TYPE)

        try:
            results = self.rc.execute_call("get", url_endpoint, query_string, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Basic Search: {}".format(err))

        devices = results.get("devices")
        return devices

    def get_auth_headers(self, content_type_header):
        """
        Generate auth headers.
        :return:
        """
        auth_headers = {"Accept": "application/json",
                        "Content-Type": u"{}".format(content_type_header),
                        "Authorization": u"MaaS token='{}'".format(self.authToken)}
        return auth_headers

    def locate_device(self, url, device_id):
        """
        Function performs a real-time lookup on Android devices or provides Last Known location on iOS
        and Windows Phone devices. The results is latitude and longitude information.
        :param url:
        :param device_id
        :return: action_response
        """
        url_endpoint = self.host + url + self.billingId
        auth_headers = self.get_auth_headers(URL_ENCODED_FORM)
        request_body = {"deviceId": u"{}".format(device_id)}

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Locate Device: {}".format(err))

        action_response = results.get("actionResponse")
        if action_response is None:
            return None

        action_status = action_response.get("actionStatus")  # 0:success; 1:error
        if action_status == 1:
            raise IntegrationError(u"Unable to execute call Locate Device: {}".format(action_response.get("description")))

        return action_response

    def get_software_installed(self, url, device_id):
        """
        Function gets software installed for a device.
        :param url:
        :param device_id
        :return: device_softwares
        """
        url_endpoint = self.host + url + self.billingId
        auth_headers = self.get_auth_headers(JSON_CONTENT_TYPE)
        query_string = {"deviceId": u"{}".format(device_id)}

        try:
            results = self.rc.execute_call("get", url_endpoint, query_string, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Get Software Installed: {}".format(err))

        device_softwares = results.get("deviceSoftwares")
        return device_softwares
