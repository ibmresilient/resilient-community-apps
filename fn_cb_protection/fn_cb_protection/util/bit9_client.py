# -*- coding: utf-8 -*-

"""CbProtection (aka bit) API client"""

import requests
import logging
import json

URI_PATH = "api/bit9platform/v1"


def _is_true(flag):
    """helper for the 'verify' flag"""
    return str(flag).lower()[:1] not in ["f", "n", "0"]


def escape(query):
    """Escape a value to be used in a query"""
    query = query.replace("\\", "\\\\")
    query = query.replace("|", "\\|")
    query = query.replace("*", "\\*")
    return query


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
        """generic get"""
        uri = "https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.get(uri, headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def put(self, specific_uri, payload):
        """generic update"""
        uri = "https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.put(uri, json.dumps(payload), headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def post(self, specific_uri, payload):
        """generic post"""
        uri = "https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.post(uri, json=payload, headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def get_approval_request(self, id):
        """get an approval request"""
        return self.get("approvalRequest/{}".format(id))

    def query_approval_request(self, query):
        """get approval requests that match the query string"""
        return self.get("approvalRequest?q={}".format(query))

    def update_approval_request(self, id, payload):
        """update an approval request"""
        return self.put("approvalRequest/{}".format(id), payload=payload)

    def get_file_catalog(self, id):
        """Get a file catalog item by ID"""
        return self.get("fileCatalog/{}".format(id))

    def query_file_catalog(self, query):
        """get file catalog items that match the query string"""
        return self.get("fileCatalog?q={}".format(query))

    def query_file_instance(self, query):
        """get file rules that match the query string"""
        return self.get("fileInstance?q={}".format(query))

    def update_file_instance(self, id, payload):
        """update an file instance"""
        return self.put("fileInstance/{}".format(id), payload=payload)

    def get_file_rule(self, id):
        """Get a file rule by ID"""
        return self.get("fileRule/{}".format(id))

    def query_file_rule(self, query):
        """get file rules that match the query string"""
        return self.get("fileRule?q={}".format(query))

    def update_file_rule(self, id, payload):
        """Update a file rule"""
        # The file rule id can be None
        if id is None:
            return self.post("fileRule", payload=payload)
        else:
            return self.put("fileRule/{}".format(id), payload=payload)