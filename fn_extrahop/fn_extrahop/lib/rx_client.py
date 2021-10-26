# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Reveal(x) client class for SOAR app supporting Extrahop integration"""
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

    def get_devices(self, device_id=None):
        """Get information about devices or a specific computer by device id

        For more details on api, see https://docs.extrahop.com/8.6/rx360-rest-api/

        :param device_id: device_id (str)
        :return Result in json format.

        """
        # Set default uri
        uri = self._endpoints["devices"].format('')

        if device_id:
            uri = self._endpoints["devices"].format(device_id)

        r = self.rc.execute_call_v2("get", uri, headers=self._headers, proxies=self.proxies)

        return r
