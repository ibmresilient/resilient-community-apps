# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Secureworks CTP API client"""

import os
import logging
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)


def get_headers(apikey):
    return {
        'Authorization': apikey,
        'content-type': "application/json"
    }

class SCWXClient(object):

    """A simple client for the Secureworks CTP API.

       There are no "sessions", each API call is independent.
    """

    def __init__(self, opts, options):
        # Read the configuration options
        self.base_url = options.get('base_url')
        self.username = options.get('username')
        self.password = options.get('password')
        self.limit = options.get('query_limit')
        self.ticket_types = options.get('query_ticket_types', '').split(",")
        self.grouping_types = options.get('query_grouping_types', '').split(",")
        self.assigned_to_customer = options.get('assigned_to_customer')
        self.cafile = options.get('cafile')
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False

        self.rc = RequestsCommon(opts, options)
        self.APIKEY = u"APIKEY {0}:{1}".format(self.username, self.password)
        self.headers = get_headers(self.APIKEY)

    def post_tickets_updates(self):
        """POST get a list of updated tickets not yet acknowledged """
        url = u"{0}/tickets/updates".format(self.base_url)
        payload = {'ticketType': self.ticket_types,
                   'limit': self.limit,
                   'groupingType': self.grouping_types,
                   'assignedToCustomer': self.assigned_to_customer,
                   'worklogs': "UPDATED"}

        response = self.rc.execute_call_v2("post", url, headers=self.headers, params=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def post_tickets_acknowledge(self, ticket):
        """POST acknowledgement to Secureworks CTP that ticket has been received."""

        url = u"{0}/tickets/acknowledge".format(self.base_url)
        ticketId = ticket.get('ticketId')
        version = ticket.get('version')
        payload = {'ticketVersions': [{'ticketId': ticketId, 'version': version}]}

        response = self.rc.execute_call_v2("post", url, headers=self.headers, json=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def get_ticket_attachment(self, ticket_id, attachment_id):
        """GET get a ticket attachment """
        url = u"{0}/tickets/{1}/attachments/{2}".format(self.base_url, ticket_id, attachment_id)
        payload = {'id': ticket_id,
                   'attachmentId': attachment_id}

        response = self.rc.execute_call_v2("get", url, headers=self.headers, params=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()
