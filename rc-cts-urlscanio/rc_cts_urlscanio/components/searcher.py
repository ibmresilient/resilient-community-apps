#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp

LOG = logging.getLogger(__name__)

class UrlScanIoSearcher(BaseComponent):
    """
    A custom threat service 'searcher' for urlscan.io

    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/usio'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'

    Test example of a potentially malicious url in urlscan.io search database is "http://detailsindia.in".
    Test example of a non-malicious url in urlscan.io search database is "www.bai.org"
    """

    CONFIG_SECTION = "urlscanio"
    URLSCAN_IO_SEARCH_API_URL = "https://urlscan.io/api/v1/search/?q=page.url:"
    URLSCAN_IO_RESULT_API_URL = "https://urlscan.io/api/v1/result/"
    HEADERS = {'Content-Type': 'application/json'}
    SIZE_QUERY_PARAM_FOR_SERACH_API = "&size="

    def __init__(self, opts):
        super(UrlScanIoSearcher, self).__init__(opts)
        LOG.info(opts)

        # Load config settings
        self.urlscan_io_search_size = opts.get(self.CONFIG_SECTION, {}).get("urlscan_io_search_size")

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("usio")

    @handler("net.uri")
    def _lookup_net_uri(self, event, *args, **kwargs):
        """
        Handle lookups for artifacts of type 'net uri' (URL artifacts)
        """

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.info("Looking up with urlscan.io Search API started for Artifact Type {0} - Artifact Value {1}".format(
            artifact_type, artifact_value))
        hits = self._query_urlscan_io_api(artifact_value)
        yield hits

    def _query_urlscan_io_api(self, artifact_value):
        """
        Query urlscan io Search API for the given URL.
        :param artifact_value: URL
        """
        hits = []

        try:
            optional_size_param = "{0}{1}".format(self.SIZE_QUERY_PARAM_FOR_SERACH_API, self.urlscan_io_search_size) \
                if self.urlscan_io_search_size else ""
            url = "{0}\"{1}\"{2}".format(self.URLSCAN_IO_SEARCH_API_URL, artifact_value, optional_size_param)
            search_response = requests.get(url, headers=self.HEADERS)

            if search_response.status_code == 200:
                content = json.loads(search_response.text)

                total_hits = content.get('total', None)
                if total_hits is None or total_hits == 0:
                    LOG.info("No Results for the URL.")
                    return hits

                LOG.info("Getting the report for the URL.")

                search_results = content.get('results', None)
                if not search_results:
                    return hits

                for result in search_results:
                    if not result:
                        continue

                    hits.append(self._generate_hit_from_search_result(result))

                if not hits:
                    LOG.info("URL {0} isn't marked as malicious.".format(artifact_value))
            else:
                LOG.info("No hit information found on URL: {0}".format(artifact_value))

        except BaseException as ex:
            LOG.exception(ex.message)
        return hits

    def _generate_hit_from_search_result(self, search_result):
        """
        Query urlscan io Result API for the given URL search result - hit.
        :param search_result: dictionary
        """
        result_id = search_result.get('_id', None)
        result_url = "{0}{1}".format(self.URLSCAN_IO_RESULT_API_URL, result_id)
        result_response = requests.get(result_url, headers=self.HEADERS)

        if result_response.status_code == 200:
            result_content = json.loads(result_response.text)
            LOG.debug(result_content)

            report_stats = result_content.get('stats', None)

            if report_stats:
                malicious_flag = report_stats.get('malicious', None)

                if malicious_flag and malicious_flag == 1:
                    task = result_content.get('task', None)
                    stats = result_content.get('stats', None)
                    page = result_content.get('page', None)

                    png_url = task.get('screenshotURL', None) if task else None
                    scan_time = task.get('time', None) if task else None
                    report_url = task.get('reportURL', None) if task else None
                    countries = str(stats.get('uniqCountries', None)) if stats else None
                    city_country_list = self._prepare_city_contry(page.get('city', None),
                                                                  page.get('country', None)) if page else None
                    city_country = ",".join(city_country_list) if city_country_list else None
                    server = page.get('server', None) if page else None
                    asn = page.get('asnname', None) if page else None

                    return Hit(
                        StringProp(name="Time Last Scanner", value=scan_time),
                        StringProp(name="Number of Countries", value=countries),
                        StringProp(name="City and Country", value=city_country),
                        StringProp(name="Server", value=server),
                        StringProp(name="ASN Name", value=asn),
                        UriProp(name="Report Link", value=report_url),
                        UriProp(name="Screenshot Link", value=png_url)
                    )

    def _prepare_city_contry(self, *argv):
        """
        Prepare a list of non None value or blank "Falsy" parameters.
        :param *argv - city, country
        :return: list
        """
        city_country_list = [el for el in argv if el]
        return city_country_list
