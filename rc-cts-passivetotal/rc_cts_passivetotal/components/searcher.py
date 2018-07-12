#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A custom threat service 'searcher' for Passive Total
    Test using 'curl':
        curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"net.uri","value":"http://example.org"}' 'http://127.0.0.1:9000/cts/pst'
        curl -v 'http://127.0.0.1:9000/cts/example/f9acc1b7-6184-5746-873e-e385e6214261'
"""

import os
import logging
import json
import requests
import re
from functools import partial
from circuits import BaseComponent, handler
from rc_cts import searcher_channel, Hit, NumberProp, StringProp, UriProp, IpProp, LatLngProp

LOG = logging.getLogger(__name__)

SB_CLIENT_ID = "Resilient"
SB_CLIENT_VER = "0.0.3"

CONFIG_SECTION = "custom_threat_service"
API_URL = "http:"

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
            exc = "Configuration value `passive_tags=['Compromised','Ransomware']` is missing in [{}] section".format(CONFIG_SECTION)
            raise Exception(exc)

    @handler("net.name")
    def _lookup_net_name(self, event, *args, **kwargs):
        LOG.info("Looking up with Passive Total API")

	auth = (self.userkey, self.apikey)
	base_url = 'https://api.passivetotal.org'

	a_value = event.artifact['value']
        LOG.info("Looking up URL: " + str(a_value))

	def passivetotal_get(path, query):
    		url = base_url + path
    		data = {'query': query}
		response = requests.get(url, auth=auth, json=data)
		return response.json()

	# checks if over quota
	account_results = passivetotal_get('/v2/account', '')
	account_oversub = account_results["searchApiQuotaExceeded"]
	if account_oversub:
		LOG.info("Your Account is has no API queries left")
		hits = []
		return hits

	# compares your definition of a hit with the tags in PassiveTotal
	tags_results = passivetotal_get('/v2/actions/tags', a_value)
	tags_hits = json.dumps(tags_results['tags'])
	LOG.info("Comparing tags " + str(tags_hits) + " and " + str(self.passive_tags))
	
	# Tests the site has tags you have flagged 
	if set(tags_hits) & set(self.passive_tags):
       		LOG.info("Positive Threat Intel for " + a_value)
		
		# Passive DNS Results
		pdns_results = passivetotal_get('/v2/dns/passive', a_value)
		pdns_hit = pdns_results["totalRecords"]
		LOG.info(str(pdns_hit))
	
		# URL Classification
		classification_results = passivetotal_get('/v2/actions/classification', a_value)
		classification_hit = classification_results['classification']
		LOG.info(str(classification_hit))	

		# Count of subdomains
		subdomain_results = passivetotal_get('/v2/enrichment/subdomains', a_value)
		subdomain_hits = len(subdomain_results['subdomains'])
		LOG.info(str(subdomain_hits))
		
		# Construct simple link to PT 
		report_url = "https://community.riskiq.com/search/" + a_value

		hits = []

		# Create the array for back in Resilient
        	hits.append(Hit(
                	StringProp(name="Passive DNS Hits", value=str(pdns_hit)),
                	StringProp(name="Number of subdomains", value=str(subdomain_hits)),                
			StringProp(name="Tags", value=str(tags_hits)),
			StringProp(name="Classification", value=str(classification_hit)),
        	        UriProp(name="Report Link", value=report_url)
            	))
        	return hits

	# failure condition if the site doesn't match your definition
	else:
		LOG.info("The site isn't currently listed as compromised acccording to your definition")
		hits = []
		return hits


def main():
    """Just some tests"""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
