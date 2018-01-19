#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

"""
    Test using 'curl':

        curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/abuseipdb_threat_feed'
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.name","value":"localhost"}' 'http://127.0.0.1:9000/cts/abuseipdb_threat_feed'
        curl -v 'http://127.0.0.1:9000/cts/abuseipdb_threat_feed/9dd7b18b-48a1-5108-9d79-1a67641d0df5'
        curl -v -X GET 'http://127.0.0.1:9000/cts/abuseipdb_threat_feed/7c796ece-e3b7-5dd1-a14c-a9c3179087e4'
"""

import logging
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, ThreatServiceLookupEvent
from circuits import Event, Timer, handler
from resilient_circuits.actions_component import ResilientComponent
import requests, requests_toolbelt
import json


LOG = logging.getLogger(__name__)


def config_section_data():
    return """[abuseipdb_cts]
abuseipdb_url=https://www.abuseipdb.com/check
abuseipdb_key=
ignore_white_listed=True
"""


class AbuseIPDBThreatFeedSearcher(ResilientComponent):
    """
    Example of a custom threat searcher component
    """
    def __init__(self, opts):
        super(AbuseIPDBThreatFeedSearcher, self).__init__(opts)

        self.options = opts.get("abuseipdb_cts", {})
        LOG.debug(opts)
        """check https://www.abuseipdb.com/categories for more information"""
        self.abuseipdb_categories = {
            3: "Fraud Orders",
            4: "DDoS Attack",
            5: "FTP Brute-Force",
            6: "Ping of Death",
            7: "Phishing",
            8: "Fraud VoIP",
            9: "Open Proxy",
            10: "Web Spam",
            11: "Email Spam",
            12: "Blog Spam",
            13: "VPN IP",
            14: "Port Scan",
            15: "Hacking",
            16: "SQL Injection",
            17: "Spoofing",
            18: "Brute-Force",
            19: "Bad Web Bot",
            20: "Exploited Host",
            21: "Web App Attack",
            22: "SSH",
            23: "IoT Targeted",
        }

    # Register this as an async searcher for the URL /<root>/example
    channel = searcher_channel("abuseipdb_threat_feed")

    @handler("net.ip")
    def _lookup_net_ip(self, event, *args, **kwargs):
        """Lookup an artifact"""

        # This is a generic handler - we only care about lookup events but might be sent others
        if not isinstance(event, ThreatServiceLookupEvent):
            return

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = event.artifact['type']
        artifact_value = event.artifact['value']

        if not self.options.get("abuseipdb_key"):
            LOG.error("AbuseIPDB api key not set. You must set an api key to run this CTS.")
            return

        LOG.info("AbuseIPDB lookup started for Artifact Type {0} - Artifact Value {1}"
                 .format(artifact_type, artifact_value))
        hits = self._query_abuseipdb(artifact_value)

        yield hits

    def _query_abuseipdb(self, artifact_value):
        hits = []
        ignore_white_listed = True
        if self.options.get("ignore_white_listed", "True").lower() != "true":
            ignore_white_listed = False
        try:
            url = "{0}/{1}/json?key={2}".format(self.options.get("abuseipdb_url", "https://www.abuseipdb.com/check"),
                                                artifact_value,
                                                self.options.get("abuseipdb_key"))

            adapter = requests_toolbelt.SSLAdapter("SSLv23")
            session = requests.Session()
            session.mount('https://', adapter)
            LOG.debug("Getting info from {0}".format(url))
            response = session.get(url)
            if response.status_code == 200:
                resp_json = json.loads(response.text)
                category_list = set([])
                number_of_reports = len(resp_json)
                country = resp_json[0]["country"]
                most_recent_report = resp_json[0]["created"]

                """First we clean list of duplicated categories
                We also check for whitelisted reports. 
                If the option to ignore is set to true, we ignore ALL reports if we found at least one white listed """
                for report in resp_json:
                    if report["isWhitelisted"] and ignore_white_listed:
                        LOG.info("Ignoring white listed reports for {0}".format(artifact_value))
                        return hits

                    for category in report["category"]:
                        if category != 0:
                            category_list.add(category)

                """Then we build the string with the values"""
                categories_string = ""
                for cat in category_list:
                    if categories_string != "":
                        categories_string += ", "
                    categories_string += self.abuseipdb_categories[cat]

                # Return zero or more hits.  Here's one example.
                hits.append(
                    Hit(
                        NumberProp(name="Number of reports", value=number_of_reports),
                        StringProp(name="Country", value=country),
                        StringProp(name="Most Recent Report", value=most_recent_report),
                        StringProp(name="Categories", value=categories_string)
                        )
                )
            else:
                LOG.warn("Got response status {0} from AbuseIPDB".format(response.status_code))

        except BaseException as e:
            LOG.exception(e.message)
        return hits
