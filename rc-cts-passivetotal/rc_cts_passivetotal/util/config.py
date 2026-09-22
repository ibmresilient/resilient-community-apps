# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_cts_urlscanio"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[passivetotal]
    
# API credentials
passivetotal_api_key=your_api_key
passivetotal_username=username

# API URLS
passivetotal_base_url=https://api.passivetotal.org
passivetotal_account_api_url=/v2/account
passivetotal_actions_tags_api_url=/v2/actions/tags
passivetotal_passive_dns_api_url=/v2/dns/passive
passivetotal_actions_class_api_url=/v2/actions/classification
passivetotal_enrich_subdom_api_url=/v2/enrichment/subdomains
passivetotal_community_url=https://community.riskiq.com/search/

# Define the tags you classify as "hits", separated by a comma
# Global tasks defined by RiskIQ Passive total include
# apt32, oceanlotus, compromised, espionage, bad rabbit, ransomware and more
passivetotal_tags=compromised,ransomware
    """
    return config_data
