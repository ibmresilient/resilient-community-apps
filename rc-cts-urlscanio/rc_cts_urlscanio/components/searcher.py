#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import logging
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp

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
    HEADERS = {'Content-Type': 'application/json'}
    SEARCH_API_SIZE_QUERY_PARAM = "&size="
    SEARCH_API_QUERY_TERM_PAGE_URL_PARAM = "?q=page.url:"

    def __init__(self, opts):
        super(UrlScanIoSearcher, self).__init__(opts)
        LOG.debug(opts)
        self.options = opts.get(self.CONFIG_SECTION, {})

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("usio")

    @handler("net.uri")
    def _lookup_net_uri(self, event, *args, **kwargs):
        """
        Handle lookups for artifacts of type 'net uri' (URL artifacts)
        """

        # Read configuration settings:

        self.urlscan_io_search_api_url = self._get_value_from_options("urlscan_io_search_api_url")
        self.urlscan_io_result_api_url = self._get_value_from_options("urlscan_io_result_api_url")
        self.urlscan_io_search_size = self.options.get("urlscan_io_search_size", None)

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']
        LOG.info("Looking up with urlscan.io Search API started for Artifact Type {0} - Artifact Value {1}".format(
            artifact_type, artifact_value))
        hits = self._query_urlscan_io_api(artifact_value)
        yield hits

    def _get_value_from_options(self, app_config_setting_key):
        """
        Get value from options dict or raise ValueError for the mandatory config setting.
        :param app_config_setting_name key
        """
        if app_config_setting_key in self.options:
            return self.options[app_config_setting_key]
        else:
            error_msg = "Mandatory config setting '{}' not set.".format(app_config_setting_key)
            LOG.error(error_msg)
            raise ValueError(error_msg)

    def _query_urlscan_io_api(self, artifact_value):
        """
        Query urlscan io Search API for the given URL.
        :param artifact_value: URL
        """
        hits = []

        try:
            optional_size_param = "{0}{1}".format(self.SEARCH_API_SIZE_QUERY_PARAM, self.urlscan_io_search_size) \
                if self.urlscan_io_search_size else ""

            url = "{0}{1}\"{2}\"{3}".format(self.urlscan_io_search_api_url, self.SEARCH_API_QUERY_TERM_PAGE_URL_PARAM,
                                            artifact_value, optional_size_param)

            search_response = requests.get(url, headers=self.HEADERS)

            if search_response.status_code == 200:
                content = search_response.json()

                total_hits = content.get('total', None)
                if total_hits is None or total_hits == 0:
                    LOG.info("No Results for the URL.")
                    LOG.debug(search_response.text)
                    return hits

                LOG.info("Getting the report for the URL.")

                search_results = content.get('results', None)
                if not search_results:
                    LOG.info("No Results for the URL.")
                    LOG.debug(search_response.text)
                    return hits

                for result in search_results:
                    if not result:
                        continue

                    result_hit = self._generate_hit_from_search_result(result)
                    if result_hit:  # Do not include None value
                        hits.append(result_hit)

                if not hits:
                    LOG.info("URL {0} isn't marked as malicious.".format(artifact_value))
            else:
                LOG.info("No hit information found on URL: {0}".format(artifact_value))
                LOG.debug(search_response.text)

        except BaseException as ex:
            LOG.exception(ex.message)
        return hits

    def _generate_hit_from_search_result(self, search_result):
        """
        Query urlscan io Result API for the given URL search result - hit.
        :param search_result: dictionary
        """
        result_id = search_result.get('_id', None)
        result_url = "{0}{1}".format(self.urlscan_io_result_api_url, result_id)
        result_response = requests.get(result_url, headers=self.HEADERS)

        if result_response.status_code == 200:
            result_content = result_response.json()

            stats = result_content.get('stats', None)
            if stats:
                malicious_flag = stats.get('malicious', None)

                if malicious_flag == 1:

                    # Some malicious scans show as failed, do not include those
                    if self._verify_for_scan_failed_flag(result_content):
                        return None

                    task = result_content.get('task', None)
                    page = result_content.get('page', None)

                    png_url = task.get('screenshotURL', None) if task else None
                    scan_time = task.get('time', None) if task else None
                    report_url = task.get('reportURL', None) if task else None
                    uniq_countries_int = stats.get('uniqCountries', None)
                    city_country_list = self._prepare_city_contry(page.get('city', None),
                                                                  page.get('country', None)) if page else None
                    city_country = ",".join(city_country_list) if city_country_list else None
                    server = page.get('server', None) if page else None
                    asn = page.get('asnname', None) if page else None

                    return Hit(
                        StringProp(name="Time Last Scanner", value=scan_time),
                        NumberProp(name="Number of Countries", value=uniq_countries_int),
                        StringProp(name="City and Country", value=city_country),
                        StringProp(name="Server", value=server),
                        StringProp(name="ASN Name", value=asn),
                        UriProp(name="Report Link", value=report_url),
                        UriProp(name="Screenshot Link", value=png_url)
                    )
        else:
            LOG.info("No Result information found on URL: {0}".format(result_url))
            LOG.debug(result_response.text)

    @staticmethod
    def _verify_for_scan_failed_flag(result_content):
        """ Verify if scan failed """

        result_data = result_content.get('data', None)
        if not result_data:
            return True

        result_data_requests_list = result_data.get('requests', None)
        if not result_data_requests_list:
            return True

        # get first element from the list
        requests_first_el = result_data_requests_list[0]
        if not requests_first_el:
            return True

        response = requests_first_el.get('response', None)
        if not response or 'failed' in response:
            return True

        return False

    @staticmethod
    def _prepare_city_contry(*argv):
        """
        Prepare a list of non None value or blank "Falsy" parameters.
        :param *argv - city, country
        :return: list
        """
        city_country_list = [el for el in argv if el]
        return city_country_list
