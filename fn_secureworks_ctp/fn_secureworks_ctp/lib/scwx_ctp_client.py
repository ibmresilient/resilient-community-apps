# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Secureworks CTP API client"""

import json
import os
import logging
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)


def get_headers(apikey):
    return {
        'Authorization': apikey,
        'content-type': "application/json"
    }

def get_query_types(query_list):
    """
    This function is used to parse the query_ticket_grouping_types string from the app.config
    :param query_list: the string to parse into ticketType groupingType pairs for querying Securework ticket endpoint
    :return: List of json objects.  Each json entry is a ticketType, groupingType pair
    """
    query_pair_list = query_list.split(',')
    query_types = []
    for pair in query_pair_list:
        entry = {'ticketType': pair.split(':')[0].strip(),
                 'groupingType': pair.split(':')[1].strip()
                 }
        query_types.append(entry)
    return query_types

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
        self.query_types = get_query_types(options.get('query_ticket_grouping_types'))
        self.cafile = options.get('cafile')
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False
        self.close_codes = options.get('close_codes', None)

        self.rc = RequestsCommon(opts, options)
        self.APIKEY = u"APIKEY {0}:{1}".format(self.username, self.password)
        self.headers = get_headers(self.APIKEY)

    def post_tickets_updates(self, ticket_type, grouping_type):
        """POST get a list of updated tickets not yet acknowledged """
        # Pass the parameters in the URL not in the payload for this endpoint only.
        url = u"{0}/tickets/updates".format(self.base_url)
        url = u"{0}?ticketType={1}".format(url, ticket_type)
        url = u"{0}&limit={1}".format(url, self.limit)
        #url = u"{0}&worklogs={1}".format(url, "UPDATED")
        if grouping_type:
            url = u"{0}&groupingType={1}".format(url, grouping_type)

        response = self.rc.execute_call_v2("post", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def post_tickets_acknowledge(self, ticket):
        """POST acknowledgement to Secureworks CTP that ticket has been received."""

        url = u"{0}/tickets/acknowledge".format(self.base_url)
        ticket_id = ticket.get('ticketId')
        version = ticket.get('version')
        payload = {'ticketVersions': [{'ticketId': ticket_id, 'version': version}]}

        response = self.rc.execute_call_v2("post", url, headers=self.headers, json=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def get_tickets_attachment(self, ticket_id, attachment_id):
        """GET get a ticket attachment """

        url = u"{0}/tickets/{1}/attachments/{2}".format(self.base_url, ticket_id, attachment_id)
        payload = {'id': ticket_id,
                   'attachmentId': attachment_id}

        response = self.rc.execute_call_v2("get", url, headers=self.headers, json=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def post_tickets_close(self, ticket_id, reason_summary, close_code):
        """POST close a ticket"""

        url = u"{0}/tickets/{1}/close".format(self.base_url, ticket_id)

        payload = {'worklogContent': reason_summary,
                   'closeCode': close_code}

        response = self.rc.execute_call_v2("post", url, headers=self.headers, json=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def get_tickets_close_codes(self, ticket_id):
        """GET get close codes for a ticket """

        url = u"{0}/tickets/{1}/close-codes".format(self.base_url, ticket_id)
        payload = {'id': ticket_id}

        response = self.rc.execute_call_v2("get", url, headers=self.headers, json=payload, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()
