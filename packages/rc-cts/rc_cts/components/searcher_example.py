#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

"""Circuits component to implement a simple custom threat 'searcher'

    To implement your own searcher:

    *  Implement a Circuits component (derive from BaseComponent, or Component,
       or from ResilientComponent if you want access to the Resilient REST API)
    *  Set the channel to `searcher_channel("your_specific_url_path")
       (the base URL, for example '/cts/', is set in the webservice; the searcher
       responds to a specific path below this, such as '/cts/example')
    *  Provide a handler for one or more of the artifact type names
       ("net.ip", "net.uri", "hash.md5", etc -- see the Custom Threat Service Guide)
       that returns a response structure of
       {"hits": [...array of ArtifactHitDTO...]

    A single searcher can implement any number of these artifact handlers,
    and your application can include any number of these searchers.

    Test using 'curl':

        curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/example'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/example'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'

    To install the threat service with your Resilient server
    (assuming that resilient-circuits application is running on the same server):
        sudo resutil threatserviceedit -name example -resturl http://127.0.0.1:9000/cts/example
        sudo resutil threatservicetest -name example
    To delete,
        sudo resutil threatservicedel -name example

"""

import logging
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp


LOG = logging.getLogger(__name__)


class SearcherExample(BaseComponent):
    """
    Example of a custom threat searcher component
    """

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("example")

    # Handle lookups for artifacts of type 'net.uri' (see doc for full list)
    @handler("net.uri")
    def _lookup_net_uri(self, event, *args, **kwargs):
        """Return hits for URL artifacts"""
        hits = []

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']

        # Return zero or more hits.  Here's one example.
        hits.append(
            Hit(
                NumberProp(name="id", value=123),
                StringProp(name="Type", value=artifact_type),
                UriProp(name="Link", value=artifact_value),
                IpProp(name="IP Address", value="127.0.0.1"),
                LatLngProp(name="Location", lat=42.366, lng=-71.081)
            )
        )
        hits.append(
            Hit(
                NumberProp(name="id", value=456),
                StringProp(name="Type", value=artifact_type),
                UriProp(name="Link", value=artifact_value),
                IpProp(name="IP Address", value="0.0.0.0"),
            )
        )
        yield hits
