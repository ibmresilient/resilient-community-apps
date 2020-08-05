# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging

CONFIG_DATA_SECTION = 'fn_ip_void'
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
        },
        "selftest": {
            "url": "iprep",
            "params": {
                "stats": value
            }
        },
    }

    try:
        request_url = url_map.get(query_type).get("url")

    except KeyError:
        raise ValueError("%s is an Invalid IP Void request type or it's not supported", query_type)

    the_url = "/".join((base_url, request_url, sub_url))

    LOG.info("Using URL: %s", the_url)

    return (the_url, url_map.get(query_type).get("params"))


def make_api_call(base_url, sub_url, query_type, value, api_key, rc):
    """
    Function that makes the api call to IP Void

    :param base_url: The base URL from the app.config
    :param sub_url: The sub URL from the app.config file. If not defined it will be: "v1/pay-as-you-go/"
    :param query_type: The query type of the request
    :param value: The artifact value
    :param api_key: The API Key to IP Void read from the app.config file
    :param rc: RequestsCommon object

    :return: The response of the API call
    :rtype: response
    """

    # Get url and params
    request_info = get_request_info(base_url, sub_url, query_type, value)

    # Combine params
    params = {"key": api_key}
    params.update(request_info[1])

    # Execute api call and return response
    return rc.execute_call_v2(
        method="get",
        url=request_info[0],
        params=params
    )


def format_dict(dict_to_format):
    """
    Function that formats the passed dictionary
    and returns a string

    :param dict_to_format: A dict you want to format

    :return: String of the keys and values in the dict formatted
    :rtype: str
    """
    str_to_rtn = "\n-----------------\n"

    if not dict_to_format:
        str_to_rtn += "NONE\n"

    for (k, v) in dict_to_format.items():

        str_to_rtn += "{0}: {1}\n".format(k, v)

    str_to_rtn += "-----------------\n"

    return str_to_rtn
