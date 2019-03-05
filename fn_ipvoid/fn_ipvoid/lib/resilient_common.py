# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
BASE_URL = 'https://endpoint.apivoid.com/{}/v1/pay-as-you-go/?key={}&{}'

def get_url(api_key, query_type, value):
    """
    Method Will return appropriate URL based on query type    
    """
    type_api_pattern_mapping = {
        'IP Reputation': ['iprep', 'ip={}'],
        'Domain Blacklist': ['domainbl', 'host={}'],
        'DNS Lookup': ['dnslookup', 'action=dns-a&host={}'],
        'Email Verify': ['emailverify', 'host={}'],
        'Threat Log': ['threatlog', 'host={}'],
        'SSL Info': ['sslinfo', 'host={}']
    }

    # Checking for invalid key
    if type_api_pattern_mapping.get(query_type) is not None:
        url_pattern1 = type_api_pattern_mapping.get(query_type)[0]
        url_pattern2 = type_api_pattern_mapping.get(query_type)[1].format(value)
    else:
        raise ValueError("Invalid IPVOID request type or request type not present.")

    return BASE_URL.format(url_pattern1, api_key, url_pattern2)
