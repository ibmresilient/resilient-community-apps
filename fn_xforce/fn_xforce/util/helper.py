# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from resilient_circuits import FunctionError
from logging import getLogger
from resilient_lib import validate_fields

PACKAGE_NAME = 'fn_xforce'
LOG = getLogger(__name__)

class XForceHelper:

    def __init__(self, options):
        self.options = options

    def setup_config(self):
        validate_fields(["xforce_apikey", "xforce_password", "xforce_baseurl"], self.options)
        return self.options.get("xforce_apikey"),\
               self.options.get("xforce_baseurl"),\
               self.options.get("xforce_password")

    def setup_proxies(self):
        # Get http proxies from the app.config
        http_proxy = self.options.get("xforce_http_proxy")
        # Get https proxies from the app.config
        https_proxy = self.options.get("xforce_https_proxy")
        LOG.info(f"X-Force Proxies: HTTP {http_proxy} and HTTPS {https_proxy}")

        # Set proxies as empty dict
        proxies = {}

        if http_proxy:
            proxies["http"] = http_proxy
        if https_proxy:
            proxies["https"] = https_proxy

        return proxies

    def handle_case_response(self, res):
        results = None
        if int(res.status_code / 100) == 2:
            results = res
        elif res.status_code == 401:
            raise FunctionError(
                "401 Status code returned. Retry function with updated credentials")
        elif res.status_code == 403:
            raise FunctionError("403 Forbidden response received by API")
        else:
            LOG.error("Got unexpected result from request.")
            results = res

        return results
