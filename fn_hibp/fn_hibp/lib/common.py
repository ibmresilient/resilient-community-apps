# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.

import requests
import time
from resilient_lib import IntegrationError

BASE_URL = "https://haveibeenpwned.com/api/v3"
HAVE_I_BEEN_PWNED_BREACH_URL = "/".join((BASE_URL, "breachedaccount"))
HAVE_I_BEEN_PWNED_PASTES_URL = "/".join((BASE_URL, "pasteaccount"))

SLEEP_SECS = 5

class Hibp():
    def __init__(self, options):
        self.options = options

    def get_config_option(self, option_name, optional=False):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = self.options.get(option_name)

        if not option and optional is False:
            err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this " \
                  "function".format(option_name)
            raise ValueError(err)

        return option

    def make_headers(self):
        """
        build the headers for API calls
        :param hibp_api_key:
        :return: json headers
        """
        return {
            'User-Agent': 'Resilient HIBP/2.0',
            'hibp-api-key': self.get_config_option("hibp_api_key", False)
        }

    def get_proxies(self):
        """
        build the proxy list
        :param opts:
        :return: dict of proxies
        """
        proxies = {}
        # Get proxies
        proxy_http = self.get_config_option("hibp_proxy_http", True)
        proxy_https = self.get_config_option("hibp_proxy_https", True)

        if proxy_http is not None:
            proxies["http"] = proxy_http

        if proxy_https is not None:
            proxies["https"] = proxy_https

    def execute_call(self, url, depth=1):
        """
        make call to HIBP, returning the results
        :param url:
        :param depth: recursion count
        :return: json returns
        """
        response = requests.get(url, headers=self.make_headers(), proxies=self.get_proxies())

        results = None
        # Good response
        if response.status_code == 200:
            results = response.json()
        # 404 is returned when an email was not found
        elif response.status_code == 404:
            pass
        # Rate limit was hit, wait 2 seconds and try again
        elif response.status_code == 429:
            if depth == 1:
                time.sleep(SLEEP_SECS)
                return self.execute_call(url, depth+1)

            raise IntegrationError("Rate limit exceeded")
        else:
            raise IntegrationError("Have I Been Pwned returned {} unexpected status code".format(response.status_code))

        return results
