# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Zia client class class for SOAR app supporting Zscalar Internet Access """
import logging
import json
import re
from .auth import Auth

LOG = logging.getLogger(__name__)


class ZiaClient(Auth):
    """ Class to support Zscaler Internet Access (Zia) api.

    """
    def __init__(self, opts, fn_opts):
        """ Class constructor.

        :param opts: Resilient options dict.
        :param fn_opts: Function specific options dict.

        """
        if not isinstance(opts, dict) and not opts:
            raise ValueError("The 'opts' parameter is not set correctly.")
        if not isinstance(fn_opts, dict) and not fn_opts:
            raise ValueError("The 'fn_opts' parameter is not set correctly.")
        self.api_base_url = fn_opts.get("zia_api_base_url")
        # Define api endpoints
        self._endpoints = {
            # Block lists
            "blocklist":        "/".join([self.api_base_url, "security/advanced"]),
            "blocklist_action": "/".join([self.api_base_url, "security/advanced/blacklistUrls?action={}"]),            # Allow lists
            # Custom lists
            # Sandbox
            # Activation
        }
        super(ZiaClient, self).__init__(opts, fn_opts)

    def _perform_method(self, method, uri, **kwargs):
        """Handle requests to zia endpoints .

        :param method: Request method such as "get","post", "put"
        :param uri: The uri of the request.
        :param kwargs: Can include request parameter dicts such as headers, data etc.
        :return res: Parsed response
        """
        result = None
        try:
            res = self._req.execute_call_v2(method, uri, proxies=self.proxies, **kwargs)

        except Exception as int_ex:
            LOG.error("ERROR for '%s' call for uri '%s', Got exception: %s",
                      "get", uri, str(int_ex))
            raise int_ex

        if res.content:
            try:
                result = res.json()
            except ValueError:
                # Default response likely not in json format just return content as is.
                #return res.content
                result = res.content
        else:
            result = {"status": "OK"}

        return result

    def get_blocklist_urls(self):
        """Get a list of blocklisted URLs.

        The URLs can be either a url or ip address.

        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        return res: Parsed response
        """
        uri = self._endpoints["blocklist"]
        res = self._perform_method("get", uri, headers=self._headers)

        return res

    def blocklist_action(self, blocklisturls=None, action=None):
        """ Perform an add or remove action on a list of URLs to the blocklist.

        The URLs can be either urls or ip addresses.
        Valid actions are "ADD_TO_LIST" and "REMOVE_FROM_LIST".
        See following for url guidelines
        https://help.zscaler.com/zia/url-format-guidelines

        :param blocklist_urls: List of urls and/or ipaddresses
        return res: Parsed response
        """
        if blocklisturls:
            blacklisturls = re.split("\s+|,", blocklisturls)

        payload = {
            "blacklistUrls": blacklisturls
        }

        uri = self._endpoints["blocklist_action"].format(action)
        res = self._perform_method("post", uri, data=json.dumps(payload), headers=self._headers)

        return res
