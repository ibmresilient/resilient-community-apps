#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Model parts"""

import collections


def searcher_channel(*sub_urls):
    """
    Channel name for searchers
    lookup_channel("sub", "url") ==> channel for searcher at /<root>/sub/url
    """
    return "cts_search." + ".".join(sub_urls)


# Standard artifact types in Resilient
ARTIFACT_TYPES = [
    "file.content",
    "file.name",
    "file.path",
    "email",
    "email.body",
    "email.header",
    "email.header.sender_address",
    "email.header.sender_name",
    "email.header.to",
    "hash.md5",
    "hash.sha1",
    "hash.sha256",
    "hash.fuzzy",
    "cert.x509",
    "net.cidr",
    "net.ip",
    "net.name",
    "net.mac",
    "net.port",
    "net.uri",
    "net.uri.path",
    "net.http.request.header",
    "net.http.response.header",
    "process.name",
    "system.name",
    "system.mutex",
    "system.registry",
    "system.service.name",
    "system.service.name",
    "system.user.name",
    "threat.report.cve",
    "threat.malware.family"
]


class Hit(collections.OrderedDict):
    """A dict representing a Hit and its properties"""
    def __init__(self, *props):
        super(Hit, self).__init__(props=[prop for prop in list(props) if prop["value"] is not None])

    def append(self, prop):
        """Append a property to the hit.  Note: property names must be unique within the hit."""
        if prop["value"] is not None:
            self["props"].append(prop)


class StringProp(dict):
    """A dict representing a string property of a hit"""
    def __init__(self, name=None, value=None):
        super(StringProp, self).__init__(type="string", name=name, value=value)


class UriProp(dict):
    """A dict representing a URI property of a hit"""
    def __init__(self, name=None, value=None):
        super(UriProp, self).__init__(type="uri", name=name, value=value)


class NumberProp(dict):
    """A dict representing a numeric property of a hit"""
    def __init__(self, name=None, value=None):
        super(NumberProp, self).__init__(type="number", name=name, value=str(value))


class IpProp(dict):
    """A dict representing an IP-address property of a hit"""
    def __init__(self, name=None, value=None):
        super(IpProp, self).__init__(type="ip", name=name, value=value)


class LatLngProp(dict):
    """A dict representing a lat/long property of a hit"""
    def __init__(self, name=None, lat=None, lng=None):
        super(LatLngProp, self).__init__(type="lat_lng", name=name, value={"lat": lat, "lng": lng})
