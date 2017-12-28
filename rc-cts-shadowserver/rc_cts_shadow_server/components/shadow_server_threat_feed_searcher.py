#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

"""
    Test using 'curl':

        curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/shadow_server_threat_feed'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.name","value":"localhost"}' 'http://127.0.0.1:9000/cts/shadow_server_threat_feed'
        curl -v 'http://127.0.0.1:9000/cts/shadow_server_threat_feed/9dd7b18b-48a1-5108-9d79-1a67641d0df5'
        curl -v -X GET 'http://127.0.0.1:9000/cts/shadow_server_threat_feed/7c796ece-e3b7-5dd1-a14c-a9c3179087e4'
"""

import logging
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp
from circuits import Event, Timer, handler
from resilient_circuits.actions_component import ResilientComponent
import requests
import time
import json


LOG = logging.getLogger(__name__)


def config_section_data():
    return """[shadow_server_cts]
shadow_server_url=http://bin-test.shadowserver.org/api
"""


class ShadowServerThreatFeedSearcher(ResilientComponent):
    """
    Example of a custom threat searcher component
    """
    def __init__(self, opts):
        super(ShadowServerThreatFeedSearcher, self).__init__(opts)

        self.options = opts.get("shadow_server_url", {})
        LOG.debug(opts)
        self.allowed_artifacts = {
            "hash.md5": "md5",
            "hash.sha1": "sha1"
        }
    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("shadow_server_threat_feed")

    @handler("hash.md5")
    def _lookup_hash_md5(self, event, *args, **kwargs):
        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.debug("_lookup_hash_md5 started for Artifact Type {0} - Artifact Value {1}",
                  artifact_type, artifact_value)

        hits = self._query_shadow_server_(artifact_type, artifact_value)

        yield hits

    @handler("hash.sha1")
    def _lookup_hash_sha1(self, event, *args, **kwargs):
        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.debug("_lookup_process_name started for Artifact Type {0} - Artifact Value {1}",
                  artifact_type, artifact_value)

        hits = self._query_shadow_server_(artifact_type, artifact_value)

        yield hits

    def _query_shadow_server_(self, artifact_type, artifact_value):
        hits = []
        try:
            url = "{0}?{1}={2}".format(self.options.get("shadow_server_url", "http://bin-test.shadowserver.org/api"),
                                       self.allowed_artifacts.get(artifact_type),
                                       artifact_value)
            LOG.debug("Getting info from {0}".format(url))
            response = requests.get(url)
            if response.status_code == 200:
                resp_json = json.loads(response.text.replace(artifact_value, "", 1))
                hit = Hit()
                for attribute, value in resp_json.iteritems():
                    hit.append(StringProp(name=attribute, value=value))

                # Return zero or more hits.  Here's one example.
                hits.append(hit)
            else:
                LOG.warn("Got response status {0} from Shadow Server".format(response.status_code))

        except BaseException as e:
            LOG.exception(e.message)
        return hits
