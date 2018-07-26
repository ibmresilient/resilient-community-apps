#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp

LOG = logging.getLogger(__name__)

CONFIG_SECTION = "urlscanio"


class UrlScanIoSearcher(BaseComponent):
    """
    A custom threat service 'searcher' for urlscan.io

    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/usio'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'
    """

    URLSCAN_IO_SEARCH_URL = "https://urlscan.io/api/v1/search/?q=page.url"
    URLSCAN_IO_RESULT_URL = "https://urlscan.io/api/v1/result"

    def __init__(self, opts):
        super(UrlScanIoSearcher, self).__init__(opts)
        LOG.info(opts)

        # self.api_key = opts.get(CONFIG_SECTION, {}).get("urlscanio_api_key")
        # if self.api_key is None:
        #     raise ValueError("Mandatory config setting 'urlscanio_api_key` not set.")

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("usio")

    # Handle lookups for artifacts of type 'net uri' (URL artifacts)
    @handler("net.uri")
    def _lookup_net_uri(self, event, *args, **kwargs):

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.info("Looking up with urlscan.io Search API started for Artifact Type {0} - Artifact Value {1}".format(
            artifact_type, artifact_value))

        hits = self._query_urlscan_io_api(artifact_value)

        yield hits

    def _query_urlscan_io_api(self, artifact_value):

        hits = []

        try:
            headers = {'Content-Type': 'application/json'}
            url = "{0}:\"{1}\"".format(self.URLSCAN_IO_SEARCH_URL, artifact_value)
            search_response = requests.get(url, headers=headers)

            if search_response.status_code == 200:
                content = json.loads(search_response.text)

                total_hits = content['total']
                if total_hits is None or total_hits == 0:
                    LOG.info("No Results for the URL.")
                    return hits

                LOG.info("Getting the report for the URL.")

                search_results = content['results']
                if not search_results:
                    return hits

                first_result = search_results[0] # check the first result only
                if not first_result:
                    return hits

                result_id = first_result['_id']
                result_url = "{0}/{1}/".format(self.URLSCAN_IO_RESULT_URL, result_id)
                result_response = requests.get(result_url, headers=headers)

                if result_response.status_code == 200:
                    result_content = json.loads(result_response.text)
                    LOG.debug(result_content)

                    report_stats = result_content['stats']

                    if report_stats:
                        malicious_flag = report_stats['malicious']

                        if malicious_flag == 1:
                            png_url = result_content['task']['screenshotURL']
                            scan_time = result_content['task']['time']
                            report_url = result_content['task']['reportURL']
                            countries = result_content['stats']['uniqCountries']
                            city_country = result_content['page']['city'] + ", " + result_content['page']['country']
                            server = result_content['page']['server']
                            asn = result_content['page']['asnname']

                            hits.append(Hit(
                                StringProp(name="Time Last Scanner", value=scan_time),
                                StringProp(name="Number of Countries", value=str(countries)),
                                StringProp(name="City and Country", value=city_country),
                                StringProp(name="Server", value=server),
                                StringProp(name="ASN Name", value=asn),
                                UriProp(name="Report Link", value=report_url),
                                UriProp(name="Screenshot Link", value=png_url)
                            ))
                if not hits:
                    LOG.info("URL {0} isn't marked as malicious.".format(artifact_value))
            else:
                LOG.info("No hit information found on URL: {0}".format(artifact_value))

        except BaseException as ex:
            LOG.exception(ex.message)
        return hits


def main():
    """Just some tests"""
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
