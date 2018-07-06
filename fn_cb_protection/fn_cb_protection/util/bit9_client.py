# -*- coding: utf-8 -*-

"""CbProtection (aka bit) API client"""

import requests
import logging
import json

URI_PATH = "api/bit9platform/v1"


class SimpleHTTPException(Exception):
    """Exception for HTTP errors."""
    def __init__(self, response):
        """
        Args:
          response - the Response object from the get/put/etc.
        """
        if isinstance(response, str):
            text = response
            status = 500
        else:
            text = response.text
            status = response.status_code

        logging.getLogger(__name__).error("SimpleHTTPException %s", status)
        self.response = response


def _raise_if_error(response):
    """raise error for failed GET request"""
    if response.status_code != 200:
        raise SimpleHTTPException(response)


def _raise_if_posterror(response):
    """raise error for failed POST request"""
    if response.status_code not in [200, 201]:
        logging.getLogger(__name__).error(response.text)
        raise SimpleHTTPException(response)


def _is_true(flag):
    return str(flag).lower()[:1] not in ["f", "n", "0"]


class CbProtectClient(object):

    """A simple client for the CbProtect API.

       There are no "sessions", each API call is independent.
       This client just makes it easier to
    """

    def __init__(self, options):
        # Read the configuration options
        self.server = options["server"]
        self.token = options["token"]
        self.verify = _is_true(options.get("verify", "True"))

    def _headers(self):
        return {
            'X-Auth-Token': self.token,
            'content-type': 'application/json'
        }

    def get(self, specific_uri):
        uri = "https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.get(uri, headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def put(self, specific_uri, payload):
        uri = "https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.put(uri, json.dumps(payload), headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def post(self, specific_uri, payload):
        uri = "https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.post(uri, json=payload, headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def get_approval_request(self, id):
        return self.get("approvalRequest/{}".format(id))

    def query_approval_request(self, query):
        return self.get("approvalRequest?q={}".format(query))

    def update_approval_request(self, id, payload):
        return self.put("approvalRequest/{}".format(id), payload=payload)
