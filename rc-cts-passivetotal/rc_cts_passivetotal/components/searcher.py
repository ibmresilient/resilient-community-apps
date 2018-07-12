#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A custom threat service 'searcher' for Passive Total
    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/pst'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'
"""

from __future__ import unicode_literals
import logging
import json
import requests
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp


LOG = logging.getLogger(__name__)

CONFIG_SECTION = "passivetotal"

PASSIVETOTAL_BASE_URL = 'https://api.passivetotal.org'


class PassiveTotalSearcher(BaseComponent):
    """
    Custom threat lookup for Passive Total API
    """
    channel = searcher_channel("pst")

    def __init__(self, opts):
        super(PassiveTotalSearcher, self).__init__(opts)

        self.apikey = opts.get(CONFIG_SECTION, {}).get("passive_api_key")
        self.userkey = opts.get(CONFIG_SECTION, {}).get("passive_user")
        self.passive_tags = opts.get(CONFIG_SECTION, {}).get("passive_tags")
        if self.apikey is None:
            exc = "Configuration value `passive_api_key=XXX` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)
        if self.userkey is None:
            exc = "Configuration value `passive_user=me@my.com` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)
        if self.passive_tags is None:
            exc = "Configuration value `passive_tags=tag1,tag2` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)
        self.passive_tag_set = set(self.passive_tags.split(","))

    @handler("net.name", "net.uri", "net.ip")
    def _lookup(self, event, *args, **kwargs):
        """Threat service searcher for 'net.name' (domain name artifact), 'net.uri' (URL) or 'net.ip' (IP address)"""
        hits = []
        auth = (self.userkey, self.apikey)
        a_value = event.artifact['value']
        LOG.info("PassiveTotal lookup: %s", a_value)

        def passivetotal_get(path, query):
            """get URL from PT"""
            url = PASSIVETOTAL_BASE_URL + path
            data = {'query': query}
            response = requests.get(url, auth=auth, json=data)
            return response.json()

        # checks if over quota
        account_results = passivetotal_get('/v2/account', '')
        account_oversub = account_results["searchApiQuotaExceeded"]
        if account_oversub:
            LOG.warn("Your PassiveTotal Account has no API queries left")
            return hits

        # compares your definition of a hit with the tags in PassiveTotal
        tags_results = passivetotal_get('/v2/actions/tags', a_value)
        tags_hits = json.dumps(tags_results['tags'])
        LOG.info("Comparing tags " + str(tags_hits) + " and " + str(self.passive_tags))

        # Tests the site has tags you have flagged
        if set(tags_hits) & self.passive_tag_set:
            LOG.info("Positive Threat Intel for %s", a_value)

            # Passive DNS Results
            pdns_results = passivetotal_get('/v2/dns/passive', a_value)
            pdns_hit = pdns_results["totalRecords"]
            LOG.debug(pdns_results)
            LOG.info(pdns_hit)

            # URL Classification
            classification_results = passivetotal_get('/v2/actions/classification', a_value)
            classification_hit = classification_results['classification']
            LOG.debug(classification_results)
            LOG.info(classification_hit)

            # Count of subdomains
            subdomain_results = passivetotal_get('/v2/enrichment/subdomains', a_value)
            subdomain_hits = len(subdomain_results['subdomains'])
            LOG.debug(subdomain_results)
            LOG.info(subdomain_hits)

            # Construct simple link to PT
            report_url = "https://community.riskiq.com/search/" + a_value

            # Create the hits array to sent back to Resilient
            hits.append(Hit(
                StringProp(name="Passive DNS Hits", value=str(pdns_hit)),
                StringProp(name="Number of subdomains", value=str(subdomain_hits)),
                StringProp(name="Tags", value=str(tags_hits)),
                StringProp(name="Classification", value=str(classification_hit)),
                UriProp(name="Report Link", value=report_url)
            ))
        else:
            # failure condition if the site doesn't match your definition
            LOG.info("The site isn't currently listed as compromised according to your definition")
        return hits


def main():
    """Just some tests"""
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
