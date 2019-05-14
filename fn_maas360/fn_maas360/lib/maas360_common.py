# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
import json
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib.components.requests_common import RequestsCommon
from resilient_lib.components.resilient_common import validate_fields

LOG = logging.getLogger(__name__)
CON_TYPE_JSON = "application/json"
CON_TYPE_FORM_ENCODED = "application/x-www-form-urlencoded"
APP_TYPE_DICT = {"iOS Enterprise Application": 1,
                 "iOS App Store Application": 2,
                 "Android Enterprise Application": 3,
                 "Android Market Application": 4}
TARGET_DEVICES_DICT = {"All Devices": 0,
                       "Device Group": 1,
                       "Specific Device": 2}


class MaaS360Utils(object):
    """
    Helper object MaaS360Utils.
    """
    _the_maas360_utils = None

    @staticmethod
    def get_the_maas360_utils(opts, config_data_selection):
        if not MaaS360Utils._the_maas360_utils:
            MaaS360Utils._the_maas360_utils = MaaS360Utils(opts, config_data_selection)
        return MaaS360Utils._the_maas360_utils

    def __init__(self, opts, config_data_selection):
        """
        Constructor for MaaS360Utils
        Note: Object will not be created if auth token is not generated successfully
        :param opts
        """
        self.config_data_selection = config_data_selection

        # Initialize instance variables
        self.host_url = None
        self.billing_id = None
        self.platform_id = None
        self.app_id = None
        self.app_version = None
        self.app_access_key = None
        self.username = None
        self.password = None
        self.auth_url = None
        self.rc = None
        self.auth_token = None

        # Read configuration settings
        self.reload_options(opts)

        # Generating auth token
        self.reconnect()

    def get_auth_token(self):
        """
        Return instance variable auth_token.
        :return: authToken
        """
        return self.auth_token

    def generate_auth_token(self):
        """
        Generates auth token with given user credentials.
        :return: String, auth token, if auth token is generated for portal admin or an error
        """
        complete_auth_url = self.get_url_endpoint(self.auth_url)
        auth_request_body = {
            "authRequest": {
                "maaS360AdminAuth": {
                    "billingID": self.billing_id,
                    "password": self.password,
                    "userName": self.username,
                    "appID": self.app_id,
                    "appVersion": self.app_version,
                    "platformID": self.platform_id,
                    "appAccessKey": self.app_access_key
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
                        "Authorization": u"MaaS token='{}'".format(self.auth_token)}
        return auth_headers

    def get_url_endpoint(self, url):
        """
        Returns url of the endpoint.
        :return: url
        """
        return self.host_url + url + self.billing_id

    def reload_options(self, opts):

        options = opts.get(self.config_data_selection, {})

        # Validate fields
        validate_fields(['maas360_host_url', 'maas360_billing_id', 'maas360_platform_id', 'maas360_app_id',
                         'maas360_app_version', 'maas360_app_access_key', 'maas360_username', 'maas360_auth_url',
                         'maas360_password'], options)

        # Read configuration settings:
        self.host_url = options["maas360_host_url"]
        self.billing_id = options["maas360_billing_id"]
        self.platform_id = options["maas360_platform_id"]
        self.app_id = options["maas360_app_id"]
        self.app_version = options["maas360_app_version"]
        self.app_access_key = options["maas360_app_access_key"]
        self.username = options["maas360_username"]
        self.password = options["maas360_password"]
        self.auth_url = options["maas360_auth_url"]

        self.rc = RequestsCommon(opts, options)

    def reconnect(self):
        # generating auth token and setting it in the object, to be used in further api calls
        self.auth_token = self.generate_auth_token()

    def execute_with_retry(self, verb, url, payload={}, log=None, headers=None):
        for _ in range(2):
            try:
                return self.rc.execute_call(verb, url, payload, log=log, headers=headers)

            except IntegrationError as err:
                # catch expired token error
                if err.value == "I have expired":  # FIXME: catch status code 401
                    self.reconnect()
                    continue
                # any other error
                raise err

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
            #results = self.rc.execute_call("get", url_endpoint, query_string, log=LOG, headers=auth_headers)
            results = self.execute_with_retry("get", url_endpoint, query_string, log=LOG, headers=auth_headers)
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

    def stop_app_distribution(self, url, app_type, installed_app_id, target_devices, device_id, device_group_id):
        """
        Function stops a specific distributions of an app.
        :param url:
        :param app_type:
        :param installed_app_id
        :param target_devices
        :param device_id
        :param device_group_id
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
        request_body = {"appId": u"{}".format(installed_app_id),
                        "appType": u"{}".format(APP_TYPE_DICT.get(app_type)),
                        "targetDevices": u"{}".format(TARGET_DEVICES_DICT.get(target_devices))}

        # add to request_body of not None
        self.add_to_dict("deviceId", device_id, request_body)
        self.add_to_dict("deviceGroupId", device_group_id, request_body)

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            # The Response 400 doesn't return with a meaningful message.
            # We're adding a msg to recheck the combination of inputs on the activity prompt.
            if "status_code: 400, msg: N/A" in err.value:
                raise IntegrationError("Unable to execute call Stop App Distribution: {}. Check combination of your "
                                       "function input values (App Type and Target Devices).".format(err))
            else:
                raise IntegrationError("Unable to execute call Stop App Distribution: {}".format(err))

        action_response = results.get("actionResponse")
        return action_response

    def delete_app(self, url, app_type, installed_app_id):
        """
        Function stop all distributions of the app and deletes the app.
        :param url:
        :param app_type:
        :param installed_app_id
        :return: action_response
        """
        url_endpoint = self.get_url_endpoint(url)
        auth_headers = self.get_auth_headers(CON_TYPE_FORM_ENCODED)
        request_body = {"appType": u"{}".format(APP_TYPE_DICT.get(app_type)),
                        "appId": u"{}".format(installed_app_id)}

        try:
            results = self.rc.execute_call("post", url_endpoint, request_body, log=LOG, headers=auth_headers)
        except IntegrationError as err:
            raise IntegrationError("Unable to execute call Delete App: {}".format(err))

        action_response = results.get("actionResponse")

        return action_response

    @staticmethod
    def add_to_dict(key, value, params):
        """
        Adds a key-value pair to a dictionary if value is not None or "".
        :param params
        :param key:
        :param value:
        """
        if value:
            params[key] = value
