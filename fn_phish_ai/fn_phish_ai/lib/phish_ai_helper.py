# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
import os
import logging
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)

PACKAGE_NAME = 'fn_phish_ai'
DEFAULT_TIMEOUT = 60
ENDPOINT_URL = 'https://app.phish.ai/api/'
ENDPOINT_SCAN_URL = 'url/scan'
ENDPOINT_REPORT_URL = 'url/report?scan_id='

class PhishAI(object):
    def __init__(self, opts, options):
        self.rc = RequestsCommon(opts, options)
        self.api_key = options.get("phishai_api_key")
        self.timeout_seconds = int(options.get("timeout_seconds", DEFAULT_TIMEOUT))
        self.headers = {'Authorization': self.api_key}
        self.cafile = options.get('cafile')
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False

    def scan_url(self, url):
        """
        scan_url
        """
        endpoint_url = u"{0}{1}".format(ENDPOINT_URL, ENDPOINT_SCAN_URL)
        response = self.rc.execute_call_v2("post", endpoint_url, data={'url': url}, headers=self.headers,
                                           verify=self.bundle, proxies=self.rc.get_proxies())

        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def get_report(self, scan_id):
        """"
        get_report
        """

        endpoint_url = u"{0}{1}{2}".format(ENDPOINT_URL, ENDPOINT_REPORT_URL, scan_id)
        response = self.rc.execute_call_v2("get", endpoint_url, timeout=self.timeout_seconds, headers=self.headers,
                                           verify=self.bundle, proxies=self.rc.get_proxies())

        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()