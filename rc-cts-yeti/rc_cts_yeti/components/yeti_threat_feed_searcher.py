#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import traceback

from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, ThreatServiceLookupEvent
from rc_cts.components.threat_webservice import ThreatServiceLookupEvent

import pyeti

LOG = logging.getLogger(__name__)

CONFIG_SECTION = "yeti"


def config_section_data():

    config_result = """
[yeti]
urlbase=http://yeti-server:5000/api
username=yeti
password=
api_key=api_key_value
    """
    return config_result


class YetiThreatFeedSearcher(BaseComponent):
    """
       YETI custom threat searcher component

       Test using 'curl':
           curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/yeti_threat_service'
           curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.ip",
           "value":"11.11.11.11"}' 'http://127.0.0.1:9000/cts/yeti_threat_service'

    """
    channel = searcher_channel("yeti_threat_service")

    def __init__(self, opts):
        super(YetiThreatFeedSearcher, self).__init__(opts)

        self.options = opts.get(CONFIG_SECTION)
        url = self.options.get("urlbase")
        username = self.options.get("username")
        password = self.options.get("password")
        api_key = self.options.get("api_key")

        self.yeti_client = pyeti.YetiApi(url, (username, password), api_key)

    @handler()
    def lookup_artifact(self, event, *args, **kwargs):
        """
        Use YETI to search for artifact value

        """

        if not isinstance(event, ThreatServiceLookupEvent):
            return

        hits = []
        LOG.info("Querying YETI")

        artifact = event.artifact
        artifact_value = artifact['value']
        LOG.info(artifact)
        LOG.info("Looking up ({art_type}): {art_value}"
                 .format(art_type=artifact['type'], art_value=artifact_value))

        try:
            # init new indicators object
            indicators = self.yeti_client.observable_search(regex=False,
                                                            value=artifact_value)
            LOG.debug(indicators)
        except ValueError as e:
            LOG.error(traceback.format_exc())
            raise e

        if not indicators or len(indicators) < 1:
            return hits

        tags = ""
        for tag in indicators[0]["tags"]:
            if tags != "":
                tags += ", "
            tags += tag["name"]

        description = indicators[0]["description"] if indicators[0]["description"] else "None"
        try:
            hits.append(
                Hit(
                    StringProp(name="Type", value=indicators[0]["type"]),
                    StringProp(name="Value", value=indicators[0]["value"]),
                    StringProp(name="Tags", value=tags),
                    StringProp(name="Created", value=indicators[0]["created"]),
                    UriProp(name="URL", value=indicators[0]["human_url"]),
                    StringProp(name="Description", value=description)
                )
            )
            return hits
        except Exception as e:
            LOG.error(traceback.format_exc())
            raise e
