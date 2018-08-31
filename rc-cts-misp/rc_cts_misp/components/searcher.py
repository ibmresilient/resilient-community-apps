#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A custom threat service 'searcher' for MISP

    Tested with PyMISP version: 2.4.79

    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/misp'
        curl -v 'http://127.0.0.1:9000/cts/misp/<id>'

    Interesting test values:
        {"type":"email.header","value":"X-Mailer: Microsoft Windows Live Mail 16.4.3528.331"}
        {"type":"net.uri","value":"NOGIVOVANA.ml"}
        {"type":"net.cidr","value":"117.192.168.0/24"}
        {"type":"net.cidr","value":"117.192.0.0/16"}
        {"type":"net.ip","value":"117.192.168.192"}

"""

from __future__ import unicode_literals
import logging
import json
from pkg_resources import Requirement, resource_filename
from pymisp import PyMISP
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp, ThreatServiceLookupEvent

LOG = logging.getLogger(__name__)

CONFIG_SECTION = "custom_threat_service_misp"

# Map from the Resilient Custom Threat Service API type to the MISP types
#   MISP: https://www.circl.lu/doc/misp/categories-and-types/)
MISP_TYPES = {
    "file.content": None,
    "file.name": ["filename",
                  "email-attachment",
                  "filename|md5",
                  "filename|sha1",
                  "filename|sha256",
                  "filename|authentihash",
                  "filename|ssdeep",
                  "filename|imphash",
                  "filename|pehash",
                  "filename|sha224",
                  "filename|sha384",
                  "filename|sha512",
                  "filename|sha512/224",
                  "filename|sha512/256"],
    "file.path": ["other"],
    "email": None,
    "email.body": ["text"],
    "email.header": ["email-src", "email-dst", "target-email", "whois-registrant-email",
                     "dns-soa-email", "email-reply-to", "email-subject", "email-header",
                     "email-x-mailer", "email-message-id", "email-mime-boundary"],
    "email.header.sender_address": ["email-src", "email-dst", "target-email", "whois-registrant-email",
                                    "dns-soa-email", "email-reply-to"],
    "email.header.sender_name": None,
    "email.header.to": ["email-src", "email-dst", "target-email", "whois-registrant-email",
                        "dns-soa-email", "email-reply-to"],
    "hash.md5": ["md5", "authentihash", "filename|md5"],
    "hash.sha1": ["sha1", "x509-fingerprint-sha1", "filename|sha1"],
    "hash.fuzzy": ["other"],
    "hash.sha256": ["sha256", "sha512/256", "filename|sha256"],
    "cert.x509": ["other"],
    "net.cidr": ["ip-src", "ip-dst"],
    "net.ip": ["ip-src", "ip-dst",
               "ip-dst|port", "ip-src|port", "domain|ip"],
    "net.name": ["hostname", "domain", "domain|ip"],
    "net.mac": ["other"],
    "net.port": ["port"],
    "net.uri": ["url", "uri", "link"],
    "net.uri.path": ["uri"],
    "net.http.request.header": ["http-method", "user-agent"],
    "net.http.response.header": None,
    "process.name": ["other"],
    "system.name": ["target-machine"],
    "system.mutex": ["mutex"],
    "system.registry": ["regkey"],
    "system.service.name": ["windows-service-name", "windows-service-displayname"],
    "system.user.name": ["text", "target-user", "github-username"],
    "system.user.password": ["other"],
    "threat.report.cve": ["vulnerability"],
    "threat.malware.family": ["malware-type"]
}


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement.parse("rc-cts-misp"), "rc_cts_misp/data/app.config.cts-misp")
    with open(section_config_fn, b'r') as section_config_file:
        return section_config_file.read()


class MISPThreatSearcher(BaseComponent):
    """
    Custom threat lookup for MISP
    """
    channel = searcher_channel("misp")

    def __init__(self, opts):
        super(MISPThreatSearcher, self).__init__(opts)

        # misp_url is the base URL for the MISP server (e.g. 'https://misp.example.com:883/')
        self.misp_url = opts.get(CONFIG_SECTION, {}).get("misp_url")
        if not self.misp_url:
            exc = "Configuration value `misp_url=XXX` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)

        # misp_link_url is the base URL for hyperlinks - default to same as 'misp_url'
        self.misp_link_url = opts.get(CONFIG_SECTION, {}).get("misp_link_url", self.misp_url)

        # Authentication key for API access, e.g.: 3PhYSFDeC8xpqjC0ZrFZDwazoSRDUQ1j4IlKbu0G
        # (get this from MISP: Event Actions -> Automation)
        self.misp_key = opts.get(CONFIG_SECTION, {}).get("misp_key")
        if not self.misp_key:
            exc = "Configuration value `misp_key=XXX` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)

        # verify the MISP server HTTPS certificate?
        self.misp_verifycert = opts.get(CONFIG_SECTION, {}).get("misp_verifycert", True)

        # Optionally, filter on:
        # tags=one,two
        self.misp_tag = opts.get(CONFIG_SECTION, {}).get("misp_tag")
        if self.misp_tag:
            self.misp_tag = self.misp_tag.split(",")
        # org=one,two
        self.misp_org = opts.get(CONFIG_SECTION, {}).get("misp_org")
        if self.misp_org:
            self.misp_org = self.misp_org.split(",")

    @handler()
    def _lookup_artifact(self, event, *args, **kwargs):
        """Lookup an artifact"""

        # This is a generic handler - we only care about lookup events but might be sent others
        if not isinstance(event, ThreatServiceLookupEvent):
            return

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']

        # Check that the event matches an artifact type that we want to search in MISP
        if artifact_type not in MISP_TYPES:
            # Nothing to do
            LOG.info(u"MISP lookup not implemented for %s", artifact_type)
            return

        # Doc says: MISP search for IP addresses using CIDR, uses '|' (pipe) instead of '/' (slashes) in the value.
        # But this appears not to be the case, we just search for the unchanged value.
        # if artifact_type == "net.cidr":
        #     artifact_value = str(artifact_value).replace('/', '|')

        LOG.info("MISP Lookup: " + str(artifact_value))

        misp_api = PyMISP(self.misp_url, self.misp_key, self.misp_verifycert, 'json')

        # MISP search_index: produces a list of events, and their key attributes, based on search criteria.
        # But does not filter by attribute type (only by the value that matched),
        # and the value matches include substrings, so we can't filter the results effectively.
        # matches = misp_api.search_index(published=1,
        #                                 tag=self.misp_tag,
        #                                 org=self.misp_org,
        #                                 attribute=str(artifact_value))

        # MISP search: produce events or attribute values, but only for a single type of attribute (or all types).
        # Attribute value matches partial strings (LIKE %value%), but we usually want exact-match searching.
        # Our search strategy is this:
        # - search for each type, returning only attributes;
        # - filter the attribute results for case-insensitive exact matches only,
        # - collect the list of events that the attributes belong to,
        # - finally retrieve the event metadata for our results.
        #
        # (This strategy will likely change with future versions of MISP!)

        misp_types = MISP_TYPES[artifact_type]
        search_value = str(artifact_value).lower()
        event_ids = set()

        def matches(an_attribute):
            """Does the attribute value match?  MISP does substring searches but we want exact."""
            if artifact_type == "net.cidr":
                # Match any CIDR, we assume the server did the logical search
                return True
            if an_attribute["value"].lower() == search_value:
                # Match the whole attribute value, lowercase.
                return True
            if "|" in misp_type and "|" in an_attribute["value"]:
                # Some misp types are compound types, allow searching of both parts of the compound type
                my_misp_value = an_attribute["value"].lower()
                return search_value in my_misp_value.split("|")
            return False

        for misp_type in misp_types:
            # Search for this one attribute-type
            result = misp_api.search(controller='attributes',
                                     values=[search_value],
                                     type_attribute=misp_type,
                                     tags=self.misp_tag,
                                     org=self.misp_org,
                                     withAttachments=0)
            LOG.debug("Search for %s", misp_type)
            LOG.debug(json.dumps(result))
            if result:
                response = result.get("response", {})
                if isinstance(response, dict):
                    attributes = response.get("Attribute", [])
                    for attribute in attributes:
                        if matches(attribute):
                            event_ids.add(attribute["event_id"])

        hits = []
        if not event_ids:
            # Nothing to do
            return hits

        # Finally let's get summary for each event.
        # (Don't use the search api for this, it will match partial event ids).
        for event_id in event_ids:
            result = misp_api.get_event(event_id)
            if "Event" in result:
                event = result["Event"]
                LOG.debug(json.dumps(event))
                event_id = event["id"]
                link = self.misp_link_url + "/events/view/" + str(event_id)
                info = event.get("info")
                datestr = event.get("date")
                hit = Hit(
                    StringProp(name="Info", value=info),
                    StringProp(name="Date", value=datestr),
                    UriProp(name="MISP Link", value=link),
                )
                # Add all the tags as separate properties
                if event.get("Tag"):
                    for tag in event.get("Tag"):
                        if ":" in tag["name"]:
                            tag_name, tag_value = tag["name"].split(":", 1)
                        else:
                            tag_name = tag_value = tag["name"]
                        hit.append(StringProp(name="{}:".format(tag_name), value=tag_value))

                hits.append(hit)

        return hits


def main():
    """Just some tests"""
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
