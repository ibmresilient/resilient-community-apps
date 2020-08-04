# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging

SUB_URL = "v1/pay-as-you-go/"
LOG = logging.getLogger(__name__)


def get_request_info(base_url, sub_url, query_type, value):
    """
    Function that creates the url and parameters

    :param base_url: The base URL from the app.config
    :param sub_url: The sub URL from the app.config file. If not defined it will be: "v1/pay-as-you-go/"
    :param query_type: The query type of the request
    :param value: The artifact value

    :return: Tuple. A string of the URL and a dict of the params
    :rtype: tuple
    """
    # If no sub url defined in app.config file use the default one
    if not sub_url:
        sub_url = SUB_URL

    url_map = {
        "IP Reputation": {
            "url": "iprep",
            "params": {
                "ip": value
            }
        },
        "Domain Blacklist": {
            "url": "domainbl",
            "params": {
                "host": value
            }
        },
        "DNS Lookup": {
            "url": "dnslookup",
            "params": {
                "action": "dns-a",
                "host": value
            }
        },
        "Email Verify": {
            "url": "emailverify",
            "params": {
                "host": value
            }
        },
        "Threat Log": {
            "url": "threatlog",
            "params": {
                "host": value
            }
        },
        "SSL Info": {
            "url": "sslinfo",
            "params": {
                "host": value
            }
        }
    }

    try:
        request_url = url_map.get(query_type).get("url")

    except KeyError:
        raise ValueError("%s is an Invalid IP Void request type or it's not supported", query_type)

    the_url = "/".join((base_url, request_url, sub_url))

    LOG.info("Using URL: %s", the_url)

    return (the_url, url_map.get(query_type).get("params"))
