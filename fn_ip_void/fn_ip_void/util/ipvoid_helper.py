# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

SUB_URL = "{}/v1/pay-as-you-go/?key={}&{}"


def get_url(base_url, api_key, query_type, value):
    """
    Method Will return appropriate URL based on query type
    """
    url_skeleton = "/".join((base_url, SUB_URL))
    type_api_pattern_mapping = {
        "IP Reputation": ["iprep", "ip={}"],
        "Domain Blacklist": ["domainbl", "host={}"],
        "DNS Lookup": ["dnslookup", "action=dns-a&host={}"],
        "Email Verify": ["emailverify", "host={}"],
        "Threat Log": ["threatlog", "host={}"],
        "SSL Info": ["sslinfo", "host={}"],
    }

    # Checking for invalid key
    if type_api_pattern_mapping.get(query_type) is not None:
        url_pattern1 = type_api_pattern_mapping.get(query_type)[0]
        url_pattern2 = type_api_pattern_mapping.get(query_type)[1].format(value)
    else:
        raise ValueError(
            "Invalid IPVOID request type or \
            request type not present."
        )

    return url_skeleton.format(url_pattern1, api_key, url_pattern2)


def get_config_option(option_name, opts, optional=False):
    """Given option_name, checks if it is in appconfig.
        Raises ValueError if a mandatory option is missing
    """
    option_value = opts.get(option_name)

    if not option_value and optional is False:
        msg = "'{0}' is mandatory and is not set in the app.config \
            file. You must set this value to run this function"
        err = msg.format(option_name)
        raise ValueError(err)
    else:
        return option_value
