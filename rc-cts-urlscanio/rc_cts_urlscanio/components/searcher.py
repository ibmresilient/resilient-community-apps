#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A custom threat service 'searcher' for urlscan.io
    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/usio'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'
"""

import logging
import json
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp

LOG = logging.getLogger(__name__)

CONFIG_SECTION = "urlscanio"


class UrlScanIoSearcher(BaseComponent):
    """
    Custom threat lookup for URL Scan IO
    """
    channel = searcher_channel("usio")

    def __init__(self, opts):
        super(UrlScanIoSearcher, self).__init__(opts)

        self.apikey = opts.get(CONFIG_SECTION, {}).get("urlscanio_api_key")
        if self.apikey is None:
            exc = "Configuration value `urlscanio_api_key=XXX` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)

    @handler("net.uri")
    def _lookup_net_uri(self, event, *args, **kwargs):
        """Custom searcher for 'net.uri' (URL artifacts)"""
        LOG.info("Looking up with URL Scan IO API")

        a_value = event.artifact['value']
        LOG.info("Looking up URL: %s", a_value)

        headers = {
            'Content-Type': 'application/json',
            'API-Key': self.apikey
        }

        search_url = "https://urlscan.io/api/v1/search/?q=page.url:"
        search_response = requests.get(search_url + '"' + a_value + '"', headers=headers)
        search_response_json = json.loads(search_response.text)

        hits = []
        if search_response_json['total'] == 0:
            LOG.info("No Results for the URL")
            return hits

        LOG.info("Getting the report")
        r_id = search_response_json['results'][0]['_id']
        report_response = requests.get("https://urlscan.io/api/v1/result/{}/".format(r_id), headers=headers)
        rrj = json.loads(report_response.text)
        LOG.debug(rrj)
        malicious = rrj['stats']['malicious']

        if malicious == 1:
            png_url = rrj['task']['screenshotURL']
            scan_time = rrj['task']['time']
            report_url = rrj['task']['reportURL']
            countries = rrj['stats']['uniqCountries']
            city_country = rrj['page']['city'] + ", " + rrj['page']['country']
            server = rrj['page']['server']
            asn = rrj['page']['asnname']
            hits.append(Hit(
                StringProp(name="Time Last Scanner", value=scan_time),
                StringProp(name="Number of Countries", value=str(countries)),
                StringProp(name="City and Country", value=city_country),
                StringProp(name="Server", value=server),
                StringProp(name="ASN Name", value=asn),
                UriProp(name="Report Link", value=report_url),
                UriProp(name="Screenshot Link", value=png_url)
            ))
        else:
            LOG.info("%s isn't marked as malicious", a_value)
        return hits


def main():
    """Just some tests"""
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
