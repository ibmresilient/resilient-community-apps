# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Secureworks CTP API client"""

import requests
import logging
from resilient_lib import validate_fields, RequestsCommon

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = "fn_secureworks_ctp"

def _is_true(flag):
    """helper for the 'verify' flag"""
    return str(flag).lower()[:1] not in ["f", "n", "0"]

class ticketVersionsObject(object):
    def __init__(self):
        self.ticketVersions = []

    def __iter__(self):
        yield self.ticketVersions

    def addticket(self, ticketId, version):
        self.ticketVersions.append({"ticketId": ticketId, "version": version})

class SCWXClient(object):

    """A simple client for the Secureworks CTP API.

       There are no "sessions", each API call is independent.
    """

    def __init__(self, opts, options):
        # Read the configuration options
        self.base_url = options.get("base_url")
        self.username = options.get("username")
        self.password = options.get("password")
        self.verify = options.get("verify")
        self.ticket_types = options.get("query_ticket_types").split(",")
        self.grouping_types = options.get("query_grouping_types").split(",")

        self.rc = RequestsCommon(opts, options)
        self.APIKEY = u"APIKEY {0}:{1}".format(self.username, self.password)
        self.headers = self.get_headers()

    def get_headers(self):
        return {
            "Authorization": self.APIKEY,
            "content-type": "application/json"
        }

    def post_tickets_updates(self):
        """POST get a list of updated tickets not yet acknowledged """
        url = u"{0}/tickets/updates".format(self.base_url)
        payload = {"ticketType": self.ticket_types,
                  "groupingType": self.grouping_types,
                  "worklogs": "ALL"}

        response = self.rc.execute_call_v2("post", url, headers=self.headers, params=payload, verify=False,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: {0}".format(response.text))
        response.raise_for_status()
        return response.json()

    def post_tickets_acknowledge(self, ticket):
        """POST """

        url = u"{0}/tickets/acknowledge".format(self.base_url)
        ticketId = ticket.get('ticketId')
        version = ticket.get('version')
        payload = {'ticketVersions': [{'ticketId': ticketId, 'version': version}]}

        #response = requests.post(url, headers=self.headers, json=payload, verify=False)
        response = self.rc.execute_call_v2("post", url, headers=self.headers, json=payload, verify=False,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: {0}".format(response.text))
        response.raise_for_status()
        return response.json()
