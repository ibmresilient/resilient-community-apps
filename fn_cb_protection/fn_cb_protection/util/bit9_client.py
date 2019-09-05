# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""CbProtection (aka bit9) API client"""

import sys
import json
import requests
import logging

URI_PATH = "api/bit9platform/v1"
log = logging.getLogger(__name__)


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
        log.debug(u"Response: {}".format(response.text))
        self.raise_for_status_include_content(response)
        return response.json()

    def put(self, specific_uri, payload):
        """generic update"""
        uri = u"https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.put(uri, json.dumps(payload), headers=self._headers(), verify=self.verify)
        log.debug(u"Response: {}".format(response.text))
        self.raise_for_status_include_content(response)
        return response.json()

    def post(self, specific_uri, payload):
        """generic post"""
        uri = u"https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.post(uri, json=payload, headers=self._headers(), verify=self.verify)
        log.debug(u"Response: {}".format(response.text))
        self.raise_for_status_include_content(response)
        return response.json()

    def delete(self, specific_uri):
        """generic delete"""
        uri = u"https://{}/{}/{}".format(self.server, URI_PATH, specific_uri)
        response = requests.delete(uri, headers=self._headers(), verify=self.verify)
        log.debug(u"Response: {}".format(response.text))
        self.raise_for_status_include_content(response)
        return response.text

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
        if file_rule_id is None:
            return self.post("fileRule", payload=payload)  # create
        return self.put(u"fileRule/{}".format(file_rule_id), payload=payload)  # update a specific one

    def delete_file_rule(self, file_rule_id):
        """Deletes a file rule by ID"""
        return self.delete(u"fileRule/{}".format(file_rule_id))

    def delete_file(self, payload):
        """Deletes a file from all or a specific system"""
        uri = u"https://{}/{}".format(self.server, "api/bit9platform/restricted/fileAction")
        response = requests.post(uri, json=payload, headers=self._headers(), verify=self.verify)
        self.raise_for_status_include_content(response)
        return response.json()

    @staticmethod
    def raise_for_status_include_content(response):
        """
        Raises stored :class:`HTTPError`, if one occurred.
        :param response:
        :return:
        """
        try:
            # Debug logging
            log.debug(response.status_code)
            log.debug(response.content)

            # Raises stored :class:`HTTPError`, if one occurred.
            response.raise_for_status()

        except requests.HTTPError as err:
            if sys.version_info[0] < 3:
                # add content to the error message
                new_msg = u"{} {}".format(err.message, response.content)
                raise requests.HTTPError(new_msg)
            else:
                raise requests.HTTPError(err)