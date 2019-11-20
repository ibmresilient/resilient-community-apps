#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

"""
    Test using 'curl':

        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.ip","value":"8.8.8.8"}' 'http://127.0.0.1:9000/cts/abuseipdb_threat_feed'
"""

import logging
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, ThreatServiceLookupEvent
from circuits import handler
from resilient_circuits.actions_component import ResilientComponent
from resilient_lib import RequestsCommon, validate_fields

LOG = logging.getLogger(__name__)

HEADER_TEMPLATE = {
    "Key": None,
    "Accept": "application/json"
}


class AbuseIPDBThreatFeedSearcher(ResilientComponent):
    """
    custom threat searcher component for abuseipdb
    """
    def __init__(self, opts):
        super(AbuseIPDBThreatFeedSearcher, self).__init__(opts)

        self.opts = opts
        self.options = opts.get("abuseipdb_cts", {})
        LOG.debug(opts)
        # check https://www.abuseipdb.com/categories for more information
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

        validate_fields(("abuseipdb_key", "abuseipdb_url"), self.options)

        LOG.info("AbuseIPDB lookup started for Artifact Type {0} - Artifact Value {1}"
                 .format(artifact_type, artifact_value))

        rc = RequestsCommon(self.opts, self.options)
        hits = self._query_abuseipdb(rc, artifact_value)

        yield hits

    def _query_abuseipdb(self, rc, artifact_value):
        """
        perform the query to abuseipdb
        :param rc: resilient-lib object
        :param artifact_value:
        :return: hits object
        """

        hits = []

        try:
            headers = HEADER_TEMPLATE.copy()
            headers['Key'] = self.options.get("abuseipdb_key")

            url = self.options.get("abuseipdb_url")
            params = {
                'ipAddress': artifact_value,
                'isWhitelisted': self.options.get("ignore_white_listed", "True"),
                'verbose': True
            }

            response = rc.execute_call_v2("get", url, params=params, headers=headers)
            LOG.debug(response.json())

            resp_data = response.json()['data']
            number_of_reports = resp_data['totalReports']
            country = resp_data['countryName']
            most_recent_report = resp_data['lastReportedAt']

            # get clean list of de-duped categories
            categories_names = ""
            if resp_data.get('reports'):
                categories_list = []
                for report in resp_data['reports']:
                    categories_list.extend(report["categories"])
                categories_set = set(categories_list)  # dedup list
                categories_names = u', '.join((self.abuseipdb_categories.get(item, 'unknown') for item in categories_set))

            # Return zero or more hits.  Here's one example.
            hits.append(
                Hit(
                    NumberProp(name="Confidence Score", value=resp_data.get("abuseConfidenceScore", 0)),
                    NumberProp(name="Number of Reports", value=number_of_reports),
                    StringProp(name="Country", value=country),
                    StringProp(name="Most Recent Report", value=most_recent_report),
                    StringProp(name="Categories", value=categories_names)
                    )
            )

        except Exception as err:
            LOG.exception(str(err))
        return hits
