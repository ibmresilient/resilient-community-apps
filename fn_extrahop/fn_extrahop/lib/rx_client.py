# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Reveal(x) client class for SOAR app supporting Extrahop integration"""
import json
import logging
import base64
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)


class RxClient():
    """ Class to support Extrahop Reveal(x) api.

    """
    def __init__(self, opts, fn_opts):
        """ Class constructor.

        :param opts: SOAR options dict.
        :param fn_opts: Function specific options dict.

        """
        if not isinstance(opts, dict) and not opts:
            raise ValueError("The 'opts' parameter is not set correctly.")
        if not isinstance(fn_opts, dict) and not fn_opts:
            raise ValueError("The 'fn_opts' parameter is not set correctly.")
        self.host_url = fn_opts.get("extrahop_rx_host_url")
        self.key_id = fn_opts.get("extrahop_rx_key_id")
        self.key_secret = fn_opts.get("extrahop_rx_key_secret")
        self.api_version = fn_opts.get("extrahop_rx_api_version")
        self.api_base_url = "{}/api/{}".format(self.host_url, self.api_version)
        # Define api endpoints
        self._endpoints = {
            # Devices
            "token":          "/".join([self.host_url, "oauth2/token"]),
            "devices":        "/".join([self.api_base_url, "devices/{}"]),
            "search_devices": "/".join([self.api_base_url, "devices/search"]),
        }
        self.rc = RequestsCommon(opts=opts, function_opts=fn_opts)
        self._headers = {"Authorization": "Bearer " + self.get_token()}


    def get_token(self):
        """
        Get an API access token for Reveal(x) 360 authentication.

        :return: API Access token (string)
        """
        uri = self._endpoints["token"]

        auth = base64.b64encode(bytes(self.key_id + ":" + self.key_secret, "utf-8")).decode("utf-8")

        headers = {
            "Authorization": "Basic " + auth,
            "Content-Type": "application/x-www-form-urlencoded",
        }

        r = self.rc.execute_call_v2("post", uri, headers=headers, data="grant_type=client_credentials")

        return r.json()["access_token"]

    def get_devices(self, active_from=None, active_until=None, limit=None, offset=None, device_id=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param device_id: device_id (str)
        :param active_from: (Optional) The beginning timestamp (in millisecs) for the request. Default 0 (int)
        :param active_until: (Optional) The ending timestamp (in millisecs) for the request. Default 0 (int)
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :return Result in json format.

        """
        # Set default uri
        uri = self._endpoints["devices"].format('')
        params = {}

        params["active_from"] = active_from if active_from else 0
        params["active_until"] = active_until if active_until else 0
        params["limit"] = int(limit) if limit else 0
        params["offset"] = int(offset) if offset else 0

        if device_id:
            uri = self._endpoints["devices"].format(device_id)

        r = self.rc.execute_call_v2("get", uri, headers=self._headers, params=params)

        return r

    def search_devices(self, active_from=None, active_until=None, limit=None, offset=None, search_filter=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param active_from: (Optional) The beginning timestamp (in millisecs) for the request. Default 0 (int)
        :param active_until: (Optional) The ending timestamp (in millisecs) for the request. Default 0 (int)
        :param limit(int): (Optional) Limit the number of devices returned to the specified maximum number (int).
        :param offset: (Optional) Skip the specified number of devices (int).
        :param search_filter: Search filter (json str)
        :return Result in json format.`
        """
        uri = self._endpoints["search_devices"]
        data = {"filter": {}}

        if search_filter:
            try:
                filter_data = json.loads(search_filter)
            except ValueError:
                raise ValueError("The search filter is not valid json content")
        if filter_data.get("filter"):
            data["filter"] = filter_data.get("filter")
        data["active_from"] = active_from if active_from else 0
        data["active_until"] = active_until if active_until else 0
        data["limit"] = int(limit) if limit else 0
        data["offset"] = int(offset) if offset else 0

        r = self.rc.execute_call_v2("post", uri, headers=self._headers, data=json.dumps(data))

        return r
