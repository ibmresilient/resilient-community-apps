#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A custom threat service 'searcher' for Google Safe Browsing API

    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/gsb'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'


"""

import os
import logging
import json
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp


LOG = logging.getLogger(__name__)

SB_CLIENT_ID = "Resilient"
SB_CLIENT_VER = "0.0.3"

CONFIG_SECTION = "custom_threat_service"
API_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key={}"
LINK_URL = "https://www.google.com/transparencyreport/safebrowsing/diagnostic/#url={}"


class SafeBrowsingAPI(object):
    """
    Utility class to access the Google Safe Browsing Lookup API
    https://developers.google.com/safe-browsing/v4/get-started

    >>> sb = SafeBrowsingAPI(os.environ.get("SAFEBROWSING_API_KEY"))

    # {u'matches': [{u'threatType': u'SOCIAL_ENGINEERING', u'threatEntryType': u'URL', u'platformType': u'ANY_PLATFORM', u'threat': {u'url': u'ihaveaproblem.info'}, u'cacheDuration': u'300s'}]}
    >>> result = sb.lookup_urls("ihaveaproblem.info")
    >>> len(result["matches"]) > 0
    True

    """
    def __init__(self, apikey):
        self.apiurl = API_URL.format(apikey)
        self.platform_types = ['ANY_PLATFORM']
        self.threat_types = ['THREAT_TYPE_UNSPECIFIED',
                             'MALWARE', 
                             'SOCIAL_ENGINEERING', 
                             'UNWANTED_SOFTWARE', 
                             'POTENTIALLY_HARMFUL_APPLICATION']
        self.threat_entry_types = ['URL']

    def lookup_urls(self, *urls):
        """Find threat results"""

        threat_entries = []

        for url_ in urls: 
            url = {'url': url_} 
            threat_entries.append(url)
 
        reqbody = {
            'client': {
                 'clientId': SB_CLIENT_ID,
                 'clientVersion': SB_CLIENT_VER
            },
            'threatInfo': {
                'threatTypes': self.threat_types,
                'platformTypes': self.platform_types,
                'threatEntryTypes': self.threat_entry_types,
                'threatEntries': threat_entries
            }
        }

        LOG.debug(reqbody)
        
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.apiurl, 
                          data=json.dumps(reqbody), 
                          headers=headers)

        return r.json()


class GoogleSafeBrowsingThreatSearcher(BaseComponent):
    """
    Custom threat lookup for Google Safe Browsing API

    """
    channel = searcher_channel("gsb")

    def __init__(self, opts):
        super(GoogleSafeBrowsingThreatSearcher, self).__init__(opts)

        self.apikey = opts.get(CONFIG_SECTION, {}).get("google_api_key")
        if self.apikey is None:
            exc = "Configuration value `google_api_key=XXX` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)

    @handler("net.uri", "net.uri.path")
    def _lookup_net_uri(self, event, *args, **kwargs):
        LOG.info("Looking up with Google Safe Browsing API")

        value = event.artifact['value']
        LOG.info("Looking up URL: " + str(value))

        sb = SafeBrowsingAPI(self.apikey)
        resp = sb.lookup_urls(value)
        hits = []
        LOG.debug(resp)
        for match in resp.get("matches", []):
            linkurl = match["threat"]["url"]
            link = LINK_URL.format(match["threat"]["url"])
            hits.append(Hit(
                StringProp(name="Threat Type", value=match["threatType"]),
                UriProp(name="Report Link", value=link),
                StringProp(name="Platform Type", value=match["platformType"]),
                StringProp(name="URL Name", value=linkurl)
            ))
        return hits


def main():
    """Just some tests"""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
