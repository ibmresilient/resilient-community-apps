# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
import json
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib.components.requests_common import RequestsCommon

LOG = logging.getLogger(__name__)
CON_TYPE_JSON = "application/json"
CON_TYPE_FORM_ENCODED = "application/x-www-form-urlencoded"


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
        self.authToken = self.generate_auth_token(userName, password, appID, appVersion, platformID,
                                                  appAccessKey, auth_url)

    def get_auth_token(self):
        """
        Return instance variable authToken.
        :return: authToken
        """
        return self.authToken

    def generate_auth_token(self, userName, password, appID, appVersion, platformID, appAccessKey, auth_url):
        """
        Generates auth token with given user credentials.
        :param userName:
        :param password:
        :param appID:
        :param appVersion:
        :param platformID:
        :param appAccessKey:
        :return: String, auth token, if auth token is generated for portal admin or an error
        """
        complete_auth_url = self.get_url_endpoint(auth_url)
        auth_request_body = {
            "authRequest": {
                "maaS360AdminAuth": {
                    "billingID": self.billingId,
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

    def get_auth_headers(self, content_type_header):
        """
        Generate auth headers.
        :return: auth headers
        """
        auth_headers = {"Accept": "application/json",
                        "Content-Type": u"{}".format(content_type_header),
                        "Authorization": u"MaaS token='{}'".format(self.authToken)}
        return auth_headers

    def get_url_endpoint(self, url):
        """
        Returns url of the endpoint.
        :return: url
        """
        return self.host + url + self.billingId

    def basic_search(self, url, query_string):
        """
        Search for devices by Device Name, Username, Phone Number, Platform, Device Status and other Device Identifiers.
        Support for partial match for Device Name, Username, Phone Number.
        :param url:
        :param query_string:
        :return: device or list of devices or None if there aren't any found
        """

        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_JSON)

        try:
            results = self.rc.execute_call("get", url_endpoint, query_string, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Basic Search: {}".format(err))

        devices = results.get("devices")
        return devices

    def locate_device(self, url, device_id):
        """
        Function performs a real-time lookup on Android devices or provides Last Known location on iOS
        and Windows Phone devices. The results is latitude and longitude information.
        :param url:
        :param device_id
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
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
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_JSON)
        request_body = {"deviceId": u"{}".format(device_id)}

        try:
            results = self.rc.execute_call("get", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Get Software Installed: {}".format(err))

        device_softwares = results.get("deviceSoftwares")
        return device_softwares

    def lock_device(self, url, device_id):
        """
        Function locks the device .
        :param url:
        :param device_id
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
        request_body = {"deviceId": u"{}".format(device_id)}

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Lock Device: {}".format(err))

        action_response = results.get("actionResponse")
        return action_response

    def wipe_device(self, url, device_id, notify_me, notify_user, notify_others):
        """
        Function performs a remote Wipe of the device.
        :param url:
        :param device_id:
        :param notify_me:
        :param notify_user:
        :param notify_others:
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
        request_body = {"deviceId": u"{}".format(device_id),
                        "notifyMe": u"{}".format(notify_me),
                        "notifyUser": u"{}".format(notify_user),
                        "notifyOthers": u"{}".format(notify_others)}

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Wipe Device: {}".format(err))

        action_response = results.get("actionResponse")
        return action_response

    def cancel_pending_wipe(self, url, device_id):
        """
        Function cancels outstanding Remote Wipe sent to the device.
        :param url:
        :param device_id:
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
        request_body = {"deviceId": u"{}".format(device_id)}

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Cancel Pending Wipe: {}".format(err))

        action_response = results.get("actionResponse")
        return action_response

    def stop_app_distribution(self, url, app_type, installed_app_id, device_id):
        """
        Function stops a specific distributions of an app.
        :param url:
        :param app_type:
        :param installed_app_id
        :param device_id
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
        request_body = {"appType": u"{}".format(app_type),
                        "appId": u"{}".format(installed_app_id),
                        "targetDevices": u"{}".format(2),  # Possible values: 0: All Devices  1: Device Group 2: Specific Device
                        "deviceId": u"{}".format(device_id)}

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Stop App Distribution: {}".format(err))

        action_response = results.get("actionResponse")
        return action_response
