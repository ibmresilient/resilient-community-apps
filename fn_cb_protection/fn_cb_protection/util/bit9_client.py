# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""CbProtection (aka bit9) API client"""

import json
import requests


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
    """

    def __init__(self, options):
        # Read the configuration options
        self.server = options["server"]
        self.token = options["token"]
        self.verify = _is_true(options.get("verify_cert", "True"))

    def _headers(self):
        return {
            'X-Auth-Token': self.token,
            'content-type': 'application/json'
        }

    def get(self, specific_uri):
        """generic get"""
        uri = u"https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.get(uri, headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def put(self, specific_uri, payload):
        """generic update"""
        uri = u"https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.put(uri, json.dumps(payload), headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def post(self, specific_uri, payload):
        """generic post"""
        uri = u"https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.post(uri, json=payload, headers=self._headers(), verify=self.verify)
        response.raise_for_status()
        return response.json()

    def get_approval_request(self, request_id):
        """get an approval request"""
        return self.get(u"approvalRequest/{}".format(request_id))

    def query_approval_request(self, query):
        """get approval requests that match the query string"""
        return self.get(u"approvalRequest?q={}".format(query))

    def update_approval_request(self, request_id, payload):
        """update an approval request"""
        return self.put(u"approvalRequest/{}".format(request_id), payload=payload)

    def get_file_catalog(self, file_catalog_id):
        """Get a file catalog item by ID"""
        return self.get(u"fileCatalog/{}".format(file_catalog_id))

    def query_file_catalog(self, query):
        """get file catalog items that match the query string"""
        return self.get(u"fileCatalog?q={}".format(query))

    def query_file_instance(self, query):
        """get file instances that match the query string"""
        return self.get(u"fileInstance?q={}".format(query))

    def update_file_instance(self, file_instance_id, payload):
        """update an file instance by ID"""
        return self.put(u"fileInstance/{}".format(file_instance_id), payload=payload)

    def get_file_rule(self, file_rule_id):
        """Get a file rule by ID"""
        return self.get(u"fileRule/{}".format(file_rule_id))

    def query_file_rule(self, query):
        """get file rules that match the query string"""
        return self.get(u"fileRule?q={}".format(query))

    def update_file_rule(self, file_rule_id, payload):
        """Update a file rule"""
        # The file rule id can be None
        if id is None:
            return self.post("fileRule", payload=payload)
        return self.put(u"fileRule/{}".format(file_rule_id), payload=payload)
