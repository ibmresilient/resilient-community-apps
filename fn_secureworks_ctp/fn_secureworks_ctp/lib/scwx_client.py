# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010. All Rights Reserved.

"""Secureworks CTP API client"""

import json
import requests
import logging

LOG = logging.getLogger(__name__)

def _is_true(flag):
    """helper for the 'verify' flag"""
    return str(flag).lower()[:1] not in ["f", "n", "0"]

class SCWXClient(object):

    """A simple client for the Secureworks CTP API.

       There are no "sessions", each API call is independent.
    """

    def __init__(self, options):
        # Read the configuration options
        self.base_url = options.get("base_url")
        self.username = options.get("username")
        self.password = options.get("password")
        self.verify = _is_true(options.get("verify_cert", "True"))

    def _headers(self):
        authorization = u"APIKEY {0}:{1}".format(self.username, self.password)
        return {
            'Authorization': authorization,
            'content-type': 'application/json'
        }

    def post_tickets_updates(self):
        """POST """
        url = u"{0}/tickets/updates".format(self.base_url)
        response = requests.post(url, headers=self._headers(), verify=self.verify)
        LOG.debug(u"Response: {0}".format(response.text))
        response.raise_for_status()
        return response.json()

