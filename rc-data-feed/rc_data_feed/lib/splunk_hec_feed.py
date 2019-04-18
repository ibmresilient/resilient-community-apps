# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

"""
This module contains the SplunkHECFeedDestination for writing Resilient data
to an Splunk HTTP Event Collector index.
"""

import logging

from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo
from .splunk_http_event_collector import http_event_collector

LOG = logging.getLogger(__name__)


class SplunkHECFeedDestination(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed destination for writing Resilient data to a local directory."""
    def __init__(self, rest_client, options):   # pylint: disable=unused-argument
        super(SplunkHECFeedDestination, self).__init__()
        self.host = options.get("host")
        self.port = options.get("port")
        self.token = options.get("token")
        self.index = options.get("index")
        self.use_ssl = True if options.get("use_ssl", "false").lower() == "true" else False
        self.event_source = options.get("event_source")
        self.event_host = options.get("event_host")
        self.event_source_type = options.get("event_source_type")

        self.hec_event = http_event_collector(self.token, self.host,
                                              http_event_port=self.port,
                                              http_event_server_ssl=self.use_ssl,
                                              host=self.event_host,
                                              input_type='json')
        self.hec_event.index = self.index

        if self.event_source:
            self.hec_event.source = self.event_source
        if self.event_source_type:
            self.hec_event.sourcetype = self.event_source_type



    def send_data(self, context, payload):
        """
        Write a simplified version of the payload to a creatively named
        file in the configured 'directory'.
        """
        name = context.type_info.get_pretty_type_name()

        # add the incident id to all payloads, if needed
        flat_payload = context.type_info.flatten(payload, TypeInfo.translate_value)
        flat_payload['inc_id'] = context.inc_id

        elastic_payload = { "event": flat_payload }

        if context.is_deleted:
            LOG.info('NOT IMPLEMENTED deleting %s(%s) on index %s', name, payload['id'], self.index)
        else:
            LOG.debug('adding %s(%s) on index %s', name, payload['id'], self.index)
            self.hec_event.sendEvent(elastic_payload, source_type=name)


    def _fn_elasticsearch_delete(self, index, type, type_id):
        """Function: Allows a user to delete a specified payload"""
        pass


    def filter_nulls(self, payload):
        """
        remove key values pairs where value is null, elastic cannot index these
        :param payload:
        :return: new_payload
        """
        new_payload =  dict((key, value) for key, value in payload.items() if value)
        return new_payload
