# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
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
    def __init__(self, rest_client_helper, options):   # pylint: disable=unused-argument
        super(SplunkHECFeedDestination, self).__init__()
        self.host = options.get("host")
        self.port = options.get("port")
        self.token = options.get("token")
        self.index = options.get("index")
        self.use_ssl = True if options.get("use_ssl", "false").lower() == "true" else False
        self.event_source = options.get("event_source")
        self.event_host = options.get("event_host")
        self.event_source_type = options.get("event_source_type")
        self.http_proxy = options.get("http_proxy")
        self.https_proxy = options.get("https_proxy")

        self.hec_event = http_event_collector(self.token, self.host,
                                              http_event_port=self.port,
                                              http_event_server_ssl=self.use_ssl,
                                              host=self.event_host,
                                              input_type='json')
        self.hec_event.set_proxies(self.http_proxy, self.https_proxy)
        self.hec_event.index = self.index

        if self.event_source:
            self.hec_event.source = self.event_source
        if self.event_source_type:
            self.hec_event.sourcetype = self.event_source_type

        self.exclude_fields = self._get_exclude_incident_fields(options)
        LOG.info("Excluding incident fields: %s", self.exclude_fields)

    def _get_exclude_incident_fields(self, options: dict) -> list:
        """read file of excluded fields for db column filtering

        :param options: app.config settings
        :type options: dict
        :return: excluded fields or [] when no file is specified
        :rtype: list
        """

        file_path = options.get("exclude_incident_fields_file")
        exclude_fields = []
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # remove any blank lines
                    exclude_fields = [line.strip() for line in f.read().splitlines() if line]
            except FileNotFoundError:
                LOG.error("Unable to read exclude_incident_fields_file: %s", file_path)

        return exclude_fields

    def send_data(self, context, payload):
        """
        Write a simplified version of the payload to a creatively named
        file in the configured 'directory'.
        """
        name = context.type_info.get_pretty_type_name()

        # add the incident_id and object id to all payloads, if needed
        flat_payload = context.type_info.flatten(payload, TypeInfo.translate_value)

        # remove customer specified fields
        flat_payload_filtered = context.type_info.filter_incident_fields(flat_payload, 
                                                                         self.exclude_fields)

        flat_payload_filtered['inc_id'] = context.inc_id
        if payload.get('id'):
            flat_payload_filtered['id'] = payload['id']

        elastic_payload = { "event": flat_payload_filtered }

        if context.is_deleted:
            LOG.warn('NOT IMPLEMENTED deleting %s(%s) on index %s', name, payload['id'], self.index)
        else:
            LOG.debug('adding %s(%s) on index %s', name, payload['id'], self.index)
            self.hec_event.sendEvent(elastic_payload, source_type=name)


    def _fn_splunk_delete(self, index, type, type_id):
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
