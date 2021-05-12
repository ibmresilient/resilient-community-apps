# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Zia client Auth class for SOAR app supporting Zscalar Internet Access """
import logging
import time
import re
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)
MILLISEC_MULTIPLIER = 1000

class Auth():
    """ Class to support Zscaler Internet Access (Zia) api authentication
        setup.

    """
    def __init__(self, opts, fn_opts):
        """ Class constructor.

        :param opts: Resilient options dict.
        :param fn_opts: Function specific options dict.
        """
        self.username = fn_opts.get("zia_username")
        self.password = fn_opts.get("zia_password")
        self.api_key = fn_opts.get("zia_api_key")
        self._req = RequestsCommon(opts, fn_opts)
        self.proxies = self._req.get_proxies()
        self._timestamp = str(int(time.time() * MILLISEC_MULTIPLIER))
        self._obf_api_key = ''
        self._jsession_id = ''
        # Set basic request headers.
        self._headers = {
            "content-type": "application/json",
            "cache-control": "no-cache",
            "User-Agent": "SOARCLIENT"
        }
        # Add authenticate endpoint.
        if not self._endpoints:
            self._endpoints = {}
        self._endpoints.update({"authenticate": "/".join([self.api_base_url, "authenticatedSession"])})
        self._obfuscate_api_key()
        self._set_jsession_header()

    def __getattr__(self, name):
        """Log warning for undefined class attributes."""
        LOG.warning("The attribute '%s' not defined.", name)
        return ''

    def _set_jsession_header(self):
        """ Setup headers to allow authentication to Zia server.

        Get 'JSESSIONID' and add to headers for use in subsequent api requests.
        """
        uri = self._endpoints["authenticate"]
        res = None

        # Payload with credentials.
        payload = {
            "apiKey": self._obf_api_key,
            "username": self.username,
            "password": self.password,
            "timestamp": self._timestamp
        }

        try:
            res = self._req.execute_call_v2("post", uri, headers=self._headers, proxies=self.proxies, json=payload)
        except Exception as int_ex:
            LOG.error("ERROR for '%s' call for uri '%s', Got exception: %s",
                      "post", uri, str(int_ex))
            raise int_ex

        # Get JSESSIONID value .
        self._jsession_id = self._parse_jsessionid(res.headers["Set-Cookie"])
        # Update request headers to include JSESSIONID .
        self._headers.update({"cookie": self._jsession_id})

    def _obfuscate_api_key(self, timestamp=None):
        """ Obfuscate api key to be used in api requests.
            Set obfuscated key and timestamp.

        :param timestamp: Optional parameter (Unix epoch value in millisecs)
        """
        if timestamp:
            now = self._timestamp = timestamp
        else:
            now = self._timestamp
        n = now[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(n), 1):
            key += self.api_key[int(n[i])]
        for j in range(0, len(r), 1):
            key += self.api_key[int(r[j]) + 2]
        self._obf_api_key = key

    def _parse_jsessionid(self, set_cookie):
        """ Parse JSESSIONID from response header.

        Example set-cookie value =
            "JSESSIONID=6C42F97B950DE134775BCAC65F16F614; Path=/; Secure; HttpOnly"
        jsession_id = "JSESSIONID=6C42F97B950DE134775BCAC65F16F614"

        :param set-cookie: The set-cookie parameter form response
        return res: The jsession iD
        """
        jsession_id = re.sub(r";.*$", "", set_cookie)
        return jsession_id
